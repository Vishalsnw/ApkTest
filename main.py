from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

import fitz  # PyMuPDF
from PIL import Image as PILImage
import io
import os

# Android-specific imports
from android.permissions import request_permissions, Permission
from android import activity
from jnius import autoclass, cast

Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')
File = autoclass('java.io.File')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

class PDFApp(App):
    def build(self):
        request_permissions([Permission.READ_EXTERNAL_STORAGE])

        self.layout = BoxLayout(orientation='vertical')
        self.img_widget = Image()
        self.layout.add_widget(self.img_widget)

        btn_layout = BoxLayout(size_hint_y=0.2)
        btn_prev = Button(text="Previous")
        btn_prev.bind(on_press=self.prev_page)
        btn_next = Button(text="Next")
        btn_next.bind(on_press=self.next_page)
        btn_layout.add_widget(btn_prev)
        btn_layout.add_widget(btn_next)
        self.layout.add_widget(btn_layout)

        Clock.schedule_once(lambda dt: self.open_file_picker(), 1)

        activity.bind(on_activity_result=self.on_activity_result)
        return self.layout

    def open_file_picker(self):
        intent = Intent(Intent.ACTION_GET_CONTENT)
        intent.setType("application/pdf")
        intent.addCategory(Intent.CATEGORY_OPENABLE)
        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivityForResult(intent, 1)

    def on_activity_result(self, requestCode, resultCode, intent):
        if resultCode == -1 and intent:
            uri = intent.getData()
            context = PythonActivity.mActivity.getApplicationContext()
            path = self.get_real_path_from_uri(uri)
            if path:
                self.load_pdf(path)

    def get_real_path_from_uri(self, uri):
        # Convert Android content URI to file path
        context = PythonActivity.mActivity
        file_path = None

        try:
            file_path = os.path.join(
                context.getCacheDir().getAbsolutePath(), "selected.pdf")
            inputStream = context.getContentResolver().openInputStream(uri)
            outputStream = open(file_path, "wb")
            buffer = bytearray(1024)
            while True:
                length = inputStream.read(buffer)
                if length == -1 or length == 0:
                    break
                outputStream.write(buffer[:length])
            inputStream.close()
            outputStream.close()
            return file_path
        except Exception as e:
            print("Error copying file:", e)
            return None

    def load_pdf(self, path):
        try:
            self.doc = fitz.open(path)
            self.page_num = 0
            self.show_page(self.page_num)
        except Exception as e:
            print("Error loading PDF:", e)

    def show_page(self, num):
        page = self.doc.load_page(num)
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("ppm")
        img = PILImage.open(io.BytesIO(img_bytes))
        img_path = f"/data/data/org.test.pdfviewer/files/page_{num}.png"
        img.save(img_path)
        self.img_widget.source = img_path
        self.img_widget.reload()

    def next_page(self, instance):
        if hasattr(self, 'doc') and self.page_num < len(self.doc) - 1:
            self.page_num += 1
            self.show_page(self.page_num)

    def prev_page(self, instance):
        if hasattr(self, 'doc') and self.page_num > 0:
            self.page_num -= 1
            self.show_page(self.page_num)

PDFApp().run()

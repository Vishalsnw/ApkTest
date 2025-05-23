from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import fitz  # PyMuPDF
from PIL import Image as PILImage
import io
import os


class PDFApp(App):
    def build(self):
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

        self.show_file_chooser()
        return self.layout

    def show_file_chooser(self):
        chooser = FileChooserIconView(filters=["*.pdf"])
        popup = Popup(title="Select a PDF File", content=chooser, size_hint=(0.9, 0.9))

        def load_file(instance, selection):
            if selection:
                self.doc = fitz.open(selection[0])
                self.page_num = 0
                popup.dismiss()
                self.show_page(self.page_num)

        chooser.bind(on_submit=load_file)
        popup.open()

    def show_page(self, num):
        page = self.doc.load_page(num)
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("ppm")
        img = PILImage.open(io.BytesIO(img_bytes))
        img_path = "temp_page.png"
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
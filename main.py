from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup


class PDFApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Select a PDF file to begin", halign="center", valign="middle")
        self.layout.add_widget(self.label)

        select_button = Button(text="Select PDF", size_hint_y=0.2)
        select_button.bind(on_press=self.show_file_chooser)
        self.layout.add_widget(select_button)

        return self.layout

    def show_file_chooser(self, instance):
        chooser = FileChooserIconView(filters=["*.pdf"])
        popup = Popup(title="Select a PDF File", content=chooser, size_hint=(0.9, 0.9))

        def on_select(_, selection):
            if selection:
                self.label.text = f"Selected: {selection[0]}"
                popup.dismiss()

        chooser.bind(on_submit=on_select)
        popup.open()


PDFApp().run()

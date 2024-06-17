import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

kivy.require("1.11.1")


class ChatBoxLabel(Label):
    def __init__(self, is_user, **kwargs):
        super().__init__(**kwargs)
        self.is_user = is_user
        self.text_color = (0, 0, 0, 1) if not is_user else (1, 1, 1, 1)
        self.bind(size=self._update_canvas, pos=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.3, 0.6, 1, 1) if self.is_user else Color(0.9, 0.9, 0.9, 1)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10])


class ChatApp(App):
    def build(self):
        self.title = "Kivy Chatbot"

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.chat_history = BoxLayout(orientation="vertical", size_hint_y=None)
        self.chat_history.bind(minimum_height=self.chat_history.setter("height"))

        self.scroll_view = ScrollView(size_hint=(1, 0.9))
        self.scroll_view.add_widget(self.chat_history)

        self.input_box = BoxLayout(size_hint=(1, 0.1), spacing=10)
        self.user_input = TextInput(
            hint_text="Type your message here", multiline=True, size_hint=(0.8, 1)
        )
        self.send_button = Button(text="Send", size_hint=(0.2, 1))
        self.send_button.bind(on_release=self.send_message)

        self.input_box.add_widget(self.user_input)
        self.input_box.add_widget(self.send_button)

        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.input_box)

        return self.layout

    def send_message(self, instance):
        user_message = self.user_input.text
        if user_message:
            self.add_message(user_message, is_user=True)
            self.user_input.text = ""

            # Simulate bot response
            bot_response = "This is a dummy response"
            self.add_message(bot_response, is_user=False)

    def add_message(self, message, is_user):
        # Create a BoxLayout with padding and spacing
        padding_left = 10 if not is_user else 2
        padding_right = 10 if is_user else 2

        # Create the label with text wrapping
        label = ChatBoxLabel(
            text=message,
            is_user=is_user,
            size_hint_x=None,
            size_hint_y=None,
            width=Window.width * 0.8,
            padding=(5, 5, 5, 5),
        )
        label.bind(texture_size=label.setter("size"))
        label.texture_update()
        label.height = max(label.texture_size[1], label.line_height)
        label.size_hint_y = None

        box_layout = BoxLayout(
            size_hint_y=None,
            padding=(padding_left, 10, padding_right, 10),
        )

        if is_user:
            box_layout.add_widget(Label(size_hint_x=0.2))  # dummy widget for alignment

        box_layout.height = label.height + 20  # Adjust the height based on label height
        box_layout.add_widget(label)

        self.chat_history.add_widget(box_layout)
        self.scroll_view.scroll_to(box_layout)


if __name__ == "__main__":
    ChatApp().run()

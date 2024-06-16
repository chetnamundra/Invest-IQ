from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class ChatBotApp(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical")

        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.chat_layout = StackLayout(size_hint_y=None)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter("height"))
        self.scroll_view.add_widget(self.chat_layout)

        self.input_box = BoxLayout(size_hint=(1, 0.1))
        self.user_input = TextInput(size_hint=(0.8, 1))
        self.send_button = Button(text="Send", size_hint=(0.2, 1))
        self.send_button.bind(on_press=self.send_message)

        self.input_box.add_widget(self.user_input)
        self.input_box.add_widget(self.send_button)

        self.root.add_widget(self.scroll_view)
        self.root.add_widget(self.input_box)

        return self.root

    def send_message(self, instance):
        user_message = self.user_input.text
        if user_message:
            self.add_message(f"User: {user_message}", halign="right")
            bot_response = self.get_bot_response(user_message)
            self.add_message(f"Bot: {bot_response}", halign="left")
            self.user_input.text = ""

    def add_message(self, message, halign="left"):
        label = Label(text=message, size_hint_y=None, halign=halign)
        label.bind(texture_size=label.setter("size"))
        self.chat_layout.add_widget(label)
        self.scroll_view.scroll_to(label)

    def get_bot_response(self, message):
        # Replace with actual chatbot logic or API call
        return "This is a dummy response."


if __name__ == "__main__":
    ChatBotApp().run()

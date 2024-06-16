from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from app.choose_stock import create_top_layout
from app.financial import create_bottom
from web_scrape.ws_main import run_now


class HousePredictionApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.home_screen()
        return self.screen_manager

    def home_screen(self):
        home_screen = Screen(name="home")

        def main_layout(value):
            layout = BoxLayout(orientation="horizontal", size_hint=(1, 1))

            layout_1 = BoxLayout(orientation="vertical", size_hint=(0.25, 1))

            top_layout = BoxLayout(orientation="vertical", size_hint=(1, 0.2))
            top_layout, cur_stock = create_top_layout(top_layout)
            if cur_stock != "":
                financial_data, filename = run_now(cur_stock)

            bottom_layout = BoxLayout(size_hint=(1, 0.8))
            bottom_layout = create_bottom(bottom_layout, financial_data)

            layout_1.add_widget(top_layout)
            layout_1.add_widget(bottom_layout)

            layout_2 = BoxLayout(orientation="vertical", size_hint=(0.5, 1))
            ai_layout = BoxLayout(size_hint=(1, 0.5))
            ai_layout.add_widget(Label(text="ai"))
            chart_layout = BoxLayout(size_hint=(1, 0.5))
            chart_layout.add_widget(Label(text="chart"))

            layout_2.add_widget(ai_layout)
            layout_2.add_widget(chart_layout)

            layout_3 = BoxLayout(size_hint=(0.25, 1))
            layout_3.add_widget(Label(text="chatbot"))

            layout.add_widget(layout_1)
            layout.add_widget(layout_2)
            layout.add_widget(layout_3)

            return layout

        layout = main_layout(Window.width)
        home_screen.add_widget(layout)
        self.screen_manager.add_widget(home_screen)

        def on_width_change_for_main(instance, value):
            new_layout = main_layout(value)
            home_screen.clear_widgets()
            home_screen.add_widget(new_layout)

        Window.bind(width=on_width_change_for_main)


if __name__ == "__main__":
    Window.size = (825, 700)
    HousePredictionApp().run()

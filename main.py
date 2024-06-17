from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from web_scrape.ws_main import run_now
import yfinance as yf

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.lang import Builder
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from g4f.client import Client

client = Client()

Builder.load_string(
    """
<FDDButton@Button>:
    size_hint_y: None
    height: '50dp'
    
<FilterDD>:
    auto_dismiss: False
"""
)

stock = [
    "HDFCBANK.NS",
    "IRCTC",
    "INFY",
    "ICICIBANK",
    "TCS",
    "RELIANCE",
    "HINDUNILVR",
    "ASIANPAINT",
    "BAJFINANCE",
    "MARUTI",
]

cur_stock = "HDFCBANK.NS"

financial_data = """Market Cap ₹ 12,14,547 Cr.
Current Price ₹ 1,597
High / Low ₹ 1,758 / 1,363
Stock P/E 19.0
Book Value ₹ 519
Dividend Yield 1.22 %
ROCE 9.50 %
ROE 22.1 %
Face Value ₹ 1.00

Compounded Sales Growth
10 Years:21%
5 Years:22%
3 Years:30%
TTM:66%

Compounded Profit Growth
10 Years:22%
5 Years:23%
3 Years:26%
TTM:39%

Stock Price CAGR
10 Years:14%
5 Years:6%
3 Years:3%
1 Year:0%

Return on Equity
10 Years:18%
5 Years:18%
3 Years:19%
Last Year:22%

TTM PE Ratio 18.01
PB Ratio 3.97
Dividend Yield 0.94%
Sector PE 17.05
Sector PB 2.80
Sector Div Yld 0.80%"""

filename = ""

ai_content = """Based on the current financial analysis and general current affairs provided, along with the historical performance of Infosys, it appears that investing in this stock for the long term could be a viable option. Here are some key points to consider:

Pros:
1. The company is almost debt-free, indicating strong financial stability.
2. Infosys has a good track record of return on equity (ROE), with a 3-year ROE of 30.9%.
3. The company has been maintaining a healthy dividend payout of 63.3%.
4. The stock has shown consistent revenue growth over the last 5 years, with increasing market share.

Cons:
1. The stock is trading at 7.01 times its book value, which may be considered high.
2. Promoter holding is relatively low at 14.7%.

From the financial analysis, Infosys has shown strong compounded sales and profit growth over the years, along with a consistent return on equity. The current stock price CAGR and dividend yield also indicate positive performance.

Considering the general current affairs, there are no major negative news or events directly impacting Infosys that would raise concerns about its long-term prospects.

In conclusion, based on the provided information, investing in Infosys for the long term could be a favorable decision. However, it is important to conduct further research and analysis, and consider consulting with a financial advisor before making any investment decisions. Additionally, staying informed about industry trends, economic conditions, and regulatory changes is crucial for long-term investment success."""


def create_chart_layout(layout):

    def chart1():
        stock_data = yf.download(cur_stock, start="2020-01-01", end="2023-01-01")

        fig, ax = plt.subplots()

        fig.patch.set_facecolor("#000000")
        ax.set_facecolor("#000000")

        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_color("white")
        ax.spines["right"].set_color("white")
        ax.spines["left"].set_color("white")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

        stock_data["Close"].plot(ax=ax, color="#5c5cbd", label="Close Price")

        plt.title("Historical Close Prices of {}".format(cur_stock), fontsize=10)
        plt.xlabel("Date", fontsize=8)
        plt.ylabel("Close Price", fontsize=8)

        canvas = FigureCanvasKivyAgg(fig, size_hint=(1, 1))
        return canvas

    def real_chart_layout(value):
        if value > 800:

            box = BoxLayout(orientation="vertical")

            canvas1 = chart1()

            box.add_widget(canvas1)

            if len(layout.children) == 0:
                layout.add_widget(box)
            else:
                label2 = layout.children[0]
                layout.add_widget(box)
                layout.remove_widget(label2)
        # else:

        #     def chart_popup(instance):
        #         box = BoxLayout(orientation="vertical", size_hint=(1, 1))

        #         canvas1 = chart1()
        #         canvas2 = chart2()

        #         box.add_widget(canvas1)
        #         box.add_widget(canvas2)
        #         popup = Popup(
        #             title="",
        #             content=box,
        #             size_hint=(None, None),
        #             size=(400, 775),
        #             background_color=(0, 0, 0, 1),
        #         )
        #         popup.separator_height = 0

        #         popup.open()

        #     layout1 = BoxLayout(orientation="horizontal")
        #     chart_button = Button(
        #         on_press=chart_popup,
        #         background_normal="analysis.png",
        #         size=(150, 150),
        #         pos_hint={"center_x": 0.5, "center_y": 0.5},
        #         size_hint=(None, None),
        #     )
        #     layout1.add_widget(chart_button)

        # if len(layout.children) == 0:
        #     layout.add_widget(layout1)
        # else:
        #     label2 = layout.children[0]
        #     layout.add_widget(layout1)
        #     layout.remove_widget(label2)

    real_chart_layout(Window.width)

    def on_width_change_for_chart(instance, value):
        real_chart_layout(value)

    Window.bind(width=on_width_change_for_chart)


def ai_update():

    with open(filename, "r", encoding="utf-8") as file:
        file_contents = file.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": file_contents
                + "Given all this info, do analysis and tell me if i should invest in this stock for long term currently or not? ",
            }
        ],
    )
    global ai_content
    ai_content = response.choices[0].message.content
    print(ai_content)


def create_ai_layout(layout):
    global ai_content
    layout.clear_widgets()

    container = BoxLayout(orientation="vertical", padding=10, spacing=10)

    heading_label = Label(text="AI Recommendation", size_hint_y=None, font_size="20sp")
    heading_label.bind(texture_size=heading_label.setter("size"))

    scroll_view = ScrollView()

    ai_label = Label(
        text=ai_content, size_hint_y=None, size_hint_x=1, text_size=(None, None)
    )
    ai_label.bind(
        size=lambda instance, value: setattr(ai_label, "text_size", (value[0], None))
    )
    ai_label.bind(texture_size=ai_label.setter("size"))

    scroll_view.add_widget(ai_label)

    container.add_widget(heading_label)
    container.add_widget(scroll_view)

    layout.add_widget(container)


def create_bottom(layout):

    layout.clear_widgets()

    container = BoxLayout(orientation="vertical", padding=10, spacing=10)

    heading_label = Label(
        text="Recent Financial Data", size_hint_y=None, font_size="20sp"
    )
    heading_label.bind(texture_size=heading_label.setter("size"))

    scroll_view = ScrollView()

    financial_label = Label(text=financial_data, size_hint_y=None)
    financial_label.bind(texture_size=financial_label.setter("size"))

    scroll_view.add_widget(financial_label)

    container.add_widget(heading_label)
    container.add_widget(scroll_view)

    layout.add_widget(container)


def update_all(bottom_layout, ai_layout):
    # Your update_all function logic here
    print(f"Updating all with the selected stock: {cur_stock}")
    data_recieved, file_name = run_now(cur_stock)
    global financial_data, filename

    filename = "outputfiles/" + file_name
    financial_data = data_recieved
    create_bottom(bottom_layout)
    ai_update()
    create_ai_layout(ai_layout)
    # print(financial_data)


def button_update(buttons, button_to_update, bottom_layout, ai_layout):

    def button_clicked(
        button,
        dropdown,
        button_to_update,
    ):
        global cur_stock
        cur_stock = button.text
        dropdown.dismiss()
        button_to_update.text = button.text
        update_all(bottom_layout, ai_layout)

    def apply_filter(wid, value, dropdown, buttons, filter1, button_to_update):
        dropdown.clear_widgets()
        dropdown.add_widget(filter1)

        for btn_text in buttons:
            if not value or value in btn_text:
                button = Factory.FDDButton(
                    text=btn_text, background_color=(0.5, 0.5, 1, 1)
                )
                button.bind(
                    on_release=lambda btn: button_clicked(
                        btn, dropdown, button_to_update
                    )
                )
                dropdown.add_widget(button)

    def filterDD(buttons, button_to_update):
        filter1 = Factory.TextInput(size_hint_y=None)
        dropdown = Factory.DropDown()
        dropdown.add_widget(filter1)
        filter1.bind(
            text=lambda instance, value: apply_filter(
                instance, value, dropdown, buttons, filter1, button_to_update
            )
        )
        apply_filter(None, "", dropdown, buttons, filter1, button_to_update)
        return dropdown

    dropdown = filterDD(buttons, button_to_update)
    return dropdown


def create_top_layout(top_layout, bottom_layout, ai_layout):

    top_layout.clear_widgets()

    padded_layout = BoxLayout(
        orientation="vertical", padding=[10, 10, 0, 40], spacing=10
    )

    global stock

    label1 = Label(text="Stock : ")
    padded_layout.add_widget(label1)

    loc_btn = Factory.FDDButton(text=cur_stock, height=50)
    loc_fdd = button_update(stock, loc_btn, bottom_layout, ai_layout)
    loc_btn.bind(on_release=lambda btn: loc_fdd.open(loc_btn))

    loc_btn.background_color = (1, 1, 1, 0)
    loc_rect = RoundedRectangle(
        pos=loc_btn.pos, size=loc_btn.size, radius=[10, 10, 10, 10]
    )
    loc_btn.bind(pos=lambda instance, value: setattr(loc_rect, "pos", value))
    loc_btn.bind(size=lambda instance, value: setattr(loc_rect, "size", value))
    with loc_btn.canvas.before:
        Color(0.5, 0.5, 1, 0.5)
        loc_btn.canvas.before.add(loc_rect)

    padded_layout.add_widget(loc_btn)

    top_layout.add_widget(padded_layout)


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

            bottom_layout = BoxLayout(size_hint=(1, 0.8))

            create_bottom(bottom_layout)

            layout_1.add_widget(top_layout)
            layout_1.add_widget(bottom_layout)

            layout_2 = BoxLayout(orientation="vertical", size_hint=(0.5, 1))
            ai_layout = BoxLayout(size_hint=(1, 0.5))
            create_ai_layout(ai_layout)

            create_top_layout(top_layout, bottom_layout, ai_layout)

            chart_layout = BoxLayout(size_hint=(1, 0.5))
            create_chart_layout(chart_layout)

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

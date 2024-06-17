from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.lang import Builder

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
    "HDFCBANK",
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

cur_stock = ""


def create_bottom(layout, financial_data):
    layout.add_widget(Label(text=financial_data))
    return layout


def update_all(selected_stock):
    # Your update_all function logic here
    print(f"Updating all with the selected stock: {selected_stock}")


def button_update(buttons, button_to_update, callback=None):

    def button_clicked(button, dropdown, button_to_update, callback):
        global cur_stock
        cur_stock = button.text
        dropdown.dismiss()
        button_to_update.text = button.text
        if callback:
            callback(cur_stock)
        update_all(cur_stock)  # Call update_all whenever a button is clicked

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
                        btn, dropdown, button_to_update, callback
                    )
                )
                dropdown.add_widget(button)

    def filterDD(buttons, button_to_update, callback=None):
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

    dropdown = filterDD(buttons, button_to_update, callback)
    return dropdown


# Function to create the top layout
def create_top_layout(top_layout):
    global stock

    label1 = Label(text="Stock : ")
    top_layout.add_widget(label1)
    loc_btn = Factory.FDDButton(text="Select Stock", height=50)
    loc_fdd = button_update(stock, loc_btn)
    loc_btn.bind(on_release=lambda btn: loc_fdd.open(loc_btn))

    loc_btn.background_color = (1, 1, 1, 0)
    loc_rect = RoundedRectangle(
        pos=loc_btn.pos, size=loc_btn.size, radius=[10, 10, 10, 10]
    )
    loc_btn.bind(pos=lambda instance, value: setattr(loc_rect, "pos", value))
    loc_btn.bind(size=lambda instance, value: setattr(loc_rect, "size", value))
    loc_btn.canvas.before.add(Color(0.5, 0.5, 1, 0.5))
    loc_btn.canvas.before.add(loc_rect)
    top_layout.add_widget(loc_btn)

    return top_layout, cur_stock

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!!")
    count_enabled = BooleanProperty(False)
    counter = 0
    text_input_str = StringProperty("foo")
    # my_slider_value = StringProperty("0")

    def on_button_click(self, widget):
        if self.count_enabled:
            self.counter += 1
            self.my_text = "Clicked " + str(self.counter) + " times!!"

    def on_toogle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch " + str(widget.active))

    def on_slider_value(self, widget):
        #self.my_slider_value = str(int(widget.value))
        pass

    def on_text_validate(self, widget):
        self.text_input_str = widget.text



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            # size = dp(100) + i*10
            size = dp(100)
            # b = Button(text=str(i+1), size_hint=(.2, .2))
            # b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            b = Button(text=str(i+1), size_hint=(None, None),
                       size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     self.add_widget(b1)
    #     self.add_widget(b2)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class TheLab2App(App):
    pass


TheLabApp().run()

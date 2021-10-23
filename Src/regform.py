import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    address = ObjectProperty(None)
    zipcode = ObjectProperty(None)

    def on_submit(self):
        fname = self.fname.text
        lname = self.lname.text
        address = self.address.text
        zipcode = self.zipcode.text
        print(dir(self))
        print({fname, lname, address, zipcode})

class RegFormApp(App):
    pass

RegFormApp().run()
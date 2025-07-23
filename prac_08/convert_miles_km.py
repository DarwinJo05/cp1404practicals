from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # constant for conversion

class ConvertMilesKmApp(App):
    km_text = StringProperty('0.0')  # this will update the label automatically

    def build(self):
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KM
        self.km_text = str(round(km, 2))

    def handle_increment(self, change):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0
        miles += change
        self.root.ids.miles_input.text = str(miles)
        self.handle_convert()

if __name__ == '__main__':
    ConvertMilesKmApp().run()

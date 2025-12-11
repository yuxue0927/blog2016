from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Calculator(BoxLayout):
    def append_number(self, num):
        self.ids.display.text += num

    def clear(self):
        self.ids.display.text = ""

    def calculate(self):
        try:
            result = str(eval(self.ids.display.text))
            self.ids.display.text = result
        except:
            self.ids.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()

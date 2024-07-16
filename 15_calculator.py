from kivy.app import App                # libraries and dependancies
from kivy.uix.widget import Widget      # at first they were like 10+ but the deeper i went with the tutorials the less they got
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Window.size = (500, 700) #this sets the size of the window
Builder.load_file('calculator.kv') #this loads all the styling settings from 'box_layout'



class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def press_button(self, button):
        prior = self.ids.calc_input.text

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def add_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}+"

    def subtract_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}-"

    def multiply_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}*"
    
    def divide_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}/"

    def equals_button(self):
        prior = self.ids.calc_input.text
        if "+" in prior:   
            num_list = prior.split('+')
            answer = 0

            for num in num_list:
                answer = answer + int(num)
            self.ids.calc_input.text = str(answer)

        elif "-" in prior:
            num_list = prior.split('-')
            answer = 0

            for num in num_list:
                answer = answer - int(num)
            self.ids.calc_input.text = str(answer) 

#the class that runs the window and shows the window title automatically, for some reason kivy ignores 'App'
class Basic_CalculatorApp(App): 
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return MyLayout()
    
if __name__ == '__main__':
    Basic_CalculatorApp().run()
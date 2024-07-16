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

    def press_one(self):
        self.ids.calc_input.text.text = '1'

    def press_two(self):
        self.ids.calc_input.text = '2'

    def press_three(self):
        self.ids.calc_input.text = '3'

    def press_four(self):
        self.ids.calc_input.text = '4'

    def press_five(self):
        self.ids.calc_input.text = '5'

    def press_six(self):
        self.ids.calc_input.text = '6'

    def press_seven(self):
        self.ids.calc_input.text = '7'

    def press_eight(self):
        self.ids.calc_input.text = '8'

    def press_nine(self):
        self.ids.calc_input.text = '9'

    def press_zero(self):
        self.ids.calc_input.text = '0'
    

#the class that runs the window and shows the window title automatically, for some reason kivy ignores 'App'
class Basic_CalculatorApp(App): 
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return MyLayout()
    
if __name__ == '__main__':
    Basic_CalculatorApp().run()
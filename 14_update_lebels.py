from kivy.app import App                # libraries and dependancies
from kivy.uix.widget import Widget      # at first they were like 10+ but the deeper i went with the tutorials the less they got
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('update_lebels.kv') #this loads all the styling settings from 'box_layout'



#class that handles the whole main window
class MyLayout(Widget):
    def press(self):
        # get the name(str) from Input text
        name = self.ids.name_input.text
        print("Hello", name)

        # update the label text by id
        self.ids.my_label.text = "Hello, " + name

        # clear the input box
        self.ids.name_input.text = ""

#the class that runs the window and shows the window title automatically, for some reason kivy ignores 'App'
class AwesomeApp(App): 
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()
from kivy.app import App                # libraries and dependancies
from kivy.uix.widget import Widget      # at first they were like 10+ but the deeper i went with the tutorials the less they got
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('float_layout.kv') #this loads all the styling settings from 'box_layout'



#class that handles the whole main window
class MyLayout(Widget):
    pass

#the class that runs the window and shows the window title automatically, for some reason kivy ignores 'App'
class AwesomeApp(App): 
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()
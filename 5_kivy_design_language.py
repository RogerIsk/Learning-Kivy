import kivy                             # Kivy
from kivy.app import App                # libraries and
from kivy.uix.label import Label        # allows us to create labels
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    name = ObjectProperty(None) # None because at the beggining this doesnt have any values
    age = ObjectProperty(None)
    sex = ObjectProperty(None)




    # when buttons is pressed this happens:
    def press(self): #without instance it doesnt work
        name = self.name.text
        age = self.age.text
        sex = self.sex.text

        #self.add_widget(Label(text=f'{name} is {age} years old and is a {sex}.'))

        print(f'{name} is {age} years old and is a {sex}.')

        self.name.text = '' # all of these 3 attributes gets cleared
        self.age.text = ''
        self.sex.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()
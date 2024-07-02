import kivy                             # Kivy
from kivy.app import App                # libraries and
from kivy.uix.label import Label        # allows us to create labels
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGridLayout(GridLayout):                         # there are several buttons layouts
    def __init__(self, **kwargs):                       # initialize infinite keywords
        super(MyGridLayout, self).__init__(**kwargs)    # calling the grid layout constructor
        self.cols = 1                                  # setting number of columns
        
        self.top_grid = GridLayout() # creating a new widget with 2 columns that will hold only the texts and input boxes
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="Name: "))           # adding a widget with a visible text 'Name'
        self.name = TextInput(multiline=True)           # creating a line for input that allows input on multiple lines
        self.top_grid.add_widget(self.name)                      # adding a widget with a line for input

        self.top_grid.add_widget(Label(text="Age: "))            # adding a widget with a visible text 'Name'
        self.age = TextInput(multiline=True)            # creating a line for input that allows input on multiple lines
        self.top_grid.add_widget(self.age)                       # adding a widget with a line for input

        self.top_grid.add_widget(Label(text="Sex: "))            # adding a widget with a visible text 'Name'
        self.sex = TextInput(multiline=True)            # creating a line for input that allows input on multiple lines
        self.top_grid.add_widget(self.sex)                       # adding a widget with a line for input

        self.add_widget(self.top_grid) # adding the 2 columns widget to the main window widget



        self.submit = Button(text='Submit', font_size=32) # creating a button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    # when buttons is pressed this happens:
    def press(self, instance): #without instance it doesnt work
        name = self.name.text
        age = self.age.text
        sex = self.sex.text

        self.add_widget(Label(text=f'{name} is {age} years old and is a {sex}.'))

        self.name.text = '' # all of these 3 attributes gets cleared
        self.age.text = ''
        self.sex.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()
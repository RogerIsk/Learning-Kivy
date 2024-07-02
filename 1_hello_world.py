import kivy                             # Kivy
from kivy.app import App                # libraries and
from kivy.uix.label import Label        # dependancies


class MyApp(App):
    def build(self):
        return Label(text="Hello World", font_size = 73)
    
if __name__ == '__main__':
    MyApp().run()
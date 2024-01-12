import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

class MainApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(HomeScreen(name='home'))
		sm.add_widget(SecondScreen(name='second'))
		return sm

randomApp = MainApp()
randomApp.run()

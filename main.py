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
    

class addTaskScreen(Screen):
    def __init__(self, **kwargs):
        super(addTaskScreen, self).__init__(**kwargs)

class MainApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(HomeScreen(name='home'))
		sm.add_widget(addTaskScreen(name='addTask'))
          
		taskList = ['Item 1', 'Item 2', 'Item 3']
		
		homeScreen = sm.get_screen('home')
		tasksLayout = homeScreen.ids.tasks

		for item in range(100):
			label = Label(text=str(item), size_hint_y=None, height=40)
			tasksLayout.add_widget(label)

		return sm

randomApp = MainApp()
randomApp.run()

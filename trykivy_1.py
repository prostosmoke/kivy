from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import Screen

class Screen1(Screen):
   pass

class Screen2(Screen):
   pass

class MyApp(MDApp):
   def build(self):
      self.sm = MDScreenManager()
      self.sm.add_widget(Screen1(name='Screen1'))
      self.sm.add_widget(Screen2(name='Screen2'))
      return self.sm

MyApp().run()

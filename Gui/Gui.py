from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Wings(App):
    def build(self):
        self.window = GridLayout()  
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
        #add widgets to window 
        
        #images
        self.window.add_widget(Image(source="ws.png"))
        
        #Label
        self.greeting = Label(text="Please Enter Your Name" , font_size = 18, color = '#3366ff')
        self.window.add_widget(self.greeting)
        
        #text input widget
        self.user = TextInput(multiline = False, padding_y = (20,20), size_hint = (1,0.5))
        self.window.add_widget(self.user)
        
        #button widget
        self.button = Button(text="Click", size_hint = (1,0.5), bold = True, background_color = '#3366ff')
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        
        return self.window    
    
    def callback(self,instance):
        self.greeting.text = "Hello " + self.user.text + "!"
        
        

if __name__ == "__main__":
    Wings().run()
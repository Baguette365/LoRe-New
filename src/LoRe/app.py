#imports
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.style.pack import CENTER
#main class
class LoRe(toga.App):
    # main function
    def startup(self):
        # main toga box
        self.MainBox = toga.Box(style=Pack(
            background_color="black",
            alignment=CENTER,
            direction=COLUMN
        ))

        #create the window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # get the window size
        self.window_size = self.width, self.height = self.main_window.size

        #add all screens
        self.LanguageScreen()

        #load the main toga box
        self.main_window.content = self.MainBox

        #load the window
        self.main_window.show()

    def LanguageScreen(self):
        #store all components
        self.components={
            "SelectLanguageButton": toga.Label(text="select a language", style=Pack(padding=(0,5),text_align=CENTER,font_size=36,color="white", background_color="black")),
            "FrenchButton": toga.Button("francais | french",on_press=self.say_hello,style=Pack(padding=5,flex=1, width=round(self.width), height=round(self.height/3))),
            "EnglishButton": toga.Button("english | anglais", on_press=self.say_hello, style=Pack(padding=20 , flex=1, width=round(self.width), height=round(self.height/3)))
        }

        for component in self.components:
            self.MainBox.add(self.components[component])
    def say_hello(self, **kwargs):
        pass

#main function
def main():
    return LoRe()











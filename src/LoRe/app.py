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

        #put the screen on the MainBox | app.py | l.45
        self.LanguageScreen()

        #load the main toga box
        self.main_window.content = self.MainBox

        #set the language of the app to english
        self.language = "English"

        #load the window
        self.main_window.show()

    def LanguageScreen(self):
        #clear the screen
        self.MainBox.children.clear()

        #store all components
        self.LanguageComponents={
            "SelectLanguageButton": toga.Label(text="select a language", style=Pack(padding=(0,5),text_align=CENTER,font_size=36,color="white", background_color="black")),
            "FrenchButton": toga.Button("francais | french",on_press=self.FrenchLanguageSwitcher,style=Pack(padding=5,flex=1, width=round(self.width), height=round(self.height/3))),
            "EnglishButton": toga.Button("english | anglais", on_press=self.EnglishLanguageSwitcher, style=Pack(padding=20 , flex=1, width=round(self.width), height=round(self.height/3)))
        }

        #add components to the main box .
        for component in self.LanguageComponents:
            self.MainBox.add(self.LanguageComponents[component])

    def MainMenuScreen(self):
        pass

    def FrenchLanguageSwitcher(self, **kwargs):
        self.language = "French"
        self.MainMenuScreen()

    def EnglishLanguageSwitcher(self, **kwargs):
        self.language = "English"

#main function
def main():
    return LoRe()





















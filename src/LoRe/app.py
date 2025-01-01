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
            "FrenchButton": toga.Button("francais | french",on_press=self.FrenchLanguageSwitcher,style=Pack(padding=5,flex=1,color="white",background_color="#050c62", width=round(self.width), height=round(self.height/3))),
            "EnglishButton": toga.Button("english | anglais", on_press=self.EnglishLanguageSwitcher, style=Pack(padding=20 ,color="white",background_color="#050c62" ,flex=1, width=round(self.width), height=round(self.height/3)))
        }

        #add components to the main box .
        for component in self.LanguageComponents:
            self.MainBox.add(self.LanguageComponents[component])

    def MainMenuScreen(self, widget):
        self.MainBox.clear()

        if self.language == "French":
            self.MainMenucomponents={
            "MainMenuText": toga.Label("menu principal : ", style=Pack(padding=20, flex=1, text_align=CENTER, font_size=36, color="white", background_color="black")),
            "BlankSheetButton": toga.Button("feuille blanche",on_press=self.FrontBlankSheetScreen, style=Pack(color="white",background_color="#050c62",flex=1, width=round(self.width), height=round(self.height/6))),
            "SpacedRepetitionButton": toga.Button("répétition espacée",style=Pack(color="white",background_color="#050c62",padding=0, flex=1, width=round(self.width),height=round(self.height / 6))),
            "RevisionSheetButton": toga.Button("fiches de révisions",style=Pack(color="white",background_color="#050c62",padding=0, flex=1, width=round(self.width),height=round(self.height / 6))),
            "PngToCardsButton": toga.Button("cours vers cartes",style=Pack(color="white",background_color="#050c62",padding=0, flex=1, width=round(self.width),height=round(self.height / 6)))
        }

        if self.language == "English":
            self.MainMenucomponents={
            "MainMenuText": toga.Label("main menu : ", style=Pack(padding=20, flex=1, text_align=CENTER, font_size=36, color="white", background_color="black")),
            "BlankSheetButton": toga.Button("blank sheet method",on_press=self.FrontBlankSheetScreen, style=Pack(color="white",background_color="#050c62", flex=1, width=round(self.width), height=round(self.height/6))),
            "SpacedRepetitionButton": toga.Button("spaced repetition (Anki-like)",style=Pack(color="white",background_color="#050c62",padding=0, flex=1, width=round(self.width),height=round(self.height / 6))),
            "RevisionSheetButton": toga.Button("memo sheets",style=Pack(color="white",background_color="#050c62",padding=0, flex=1, width=round(self.width),height=round(self.height / 6))),
            "PngToCardsButton": toga.Button("image to cards",style=Pack(color="white",background_color="#050c62",padding=0, flex=1, width=round(self.width),height=round(self.height / 6)))
        }

        for component in self.MainMenucomponents:
            self.MainBox.add(self.MainMenucomponents[component])

    def FrontBlankSheetScreen(self, widget):
        self.MainBox.clear()


        if self.language == "English":
            self.BlankSheetComponents={
                "front": toga.MultilineTextInput(style=Pack(height=400)),
                "ValidateButton": toga.Button("go back the sheet", on_press=self.BackBlankSheetScreen, style=Pack(color="white",background_color="#050c62"))
            }
        if self.language == "French":
            self.BlankSheetComponents={
                "front": toga.MultilineTextInput(style=Pack(height=400)),
                "ValidateButton": toga.Button("retourner la feuille", on_press=self.BackBlankSheetScreen, style=Pack(ccolor="white",background_color="#050c62"))
            }

        for component in self.BlankSheetComponents:
            self.MainBox.add(self.BlankSheetComponents[component])

    def BackBlankSheetScreen(self, widget):
        self.MainBox.clear()

        self.input=self.BlankSheetComponents["front"].value

        if self.language == "French":
            self.BackBlankSheetComponents={
                "back": toga.MultilineTextInput(style=Pack(height=400)),
                "ValidateButton": toga.Button("afficher le recto(devant)", on_press=self.ShowFront, style=Pack(color="white",background_color="#050c62"))
            }
        if self.language == "English":
            self.BackBlankSheetComponents={
                "back": toga.MultilineTextInput(style=Pack(height=400)),
                "ValidateButton": toga.Button("show front", on_press=self.ShowFront, style=Pack(color="white",background_color="#050c62"))
            }
        for component in self.BackBlankSheetComponents:
            self.MainBox.add(self.BackBlankSheetComponents[component])

    def ShowFront(self, widget):
        self.MainBox.clear()

        self.MainBox.add(toga.Label(self.input, style=Pack(color="white", background_color="black")))
        if self.language == "French":
            self.MainBox.add(toga.Button("Main menu", on_press=self.MainMenuScreen, style=Pack(color="white",background_color="#050c62")))
        if self.language == "English":
            self.MainBox.add(toga.Button("menu principal", on_press=self.MainMenuScreen, style=Pack(color="white",background_color="#050c62")))

    def FrenchLanguageSwitcher(self, widget):
        self.language = "French"
        self.MainMenuScreen(0)

    def EnglishLanguageSwitcher(self, widget):
        self.language = "English"
        self.MainMenuScreen(0)

#main function
def main():
    return LoRe()





















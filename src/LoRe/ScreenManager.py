import toga
class ScreenManager:
    def __init__(self, app, _startingScreen = None):
        self.StartingScreen = _startingScreen
        self.ActualScreen = self.StartingScreen
        self.History = []

    def ChangeScreen(self, _actualScreen):
        self.History.append(self.ActualScreen)
        self.ActualScreen = _actualScreen
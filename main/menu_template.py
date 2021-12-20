import PySimpleGUI as sg


class MenuTemplate:
    
    sg.theme('Reddit')
    
    def __init__(self):
        self.running = True
        self.choice = 0

    def run(self, window):
        self.events()
        window.close()
        return self.choice

    def events(self):
        while self.running:
            self.events_inside()
    
    def events_inside(self):
        pass





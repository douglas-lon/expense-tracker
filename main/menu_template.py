import PySimpleGUI as sg


class MenuTemplate:
    
    sg.theme('Reddit')
    
    def __init__(self):
        self.running = True

    def run(self, window):
        self.events()
        window.close()

    def events(self):
        while self.running:
            self.events_inside()
    
    def events_inside(self):
        pass





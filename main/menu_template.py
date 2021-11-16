import PySimpleGUI as sg


class MenuTemplate:
    running = True
    sg.theme('Reddit')

    def run(self, window):
        self.events()
        window.close()

    def events(self):
        while MenuTemplate.running:
            self.events_inside()
    
    def events_inside(self):
        pass





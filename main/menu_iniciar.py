from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuIniciar(MenuTemplate):
    def __init__(self):
        super(MenuIniciar, self).__init__()
        title = 'Expense Tracker'
        layout = [
            [sg.Button('Adicionar Despesa', size=(20,1))],
            [sg.Button('Remover Depesa', size=(20,1))],
            [sg.Button('Consultar Despesas', size=(20,1))],
            [sg.Button('Histórico', size=(20,1))],
            [sg.Button('Sair', size=(20,1))]
        ]
        self.choice = 0

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Adicionar Despesa':
            self.choice = 1

        if event == 'Remover Depesa':
            self.choice = 2

        if event == 'Consultar Despesas':
            self.choice = 3

        if event == 'Histórico':
            self.choice = 4

        if event == 'Sair':
            self.choice = -1

        if self.choice != 0:
            self.running = False

    def take_choice(self):
        return self.choice


if __name__ == '__main__':
    m = MenuIniciar()
    m.run(m.window)
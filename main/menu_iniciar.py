from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuIniciar(MenuTemplate):
    def __init__(self):
        super(MenuIniciar, self).__init__()
        title = 'Expense Tracker'
        layout = [
            [sg.Button('Adicionar Despesa')],
            [sg.Button('Remover Depesa')],
            [sg.Button('Consultar Despesas')]
        ]

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            MenuTemplate.running = False


if __name__ == '__main__':
    m = MenuIniciar()
    m.run(m.window)
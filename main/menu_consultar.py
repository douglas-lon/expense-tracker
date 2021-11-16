from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuConsultar(MenuTemplate):
    def __init__(self):
        super(MenuConsultar, self).__init__()
        title = 'Expense Tracker'
        contas_aberto_columns = [
            [sg.Text('Contas em Aberto')]
        ]

        contas_pagas_columns = [
            [sg.Text('Contas Pagas')]
        ]

        layout = [
            [
                sg.Column(contas_aberto_columns),
                sg.Column(contas_pagas_columns)
            ]
        ]

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            MenuTemplate.running = False


if __name__ == '__main__':
    m = MenuConsultar()
    m.run(m.window)
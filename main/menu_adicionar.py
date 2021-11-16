from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuAdicionar(MenuTemplate):
    def __init__(self):
        super(MenuAdicionar, self).__init__()
        title = 'Adicionar Despesa'
        layout = [
            [sg.Text('Valor: '), sg.Input()],
            [sg.Text('Data: '), sg.Input()],
            [sg.Text('Local: '), sg.Input()],
            [sg.Text('Quantidade de Parcelas: '), sg.Input()],
            [sg.Button('Adicionar')]
        ]

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            MenuTemplate.running = False


if __name__ == '__main__':
    m = MenuAdicionar()
    m.run(m.window)
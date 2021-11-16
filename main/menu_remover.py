from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuRemover(MenuTemplate):
    def __init__(self):
        super(MenuRemover, self).__init__()
        title = 'Remover Despesa'
        layout = [
            [sg.Text('Valor: '), sg.Input()],
            [sg.Text('Data: '), sg.Input()],
            [sg.Text('Quantidade de Parcelas: '), sg.Input()],
            [sg.Button('Remover')]
        ]

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            MenuTemplate.running = False


if __name__ == '__main__':
    m = MenuRemover()
    m.run(m.window)
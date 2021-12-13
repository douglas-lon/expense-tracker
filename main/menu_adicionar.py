from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuAdicionar(MenuTemplate):
    def __init__(self):
        super(MenuAdicionar, self).__init__()
        title = 'Adicionar Despesa'
        layout = [
            [sg.Text('Nome: '), sg.Input()],
            [sg.Text('Valor: '), sg.Input()],
            [sg.Text('Data: '), sg.Input()],
            [sg.Text('Local: '), sg.Input()],
            [sg.Text('Quantidade de Parcelas: '), sg.Input()],
            [sg.Button('Voltar'),sg.Button('Adicionar')]
        ]
        self.choice = 1

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Voltar':
            self.choice = 0
        
        if event == 'Adicionar':
            sg.Popup('Conta Adicionada\n com Sucesso')
            self.choice = 0

        if self.choice != 1:
            self.running = False


    def take_choice(self):
        return self.choice

if __name__ == '__main__':
    m = MenuAdicionar()
    m.run(m.window)
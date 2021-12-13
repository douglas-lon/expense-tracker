from menu_template import MenuTemplate
import PySimpleGUI as sg

class MenuRemoverPesquisa(MenuTemplate):
    def __init__(self):
        super(MenuRemoverPesquisa, self).__init__()
        title = 'Pesquisar Despesa'
        layout = [
            [sg.Text('Nome: '), sg.Input()],
            [sg.Button('Voltar'), sg.Button('Procurar')]
        ]

        self.value = ''
        self.choice = 2
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Procurar':
            self.value = values[0]
            self.running = False

        if event == 'Voltar':
            self.choice = 0

        if self.choice != 2:
            self.running = False

    def take_name(self):
        return self.value

    def take_choice(self):
        return self.choice


class MenuRemoverResultado(MenuTemplate):
    def __init__(self, nome):
        super(MenuRemoverResultado, self).__init__()
        title = 'Resultados'
        self.nome = nome
        layout = [
            [sg.Text('Contas em aberto com esse nome: ')],
            [sg.Text(f'{self.nome}, Valor, Data, Qtd Parcelas'), 
             sg.Button('Pagar')]
        ]

        self.value = ''
        self.choice = 2
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Pagar':
            self.value = self.nome
            self.running = False
        

    def take_expense(self):
        return self.value

    def take_choice(self):
        return self.choice


class MenuRemoverConta(MenuTemplate):
    def __init__(self, conta):
        super(MenuRemoverConta, self).__init__()
        title = 'Remover Conta'

        total_columns = [
            [sg.Text('Total')],
            [sg.Text('Valor Total')],
            [sg.Text('Qtd Parcelas Total')]
        ]

        restante_columns = [
            [sg.Text('Restante')],
            [sg.Text('Valor Restante')],
            [sg.Text('Qtd Parcelas Restante')]
        ]

        layout = [
            [sg.Text(f'{conta}')],
            [
                sg.Column(total_columns),
                sg.Column(restante_columns)
            ],
            [sg.Text('Valor'), sg.Input()],
            [sg.Text('Qtd Parcelas'), sg.Input()],
            [sg.Button('Pagar')]
        ]

        self.choice = 2
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Pagar':
            self.choice = 0
            sg.Popup('Conta paga com sucesso')
        
        
        
        if self.choice != 2:
            self.running = False

    def take_choice(self):
        return self.choice

if __name__ == '__main__':
    m = MenuRemoverPesquisa()
    m.run(m.window)
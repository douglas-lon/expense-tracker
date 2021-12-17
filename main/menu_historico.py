from menu_template import MenuTemplate
import PySimpleGUI as sg
from models import ContaHistorico, ContaOriginal

class MenuHistorico(MenuTemplate):
    def __init__(self, session):
        super(MenuHistorico, self).__init__()
        title = 'Expense Tracker'

        self.session = session

        historico_contas = self.create_layout(ContaOriginal)
        historico_parcelas = self.create_layout(ContaHistorico)
        layout = [
            [sg.Text('Histórico de Compras', pad=((150, 10),(5,5))), sg.Text('Parcelas Pagas', pad=((300, 10),(5,5)))],
            [   
                sg.Column(historico_contas),
                sg.Text('|'),
                sg.Column(historico_parcelas)
            ],
            [sg.Button('Voltar')]
        ]


        self.choice = 4
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Voltar':
            self.choice = 0

        if self.choice != 4:
            self.running = False

    def create_layout(self, clas):
        contas = self.session.query(clas).all()
        layout = []

        for conta in contas:

            try:
                nome = conta.nome.split(' ')
                nome = f'{nome[0]}  {nome[1]}'
            except:
                nome = conta.nome
                print('nome simples')

            layout.append([sg.Text(f'{nome:<20}{conta.valor:^20,.2f}{conta.parcelas:^10}{conta.data.strftime("%d/%m/%Y"):^20}{conta.local:>10}')])
            
        return layout

    def take_choice(self):
        return self.choice

if __name__ == '__main__':
    m = MenuHistorico()
    m.run(m.window)

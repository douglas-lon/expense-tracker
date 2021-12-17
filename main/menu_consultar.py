from menu_template import MenuTemplate
import PySimpleGUI as sg
from models import ContaMudanca

class MenuConsultar(MenuTemplate):
    def __init__(self, session):
        super(MenuConsultar, self).__init__()
        title = 'Expense Tracker'

        self.session = session

        contas = self.create_layout()
        layout = [
            [sg.Text('Contas em aberto')],
            contas,
            [sg.Button('Voltar')]
        ]


        self.choice = 3
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Voltar':
            self.choice = 0

        if self.choice != 3:
            self.running = False

    def create_layout(self):
        contas = self.session.query(ContaMudanca).all()
        layout = []

        for conta in contas:
            if conta.valor > 0:
                layout.append([sg.Text(f'{conta.nome:<20}{conta.valor:^20,.2f}{conta.parcelas:^10}{conta.data.strftime("%d/%m/%Y"):^20}{conta.local:>10}')])
            
        return layout

    def take_choice(self):
        return self.choice

if __name__ == '__main__':
    m = MenuConsultar()
    m.run(m.window)

from main.menu_template import MenuTemplate
import PySimpleGUI as sg
from main.models import ContaOriginal, ContaMudanca, ContaHistorico
from main.utils import validate_type
from datetime import date

class MenuRemoverPesquisa(MenuTemplate):
    def __init__(self, session):
        super(MenuRemoverPesquisa, self).__init__()
        title = 'Pesquisar Despesa'
        layout = [
            [
                sg.Text('Nome: ', size=(12,1)), 
                sg.InputText(key='nome')
            ],
            [sg.Button('Voltar'), sg.Button('Procurar')]
        ]
        self.session = session

        self.value = ''
        self.choice = 2
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Procurar':
            nome = validate_type(values["nome"], 'str')
            if type(nome) == tuple:
                sg.popup('Digite um nome válido')
            else:
                self.value = self.session.query(
                    ContaMudanca).filter(
                        ContaMudanca.nome.like(f'%{nome}%'), 
                        ContaMudanca.valor != 0).all()
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

        self.nomes = nome
        if self.nomes:
            nomes_layout = self.create_nomes_layout(nome)
            layout = [
                [sg.Text('Contas em aberto com esse nome: ')],
                nomes_layout
            ]
        else:
            layout = [
                [sg.Text('Não há nenhuma conta em aberto com esse nome!')],
                [sg.Button('Menu Iniciar')]
            ]

        self.value = ''
        self.choice = 2
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event != sg.WIN_CLOSED:
            if event == 'Menu Iniciar':
                self.choice = 0
            else:
                self.value = self.nomes[int(event)]
            
            self.running = False
        

    def take_expense(self):
        return self.value

    def create_nomes_layout(self, ls):
        p = []
        pos = 0
        for i in ls:

            p.append([
                    sg.Text(f'{i.nome}, {i.valor:.2f},'
                            f'{i.data}, {i.parcelas}', 
                            size=(80,1)), 
                    sg.Button(f'Pagar', key=f'{pos}')
                    ])
            pos += 1

        return p


    def take_choice(self):
        return self.choice


class MenuRemoverConta(MenuTemplate):
    def __init__(self, conta, session):
        super(MenuRemoverConta, self).__init__()
        title = 'Remover Conta'
        self.conta = conta
        self.session = session
        self.original = self.session.query(
            ContaOriginal).filter(
                ContaOriginal.id==f'{conta.id}').first()

        total_columns = [
            [sg.Text('Total')],
            [sg.Text(f'Valor Total: {self.original.valor}')],
            [sg.Text(f'Qtd Parcelas Total: {self.original.parcelas}')]
        ]

        restante_columns = [
            [sg.Text('Restante')],
            [sg.Text(f'Valor Restante: {self.conta.valor}')],
            [sg.Text(f'Qtd Parcelas Restante {self.conta.parcelas}')]
        ]

        self.per_parcela = self.original.valor / self.original.parcelas

        c = []
        for i in range(0, self.conta.parcelas):
            c.append(i +1)
        layout = [
            [sg.Text(f'{conta.nome}')],
            [
                sg.Column(total_columns),
                sg.Column(restante_columns)
            ],
            [
                sg.Text('Valor', size=(12,1)), 
                sg.Input(default_text=f'{self.per_parcela:.2f}', 
                         key='vl',readonly=True)
            ],
            [
                sg.Text('Quantidade de Parcelas: ', size=(12,2)), 
                sg.Combo(c, 
                         default_value=1, key='parcela',
                         size=(5,1), readonly=True,
                         enable_events=True)
            ],
            [
                sg.Button('Menu Iniciar'),
                sg.Text('', size=(36,1)),sg.Button('Pagar')
            ]
        ]


        self.choice = 2
        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Pagar':
            valor_valido = validate_type(values['vl'], 'float')
            if type(valor_valido) != tuple:
                if valor_valido < self.per_parcela:
                    sg.popup('Valor abaixo do minimo')
                elif valor_valido > self.conta.valor:
                    sg.popup('Valor acima do que está devendo')
                else:
                    historico = ContaHistorico(nome=self.conta.nome, 
                                               valor=valor_valido, 
                                               data=date.today(), 
                                               local=self.conta.local, 
                                               parcelas=values["parcela"])

                    self.conta.valor = self.conta.valor - valor_valido
                    self.conta.parcelas = (self.conta.parcelas 
                                           - values['parcela'])

                    self.session.add(historico)
                    self.session.commit()
                    sg.Popup(
                        f'Pago {values["parcela"]} parcelas de '
                        f'{self.original.valor/self.original.parcelas}'
                        f'.\n Totalizando: {valor_valido}'
                        )

                    self.choice = 0
            else:
                sg.popup(valor_valido[1])
        
        if event == 'Menu Iniciar':
            self.choice = 0    

        if event == 'parcela':
            self.per_parcela = ((self.original.valor 
                                 / self.original.parcelas) 
                                 * values['parcela']
                                 )
            self.window['vl'].Update(f'{self.per_parcela:.2f}')
            print(self.per_parcela)
        
        print(values)
        
        if self.choice != 2:
            self.running = False



if __name__ == '__main__':
    m = MenuRemoverConta('Nome do Rennan')
    m.run(m.window)
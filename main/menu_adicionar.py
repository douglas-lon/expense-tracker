from threading import local
from menu_template import MenuTemplate
import PySimpleGUI as sg
from utils import validate_type
from datetime import datetime, date
from models import ContaOriginal, ContaMudanca

class MenuAdicionar(MenuTemplate):
    def __init__(self, session):
        super(MenuAdicionar, self).__init__()
        title = 'Adicionar Despesa'
        layout = [
            [sg.Text('Nome: ', size=(12,1)), sg.InputText(key='nome')],
            [sg.Text('Valor: ', size=(12,1)), sg.Input(key='valor')],
            [
                sg.Text('Data: ', size=(12,1)), 
                sg.CalendarButton('Calendário', 
                                   format=('%d/%m/%Y'), 
                                   target='data'),  
                sg.In(f'{date.today().strftime("%d/%m/%Y")}', key='data', 
                       readonly=True, 
                       disabled_readonly_background_color='white', 
                       border_width=0)
            ],
            [sg.Text('Local: ', size=(12,1)), sg.InputText(key='local')],
            [
                sg.Text('Quantidade de Parcelas: ', size=(12,2)), 
                sg.Combo([1,2,3,4,5,6,7,8,9,10], 
                         default_value=1, key='parcela',
                         size=(5,1), readonly=True)
            ],
            [sg.Button('Voltar'),sg.Button('Adicionar')]
        ]

        self.session = session
        self.choice = 1
        self.tipos = ['str', 'float', 'date', 'str', 'int']

        self.window = sg.Window(title=title, layout=layout)

    def events_inside(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            self.running = False
            self.choice = -1

        if event == 'Voltar':
            self.choice = 0
        
        if event == 'Adicionar':
            resultados = []
            i = 0

            for value in values:

                if value != 'Calendário':

                    if value == 'data':
                        resultados.append(validate_type(values.get(value), self.tipos[i], datetime))
                    else:
                        resultados.append(validate_type(values.get(value), self.tipos[i]))
                    i += 1  
            

            if type(resultados[0]) == tuple or type(resultados[1]) == tuple or type(resultados[3]) == tuple:
                alert_message = ''

                for valor in resultados:
                    if type(valor) == tuple:
                        alert_message += f'{valor[1]}\n'

                sg.Popup(f'{alert_message}')
            else:
                c_orig = ContaOriginal(nome=resultados[0],
                                       valor=resultados[1],
                                       data=resultados[2],
                                       local=resultados[3],
                                       parcelas=resultados[4])
                
                c_mudan = ContaMudanca(nome=resultados[0],
                                       valor=resultados[1],
                                       data=resultados[2],
                                       local=resultados[3],
                                       parcelas=resultados[4])

                self.session.add(c_orig)
                self.session.add(c_mudan)
                self.session.commit()

                texto = (f'Conta no valor de '
                        f'{c_orig.valor} e {c_orig.parcelas}' 
                        f' parcelas foi adicionado com sucesso')

                sg.Popup(texto)
                self.choice = 0


        if self.choice != 1:
            self.running = False


    def take_choice(self):
        return self.choice

if __name__ == '__main__':
    m = MenuAdicionar()
    m.run(m.window)
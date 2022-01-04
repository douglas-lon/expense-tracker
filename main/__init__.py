from main.menu_iniciar import MenuIniciar
from main.menu_adicionar import MenuAdicionar
from main.menu_historico import MenuHistorico
from main.menu_remover import (MenuRemoverPesquisa, 
                               MenuRemoverResultado,
                               MenuRemoverConta)
from main.menu_consultar import MenuConsultar
from main.menu_enum import MenuNames
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


path = os.path.dirname(os.path.abspath(__file__))
print(path)
engine = create_engine(f'sqlite:///{path}/lite.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def runMain(eng, ses):
    choice = 0
    while True:
        
        match choice:
            case MenuNames.Iniciar.value:
                mi = MenuIniciar()
                choice = mi.run(mi.window)


            case MenuNames.Adicionar.value:
                ma = MenuAdicionar(ses)
                choice = ma.run(ma.window)


            case MenuNames.Remover.value:
                # Inicia com o menu de pesquisa
                mrp = MenuRemoverPesquisa(ses)
                choice = mrp.run(mrp.window)
                name = mrp.take_name()
                if choice < 0:
                    break
                if choice == 0:
                    continue

                # Vai para o menu de resultados
                mrr = MenuRemoverResultado(name)
                choice = mrr.run(mrr.window)
                conta = mrr.take_expense()
                if choice < 0:
                    break
                if choice == 0:
                    continue
                
                # Menu para pagar a conta escolhida
                mrc = MenuRemoverConta(conta, ses)
                choice = mrc.run(mrc.window)

            case MenuNames.Consultar.value:
                mc = MenuConsultar(ses)
                choice = mc.run(mc.window)

            case MenuNames.Historico.value:
                mh = MenuHistorico(ses)
                choice = mh.run(mh.window)

            case _:
                break
    
    
    ses.close()
    eng.dispose()


if __name__ == '__main__':
    runMain(engine, session)

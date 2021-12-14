from menu_iniciar import MenuIniciar
from menu_adicionar import MenuAdicionar
from menu_remover import (MenuRemoverPesquisa, 
                          MenuRemoverResultado,
                          MenuRemoverConta)
from menu_consultar import MenuConsultar

from sqlalchemy import (create_engine, 
                        Column, Integer, 
                        String)
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///main/lite.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def runMain(eng, ses):
    choice = 0

    while True:
        
        match choice:
            case 0:
                mi = MenuIniciar()
                mi.run(mi.window)
                choice = mi.take_choice()
            case 1:
                ma = MenuAdicionar(ses)
                ma.run(ma.window)
                choice = ma.take_choice()
            case 2:
                # Inicia com o menu de pesquisa
                mrp = MenuRemoverPesquisa()
                mrp.run(mrp.window)
                name = mrp.take_name()
                choice = mrp.take_choice()
                if choice < 0:
                    break
                if choice == 0:
                    continue

                # Vai para o menu de resultados
                mrr = MenuRemoverResultado(name)
                mrr.run(mrr.window)
                conta = mrr.take_expense()
                choice = mrr.take_choice()
                if choice < 0:
                    break
                
                # Menu para pagar a conta escolhida
                mrc = MenuRemoverConta(conta)
                mrc.run(mrc.window)
                choice = mrc.take_choice()
            case 3:
                mc = MenuConsultar()
                mc.run(mc.window)
                choice = mc.take_choice()
            case _:
                break
    
    ses.close()
    eng.dispose()


if __name__ == '__main__':
    runMain(engine, session)

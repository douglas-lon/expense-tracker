
from sqlalchemy import (Column, Integer, 
                        String, Float,
                        Date)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ContaOriginal(Base):
    __tablename__ = 'contaoriginal'

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    local = Column(String(100), nullable=False)
    parcelas = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<ContaOriginal(nome={self.nome},valor={self.valor},'\
               f' data={self.data}, local={self.local},'\
               f' parcelas={self.parcelas})>'


class ContaMudanca(Base):
    __tablename__ = 'contamudanca'

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    local = Column(String(100), nullable=False)
    parcelas = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<ContaMudanca(nome={self.nome},valor={self.valor},'\
               f' data={self.data}, local={self.local},'\
               f' parcelas={self.parcelas})>'


class ContaHistorico(Base):
    __tablename__ = 'contahistorico'

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    local = Column(String(100), nullable=False)
    parcelas = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<ContaHistorico(nome={self.nome},valor={self.valor},'\
               f' data={self.data}, local={self.local},'\
               f' parcelas={self.parcelas})>'


if __name__ == '__main__':
    from main import engine
    Base.metadata.create_all(engine)
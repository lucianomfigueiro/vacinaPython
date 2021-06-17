from sql_alchemy import banco
from datetime import datetime

class Pessoa(banco.Model):
    __tablename__ = 'pessoas'

    id_pessoa = banco.Column(banco.Integer, primary_key=True,sqlite_autoincrement=True)
    nome = banco.Column(banco.String(80))
    cpf = banco.Column(banco.String(15))
    dose_1 = banco.Column(banco.Boolean)
    dose_2 =banco.Column(banco.Boolean)
    data_dose_1 = banco.Column(banco.Date)
    data_dose_2 = banco.Column(banco.Date)
    lote_vacina = banco.column(banco.String, banco.ForeignKey('vacinas.lote'))
    
    def __init__(self,id_pessoa,nome,cpf,data_dose_1,data_dose_2):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.cpf = cpf
        self.dose_1 = 0
        self.dose_2 = 0
        self.data_dose_1 = data_dose_1
        self.data_dose_2 = data_dose_2
        self.lote_vacina = ''

    def json(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'dose_1': self.dose_1,
            'dose_2': self.dose_2,
            'data_dose_1': self.data_dose_1,
            'data_dose_2': self.data_dose_2,
            'lote_vacina': self.lote_vacina
        }
    
    def cadastrar_pessoa(self):
        banco.session.add(self)
        banco.session.commit()

    def vacina_pessoa(self):
        if self.dose_1 == 0 and self.dose_2 == 0:
            self.dose_1 = 1
            self.data_dose_1 = datetime.today().strftime('%d/%m/%Y')
        elif self.dose_1 == 1 and self.dose_2 == 0:
            self.dose_2 = 1            
            self.data_dose_2 = datetime.today().strftime('%d/%m/%Y')
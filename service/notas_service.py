from dao import  notas_dao
from models import  notas

class NotaService():

    def create(self, notas_param:notas.Nota):
        try:
            notas_dao_instance = notas_dao.NotasDao()
            notass = notas_dao_instance.create(notas_param)
        except:
            return 'erro ao cadastrar nota'

    def select(self):
        notas_dao_instance = notas_dao.NotasDao()
        notas_alunos = []
        notas_raw = notas_dao_instance.select()
        for nota_tmp in notas_raw:
            nota_aux = notas.Nota(None, nota_tmp[1], nota_tmp[2], nota_tmp[0])
            notas_alunos.append(nota_aux.__dict__)
        return notas_alunos
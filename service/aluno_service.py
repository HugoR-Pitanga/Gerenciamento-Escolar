from dao import aluno_dao
from models import aluno

class AlunoService():

    def create(self, aluno_param:aluno.Aluno):
        try:
            aluno_dao_instance = aluno_dao.AlunoDao()
            alunos = aluno_dao_instance.create(aluno_param)
        except:
            return 'erro na entrada de dados'

    def select(self):
        aluno_dao_instance = aluno_dao.AlunoDao()
        alunos = []
        alunos_raw = aluno_dao_instance.select()
        for aluno_aux in alunos_raw:
            aluno_tmp = aluno.Aluno(aluno_aux[0],aluno_aux[1])
            alunos.append(aluno_tmp.__dict__)
        return alunos

    def delete_aluno(self, id):
        aluno_dao_instance = aluno_dao.AlunoDao()
        aluno_dao_instance.delete_aluno(id)
        
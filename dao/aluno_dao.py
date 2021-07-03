from integration import postgresql
from models import aluno

class AlunoDao(postgresql.Postgresql):

    def __init__(self):
        super().__init__()

    def create(self, aluno_param:aluno.Aluno):
            sql = f"insert into aluno(id,nome) values(default, '{aluno_param.nome}')"
            return super().create(sql)

    def select(self):
        sql = f"select id, nome from aluno"
        return super().select(sql)

    def delete_aluno(self, id):
        sql = f"delete from aluno where id = {id}"
        print(sql)
        return super().delete(sql)
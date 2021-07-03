from integration import postgresql
from models import notas


class NotasDao(postgresql.Postgresql):

    def __init__(self):
        super().__init__()

    def create(self, notas_param:notas.Nota):
            v_nota = notas_param.nota
            v_aluno_id = notas_param.aluno_id
            v_materia = notas_param.materia
            sql = f"insert into nota(nota_id, materia, nota, aluno_id) values(default, '{(v_materia).title()}', '{v_nota}', '{v_aluno_id}')"
            return super().create(sql)


    def select(self):
        return super().select(f"select a.nome, n.materia, n.nota from aluno a inner join nota n on a.id = n.aluno_id")
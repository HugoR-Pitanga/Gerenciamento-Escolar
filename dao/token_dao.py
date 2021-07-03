from integration import postgresql
from models import token

class TokenDao(postgresql.Postgresql):

    def __init__(self):
        super().__init__()

    def create(self, token_param:token.Token):
        t_id = token_param.token_id
        t_user = token_param.token_user
        t_token = token_param.token_token
        t_data_valida = token_param.data_valida
        sql = f'insert into token(token_id, token_user, token_token, data_valida) values(default, {t_user}, {t_token}, {t_data_valida})'
        return super().create(sql)

    def select(self):
        return super().select(f'select * from token')
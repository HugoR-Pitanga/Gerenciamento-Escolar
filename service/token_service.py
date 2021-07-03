from dao import token_dao
from models import token

class TokenService():

    def create(self, token_param:token.Token):
        try:
            token_instance = token_dao.TokenDao()
            credential = token_instance.create(token_param)
        except:
            return 'entrada invalida'

    def select(self):
        token_instance = token_dao.TokenDao()
        return token_instance.select()
class Validacao():

    def isNumber(self, valor_temporario):
        try:
            isFloat = valor_temporario.find(".") != -1
            if isFloat:
                return float(valor_temporario)
            return int(valor_temporario)
        except:
            return 'ERRO!!:somente numericos'

    def isStr(self, valor_temporario):
            nome = valor_temporario
            if isNumber(nome) == True:
                return 'ERRO!!:somente alfabeticos'
            else:
                return nome

    def isMateria(self, materia):
        if materia == 'portugues' or materia == 'matematica' or materia == 'historia' or materia == 'fisica':
            return materia
        else:
            return 'ERRO!!:materia nao existe'

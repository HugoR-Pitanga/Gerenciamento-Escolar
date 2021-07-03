import psycopg2, os

class Postgresql():

    def __init__(self):
        self.host = os.environ.get('POSTGRE_HOST')
        self.user = os.environ.get('POSTGRE_USER')
        self.password = os.environ.get('POSTGRE_PASSWORD')
        self.database = os.environ.get('POSTGRE_DATABASE')

    def open(self):
        postdb = psycopg2.connect(host = self.host, user = self.user,
        password = self.password, database = self.database)
        return postdb, postdb.cursor()
        
    def execute(self, postcursor, postdb, sql):
        postcursor.execute(sql)
        postdb.commit()

    def create(self, sql):
        postdb, postcursor = self.open()
        postcursor.execute(sql)
        postdb.commit()
        postdb.close()

    def select(self, sql):
        postdb, postcursor = self.open()
        postcursor.execute(sql)
        result = postcursor.fetchall()
        postdb.close()
        return result

    def delete(self, sql):
        postdb, postcursor = self.open()
        postcursor.execute(sql)
        postdb.commit()
        postdb.close()
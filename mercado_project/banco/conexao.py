import mysql.connector

class BancoDeDados:
    def __init__(self):
        # Configura os dados da conexão com o banco MySQL
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',    # Troque pelo seu usuário MySQL
            password='',  # Troque pela sua senha
            database='mercado_db'
        )
        self.cursor = self.conexao.cursor(dictionary=True)

    def commit(self):
        self.conexao.commit()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()

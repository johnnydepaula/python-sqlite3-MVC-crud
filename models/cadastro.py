from models.connection import Connection
from prettytable import PrettyTable


class Cadastro:
    def __init__(self):
        conn = Connection()
        self.conn = conn.conn
        self.cur = conn.cur

    def create_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS cadastro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL
            )""")
        self.conn.commit()

    def insert(self, nome, sobrenome):
        self.cur.execute(
            f"""INSERT INTO cadastro (nome, sobrenome)
            VALUES ('{nome}', '{sobrenome}')""")
        self.conn.commit()

    def select(self):
        self.cur.execute("""
        SELECT id,
         nome,
         sobrenome
        FROM cadastro
        """)

        table = PrettyTable(['id', 'nome', 'sobrenome'])
        for row in self.cur.fetchall():
            table.add_row(row)
        # print(table)
        return table
        # return self.cur.fetchall()

    def update(self, id, nome, sobrenome):
        self.cur.execute(
            f"""UPDATE cadastro SET nome = '{nome}', sobrenome = '{sobrenome}'
            WHERE id = {id}""")
        self.conn.commit()

    def delete(self, id):
        self.cur.execute(f'DELETE FROM cadastro WHERE id = {id}')
        self.conn.commit()

    def __del__(self):
        self.conn.close()



# cadastro = Cadastro()
# cadastro.create_table()
# cadastro.insert('John', 'Doe')
# cadastro.insert('Jane', 'Doe')
#
# print("|   TABLE CADASTRO   |")
# for item in cadastro.select():
#     print(item)
#
# cadastro.update(1, 'John', 'Smith')
# cadastro.delete(2)
#
# print("|   TABLE CADASTRO   |")
# for item in cadastro.select():
#     print(item)
#
# cadastro.__del__()

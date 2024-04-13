from models.connection import Connection
from prettytable import PrettyTable


class Phone:
    def __init__(self):
        conn = Connection()
        self.conn = conn.conn
        self.cur = conn.cur

    def create_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS phone (
                id_phone INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT NOT NULL,
                id_cadastro INTEGER NOT NULL,
                FOREIGN KEY (id_cadastro) REFERENCES cadastro (id)
            )""")
        self.conn.commit()

    def select(self):
        self.cur.execute('SELECT * FROM phone')

        table = PrettyTable(['id_phone', 'phone_number', 'id_cadastro'])
        for row in self.cur.fetchall():
            table.add_row(row)
        return table

    def insert(self, phone_number, id_cadastro):
        self.cur.execute(f'SELECT id FROM cadastro WHERE id = {id_cadastro}')

        if self.cur.fetchone() is None:
            raise ValueError('id_cadastro does not exist')

        else:
            self.cur.execute(
                f"""INSERT INTO phone (phone_number, id_cadastro)
                VALUES ('{phone_number}', {id_cadastro})""")
            self.conn.commit()

    def update(self, id_phone, phone_number):
        self.cur.execute(
            f"""UPDATE phone SET phone_number = '{phone_number}'
            WHERE id_phone = {id_phone}""")
        self.conn.commit()

    def delete(self, id_phone):
        self.cur.execute(f'DELETE FROM phone WHERE id_phone = {id_phone}')
        self.conn.commit()

    def __del__(self):
        self.conn.close()
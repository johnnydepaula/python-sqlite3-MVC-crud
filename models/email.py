from models.connection import Connection


class Email:
    def __init__(self):
        conn = Connection()
        self.conn = conn.conn
        self.cur = conn.cur

    def create_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS email (
                id_email INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                id_cadastro INTEGER,
                FOREIGN KEY (id_cadastro) REFERENCES cadastro (id)
            )""")
        self.conn.commit()

    def insert(self, email, id_cadastro):
        self.cur.execute(f'SELECT id FROM cadastro WHERE id = {id_cadastro}')

        if self.cur.fetchone() is None:
            raise ValueError('id_cadastro does not exist')

        else:
            self.cur.execute(
                f"""INSERT INTO email (email, id_cadastro)
                VALUES ('{email}', {id_cadastro})""")
            self.conn.commit()

    def select(self):
        self.cur.execute('SELECT * FROM email')
        return self.cur.fetchall()

    def update(self, id_email, email):
        self.cur.execute(
            f"""UPDATE email SET email = '{email}'
            WHERE id_email = {id_email}""")
        self.conn.commit()

    def delete(self, id_email):
        self.cur.execute(f'DELETE FROM email WHERE id_email = {id_email}')
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# email = Email()
# email.create_table()
# email.insert('john@doe.com', 1)
# email.insert('jane@doe.com', 2)
#
# email.__del__()
#
# # for item in email.select():
# #     print(item)
# #
# # email.update(1, 'john@gmail.com')
# # email.delete(2)
# #
# # for item in email.select():
# #     print(item)

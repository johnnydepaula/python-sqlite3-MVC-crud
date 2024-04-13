from models.cadastro import Cadastro
from models.email import Email
from models.phone import Phone
from views.view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.cadastro = Cadastro()
        self.email = Email()
        self.phone = Phone()

        self.cadastro.create_table()
        self.email.create_table()
        self.phone.create_table()

    def run(self):
        while True:
            choice = self.view.main_menu()
            if choice == '1':
                self.handle_cadastro()
            elif choice == '2':
                self.handle_email()
            elif choice == '3':
                self.handle_phone()
            elif choice == '4':
                break

    def handle_cadastro(self):
        while True:
            choice = self.view.cadastro_menu()
            if choice == '1':
                print(self.cadastro.select())

            elif choice == '2':
                nome = self.view.get_nome()
                sobrenome = self.view.get_sobrenome()
                self.cadastro.insert(nome, sobrenome)

            elif choice == '3':
                id = self.view.get_id()
                new_nome = self.view.get_new_nome()
                new_sobrenome = self.view.get_new_sobrenome()
                self.cadastro.update(id, new_nome, new_sobrenome)

            elif choice == '4':
                id = self.view.get_id()
                self.cadastro.delete(id)

            elif choice == '5':
                break

    def handle_email(self):
        while True:
            choice = self.view.email_menu()

            if choice == '1':
                print(self.email.select())

            elif choice == '2':
                email = self.view.get_email()
                id_cadastro = self.view.get_id_cadastro()
                self.email.insert(email, id_cadastro)

            elif choice == '3':
                id_email = self.view.get_id_email()
                new_email = self.view.get_new_email()
                self.email.update(id_email, new_email)

            elif choice == '4':
                id_email = self.view.get_id_email()
                self.email.delete(id_email)

            elif choice == '5':
                break

    def handle_phone(self):
        while True:
            choice = self.view.phone_menu()
            if choice == '1':
                print(self.phone.select())

            elif choice == '2':
                phone_number = self.view.get_phone_number()
                id_cadastro = self.view.get_id_cadastro()
                self.phone.insert(phone_number, id_cadastro)

            elif choice == '3':
                id_phone = self.view.get_id_phone()
                new_phone_number = self.view.get_new_phone_number()
                self.phone.update(id_phone, new_phone_number)

            elif choice == '4':
                id_phone = self.view.get_id_phone()
                self.phone.delete(id_phone)

            elif choice == '5':
                break


# controller = Controller()
# controller.run()

from models.cadastro import Cadastro
from models.email import Email
from views.view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.cadastro = Cadastro()
        self.email = Email()

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

            else:
                print("\n")
                print("================================================")
                print("|        INVALID CHOICE, TRY AGAIN...          |")
                print("================================================")
                # time.sleep(2)


controller = Controller()
controller.run()

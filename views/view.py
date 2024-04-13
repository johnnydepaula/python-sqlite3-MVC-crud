from models.cadastro import Cadastro
from models.email import Email
import time


class View:
    def __init__(self):
        self.cadastro = Cadastro()
        self.email = Email()

    def main_menu(self):
        while True:
            print("\n")
            print("================================================")
            print("|               BANCO DE DADOS                 |")
            print("================================================")
            print("|               1. CADASTRO                    |")
            print("|               2. EMAIL                       |")
            print("|               3. PHONE                       |")
            print("|               4. SAIR                        |")
            print("================================================")
            choice = input("========================== OPCAO DESEJADA: -> ")
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("\n")
                print("================================================")
                print("|        INVALID CHOICE, TRY AGAIN...          |")
                print("================================================")
                time.sleep(2)

            # if choice == '1':
            #     self.cadastro_menu()
            # elif choice == '2':
            #     self.email_menu()
            # elif choice == '3':
            #     self.phone_menu()
            # elif choice == '4':
            #     break
            # else:
            #     print("\n")
            #     print("================================================")
            #     print("|        INVALID CHOICE, TRY AGAIN...          |")
            #     print("================================================")
            #     time.sleep(2)

    def cadastro_menu(self):
        while True:
            print("\n")
            print("================================================")
            print("|                 CADASTRO                     |")
            print("================================================")
            print("|               1. QUERY                       |")
            print("|               2. INSERT                      |")
            print("|               3. UPDATE                      |")
            print("|               4. DELETE                      |")
            print("|         5. BACK TO MAIN MENU                 |")
            print("================================================")
            choice = input("========================== OPCAO DESEJADA: -> ")
            return choice

            # if choice == '1':
            #     print("\n")
            #     print(self.cadastro.select())
            #
            # elif choice == '2':
            #     nome = input("ENTER NOME: ")
            #     sobrenome = input("ENTER SOBRENOME: ")
            #     self.cadastro.insert(nome, sobrenome)
            #
            # elif choice == '3':
            #     id = input("ENTER ID: ")
            #     nome = input("ENTER NEW NOME: ")
            #     sobrenome = input("ENTER NEW SOBRENOME: ")
            #     self.cadastro.update(id, nome, sobrenome)
            #
            # elif choice == '4':
            #     id = input("ENTER ID: ")
            #     self.cadastro.delete(id)
            #
            # elif choice == '5':
            #     break
            #
            # else:
            #     print("\n")
            #     print("================================================")
            #     print("|        INVALID CHOICE, TRY AGAIN...          |")
            #     print("================================================")
            #     time.sleep(2)

    def get_nome(self):
        nome = input("ENTER NOME: ")
        return nome

    def get_sobrenome(self):
        sobrenome = input("ENTER SOBRENOME: ")
        return sobrenome

    def get_id(self):
        id = input("ENTER ID: ")
        return id

    def get_new_nome(self):
        nome = input("ENTER NEW NOME: ")
        return nome

    def get_new_sobrenome(self):
        sobrenome = input("ENTER NEW SOBRENOME: ")
        return sobrenome

    # def email_menu(self):
    #     while True:
    #         print("\nEmail Menu:")
    #         print("1. Insert")
    #         print("2. Update")
    #         print("3. Query")
    #         print("4. Back to Main Menu")
    #         choice = input("Enter your choice: ")
    #
    #         if choice == '1':
    #             email = input("Enter email: ")
    #             id_cadastro = input("Enter id_cadastro: ")
    #             self.email.insert(email, id_cadastro)
    #         elif choice == '2':
    #             id_email = input("Enter id_email: ")
    #             email = input("Enter new email: ")
    #             self.email.update(id_email, email)
    #         elif choice == '3':
    #             print(self.email.select())
    #         elif choice == '4':
    #             break
    #         else:
    #             print("Invalid choice. Please try again.")
    #
    # def phone_menu(self):
    #     pass


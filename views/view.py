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
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("\n")
                print("================================================")
                print("|        INVALID CHOICE, TRY AGAIN...          |")
                print("================================================")
                time.sleep(2)

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

    def email_menu(self):
        while True:
            print("\n")
            print("================================================")
            print("|                  EMAIL                       |")
            print("================================================")
            print("|               1. QUERY                       |")
            print("|               2. INSERT                      |")
            print("|               3. UPDATE                      |")
            print("|               4. DELETE                      |")
            print("|         5. BACK TO MAIN MENU                 |")
            print("================================================")
            choice = input("========================== OPCAO DESEJADA: -> ")
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("\n")
                print("================================================")
                print("|        INVALID CHOICE, TRY AGAIN...          |")
                print("================================================")
                time.sleep(2)

    def get_id_email(self):
        id_email = input("ENTER ID_EMAIL: ")
        return id_email

    def get_email(self):
        email = input("ENTER EMAIL: ")
        return email

    def get_new_email(self):
        email = input("ENTER NEW EMAIL: ")
        return email

    def get_id_cadastro(self):
        id_cadastro = input("ENTER ID_CADASTRO: ")
        return id_cadastro


    def phone_menu(self):
        while True:
            print("\n")
            print("================================================")
            print("|                  PHONE                       |")
            print("================================================")
            print("|               1. QUERY                       |")
            print("|               2. INSERT                      |")
            print("|               3. UPDATE                      |")
            print("|               4. DELETE                      |")
            print("|         5. BACK TO MAIN MENU                 |")
            print("================================================")
            choice = input("========================== OPCAO DESEJADA: -> ")
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("\n")
                print("================================================")
                print("|        INVALID CHOICE, TRY AGAIN...          |")
                print("================================================")
                time.sleep(2)

    def get_id_phone(self):
        id_phone = input("ENTER ID_PHONE: ")
        return id_phone
    def get_phone_number(self):
        phone_number = input("ENTER PHONE_NUMBER: ")
        return phone_number
    def get_new_phone_number(self):
        phone_number = input("ENTER NEW PHONE_NUMBER: ")
        return phone_number

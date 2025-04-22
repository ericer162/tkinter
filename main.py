class Usuario:
    def __init__(self, nome, idade, email):
        """Construtor da classe Usuario"""
        self.nome = nome  # Atributo público
        self.idade = idade  # Atributo público
        self.__email = email  # Atributo privado

    def exibir_dados(self):
        """Método para exibir os dados do usuário"""
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.__email}"

    def atualizar_email(self, novo_email):
        """Método para atualizar o email do usuário"""
        self.__email = novo_email
           

# Criando Instâncias da Classe
# Criando um usuário
usuario1 = Usuario("Ana Souza", 25, "ana@email.com")
usuario1 = Usuario("eric", 17, "ericrodriguesfranco@email.com")

# Exibindo os dados do usuário
print(usuario1.exibir_dados())

# Atualizando o email do usuário
usuario1.atualizar_email("nova.ana@email.com")
print(usuario1.exibir_dados())
print(usuario1.exibir_dados())
from datetime import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, email):
        self.nome = nome
        self.__email = email
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")  # Convertendo string para data

    @property
    def idade(self):
        """Calcula a idade do usuário automaticamente"""
        hoje = datetime.today()
        return hoje.year - self.data_nascimento.year

    def exibir_dados(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.__email}"

# Criando um usuário
usuario3 = Usuario("Mariana Silva", "15/06/1995", "mariana@email.com")
print(usuario3.exibir_dados())
from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository

class AlunoService:
    def __init__(self, repository: AlunoRepository) -> None:
        self.repository = repository

    def criar_aluno(self) :
        try:
            nome = input("Digite seu nome: ")
            sobrenome = input("Digite seu sobrenome: ")
            email = input("Digite seu e-mail: ")
            senha = input("Digite seu senha: ")
            aluno = Aluno(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
            self.repository.salvar_aluno(aluno)
            print("Aluno salvo com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    # def deletar_aluno(self):
    #     try:
            
    #         aluno = 
    #         self.repository.deletar_aluno(aluno)
    #         print("Aluno deletado com sucesso")
    #     except TypeError as e:
    #         print(f"Erro ao deletar o arquivo: {e}")
    #     except Exception as e:
    #         print(f"Ocorreu um erro inesperado: {e}")

    def listar_todos_alunos(self):
        return self.repository.listar_todos_alunos()
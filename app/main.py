import os
from services.aluno_services import AlunoService
from repositories.aluno_repository import AlunoRepository
from config.connection import Session

os.system("cls || clear")

def main():
    session = Session()
    repository = AlunoRepository(session)
    service = AlunoService(repository)

    service.criar_aluno

    print("\nListando todos os alunos: ")
    alunos = service.listar_todos_alunos()

    for aluno in alunos:
        print(f"{aluno.nome} - {aluno.email}")

if __name__ == "__main__":
        main()


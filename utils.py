from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Carlos', idade=46)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Carlos').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Carlos').first()
    pessoa.nome = 'Oliveira'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Carlos').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('jose', '1234')
    insere_usuario('carlos', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #consulta_pessoas()

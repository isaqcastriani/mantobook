# Bem vindo à Biblioteca "Manto Book"

def print_header(title):
    print("\n" + "*" * 50)
    print(title.center(50))
    print("*" * 50 + "\n")

biblioteca = {
    '1984': {'quantidade': 3, 'detalhes': 'Autor: George Orwell, 1984 mostra uma futura realidade distópica ocorrida no ano de 1984.'},
    'O Senhor dos Anéis': {'quantidade': 1, 'detalhes': 'Autor: J. R. R. Tolkien, A história narra o conflito contra o mal que se alastra pela Terra-média, através da luta de várias raças.'},
    'O Príncipe': {'quantidade': 7, 'detalhes': 'Autor: Maquiavel, O Príncipe apresenta ao leitor os detalhes dos principados da época. Maquiavel os dividiu em hereditários, civis ou eclesiásticos.'}
}

def adicionar_livro():
    print_header("Adicionar Novo Livro")
    titulo = input("Digite o título do livro: ")
    detalhes = input("Conte sobre o resumo do livro: ")
    quantidade = int(input("Digite a quantidade de livros: "))
    biblioteca[titulo] = {'quantidade': quantidade, 'detalhes': detalhes}
    print(f"\nO livro '{titulo}' foi adicionado com sucesso.")

def remover_livro():
    print_header("Remover Livro")
    titulo = input("Qual livro você quer remover? ")
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"\nO livro '{titulo}' foi removido com sucesso.")
    else:
        print("\nEste livro não foi encontrado aqui na biblioteca")

def ajustar_estoque():
    print_header("Ajustar Estoque")
    titulo = input("Qual livro você quer ajustar o estoque? ")
    if titulo in biblioteca:
        nova_quantidade = int(input("Digite a nova quantidade que terá em estoque: "))
        biblioteca[titulo]['quantidade'] = nova_quantidade
        print(f"\nEstoque do livro '{titulo}' ajustado para {nova_quantidade}.")
    else:
        print("\nLivro não encontrado na biblioteca.")

def listar_livros():
    print_header("Livros Disponíveis na Biblioteca")
    for titulo, info in biblioteca.items():
        print(f"{titulo} - Quantidade: {info['quantidade']}")

def pegar_livro():
    print_header("Pegar Livro Emprestado")
    titulo = input("Qual livro você deseja pegar emprestado? ")
    if titulo in biblioteca and biblioteca[titulo]['quantidade'] > 0:
        biblioteca[titulo]['quantidade'] -= 1
        print(f"\nVocê pegou o livro '{titulo}' emprestado.")
    else:
        print("\nEste livro não está disponível no momento")

def devolver_livro():
    print_header("Devolver Livro")
    titulo = input("Qual livro você quer devolver? ")
    if titulo in biblioteca:
        biblioteca[titulo]['quantidade'] += 1
        print(f"\nO livro '{titulo}' foi devolvido! :) Obrigado pela preferência.")
    else:
        print("\nMano, não foi aqui que você pegou esse livro.")

def detalhes_livro():
    print_header("Detalhes do Livro")
    titulo = input("Qual livro você gostaria de saber mais? ")
    if titulo in biblioteca:
        print(f"\nDetalhes do livro '{titulo}': {biblioteca[titulo]['detalhes']}")
    else:
        print("\nLivro não encontrado na biblioteca.")

def menu_admin():
    while True:
        print_header("Menu Admin")
        print("1 - Adicionar novo livro à biblioteca")
        print("2 - Remover livro")
        print("3 - Listar todos os livros e ajustar o estoque")
        print("4 - Sair")
        opcao = input("Opção: ")
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            remover_livro()
        elif opcao == '3':
            listar_livros()
            ajustar_estoque()
        elif opcao == '4':
            break
        else:
            print("\nEscolha uma opção da lista!!!")

def menu_cliente():
    print_header("Bem vindo à Biblioteca Manto Book, o que deseja?")
    while True:
        print("\n[Cliente] Escolha uma opção:")
        print("1 - Ver lista de livros disponíveis")
        print("2 - Pegar um livro emprestado")
        print("3 - Devolver um livro")
        print("4 - Ver detalhes do livro")
        print("5 - Sair")
        opcao = input("Opção: ")
        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            pegar_livro()
        elif opcao == '3':
            devolver_livro()
        elif opcao == '4':
            detalhes_livro()
        elif opcao == '5':
            break
        else:
            print("\nEscolha uma opção da lista!!!")

def main():
    print("\n" + "=" * 50)
    print("=== Bem-vindo à Biblioteca Manto Book ===".center(50))
    print("=" * 50)
    senha_correta = "123"
    while True:
        tipo_usuario = input("\nIdentifique-se - Dono da biblioteca ou Cliente? (admin/cliente/sair): ")
        if tipo_usuario.lower() == 'admin':
            senha = input("Digite a senha de acesso: ")
            if senha == senha_correta:
                menu_admin()
            else:
                print("\nSenha incorreta! Acesso negado.")
        elif tipo_usuario.lower() == 'cliente':
            menu_cliente()
        elif tipo_usuario.lower() == 'sair':
            print("\nSaindo da biblioteca, foi um prazer ter você conosco! :)")
            break
        else:
            print("\nUsuário selecionado não reconhecido. Por favor, escolha uma opção válida.")

main()
# Manto Book 📕

Um sistema de biblioteca de aluguel em Python, com funções de admin, cliente, e menus personalizados para cada um.
Caso queria ver o código em ação **[Clique aqui.](https://colab.research.google.com/drive/1rkOHvSgBqbVK2BJWTIVBE7Szhw2Jz4dC?usp=sharing)** 
## 🚀 Começando

O código começa dando opção ao usuário, apresentando a opção de ele poder escolher ser cliente ou administrador.
 Caso ele escolher ser cliente, ele será redirecionado para um menu específico de cliente.
Caso ele escolher ser adminsitrador, será necessário uma senha (123) para acessar o menu de admin.
Caso ele escolha sair, a mensagem exibida é

```py
print("\nSaindo da biblioteca, foi um prazer ter você conosco! :)")
```

### Execução -

```py
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
```

### Resultado -

![image](https://github.com/isaqcastriani/mantobook/assets/82527480/b5197776-0650-4b8d-894c-f7631d619105)

## Opções do ADM 👨🏼‍💻

Assim que o usuário escolher ser admin, o código abaixo será executado 👇🏻
```py
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
```

Nesse menu acima, o usuário pode **adicionar novos livros à biblioteca**, **remover livros**, **listar todos os livros disponíveis**, **ajuste de estoque** e a opção de **sair** (trocar admin por cliente ou sair)

📕 Ao usuário escolher a opção **1**   - `(adicionar livro)`.
```py
def adicionar_livro():
    print_header("Adicionar Novo Livro")
    titulo = input("Digite o título do livro: ")
    detalhes = input("Conte sobre o resumo do livro: ")
    quantidade = int(input("Digite a quantidade de livros: "))
    biblioteca[titulo] = {'quantidade': quantidade, 'detalhes': detalhes}
    print(f"\nO livro '{titulo}' foi adicionado com sucesso.")
    ### Adiciona livros com nome, detalhes e estoque
```
📕 Ao usuário escolher a opção **2**   - `(remover livro)`.
```py
def remover_livro():
    print_header("Remover Livro")
    titulo = input("Qual livro você quer remover? ")
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"\nO livro '{titulo}' foi removido com sucesso.")
    else:
        print("\nEste livro não foi encontrado aqui na biblioteca")
    ### Pode remover qualquer livro, e excluir da biblioteca
```
📕 Ao usuário escolher a opção **3**   - `(Listar todos os livros e ajustar o estoque)`.
```py
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
    ### Ajusta estoque dos livros
    ### Vê os livros disponíveis na biblioteca
```

📕 Ao usuário escolher a opção **4**   - `(Sair)`.
```py
break 
### O programa pergunta à ele novamente qual usuário ele quer escolher
```
### Resultado -

![image](https://github.com/isaqcastriani/mantobook/assets/82527480/3eda49ae-4631-48c4-aa4d-ae17fc697aaa)

## Opções do Cliente 🙋🏼

Assim que o usuário escolher ser cliente, o código abaixo será executado 👇🏻

```py
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
```
Nesse menu acima, o usuário pode **listar os livros disponíveis** e **ver estoque**, **alugar livros**, **devolver o livro pego**, **ver detalhes dos livros** - `(como autor, resumo do livro...)` e e a opção de **sair** (trocar admin por cliente ou sair)

📕 Ao usuário escolher a opção **1**   - `(listar livros)`.
```py
def listar_livros():
    print_header("Livros Disponíveis na Biblioteca")
    for titulo, info in biblioteca.items():
        print(f"{titulo} - Quantidade: {info['quantidade']}")
    ### Vê os livros disponíveis e quantidade em estoque
```

📕 Ao usuário escolher a opção **2**   - `(pegar livro)`.
```py
def pegar_livro():
    print_header("Pegar Livro Emprestado")
    titulo = input("Qual livro você deseja pegar emprestado? ")
    if titulo in biblioteca and biblioteca[titulo]['quantidade'] > 0:
        biblioteca[titulo]['quantidade'] -= 1
        print(f"\nVocê pegou o livro '{titulo}' emprestado.")
    else:
        print("\nEste livro não está disponível no momento")
    ### O usuário pega um livro disponível na biblioteca (O estoque diminui)
```

📕 Ao usuário escolher a opção **3**   - `(devolver livro)`.
```py
def devolver_livro():
    print_header("Devolver Livro")
    titulo = input("Qual livro você quer devolver? ")
    if titulo in biblioteca:
        biblioteca[titulo]['quantidade'] += 1
        print(f"\nO livro '{titulo}' foi devolvido! :) Obrigado pela preferência.")
    else:
        print("\nMano, não foi aqui que você pegou esse livro.")
    ### O usuário devolve um livro que ele tenha pego (O estoque aumenta +1)
```

📕 Ao usuário escolher a opção **4**   - `(Sair)`.
```py
break 
### O programa pergunta à ele novamente qual usuário ele quer escolher
```
### Resultado -

![image](https://github.com/isaqcastriani/mantobook/assets/82527480/d179364c-96d5-42d9-a01c-fb0d5044e37f)

## Linguagem utilizada

[![My Skills](https://skillicons.dev/icons?i=py&perline=3)](https://skillicons.dev)

## *Developers* 👨🏼‍💻👨🏻‍💻

#### Developers do projeto:
---
<img src="https://media.discordapp.net/attachments/821393692493479987/1239654076749451387/Group_15.png?ex=664506d3&is=6643b553&hm=2c761c6f62f3dea2d30ba41c42237bc85765be788db13127ddc6240dd3c3d216&=&format=webp&quality=lossless&width=687&height=332"></a>

```
Links do nosso GitHub👇🏻
```
- **Isaque Castriani** - _DEV_ - [Github](https://github.com/isaqcastriani)
- **Luan Dias** - _DEV_ - [Github](https://github.com/diasluann)

---

⌨️ tmj

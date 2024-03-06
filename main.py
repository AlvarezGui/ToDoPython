tasks = dict()
fechar = False

# Funções
def add(task):
    tasks[task] = False 

def view():
    for i in tasks:
        if not tasks[i]:
            print(f'-{i}')
        else:
            print(f'_{i}')

def remove(task):
    tasks.pop(task)

def update(task):
    tasks.update({task: True})

# Inputs
while fechar != True:
    acao = input("Fazer: ").strip()
    if acao == "add":
        add(input("adicionar: "))
    elif acao == "view":
        view()
    elif acao == 'remove':
        remove(input("Remover: "))
    elif acao == "exit":
        fechar = True
    elif acao == "update":
        update(input("Update: "))
    else:
        print("Comando inválido")



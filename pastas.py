import os


#mvc


p = input("Projeto: ")

for d in ["controllers", "services", "repositories", "models"]:
    os.makedirs(f"{p}/app/{d}", exist_ok=True)
    open(f"{p}/app/{d}/__init__.py", "w").close()

open(f"{p}/app/__init__.py", "w").close()


# -----------------------------------------

import os

p = input("Nome do projeto: ")

estrutura = [
    'app/controllers',
    "app/services",
    'app/repositories',
    "app/models",
    "templates"
]

arquivos = [
    'app/__init__.py',
    'app/controllers/user_controller.py',
    "app/services/user_service.py",
    "app/repositories/user_repository.py",
    "app/models/user_model.py",
    "templates/index.html",
    "run.py",
    "config.py"
]

for pasta in estrutura:
    os.makedirs(f"{p}/{pasta}", exist_ok=True)

for arquivo in arquivos:
    open(f"{p}/{arquivo}", "w").close()

print("Estrutura criada.")

import os  # Importamos o módulo os para ler as variáveis de ambiente

# 1. Importa a função que cria o Flask (ajustado para o padrão comum de pacotes)
try:
    from app import create_app
except ModuleNotFoundError:
    # Caso seu arquivo se chame app.py na raiz, usamos o import direto
    from app.app import create_app 

# 2. Importa a inicialização do banco de dados que criamos
from app.repositories.user_repository import init_db

# 3. Inicializa a variável 'app' chamando a função de fábrica (Application Factory)
app = create_app()

if __name__ == "__main__":
    init_db()  # Garante que a tabela 'users' exista no SQLite antes de ligar o servidor
    
    # O Render define a variável 'PORT' automaticamente. 
    # Se não encontrar (rodando local), ele usa a porta 5000 por padrão.
    porta = int(os.environ.get("PORT", 5000))
    
    # Opcional: só ativa o debug se NÃO estiver rodando no Render
    em_producao = "RENDER" in os.environ
    
    app.run(
        host="0.0.0.0", 
        port=porta, 
        debug=not em_producao
    )

from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
DATABASE_URL = os.getenv('DATABASE_URL')  # URL do banco de dados

# Usando uma imagem base de Python
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de requisitos do projeto para o contêiner
COPY vinculus_notificacao/requirements.txt requirements.txt

# Instalar dependências do projeto
RUN pip install -r requirements.txt

# Copiar o código do projeto para o contêiner
COPY . /app

WEBSITED_PORT: 8080

PORT: 8080

# Comando para executar a aplicação
CMD ["python", "vinculus_notificacao/Notificacao.py"]

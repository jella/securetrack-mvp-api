Dockerfile# Usar uma imagem base do Python
FROM python:3.9-slim

# Setar diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o requirements.txt para o diretório de trabalho
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . /app/

# Expor a porta onde a aplicação Flask vai rodar
EXPOSE 5000

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]
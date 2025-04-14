# Usa imagem Python leve
FROM python:3.11-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar o Flask no container
CMD ["python", "app.py"]
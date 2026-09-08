# Imagem base leve com Python 3.12
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copia apenas o requirements primeiro para aproveitar o cache de camadas do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código-fonte
COPY app/ ./app/
COPY tests/ ./tests/

# Porta exposta pela aplicação Flask
EXPOSE 5000

# Variável de ambiente para modo de produção
ENV FLASK_ENV=production

# Comando padrão ao iniciar o container
CMD ["python", "app/app.py"]

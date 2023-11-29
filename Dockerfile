# Use a versão específica do Python
FROM python:3.11.4

# Configuração das variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir o diretório de trabalho
WORKDIR /app

# Copiar apenas o arquivo de requisitos e instalá-lo
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação
COPY . /app/

# CMD para iniciar o servidor de desenvolvimento do Django na porta 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


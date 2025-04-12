FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Definir variáveis de ambiente para conexão com o MySQL
ENV MYSQL_HOST=mysql-container
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=senha123
ENV MYSQL_DATABASE=microssistema

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
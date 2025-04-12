import os
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "message": "O microsserviço está funcionando corretamente!"
    })

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        # Conecta ao MySQL usando variáveis de ambiente
        conn = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'mysql-container'),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', 'senha123'),
            database=os.environ.get('MYSQL_DATABASE', 'microssistema')
        )
        
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
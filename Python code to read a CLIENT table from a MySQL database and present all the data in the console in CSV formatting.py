import mysql.connector # pip install mysql-connector
import csv
import sys

def conectar_bd():
    return mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco"
    )

def obter_clientes():
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM CLIENTE")
    colunas = [desc[0] for desc in cursor.description]
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return colunas, linhas

def imprimir_csv():
    colunas, linhas = obter_clientes()
    escritor = csv.writer(sys.stdout)
    escritor.writerow(colunas)  # Cabeçalho
    escritor.writerows(linhas)  # Dados

if __name__ == "__main__":
    imprimir_csv()
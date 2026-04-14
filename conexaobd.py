import mysql.connector


def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vinicius@1243",
        database="lad_py"
    )
    return conexao

def testar_conexao():
    try:
        conexao = conectar_banco()
        if conexao.is_connected():
            print("Conexao com o banco realizada com sucesso.")
        conexao.close()
    except mysql.connector.Error as erro:
        print(erro)
    return conexao

testar_conexao()
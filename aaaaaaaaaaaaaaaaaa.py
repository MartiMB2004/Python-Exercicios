import mariadb

conn = mariadb.connect(
    user="root",
    password="",
    host="localhost",
    port=3306,
    database="teste_phython"
)
cursor = conn.cursor()

dados =[]
dados.append(input("Nome: "))
dados.append(int(input("Idade: ")))
dados.append(input("Sobrenome: "))
dados.append(input("Cidade: "))

cursor.execute(
    "INSERT INTO testepythondb (nome, idade, sobrenome, cidade) VALUES (?, ?, ?, ?)",
    dados
)

conn.commit()
print("Dados inseridos com sucesso!")
conn.close()

'''cursor = conn.cursor()

nome = input("digie o nome: ")
idade = int(input("Digite a idade: "))
sobrenome = input("digite o sobrenome: ")
cidade = input("Digite a cidade: ")

cursor.execute(
    "INSERT INTO testepythondb (nome, idade, sobrenome, cidade) VALUES (?, ?, ?, ?)",
    (nome, idade , sobrenome, cidade)
)

conn.commit()
print("Usuário inserido com sucesso!")
conn.close()

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="teste_erro"
    )
    cursor = conn.cursor()
    print("Conexão realizada com sucesso!")

except mariadb.Error as e:
    print("erro ao conectar no banco:", e)

finally:
    if conn:
        conn.close()
        print("conexão encerrada")'''
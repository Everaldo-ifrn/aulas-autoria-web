from flask import Flask, request, jsonify
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='enapne'
)


def pegando_info():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM anexo1 WHERE ")
    objetos = cursor.fetchall()
    cursor.close()
    return objetos

print(pegando_info())



# --------------- ANOTAÇÕES DICIONÁRIO ----------------
#dicionario
"""dicionario = {
    "chave": "valor",
    "chave II": "valor II"
}"""

# pegando um valor de uma chave especídifca "chave"
"""valor = dicionario["chave"]"""

# adicionando uma nova chave e novo valor
"""dicionario["novaChave"] = "novoValor"""

# Ver todas as chaves
  #1. usando for
"""for chave in dicionario:
    print(chave)"""

  #2. usando dicionario.keys() OBS: retorna uma lista de chaves
"""print(dicionario.keys())"""

# Apagando chave e valor
"""dicionario.pop("novaChave")"""

# Vendo se exite a chave no dicionario
"""if "chave" in dicionario:
    print("Existe")
else:
    print("Não existe")"""

# Vendo se existe o valor no dicionario
"""if "valor" in dicionario.values():
    print("Exite")
else:
    print("Não existe")"""


[{'id': 1, 
  'numeroPei': '1', 'historico': 'Histórico do aluno I', 'conhecimentosHabilidades': 'Conhecimentos e habilidades I', 'dificuldades': 'Dificuldades do aluno I', 'observacoes': 'Observações gerais I'}, {'id': 2, 'numeroPei': '2', 'historico': 'Histórico do aluno II', 'conhecimentosHabilidades': 'Conhecimentos e habilidades II', 'dificuldades': 'Dificuldades do aluno II', 'observacoes': 'Observações gerais II'}, {'id': 3, 'numeroPei': '3', 'historico': 'Histórico do aluno III', 'conhecimentosHabilidades': 'Conhecimentos e habilidades III', 'dificuldades': 'Dificuldades do aluno III', 'observacoes': 'Observações gerais III'}]
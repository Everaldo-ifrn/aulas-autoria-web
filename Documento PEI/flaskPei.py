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
    cursor.execute("SELECT pei.numero, anexo1.historico, anexo1.conhecimentosHabilidades, anexo1.dificuldades, anexo1.observacoes, pei.matriculaAluno, anexo2.nome, aluno.codigoCurso, necessidadesEspecificas, curso.codigo, curso.coordenador, curso.campus, curso.nivelEnsino, equipeMultiDisciplinar.fucao, anexo2.disciplina,  FROM anexo1 INNER JOIN pei on anexo1.numeroPei = pei.numero INNER JOIN aluno on pei.matriculaAluno = aluno.matricula INNER JOIN curso on aluno.codigoCurso = curso.codigo INNER JOIN equipeMultiDisciplinar on equipeMultiDisciplinar.numeroPei = pei.numero INNER JOIN anexo2 on anexo2.numeroPei = pei.numero INNER JOIN anexo3 on anexo3.numeroPei = pei.numero INNER JOIN acompanhamento on acompanhamento.idAnexo2 = anexo2.id")
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


[{'id': 1, #Anexo1
  'numeroPei': '1', #Anexo1
  'historico': 'Histórico do aluno I', #Anexo1
  'conhecimentosHabilidades': 'Conhecimentos e habilidades I', #Anexo1
  'dificuldades': 'Dificuldades do aluno I', #Anexo1
  'observacoes': 'Observações gerais I', #Anexo1
  'numero': '1', #pei
  'matriculaAluno': '2023001', #pei
  'matricula': '2023001', #aluno
  'nome': 'E1', #anexo2
  'codigoCurso': '1111', #aluno
  'necessidadesEspecificas': 'visão', #aluno
  'codigo': 1122, #curso
  'coordenador': 'Gilbran Andrade', #curso
  'campus': 'Ceará-Mirim', #curso
  'nivelEnsino': 'Médio', #curso
  'funcao': 'Ajuda na visao', #equipeMultiDisciplinar
  'disciplina': 'Matemática', #anexo2
  'docente': 'Prof. Silva', #anexo2
  'objetivosPlanoDisciplina': 'Objetivos do Plano I', #anexo2
  'objetivosAdaptacoesDisciplina': 'Objetivos das Adaptações I', #anexo2
  'conteudoPlanoDisciplina': 'Conteúdo do Plano I', #anexo2
  'conteudoAdaptacoesDisciplina': 'Conteúdo das Adaptações I', #anexo2
  'metodologiaPlanoDisciplina': 'Metodologia do Plano I', #anexo2
  'metodologiaAdaptacoesDisciplina': 'Metodologia das Adaptações I', #anexo2
  'recursoDidaticoPlanoDisciplina': 'Recursos Didáticos do Plano I', #anexo2
  'recursoDidaticoAdaptacoesDisciplina': 'Recursos Didáticos das Adaptações I', #anexo2
  'avaliacaoPlanoDisciplina': 'Avaliação do Plano I', #anexo2
  'avaliacaoAdaptacoesDisciplina': 'Avaliação das Adaptações I', #anexo2
  'avancos': 'melhorou visão', #anexo3
  'parecer': 'Não sei I', #anexo3
  'data': datetime.date(2023, 11, 20), #acompanhamento
  'descricao': 'Hoje foi bem', #acompanhamento
  'idAnexo2': 1}, #acompanhamento
  
  
  {'id': 2, 'numeroPei': '2', 'historico': 'Histórico do aluno II', 'conhecimentosHabilidades': 'Conhecimentos e habilidades II', 'dificuldades': 'Dificuldades do aluno II', 'observacoes': 'Observações gerais II', 'numero': '2', 'matriculaAluno': '2023002', 'matricula': '2023002', 'nome': 'E2', 'codigoCurso': '2222', 'necessidadesEspecificas': 'Audição', 'codigo': 2233, 'coordenador': 'Pessoa I', 'campus': 'cm', 'nivelEnsino': 'medio', 'funcao': 'Ajudar na audição', 'disciplina': 'Matemática', 'docente': 'Prof. Silva', 'objetivosPlanoDisciplina': 'Objetivos do Plano II', 'objetivosAdaptacoesDisciplina': 'Objetivos das Adaptações II', 'conteudoPlanoDisciplina': 'Conteúdo do Plano II', 'conteudoAdaptacoesDisciplina': 'Conteúdo das Adaptações II', 'metodologiaPlanoDisciplina': 'Metodologia do Plano II', 'metodologiaAdaptacoesDisciplina': 'Metodologia das Adaptações II', 'recursoDidaticoPlanoDisciplina': 'Recursos Didáticos do Plano II', 'recursoDidaticoAdaptacoesDisciplina': 'Recursos Didáticos das Adaptações II', 'avaliacaoPlanoDisciplina': 'Avaliação do Plano II', 'avaliacaoAdaptacoesDisciplina': 'Avaliação das Adaptações II', 'avancos': 'melhorou audição', 'parecer': 'Não sei II', 'data': datetime.date(2023, 11, 22), 'descricao': 'Hoje foi mais ou menos', 'idAnexo2': 2}, 


{'id': 3, 'numeroPei': '3', 'historico': 'Histórico do aluno III', 'conhecimentosHabilidades': 'Conhecimentos e habilidades III', 'dificuldades': 'Dificuldades do aluno III', 'observacoes': 'Observações gerais III', 'numero': '3', 'matriculaAluno': '2023003', 'matricula': '2023003', 'nome': 'E3', 'codigoCurso': '3333', 'necessidadesEspecificas': 'Mobilidade', 'codigo': 3344, 'coordenador': 
'Pessoa II', 'campus': 'cm', 'nivelEnsino': 'medio', 'funcao': 'Ajudar na locomoção', 'disciplina': 'Matemática', 'docente': 'Prof. Silva', 'objetivosPlanoDisciplina': 'Objetivos do Plano III', 'objetivosAdaptacoesDisciplina': 'Objetivos das Adaptações III', 'conteudoPlanoDisciplina': 'Conteúdo do Plano III', 'conteudoAdaptacoesDisciplina': 'Conteúdo das Adaptações III', 'metodologiaPlanoDisciplina': 'Metodologia do Plano III', 'metodologiaAdaptacoesDisciplina': 'Metodologia das Adaptações III', 'recursoDidaticoPlanoDisciplina': 'Recursos Didáticos do Plano III', 'recursoDidaticoAdaptacoesDisciplina': 
'Recursos Didáticos das Adaptações III', 'avaliacaoPlanoDisciplina': 'Avaliação do Plano III', 'avaliacaoAdaptacoesDisciplina': 'Avaliação das Adaptações III', 'avancos': 'melhorou mobilidade', 'parecer': 'Não sei III', 'data': datetime.date(2023, 11, 23), 'descricao': 'Hoje foi ruim', 'idAnexo2': 3}]

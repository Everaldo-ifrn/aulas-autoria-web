# Ordem das inserções
-- 1. Curso
-- 2. Aluno
-- 3. Pei
-- 4. equipeMultiDisciplinar
-- 5. Anexo 2
-- 6. Anexo 3
-- 7. Acompanhamento
-- 8. equipeNapne
-- 9. anexo1 

USE enapne;

select * from curso;

/*INSERT INTO curso (codigo, nome, coordenador, campus, nivelEnsino) VALUES 
	('1111', 'Info', 'Gilbran Andrade', 'Ceará-Mirim', 'Médio'),
    ('2222', 'ebm', 'Pessoa I', 'cm', 'medio'),
    ('3333', 'pjd', 'Pessoa II', 'cm', 'medio');*/

/*INSERT INTO enapne.aluno (matricula, nome, codigoCurso, necessidadesEspecificas) VALUES
	('2023001', 'João Silva', '1111', 'visão'),
    ('2023002', 'Lucas', '2222', 'Audição'),
    ('2023003', 'José', '3333', 'Mobilidade');*/

/*INSERT INTO pei (numero, matriculaAluno) VALUES
	('1', '2023001'),
    ('2', '2023002'),
    ('3', '2023003');*/

/*INSERT INTO equipeMultiDisciplinar (codigo, nome, funcao, numeroPei) VALUES
	('1122', 'E1', 'Ajuda na visao', '1'),
    ('2233', 'E2', 'Ajudar na audição', '2'),
    ('3344', 'E3', 'Ajudar na locomoção', '3');*/
    
/*INSERT INTO enapne.anexo2 (numeroPei, disciplina, docente, objetivosPlanoDisciplina, objetivosAdaptacoesDisciplina, conteudoPlanoDisciplina, conteudoAdaptacoesDisciplina, metodologiaPlanoDisciplina, metodologiaAdaptacoesDisciplina, recursoDidaticoPlanoDisciplina, recursoDidaticoAdaptacoesDisciplina, avaliacaoPlanoDisciplina, avaliacaoAdaptacoesDisciplina) VALUES 
	('1', 'Matemática', 'Prof. Silva', 'Objetivos do Plano I', 'Objetivos das Adaptações I', 'Conteúdo do Plano I', 'Conteúdo das Adaptações I', 'Metodologia do Plano I', 'Metodologia das Adaptações I', 'Recursos Didáticos do Plano I', 'Recursos Didáticos das Adaptações I', 'Avaliação do Plano I', 'Avaliação das Adaptações I'),
    ('2', 'Matemática', 'Prof. Silva', 'Objetivos do Plano II', 'Objetivos das Adaptações II', 'Conteúdo do Plano II', 'Conteúdo das Adaptações II', 'Metodologia do Plano II', 'Metodologia das Adaptações II', 'Recursos Didáticos do Plano II', 'Recursos Didáticos das Adaptações II', 'Avaliação do Plano II', 'Avaliação das Adaptações II'),
    ('3', 'Matemática', 'Prof. Silva', 'Objetivos do Plano III', 'Objetivos das Adaptações III', 'Conteúdo do Plano III', 'Conteúdo das Adaptações III', 'Metodologia do Plano III', 'Metodologia das Adaptações III', 'Recursos Didáticos do Plano III', 'Recursos Didáticos das Adaptações III', 'Avaliação do Plano III', 'Avaliação das Adaptações III');*/

/*INSERT INTO anexo3 (numeroPei, avancos, parecer) VALUES
	('1', 'melhorou visão', 'Não sei I'),
    ('2', 'melhorou audição', 'Não sei II'),
    ('3', 'melhorou mobilidade', 'Não sei III');*/

/*INSERT INTO acompanhamento (data, descricao, idAnexo2) VALUES
	('2023-11-20', 'Hoje foi bem', '1'),
    ('2023-11-22', 'Hoje foi mais ou menos', '2'),
    ('2023-11-23', 'Hoje foi ruim', '3');*/

/*INSERT INTO equipeNapne (nome, funcao, ativo, usuario, senha) VALUES
	('Da visao', 'adaptar papeis', b'1', 'user I', 'senha I'),
    ('Da audição', 'adaptar vídeos', b'1', 'user II', 'senha II'),
    ('Da locomoção', 'adaptar escadas', b'1', 'user III', 'senha III');*/

/*INSERT INTO enapne.anexo1 (numeroPei, historico, conhecimentosHabilidades, dificuldades, observacoes) VALUES 
	('1', 'Histórico do aluno I', 'Conhecimentos e habilidades I', 'Dificuldades do aluno I', 'Observações gerais I'),
    ('2', 'Histórico do aluno II', 'Conhecimentos e habilidades II', 'Dificuldades do aluno II', 'Observações gerais II'),
    ('3', 'Histórico do aluno III', 'Conhecimentos e habilidades III', 'Dificuldades do aluno III', 'Observações gerais III');*/

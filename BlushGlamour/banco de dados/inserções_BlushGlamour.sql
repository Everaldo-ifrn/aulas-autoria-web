USE `mydb`;
-- DROP DATABASE `mydb`;
/*
INSERT INTO Cliente (cpf, nome, email, senha, dataNascimento, imagemPerfil) VALUES 
	('12345678901', 'Maria S.ilva', 'maria@email.com', 'senha123', '1990-05-15', 'perfil.jpg');

INSERT INTO Carrinho (carrinhoID, Cliente_cpf) VALUES 
	(1, '12345678901');

INSERT INTO Vendas (vendaID, valorTotal, carrinhoID) VALUES
	(1, 100.0, 1);

INSERT INTO Carrinho_has_Produtos (Carrinho_carrinhoID, Produtos_codigoDeBarra, quantidade, total) VALUES 
	(1, 17745, 2, 100.0);
*/
SELECT
	p.codigoDeBarra,
    p.nomeProduto,
    p.descricao,
    p.preco,
    MAX(i.imgMaisVendido) as imgMaisVendido,
    SUM(chp.quantidade) as total_vendido
FROM
	Vendas v
    INNER JOIN Carrinho c ON v.carrinhoID = c.carrinhoID
    INNER JOIN Carrinho_has_Produtos chp ON c.CarrinhoID = chp.Carrinho_carrinhoID
    INNER JOIN Produtos p ON chp.Produtos_codigoDeBarra = p.codigoDeBarra
    INNER JOIN Imagens i ON i.Produtos_codigoDeBarra = p.codigoDeBarra
GROUP BY
	p.codigoDeBarra
LIMIT 5;

/*
-- Pegando todos os dados de Cliente específico
SELECT 
	* 
FROM 
	Cliente
INNER JOIN 
	EnderecosCliente
INNER JOIN
	Telefone
WHERE
	Cliente.cpf = '12345678901' AND Cliente.cpf = EnderecosCliente.Cliente_cpf AND Cliente.cpf = Telefone.Cliente_cpf
*/

/*
-- Pegando dados de um Fornecedor específico
SELECT
	*
FROM
	Fornecedores
INNER JOIN
	EnderecosFornecedores
WHERE
	Fornecedores.cnpj = '12345678901234' AND Fornecedores.cnpj = EnderecosFornecedores.cnpjFornecedores
*/

/*
-- Inserção na tabela Cliente
INSERT INTO Cliente (cpf, nome, email, senha, dataNascimento, imagemPerfil)
VALUES ('12345678901', 'Maria S.ilva', 'maria@email.com', 'senha123', '1990-05-15', 'perfil.jpg');

-- Inserção na tabela Categoria
INSERT INTO Categoria (nomeCategoria, descricaoCategoria)
VALUES 
	('Base', 'Produtos para maquiagem dos olhos'),
    ('Batom', 'Produtos para os lábios'),
    ('Delineado', 'Produtod para os cílios');
-- Inserção na tabela Fornecedores
INSERT INTO Fornecedores (cnpj, nomeFornecedor, EmailFornecedor, senhaFornecedorl, telefoneFornecedor)
VALUES 
	('12345678901234', 'Fornecedor Base', 'fornecedor1@xyz.com', 'forn123', '981111111'),
	('11223344556677', 'Fornecedor Batom', 'fornecedor2@xyz.com', 'forn321', '982222222'),
    ('12345678901240', 'Fornecedor Batom', 'fornecedor3@xyz.com', 'forn333', '982222244'),
    ('11223344556650', 'Fornecedor Batom', 'fornecedor4@xyz.com', 'forn222', '982222233'),
    ('43210987654321', 'Fornecedor Delineado', 'fornecedor5@xyz.com', 'forn444', '983333333');

-- Inserção na tabela Produtos
INSERT INTO Produtos (codigoDeBarra, nomeProduto, preco, quantidade_estoque, descricao, Categoria_idcategoria, cnpjFornecedor)
VALUES 
	(11111, 'Base Boca Rosa', 68.00, 100, 'Boca rosa By Payot Mate 03 FRancisca, 30 ml', 1, '12345678901234'),
	(22222, 'Batom Bruna Tavares', 39.90, 100, 'Batom Líquido Bruna Matte - Bt, Bruna Tavares', 2, '11223344556677'),
    (33333, 'Delineado Mari Maria', 47.50, 100, 'Delineador Líquido Spot, Mari Maria', 3, '43210987654321'),
    (44444, 'Base Mari Maria', 29.90, 100, 'Base Aveludada e Uniforme, Mari Maria', 1, '12345678901240'),
    (55555, 'Batom Ruby Rose', 28.80, 100, 'Batom liquido matte melu', 2, '11223344556650');

-- Inserção na tabela EnderecosCliente
INSERT INTO EnderecosCliente (rua, cidade, cep, estado, numResidencia, Complemento, Cliente_cpf, bairro)
VALUES ('Rua das Flores', 'São Paulo', '12345-678', 'SP', '100', 'Apto 101', '12345678901', 'Centro');

-- Inserção na tabela Carrinho
INSERT INTO Carrinho (carrinhoID, Cliente_cpf)
VALUES (1, '12345678901');

-- Inserção na tabela Vendas
INSERT INTO Vendas (vendaID, valorTotal, carrinhoID)
VALUES (1, 50.00, 1);

-- Inserção na tabela Imagens
INSERT INTO Imagens (idImagens, Produtos_codigoDeBarra, imgCard, imgMaisVendido, imgProduto)
VALUES 
	(1, 11111, NULL, 'imagens/produtos/Bases/BaseBocaRosa01.png', NULL), 
    (2, 22222, NULL, 'imagens/produtos/Batons/BatomBrunaTavares03_semFundo.png', NULL), 
    (3, 33333, NULL, 'imagens/produtos/Delineadores/DelineadorMari01_semFundo.png', NULL), 
    (4, 44444, NULL, 'imagens/produtos/Bases/baseMari02_semFundo.png', NULL),
    (5, 55555, NULL, 'imagens/produtos/Batons/BatomMerubyr01_semFundo.png', NULL);

-- Inserção na tabela EnderecosFornecedores
INSERT INTO EnderecosFornecedores (rua, cidade, cep, estado, numResidencia, Complemento, cnpjFornecedores, bairro)
VALUES ('Av. Principal', 'Rio de Janeiro', '54321-098', 'RJ', '200', NULL, '12345678901234', 'Centro');

-- Inserção na tabela Telefone
INSERT INTO Telefone (idTelefone, telefone, Cliente_cpf)
VALUES (1, '987654321', '12345678901');

-- Inserção na tabela Carrinho_has_Produtos
INSERT INTO Carrinho_has_Produtos (Carrinho_carrinhoID, Produtos_codigoDeBarra, quantidade, total)
VALUES (1, 12345, 2, 51.00); 
*/


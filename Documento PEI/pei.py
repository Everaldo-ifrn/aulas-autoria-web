import pdfkit

#Criando o PEI usando HTML e CSS
html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>PEI</title>
    
</head>
<body>
    <header>
        <img src="imagens/logoRepublica.png" alt="Logo do Ministério da Educação Brasileiro" height="200px">
        <h5>Ministério da Educação </h5>
        <h5>Secretaria de Educação Profissional e Tecnológica</h5>
        <h5>Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte IFRN - Pró-Reitoria de Ensino</h5>
        <h6>Rua Dr. Nilo Ramalho,1692 – Tirol – Natal/RN CEP: 59.015-310 Telefone: (84) 4005-0750-0753 http://www.ifrn.edu.br – E-mail: proen@ifrn.edu.br</h6>
    </header>
    <main>
        <h2>ANEXO I</h2>
        <h2>PLANO EDUCACIONAL INDIVIDUALIZADO (PEI)</h2>
        <h2>HISTÓRICO DO ALUNO</h2>
        <img src="imagens/logoEnapne.png" alt="Logo do NAPNE" height="200px">

        <p> <strong>Alerta Ético</strong>: as informações contidas neste documento são consideradas reservadas e o compartilhamento das mesmas deve ser restrito apenas às/aos envolvidos na ação pedagógica, sob pena de implicações legais. </p>
        <table>
            <tr>
                <td>Nível de Ensino/ Forma: (   ) Técnico Integrado Regular  (  ) Técnico Integrado EJA  ( )Técnico Subsequente   (  ) Curso Superior de Tecnologia  (  ) Curso Superior de Licenciatura ( ) Engenharia  (  ) Pós-Graduação  ( ) Outros _________________________ </td>
            </tr>
            <tr>
                <td>Nome do estudante: </td>
            </tr>
            <tr>
                <td>Curso: </td>
            </tr>
            <tr>
                <td>Necessidades Educacionais Específicas: </td>
            </tr> 
            <tr>
                <td>Equipe multiprofissional responsável: </td>
            </tr>
        </table>

        <table>
            <tr>
                <td> <h4>HISTÓRICO PESSOAL E ESCOLAR DO (A) ESTUDANTE</h4> </td>
            </tr>
            <tr>
                <td> [] </td>
            </tr>
            <tr>
                <td> <h4>Necessidades Educacionais Específicas</h4> 
            </td>
            <tr>
                <td> [] </td>
            </tr>
            <tr>
                <td> <h4>Conhecimentos, Habilidades, Capacidades, Interesses, Necessidades (O que sabe? Do que gosta/afinidades?...)</h4> </td>
                <td> <h4>Dificuldades apresentadas</h4> </td>
            </tr>
        </table>
    </main>
    <footer>
        <p>Esta Instrução Normativa foi elaborada com base na Instrução Normativa nº 12/12/2018 do IFRS.  </p>
    </footer>
</body>
</html>
"""


#Configurando o caminho para o executável wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
#config = pdfkit.configuration(wkhtmltopdf=r"D:\\Users\\20211174010034\\Documents\\GitHub\\aulas-autoria-web\\Documento PEI\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")


#Convertendo HTML --> PDF
#pdfkit.from_string(html, "output.pdf", configuration=config)

pdfkit.from_string(html, "output.pdf", configuration=config, options={'no-images': None, 'disable-smart-shrinking': ''})

# ANOTAÇÕES
#1. pip install pdfkit
#2. instale o wkhtmltopdf.exe que transforma HTML para PDF
#3. mude o caminho para wkhtmltopdf.exe
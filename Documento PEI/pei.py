import pdfkit

#Criando o PEI usando HTML e CSS
html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Anexo I</title>
    <style>
        @page {
            size: A4;
            margin: 0;
        }

        body {
            margin: 1cm;
        }

        * {
            padding: 0;
            margin: 0;
        }
        body {
            background-color:#44A666;
        }

        /*parte 1: primeira pagina do pei(infromaçoes do aluno)*/
        header {
            margin: auto;
            text-align: center;
            background-color: white;
            max-width: 1000px;
            margin: auto;
            margin-top: 50px;
            padding-top: 30px;
            border-top-right-radius: 20px;
            border-top-left-radius: 20px;
        }
        main {
            margin: auto;
            max-width: 1000px;
            padding-top: 30px;
            padding-bottom: 30px;
            background-color: white;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
        }
        .dados-pessoais-aluno {
            margin: auto;
            max-width: 900px;
            margin-bottom: 50px;
            border: none;
        
        }
        .dados-pessoais-aluno > div {
            display: flex;
            flex-direction: column;
        }
        .dados-pessoais-aluno > div > input{
            height: 30px;
            margin-top: 10px;
            border-radius: 5px;
            border: 0.5px solid black;
        }

        /*parte 2: primeira pagina do pei(infromaçoes do aluno)*/
        .dados-escolar-pessoal{
            max-width: 900px;
            margin: auto;
            border: none;
        
        }
        .dados-escolar-pessoal > div{
            display: flex;
            flex-direction: column;
        }
        .dados-escolar-pessoal > div > label{
            background-color:#53A62D;
            border-top-right-radius: 5px;
            border-top-left-radius: 5px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .dados-escolar-pessoal > div > textarea{
            height: 100px;
            margin-bottom: 5px;
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
            border: 0.5px solid black;
        }

    </style>
</head>
<body>
    <header>
        <div>
            <h3>ANEXO 1<br>PLANO EDUCACIONAL INDIVIDUALIZADO(PEI)<br>HISTORICO DO ALUNO</h3>
        </div>
    </header>
    <main>
        <div class="historico-aluno">
            <form class="historico-do-aluno" action="">
                <fieldset class="dados-pessoais-aluno">
                    <div>
                        <label for="nome">Nome do Estudante</label>
                        <input type="text" name="nome" id="nome">
                    </div>
                    <div>
                        <label for="Curso">Curso</label>
                        <input type="text" name="Curso" id="Curso">
                    </div>
                    <div>
                        <label for="NEE">Necessidades Educacionais Específicas</label>
                        <input type="text" name="NEE" id="NEE">
                    </div>
                    <div>
                        <label for="EMR-nome">Equipe multiprofissional responsável(Nome)</label>
                        <input type="text" name="EMR-nome" id="EMR-nome">
                        <label for="EMR-funçao">Equipe multiprofissional responsável(Função)</label>
                        <input type="text" name="EMR-funçao" id="EMR-funçao">
                    </div>
                </fieldset>
                <fieldset class="dados-escolar-pessoal">
                    <div>
                        <label class="HPE-estudante" for="HPE-estudante">HISTÓRICO PESSOAL E ESCOLAR DO (A) ESTUDANTE</label>
                        <textarea type="text" name="HPE-estudante" id="HPE-estudante"></textarea>
                    </div>
                    <div>
                        <label class="NEE-Estudante" for="NEE-Estudante">Necessidades Educacionais Específicas</label>
                        <textarea type="text" name="NEE-EstudanteTEXT"  id="NEE-Estudante"></textarea>
                    </div>
                    <div>
                        <label for="CHCIN">Conhecimentos, Habilidades, Capacidades, 
                            Interesses, Necessidades (O que sabe? Do que gosta/afinidades?...)</label>
                        <textarea type="text" name="CHCIN" id="CHCIN"></textarea>
                    </div>
                    <div>
                        <label for="Dificuadades-apresentadas">Dificuldades apresentadas </label>
                        <textarea type="text" name="Dificuadades-apresentadas" id="Dificuadades-apresentadas"></textarea>
                    </div>
                </fieldset>
            </form>
        </div>
    </main>
</body>
</html>
"""


#Configurando o caminho para o executável wkhtmltopdf.exe
#config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=r"D:\\Users\\20211174010034\\Documents\\GitHub\\aulas-autoria-web\\Documento PEI\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

#Convertendo HTML --> PDF
pdfkit.from_string(html, "output.pdf", configuration=config)


# ANOTAÇÕES
#1. pip install pdfkit
#2. instale o wkhtmltopdf.exe que transforma HTML para PDF
#3. mude o caminho para wkhtmltopdf.exe
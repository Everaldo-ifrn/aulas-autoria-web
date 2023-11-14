import pdfkit

#Criando o PEI usando HTML e CSS
html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>PEI</title>
    <style>
        h1{
            color: grey;
        }
    </style>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Este é um exemplo simples de PDFKit em Python.</p>
</body>
</html>
"""

#Configurando o caminho para o executável wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

#Convertendo HTML --> PDF
pdfkit.from_string(html, "output.pdf", configuration=config)


# ANOTAÇÕES
#1. pip install pdfkit
#2. instale o wkhtmltopdf.exe que transforma HTML para PDF
#3. mude o caminho para wkhtmltopdf.exe
from reportlab.pdfgen import canvas  
from reportlab.lib.pagesizes import A4 #tamanho da página
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

#instânciei o canva
cnv = canvas.Canvas("C:\\Users\\Everaldo Junior\\Documents\\Algorítmos - Autoria Web\\aulas-autoria-web\\PDF Python\\estudo_pdf.pdf", pagesize=A4) 

#Defini os dados da tabela
dados = [
    ["Coluna 1", "Coluna 2", "Coluna 3"],
    ["Dado 1", "Dado 2", "Dado 3"],
    ["Dado 4", "Dado 5", "Dado 6"],
]

#Criei a tabela
table = Table(dados)

#Defini o estilo da tabela(cor de fundo, cor da letra, centralizar os dados)
style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.blue), #cor de fundo da primeira linha
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 12),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
])

#Apliquei o estilo à tabela
table.setStyle(style)

#Calculei a largura das colunas
table.wrapOn(cnv, 200, 400)
table.drawOn(cnv, 30, 700)

#Salvei o arquivo
cnv.save()
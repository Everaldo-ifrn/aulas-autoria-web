from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


#Criando o documento PDF
doc = SimpleDocTemplate("exemplo.pdf", pagesize=letter)

#Criando Cabeçalho e rodapé
def add_header(canvas, doc):
    header2_text = "Rua Dr. Nilo Ramalho,1692 – Tirol – Natal/RN CEP: 59.015-310 Telefone: (84) 4005-0750-0753 http://www.ifrn.edu.br – E-mail: proen@ifrn.edu.br"
    header2 = Paragraph(header2_text, style=doc.styles["Header"])
    header2.wrapOn(canvas, doc.width, doc.topMargin)
    header2.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - header2.height)

def add_footer(canvas, doc):
    footer_text = "Rodapé do PDF"
    footer = Paragraph(footer_text, style=doc.styles["Footer"])
    footer.wrapOn(canvas, doc.width, doc.bottomMargin)
    footer.drawOn(canvas, doc.leftMargin, footer.height)

header_frame = Frame(doc.leftMargin, doc.bottomMargin - 50, doc.width, 50)
footer_frame = Frame(doc.leftMargin, doc.bottomMargin - 50, doc.width, 50)

header_template = PageTemplate(id="header", frames=header_frame, onPage=add_header)
footer_template = PageTemplate(id="footer", frames=footer_frame, onPage=add_footer)

doc.addPageTemplates([header_template, footer_template])

#Lista de elementos do PDF
elements = []

# Caminho da imagem
caminho_imagem = "imagens/logoRepublica.png"

# Adicionar a imagem centralizada com tamanho definido
imagem = Image(caminho_imagem, width=50, height=50)
imagem.hAlign = "CENTER"
elements.append(imagem)

#Estilo para o texto centralizado
text_style = getSampleStyleSheet()["BodyText"]
text_style.alignment = 1

# Adicionar o parágrafo ao documento (substitua 'Seu texto aqui' pelo seu texto) 
text = Paragraph("Seu texto aqui", text_style)
elements.append(text)

#Estilo do título
style_Title = getSampleStyleSheet()["Heading1"]
style_Title.alignment = 1

#Títulos centrelizados
def add_title(title_text):
    title = Paragraph(f'<b>{title_text}</b>', style_Title)
    elements.append(title)

#Adcionando titulo
add_title("Sou um título centralizado")

# Construir o documento PDF
doc.build(elements)
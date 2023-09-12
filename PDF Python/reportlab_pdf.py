from PyPDF2 import PdfReader, PdfWriter

# Carregue o PDF existente
pdf = PdfReader("Modelo_PEI-2023.pdf")

# Crie um novo PDF
pdf_novo = PdfWriter()

# Copie as páginas do PDF existente para o novo PDF
for pagina in pdf.pages:
    pdf_novo.add_page(pagina)

# Adicione novo conteúdo
# Você pode usar o módulo reportlab para adicionar elementos ao pdf_novo, como texto ou imagens

# Salve o novo PDF
with open("pdf_modificado.pdf", "wb") as output_pdf:
    pdf_novo.write(output_pdf)
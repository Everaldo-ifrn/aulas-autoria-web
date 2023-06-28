from docx import Document
import win32com.client

document = Document()
str = "Olá, sou um teste! Será que funcionei???"
document.add_paragraph(str)

document.save("oi.docx")

"""
# Cria uma instância do Word
word_app = win32com.client.Dispatch("Word.Application")
word_app.Visible = False  # Mantém o Word invisível

# Abre o documento .docx
doc = word_app.Documents.Open("Área de Trabalho\oi.docx")

# Salva o documento como PDF
doc.SaveAs("Área de Trabalho/oi.pdf", FileFormat=17)  # 17 é o código para formato PDF

# Fecha o documento e o Word
doc.Close()
word_app.Quit()
"""
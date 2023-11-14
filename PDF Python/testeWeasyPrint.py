from weasyprint import HTML

# Se você preferir usar HTML local em vez de uma URL, você pode usar:
html_content = ''

# Se estiver usando HTML local, use:
pdf = HTML(string=html_content).write_pdf('output.pdf')

#pdf_file = "C://Users//Everaldo Junior//Desktop//TestePythonWeasy.pdf"

from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate, Paragraph, Frame, PageTemplate, Image, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import styles
from reportlab.lib.enums import TA_LEFT


elements = []

class MyDocTemplate(BaseDocTemplate):
    caminho_imaem2 = "C:\\Users\\Rafael\\Documents\\GitHub\\aulas-autoria-web\\Documento PEI\\imagens\\logoEnapne.png"
    #caminho_imagem2 = "imagens/logoEnapne.png"
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        main_frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height - 100)
        main_template = PageTemplate(id="main", frames=main_frame, onPage=self.add_elements, pagesize=letter)
        self.addPageTemplates([main_template])

    def add_elements(self, canvas, doc):
        self.add_header(canvas, doc)
        self.add_footer(canvas, doc)

    def add_header(self, canvas, doc):
        # Definir a posição inicial para desenhar o texto
        y_position = doc.height + doc.topMargin

        caminho_imagem = "C:\\Users\\Rafael\\Documents\\GitHub\\aulas-autoria-web\\Documento PEI\\imagens\\logoRepublica.png"
        #caminho_imagem = "imagens/logoRepublica.png"
        imagem = Image(caminho_imagem, width=50, height=50)

        # Calcular a posição horizontal para centralizar a imagem
        x_position = (doc.width + 95) / 2
        imagem.drawOn(canvas, x_position, y_position)

        header_text = ['Ministério da Educação', 'Secretaria de Educação Profissional e Tecnológica', 'Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte IFRN - Pró-Reitoria de Ensino']

        for frase in header_text:
            header_style = styles.getSampleStyleSheet()['Heading5']
            header_style.alignment = 1
            header = Paragraph(frase, style=header_style)
            # Obter a altura da Paragraph usando o método wrap
            header.wrap(doc.width, doc.topMargin)
            header_height = header.height
            # Atualizar a posição vertical antes de desenhar cada frase
            y_position -= header_height
            header.drawOn(canvas, doc.leftMargin, y_position)

        # Adiciona o título h6 centralizado
        title_text = "Rua Dr. Nilo Ramalho,1692 – Tirol – Natal/RN CEP: 59.015-310 Telefone: (84) 4005-0750-0753 http://www.ifrn.edu.br – E-mail: proen@ifrn.edu.br"
        title_style = styles.getSampleStyleSheet()['Heading6']
        title_style.alignment = 1
        title = Paragraph(title_text, style=title_style)
        title.wrap(doc.width, doc.topMargin)
        title_height = title.height
        y_position -= title_height
        title.drawOn(canvas, doc.leftMargin, y_position)

    def add_footer(self, canvas, doc):
        footer_text = "Esta Instrução Normativa foi elaborada com base na Instrução Normativa nº 12/12/2018 do IFRS."
        footer_style = styles.getSampleStyleSheet()['BodyText']
        footer = Paragraph(footer_text, style=footer_style)
        footer.wrapOn(canvas, doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, footer.height)


def create_anexoI():
    doc = MyDocTemplate("PEI_PessoaX.pdf", pagesize=letter, title="PEI_PessoaX")
    
    # Adicionar imagem centralizada sobre o título "ANEXO I"
    caminho_imagem_titulo = "C:\\Users\\Rafael\\Documents\\GitHub\\aulas-autoria-web\\Documento PEI\\imagens\\logoEnapne.png"
    #caminho_imagem_titulo = "imagens/logoEnapne.png"
    imagem_titulo = Image(caminho_imagem_titulo, width=95, height=80)
    # Calcular a posição horizontal para centralizar a imagem
    x_position_imagem = (doc.width - imagem_titulo.drawWidth) / 2
    elements.append(imagem_titulo)

    title_text = ['ANEXO I', 'PLANO EDUCACIONAL INDIVIDUALIZADO (PEI)','HISTÓRICO DO ALUNO']
    for frase in title_text:
        title_style = styles.getSampleStyleSheet()['Heading2']
        title_style.alignment = 1
        title = Paragraph(frase, style=title_style)
        elements.append(title)

    text_style = getSampleStyleSheet()["BodyText"] # CONTEÚDO AQUI!!!
    text = Paragraph("<b><u>Alerta Ético</u></b>: as informações contidas neste documento são consideradas reservadas e o compartilhamento das mesmas deve ser restrito apenas às/aos envolvidos na ação pedagógica, sob pena de implicações legais. <br/><br/>", text_style)
    elements.append(text)

    data = [[Paragraph('Nível de Ensino/ Forma: (   ) Técnico Integrado Regular  (  ) Técnico Integrado EJA   ( )Técnico Subsequente   (  ) Curso Superior de Tecnologia  (  ) Curso Superior de Licenciatura ( ) Engenharia  (  ) Pós-Graduação  ( ) Outros _________________________ ', None)],
                [Paragraph('Nome do Estudante: ', None)],
                [Paragraph('Curso: ', None)],
                [Paragraph('Necessidades Educacionais Específicas: ', None)],
                [Paragraph('Equipe multiprofissional responsável: ', None)]]

    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), 'white'),
                              ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),                              
                              ('BACKGROUND', (0, 1), (-1, -1), 'white'),
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])

    # Defina a largura da tabela como 80% da largura da página
    table_width = doc.width                          
    table = Table(data, style=table_style, colWidths=[table_width])
    elements.append(table)

    space = Spacer(1, 12)  # Espaço vertical de 12 unidades
    elements.append(space)

    ############################################################
    # Estilo para o texto em negrito
    style_bold = getSampleStyleSheet()["BodyText"]
    style_bold.alignment = 1

    style_bold2 = getSampleStyleSheet()["BodyText"]
    style_bold2.alignment = 0
    
    data2 = [[Paragraph('<b>HISTÓRICO PESSOAL E ESCOLAR DO (A) ESTUDANTE</b>', style_bold)],
            [' '],
            [Paragraph('<b>Necessidades Educacionais Específicas</b>', style_bold)],
            [' '],
            [Paragraph('<b>Conhecimentos, Habilidades, Capacidades, Interesses, Necessidades (O que sabe? Do que gosta/afinidades?...)</b> &lt;Preenchido, preferencialmente, pela ETEP, COAS e NAPNE&gt;', style_bold), Paragraph('<b>Dificuldades apresentadas</b> &lt;Preenchido, preferencialmente, pela ETEP, COAS e NAPNE&gt;', style_bold)],
            [' ', ' '],
            [Paragraph('<b>OBSERVAÇÕES 	GERAIS  SOBRE 	OUTRAS  NECESSIDADES  EDUCACIONAIS ESPECÍFICAS 	DO (A) ESTUDANTE:</b> ', style_bold2)]]
    
    table_style2 = TableStyle([('BACKGROUND', (0, 0), (-1, 0), 'white'),
                              ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('ALIGN', (0, 0), (0, 0), 'CENTER'),
                              ('ALIGN', (0, 2), (0, 2), 'CENTER'),
                              ('ALIGN', (0, 4), (1, 4), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),                              
                              ('BACKGROUND', (0, 0), (0, 0), '#D3D3D3'),
                              ('BACKGROUND', (0, 2), (0, 2), '#D3D3D3'),
                              ('BACKGROUND', (0, 4), (1, 4), '#D3D3D3'),
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])
                              
    # Defina a largura da tabela como 80% da largura da página
    table2_width = doc.width * 0.5 
    table2 = Table(data2, style=table_style2, colWidths=[table2_width])
    table2.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('SPAN', (0, 3), (1, 3)),
        ('SPAN', (0, 6), (1, 6))
    ]))
    elements.append(table2)
    
    anexoII = Paragraph('ANEXO II', style=title_style)
    anexoII_texto = Paragraph('REGISTRO DO ACOMPANHAMENTO DO PEI E PARECER DA EQUIPE', style=title_style)
    elements.append(anexoII)
    elements.append(anexoII_texto)
    
#def create_anexoII(doc):
    text_style2 = getSampleStyleSheet()["BodyText"] # CONTEÚDO AQUI!!!
    text2 = Paragraph("<b><u>Alerta Ético</u></b>: as informações contidas neste documento são consideradas reservadas e o compartilhamento das mesmas deve ser restrito apenas às/aos envolvidos na ação pedagógica, sob pena de implicações legais. <br/><br/>", text_style)
    elements.append(text2)

    data6 = [[Paragraph('Nível de Ensino/ Forma: (   ) Técnico Integrado Regular  (  ) Técnico Integrado EJA   ( )Técnico Subsequente   (  ) Curso Superior de Tecnologia  (  ) Curso Superior de Licenciatura ( ) Engenharia  (  ) Pós-Graduação  ( ) Outros _________________________ ', None)],
                [Paragraph('Nome do Estudante: ', None)],
                [Paragraph('Curso: ', None)],
                [Paragraph('Necessidades Educacionais Específicas: ', None)],
                [Paragraph('Equipe multiprofissional responsável: ', None)]]

    table_style2 = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),                              
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])

    # Defina a largura da tabela como 80% da largura da página
    table_width = doc.width                          
    table = Table(data6, style=table_style, colWidths=[table_width])
    elements.append(table)

    space = Spacer(1, 12)  # Espaço vertical de 12 unidades
    elements.append(space)
      
    dadosII = [
      [Paragraph("<b>Adaptações Curriculares (Sugestão: Anexar Plano de Ensino do Componente Curricular/Disciplina)</b> &lt;Preenchido pelos/as docentes, com apoio da equipe multiprofissional&gt;", style_bold)],
      [Paragraph('<b>Plano do Componente Curricular</b>', style_bold), Paragraph('Adaptações', style_bold)],
      [Paragraph('<b>Objetivos</b>', text_style)],
      [Paragraph('Descrever os objetivos que pretende alcançar com o/a estudante, baseado no Plano de Ensino do Componente Curricular.', None), ' '],
      [Paragraph('<b>Conteúdos Programáticos </b>', text_style)],
      [Paragraph('Baseado no Plano de Ensino do Componente Curricular.  É possível priorizar, substituir conteúdos, dependendo da necessidade, a ser avaliada junto ao corpo docente que atende o/a estudante e equipe de apoio. Deve-se abordar conteúdos que precisam ser retomados, dependendo da necessidade, a ser avaliada junto ao corpo docente que atende o/a estudante e equipe de apoio.', None), ' '],
      [Paragraph('<b>Metodologias</b>', text_style)],
      [Paragraph('Baseado no Plano de Ensino do Componente Curricular Deve-se priorizar metodologias que dinamizem o processo de ensino e aprendizagem, visando favorecer a interação e a aprendizagem do/a estudante.', None), ' '],
      [Paragraph('<b>Recursos Didáticos</b>', text_style)],
      [Paragraph('Os recursos didáticos deverão ser escolhidos de acordo com as estratégias metodológicas, de forma a favorecer a abordagem dos conteúdos selecionados e a aprendizagem do/a estudante.', None), ' '],
      [Paragraph('<b>Avaliações</b>', text_style)],
      [Paragraph('Quais instrumentos utilizados? Como foram aplicados? Recomenda-se oportunizar diversas formas de expressão da aprendizagem. Exemplos: projetos educacionais (ensino, pesquisa, extensão), atividades diferenciadas (seminários, debates, provas individuais e/ou em duplas), observando o nível de desempenho e contribuição do/a estudante no desenvolvimento do componente curricular.', None), ' '],
      [Paragraph('<b>Registro do desenvolvimento e acompanhamento processual do PEI pelo professor </b>', text_style)],
      [Paragraph("""Descrever avanços do(a) estudante, considerando os objetivos previstos para ele(a) e a superação das dificuldades. Procurar mencionar as propostas que tiveram êxito e o replanejamento daquelas que não tiveram e o que se observou em ambos os casos. Pontuar o que pretende para a próxima etapa, em termos de objetivos específicos de atuação junto à/ao estudante. Também destacar aspectos do seu desenvolvimento social. Mencionar, caso o/a estudante tenha acompanhado a turma realizando as mesmas atividades propostas para os demais, sem necessidade de adaptação. 
<br/> &bull;	Compreende e participa das atividades propostas no ambiente acadêmico? 
<br/> &bull;	Apresenta desenvolvimento satisfatório no cumprimento das atividades? (baseado nos objetivos propostos) 
<br/> &bull;	Apresenta motivação para a realização das atividades? 
<br/> &bull;	Necessita de recursos concretos/adicionais para aprender? 
<br/> &bull;	Solicita auxílio do/a colega ou do/a docente para realizar as atividades? 
<br/> &bull;	Como se dá a interação com os colegas nos diversos espaços escolares? 
<br/> &bull;	Consegue trabalhar em grupo? 
<br/> &bull;	É assíduo? 	 
<br/> &bull;	Tem cuidado e organização com o material escolar? 
<br/> &bull;	Apresenta facilidade para aprender/resolver problemas? 
""", None)]
    ]
#13 É OS DOIS!!!
    table_styleII = TableStyle([('BACKGROUND', (0, 0), (1, 1), '#D3D3D3'),
                              ('BACKGROUND', (0, 3), (0, 3), '#EAD1DC'),
                              ('BACKGROUND', (0, 5), (0, 5), '#F4CCCC'),
                              ('BACKGROUND', (0, 7), (0, 7), '#F4CCCC'),
                              ('BACKGROUND', (0, 9), (0, 9), '#F4CCCC'),
                              ('BACKGROUND', (0, 11), (0, 11), '#F4CCCC'),
                              ('BACKGROUND', (0, 13), (1, 13), '#F4CCCC'),
                              ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),                              
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])
    
    table_widthII = doc.width * 0.5                          
    tableII = Table(dadosII, style=table_styleII, colWidths=[table_widthII])
    tableII.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (0, 2), (1, 2)),
        ('SPAN', (0, 4), (1, 4)),
        ('SPAN', (0, 6), (1, 6)),
        ('SPAN', (0, 8), (1, 8)),
        ('SPAN', (0, 10), (1, 10)),
        ('SPAN', (0, 12), (1, 12)),
        ('SPAN', (0, 13), (1, 13)),
    ]))
    elements.append(tableII)
    anexoII = Paragraph('ANEXO III', style=title_style)
    anexoII_texto = Paragraph('REGISTRO DO ACOMPANHAMENTO DO PEI E PARECER DA EQUIPE', style=title_style)
    elements.append(anexoII)
    elements.append(anexoII_texto)

    dadosIII = [
        [Paragraph('Descrever avanços do/a estudante durante o acompanhamento de elaboração e execução do PEI.', style_bold)],
        [Paragraph('PARECER DA EQUIPE MULTIPROFISSIONAL', None)],
        [' ']
    ]

    table_styleIII = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),                              
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])
    
    table_widthIII = doc.width                         
    tableIII = Table(dadosIII, style=table_styleIII, colWidths=[table_widthIII])
    elements.append(tableIII)
    space = Spacer(1, 12)  # Espaço vertical de 12 unidades
    elements.append(space)
    assinatura = Paragraph('Assinatura dos/as Docentes:_________', None)
    assinatura2 = Paragraph('Assinatura da Coordenação de Curso:_______________________________________________ <br/>Assinatura do NAPNE (responsável):________________________________________________  <br/>Assinatura da ETEP (responsável):_________________________________________________  <br/>Assinatura da COAES (responsável):________________________________________________  <br/>Assinatura de outros  profissionais envolvidos: _____________________________________________________________________________________________________________________', None)
    elements.append(assinatura)
    elements.append(assinatura2)
    tituloI = Paragraph('<b><u>INFORMAÇÕES E SUGESTÕES NECESSÁRIAS A ADAPTAÇÃO CURRICULAR</u></b>', style_bold)
    elements.append(tituloI)
    tituloII = Paragraph('<b>Proposta de Adaptação Curricular</b>', style_bold)
    elements.append(tituloII)

    dadosIV = [[Paragraph('<b>DADOS DO DISCENTE</b>', style_bold)],
        [Paragraph('<b>NOME:</b> ', style_bold2)],
        [Paragraph('<b>MATRÍCULA:</b> ', style_bold2)],
        [Paragraph('<B>CURSO:</b> ', style_bold2)]
    ]

    table_styleIV = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
                              ('ALIGN', (0, 0), (0, 0), 'CENTER'),                              
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])
    
    table_widthIV = doc.width                         
    tableIV = Table(dadosIV, style=table_styleIV, colWidths=[table_widthIV])
    elements.append(tableIV)

    space = Spacer(1, 12)  # Espaço vertical de 12 unidades
    elements.append(space)

    dadosV = [[Paragraph('<b>EQUIPE RESPONSÁVEL</b>', style_bold)],
        [Paragraph('<b>COORDENAÇÃO DE CURSO: </b> ', style_bold2)],
        [Paragraph("""<b>EQUIPE NÚCLEO DE APOIO À PESSOAS COM NECESSIDADES ESPECÍFICAS</b> <br/> &bull; """, style_bold2)]
    ]

    table_styleV = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
                              ('ALIGN', (0, 0), (0, 0), 'CENTER'),                              
                              ('GRID', (0, 0), (-1, -1), 1, 'black'),
                              ('WORDWRAP', (0, 0), (-1, 0), True),
                              ('TRUNCATE', (0, 0), (-1, 0), 'END'),
                              ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])
    
    table_widthV = doc.width                         
    tableV = Table(dadosV, style=table_styleV, colWidths=[table_widthV])
    elements.append(tableV)
    
    tituloV = Paragraph('<b>1. CONTEXTUALIZAÇÃO DO CASO</b> <br/> ', style_bold2)
    elements.append(tituloV)

    



    
    doc.build(elements)
  
create_anexoI()
#create_anexoII(doc)

# --------------- ANOTAÇÕES ------------------
"""
    #TESTE DA COLUNAAS!!!!!!!!!!!!!!!!!!!!! 
    # Lista de dados para a tabela
    data3 = [
        ['Coluna 1'],  # Primeira linha com uma coluna
        ['Dado 1.1', 'Dado 1.2']  # Segunda linha com duas colunas
    ]

    # Estilo da tabela
    table_style3 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), 'grey'),  # Cor de fundo para a primeira linha
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),  # Cor do texto para a primeira linha
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento central para toda a tabela
        ('GRID', (0, 0), (-1, -1), 1, 'black')  # Grade para todas as células da tabela
    ])

    # Criar a tabela e aplicar o estilo
    table3 = Table(data3)
    table3.setStyle(table_style3)
    # Mesclar células para criar uma única coluna na primeira linha
    table3.setStyle(TableStyle([('SPAN', (0, 0), (1, 0))]))

    # Adicionar a tabela aos elementos
    elements.append(table3)"""

"""
        data = [['Coluna 1', 'Coluna 2', 'Coluna 3'],
                ['Dado 1.1', 'Dado 1.2', 'Dado 1.3'],
                ['Dado 2.1', 'Dado 2.2', 'Dado 2.3']]


        # Configuração da tabela
        table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), 'grey'),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                  ('BACKGROUND', (0, 1), (-1, -1), 'white'),
                                  ('GRID', (0, 0), (-1, -1), 1, 'black')])
        # Criar a tabela e aplicar o estilo
        table = Table(data)
        table.setStyle(table_style)
        # Adicionar a tabela aos elementos
        elements.append(table)
        """
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
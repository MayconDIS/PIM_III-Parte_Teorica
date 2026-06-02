import os
import sys

# Tenta importar fpdf2, se falhar, tenta instalar
try:
    from fpdf import FPDF
except ImportError:
    print("FPDF2 não está instalado. Tentando instalar via pip...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2"])
    from fpdf import FPDF

class NexTIDocumentosPDF(FPDF):
    def __init__(self, doc_title, doc_subtitle):
        super().__init__()
        self.doc_title = doc_title
        self.doc_subtitle = doc_subtitle
        self.set_top_margin(36)
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_auto_page_break(auto=True, margin=12)

    def header(self):
        # Fundo do cabeçalho em Slate 900
        self.set_fill_color(15, 23, 42)
        self.rect(0, 0, 210, 30, 'F')
        
        # Detalhe decorativo em Cyan
        self.set_fill_color(0, 230, 230)
        self.rect(0, 30, 210, 1.5, 'F')
        
        # Título principal do documento
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(255, 255, 255)
        self.set_y(5)
        # O FPDF2 requer parâmetros explícitos ou posicionais para cell
        self.cell(0, 7, self.doc_title, align='C', new_x="LMARGIN", new_y="NEXT")
        
        # Subtítulo
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(0, 230, 230)
        self.cell(0, 4, self.doc_subtitle, align='C', new_x="LMARGIN", new_y="NEXT")
        
        self.set_y(36)

    def footer(self):
        # Rodapé posicionado a 12 mm da margem inferior
        self.set_y(-12)
        
        # Linha decorativa
        self.set_draw_color(226, 232, 240)
        self.line(15, self.get_y(), 195, self.get_y())
        
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(100, 116, 139)
        
        # Nome do projeto e grupo à esquerda, paginação à direita
        self.cell(90, 8, 'UNIP - CST ADS (Analise e Desenv. de Sistemas) - Grupo 02', align='L')
        self.cell(90, 8, f'Página {self.page_no()}', align='R')

    def add_section_title(self, title):
        self.ln(2.0)
        self.set_font('Helvetica', 'B', 12.5)
        self.set_text_color(15, 23, 42) # Slate 900
        
        # Caixa de fundo cinza claro para títulos de seção
        self.set_fill_color(241, 245, 249) # Slate 100
        self.cell(0, 8.0, f' {title.upper()}', align='L', fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2.5)

    def add_subsection_title(self, title):
        self.ln(1.5)
        self.set_font('Helvetica', 'B', 11.0)
        self.set_text_color(13, 148, 136) # Teal
        self.cell(0, 6.0, title, align='L', new_x="LMARGIN", new_y="NEXT")
        self.ln(1.0)

    def add_paragraph(self, text):
        self.set_font('Helvetica', '', 10.0)
        self.set_text_color(51, 65, 85) # Slate 700
        self.multi_cell(180, 4.4, text)
        self.ln(2.5)

    def add_bullet(self, title, text):
        orig_left = self.l_margin
        
        # Bullet marker em Cyan/Teal
        self.set_font('Helvetica', 'B', 10.0)
        self.set_text_color(0, 180, 180)
        self.set_x(20)
        self.cell(4, 4.0, chr(149), align='L')
        
        # Texto recuado
        self.set_left_margin(24)
        self.set_x(24)
        
        if title:
            self.set_font('Helvetica', 'B', 10.0)
            self.set_text_color(15, 23, 42) # Slate 900
            self.write(4.4, f'{title}: ')
            
        self.set_font('Helvetica', '', 10.0)
        self.set_text_color(51, 65, 85) # Slate 700
        self.write(4.4, text)
        self.ln(4.8)
        
        self.set_left_margin(orig_left)
        self.set_x(orig_left)

    def add_priority_badge(self, priority_text):
        if "alta" in priority_text.lower():
            bg_color = (254, 242, 242) # Vermelho claro
            border_color = (252, 165, 165)
            text_color = (153, 27, 27) # Vermelho escuro
            label = "PRIORIDADE: ALTA"
        else:
            bg_color = (254, 243, 199) # Amarelo claro
            border_color = (253, 230, 138)
            text_color = (146, 64, 14) # Amarelo escuro
            label = "PRIORIDADE: MEDIA"
            
        x = self.get_x()
        y = self.get_y()
        
        self.set_fill_color(*bg_color)
        self.set_draw_color(*border_color)
        self.set_text_color(*text_color)
        self.set_font('Helvetica', 'B', 8.5)
        
        # Desenha a badge de status
        self.rect(x, y, 40, 5.0, 'DF')
        
        self.set_xy(x, y + 0.5)
        self.cell(40, 4.0, label, align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(2.0)

def clean_text(text):
    # Remove emojis e substitui caracteres não-Latin1 comuns para evitar erros
    emojis = ['🎯', '📝', '⚠️', '📌', '🎨', '♿', '📐', '💾', '💻', '🌐', '👥', '❤️', '✅', '❌']
    for emoji in emojis:
        text = text.replace(emoji, "")
        
    replacements = {
        '–': '-',
        '—': '-',
        '“': '"',
        '”': '"',
        '‘': "'",
        '’': "'",
        '\u2013': '-',
        '\u2014': '-',
        '\u2022': '*',
    }
    for orig, rep in replacements.items():
        text = text.replace(orig, rep)
        
    return text.strip()

def parse_markdown_to_pdf(md_path, pdf_path, doc_title, doc_subtitle):
    pdf = NexTIDocumentosPDF(doc_title, doc_subtitle)
    pdf.add_page()
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    is_first_h1 = True
    
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
            
        # Limpa emojis e normaliza pontuações
        cleaned_line = clean_text(cleaned_line)
        
        # Pula H1 na renderização de conteúdo se for o principal (já que ele é o título do header)
        if cleaned_line.startswith('# '):
            h1_text = cleaned_line[2:].strip()
            if is_first_h1:
                is_first_h1 = False
                pdf.ln(2.0)
            else:
                pdf.add_section_title(h1_text)
            continue
            
        # Linha horizontal decorativa
        if cleaned_line == '---':
            pdf.ln(1.5)
            y = pdf.get_y()
            pdf.set_draw_color(226, 232, 240)
            pdf.line(15, y, 195, y)
            pdf.ln(3.0)
            continue
            
        # H2
        if cleaned_line.startswith('## '):
            h2_text = cleaned_line[3:].strip()
            pdf.add_section_title(h2_text)
            continue
            
        # H3
        if cleaned_line.startswith('### '):
            h3_text = cleaned_line[4:].strip()
            pdf.add_subsection_title(h3_text)
            continue
            
        # Badges de Prioridade no Backlog
        if cleaned_line.startswith('*') and 'prioridade:' in cleaned_line.lower():
            priority_val = "Média"
            if "alta" in cleaned_line.lower():
                priority_val = "Alta"
            pdf.add_priority_badge(priority_val)
            continue
            
        # Bullet points
        if cleaned_line.startswith('- ') or cleaned_line.startswith('* '):
            bullet_text = cleaned_line[2:].strip()
            title = ""
            text = bullet_text
            
            if bullet_text.startswith('**'):
                end_bold = bullet_text.find('**', 2)
                if end_bold != -1:
                    title = bullet_text[2:end_bold].strip()
                    text = bullet_text[end_bold+2:].strip()
                    if title.endswith(':'):
                        title = title[:-1].strip()
            
            pdf.add_bullet(title, text)
            continue
            
        # Linhas inteiras em Negrito (como os títulos de Casos de Uso ou Story Points)
        if cleaned_line.startswith('**') and cleaned_line.endswith('**') and cleaned_line.count('**') == 2:
            bold_text = cleaned_line[2:-2].strip()
            pdf.set_font('Helvetica', 'B', 10.5)
            pdf.set_text_color(15, 23, 42)
            pdf.multi_cell(180, 5.0, bold_text)
            pdf.ln(1.5)
            continue
            
        # Metadados e chaves/valores inline (ex: **Data:** 05/03/2026)
        if cleaned_line.startswith('**') and cleaned_line.count('**') >= 2:
            end_bold = cleaned_line.find('**', 2)
            if end_bold != -1:
                meta_label = cleaned_line[2:end_bold].strip()
                meta_val = cleaned_line[end_bold+2:].strip()
                if meta_label.endswith(':'):
                    meta_label = meta_label[:-1].strip()
                
                pdf.set_font('Helvetica', 'B', 10.0)
                pdf.set_text_color(15, 23, 42)
                pdf.write(4.4, f'{meta_label}: ')
                pdf.set_font('Helvetica', '', 10.0)
                pdf.set_text_color(51, 65, 85)
                pdf.write(4.4, meta_val)
                pdf.ln(5.0)
                continue

        # Parágrafos normais de texto
        pdf.add_paragraph(cleaned_line)
        
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    pdf.output(pdf_path)
    print(f"PDF gerado com sucesso em: {pdf_path}")

def main():
    docs_to_convert = [
        {
            "md": "docs/Ata_Sprint_Planning_Nex_TI.md",
            "pdf": "docs/Ata_Sprint_Planning_Nex_TI.pdf",
            "title": "NEX_TI - ATA DE SPRINT PLANNING",
            "subtitle": "Sprint 01 (MVP - Fundacao) - Gestao Agil Scrum"
        },
        {
            "md": "docs/Documentacao_Projeto_Nex_TI.md",
            "pdf": "docs/Documentacao_Projeto_Nex_TI.pdf",
            "title": "NEX_TI - DOCUMENTACAO DO PROJETO",
            "subtitle": "Versao 2.0 (Alinhamento 2026) - Arquitetura e Escopo"
        },
        {
            "md": "docs/Product_Backlog_Nex_TI.md",
            "pdf": "docs/Product_Backlog_Nex_TI.pdf",
            "title": "NEX_TI - PRODUCT BACKLOG",
            "subtitle": "Historias de Usuario, Prioridades e Estimativas (Story Points)"
        }
    ]
    
    for doc in docs_to_convert:
        if os.path.exists(doc["md"]):
            parse_markdown_to_pdf(doc["md"], doc["pdf"], doc["title"], doc["subtitle"])
        else:
            print(f"Erro: Arquivo {doc['md']} nao encontrado.")

if __name__ == "__main__":
    main()

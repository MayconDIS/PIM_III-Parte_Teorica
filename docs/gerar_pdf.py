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

class NexTIPDF(FPDF):
    def header(self):
        # Fundo do cabeçalho em Slate 900
        self.set_fill_color(15, 23, 42)
        self.rect(0, 0, 210, 30, 'F')
        
        # Detalhe decorativo em Cyan
        self.set_fill_color(0, 230, 230)
        self.rect(0, 30, 210, 1.5, 'F')
        
        # Título principal
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(255, 255, 255)
        self.set_y(5)
        self.cell(0, 7, 'NEX_TI - ROTEIRO & SCRIPTS DE APRESENTACAO DA BANCA', 0, 1, 'C')
        
        # Subtítulo
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(0, 230, 230)
        self.cell(0, 4, 'Guia de Apoio para Defesa das 9 Etapas e Metodologia do PIM III (Proj. Integrado Multidisciplinar)', 0, 1, 'C')
        
        self.set_y(36)

    def footer(self):
        # Rodapé posicionado a 12 mm da margem inferior
        self.set_y(-12)
        
        # Linha decorativa
        self.set_draw_color(226, 232, 240)
        self.line(15, self.get_y(), 195, self.get_y())
        
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(100, 116, 139)
        
        # Nome do projeto e grupo
        self.cell(90, 8, 'UNIP - CST ADS (Analise e Desenv. de Sistemas) - Grupo 02', 0, 0, 'L')
        # Paginação
        self.cell(90, 8, f'Página {self.page_no()}', 0, 0, 'R')

    def add_slide_title(self, number, title):
        self.set_font('Helvetica', 'B', 12.5)
        self.set_text_color(15, 23, 42)
        
        # Caixa de fundo para o título do slide
        self.set_fill_color(241, 245, 249)
        self.cell(0, 8.0, f' SLIDE {number}: {title.upper()}', 0, 1, 'L', fill=True)
        self.ln(1.5)

    def add_bullet_point(self, title, text):
        orig_left = self.l_margin
        
        # Desenha o bullet
        self.set_font('Helvetica', 'B', 10.5)
        self.set_text_color(30, 41, 59)
        self.set_x(20)
        self.cell(4, 4.0, chr(149), 0, 0, 'L')
        
        # Recuo dinâmico de margem
        self.set_left_margin(24)
        self.set_x(24)
        
        # Título em negrito
        self.set_font('Helvetica', 'B', 10.5)
        self.write(4.5, f'{title}: ')
        
        # Descrição normal
        self.set_font('Helvetica', '', 10.5)
        self.set_text_color(71, 85, 105)
        self.write(4.5, text)
        
        # Quebra de linha e restauração de margem
        self.ln(5.5)
        self.set_left_margin(orig_left)

    def add_script_fala(self, texto_fala):
        # Caixa estilizada para a fala da equipe
        self.set_fill_color(248, 250, 252) # Light Slate
        self.set_draw_color(203, 213, 225) # Border Slate
        self.set_text_color(15, 23, 42)
        
        # Posicionamento e borda esquerda decorativa em ciano
        x_init = self.get_x()
        y_init = self.get_y()
        
        # Desenha um retângulo de fundo de 33mm para caber a fala expandida com fontes maiores
        self.rect(x_init, y_init, 180, 33, 'F')
        
        # Desenha a barra ciano
        self.set_fill_color(0, 200, 200)
        self.rect(x_init, y_init, 2, 33, 'F')
        
        # Escreve o texto com recuo
        self.set_xy(x_init + 5, y_init + 2)
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(13, 148, 136) # Teal
        self.cell(0, 4, 'ROTEIRO DE FALA SUGERIDO (APRESENTACAO):', 0, 1, 'L')
        
        self.set_x(x_init + 5)
        self.set_font('Helvetica', 'I', 9.0)
        self.set_text_color(30, 41, 59)
        self.multi_cell(170, 4.4, texto_fala)
        
        # Ajusta a posição Y final
        self.set_xy(x_init, y_init + 35)

    def add_defesa(self, question, answer):
        orig_left = self.l_margin
        
        # Pergunta
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(15, 23, 42) # Slate 900
        self.write(4.4, f'Duvida Banca: {question}')
        self.ln(4.8)
        
        # Recuo da resposta
        self.set_left_margin(20)
        self.set_x(20)
        
        # Resposta
        self.set_font('Helvetica', '', 9.0)
        self.set_text_color(15, 23, 42) # Slate 900
        self.write(4.4, f'Defesa Rapida: {answer}')
        
        # Linha em branco e restaura margem
        self.ln(5.8)
        self.set_left_margin(orig_left)

    def add_defesa_divider(self):
        self.set_font('Helvetica', 'B', 10.5)
        self.set_text_color(15, 23, 42) # Slate 900
        self.cell(0, 5.0, 'GUIA DE DEFESA RÁPIDA (PERGUNTAS DA BANCA):', 0, 1, 'L')
        self.ln(1.0)

def gerar_apresentacao(output_path):
    pdf = NexTIPDF()
    pdf.set_top_margin(36)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_auto_page_break(auto=True, margin=12)
    
    # ==================== PÁGINA 1: SLIDE 1 ====================
    pdf.add_page()
    pdf.add_slide_title("1", "Caracterizacao do Negocio (Etapa 1)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Visao geral da EdTech (Tecnologia Educacional) Nex_TI, regras e limites do negocio.')
    pdf.add_bullet_point('Modelo SaaS', 'Monetizacao SaaS (Software as a Service - Software como Servico) por assinaturas recorrentes.')
    pdf.add_bullet_point('Regras de Negocio', 'RN01 (Regra de Negocio 01 - recompensas ao fim do deck), perfis e economia estetica.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Ola, professores. O nosso projeto conceitua a Nex_TI, uma startup de TI (Tecnologia da Informacao) focada em resolver a alta evasao de calouros que se assustam com a enxurrada de jargoes tecnicos. Projetamos uma plataforma de nivelamento academico via flashcards com faturamento SaaS (Software as a Service - Software como Servico). Para manter as regras de negocio, modelamos a RN01 (Regra de Negocio 01): o aluno so ganha moedas e XP (Pontos de Experiencia) ao fechar todo o deck no figma.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Como voces justificam a RN01 (Regra de Negocio 01) no prototipo Figma?',
                   'Para impedir cheating (trapaças) no visual do Figma. Obrigar a conclusao total da rodada garante que o ciclo de repeticao espacada atue corretamente no cerebro do aluno.')
    pdf.add_defesa('Quem e o Publico-Alvo e como funciona a comercializacao B2B?',
                   'Faculdades contratam para calouros no modelo B2B (Business to Business - Empresa para Empresa) por pacotes de licenças, e estudantes avulsos assinam mensalmente no modelo B2C (Business to Consumer - Empresa para Consumidor).')

    # ==================== PÁGINA 2: SLIDE 2 ====================
    pdf.add_page()
    pdf.add_slide_title("2", "Engenharia de Requisitos & LGPD (Etapa 2)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Mapeamento de Requisitos, backlog do produto, Kanban (Quadro Visual) e a LGPD.')
    pdf.add_bullet_point('Requisitos', 'RFs (Requisitos Funcionais - login, responder decks) e RNFs (Requisitos Nao Funcionais - responsividade e acessibilidade).')
    pdf.add_bullet_point('LGPD e Kanban', 'Backlog priorizado em Fibonacci. Consentimento por checkbox e senhas com hash criptografico SHA-256 (Algoritmo de Hash Seguro).')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Nesta etapa, nos planejamos a engenharia de requisitos de forma agil, mapeando o que o usuario faz (Requisitos Funcionais) e criterios de qualidade (Requisitos Nao Funcionais), como responsividade e acessibilidade. Usamos a sequencia de Fibonacci no Kanban (Quadro Visual) do Trello. A privacidade atende a LGPD (Lei Geral de Protecao de Dados): projetamos no Figma o consentimento e hash SHA-256 para senhas.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Como voces estimaram e priorizaram as tarefas do backlog do produto?',
                   'Usamos a sequencia de Fibonacci nos rituais de planejamento: tarefas visuais conhecidas (Figma de login) ganharam peso 3, e tarefas logicas complexas (calculo do SM-2) ganharam peso 8.')
    pdf.add_defesa('Como a LGPD (Lei Geral de Protecao de Dados) aparece de forma concreta no seu projeto?',
                   'Modelamos o checkbox de consentimento de privacidade na tela de cadastro do Figma e criptografia hash SHA-256 no banco de dados para que ninguem leia as senhas em texto puro.')

    # ==================== PÁGINA 3: SLIDE 3 ====================
    pdf.add_page()
    pdf.add_slide_title("3", "Modelagem de Banco de Dados (Etapa 3)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Projeto relacional do banco de dados estruturado no Microsoft SQL Server.')
    pdf.add_bullet_point('Estrutura ACID', 'SQL Server garante propriedades ACID (Atomicidade, Consistencia, Isolamento, Durabilidade) no saldo de moedas.')
    pdf.add_bullet_point('Normalizacao e Cascade', 'Tabelas em 1FN/2FN/3FN (Formas Normais). Exclusao em cascata no DDL (Linguagem de Definicao de Dados) das alternativas.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Para a persistencia de dados, projetamos a base no Microsoft SQL Server. Optamos pelo modelo relacional para garantir as propriedades transacionais ACID (Atomicidade, Consistencia, Isolamento, Durabilidade), impedindo que o saldo de moedas virtuais dos calouros apresente inconsistencias. Normalizamos as tabelas nas Formas Normais e implementamos a delecao em cascata nas alternativas no script DDL fisico.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Por que nao usaram um banco NoSQL (Não Relacional, como MongoDB) para o core do sistema?',
                   'Como o aluno consome moedas para comprar itens na loja, precisamos de garantias transacionais rigidas ACID. NoSQL tem maior risco de gerar inconsistencias no saldo em acessos simultaneos.')
    pdf.add_defesa('Qual a vantagem pratica do ON DELETE CASCADE que voces modelaram?',
                   'Se o tutor apagar uma questao do banco de dados, o SQL Server apaga na hora todas as alternativas daquela questao de forma automatica no script DDL, evitando lixo relacional e dados orfaos.')

    # ==================== PÁGINA 4: SLIDE 4 ====================
    pdf.add_page()
    pdf.add_slide_title("4", "Programacao Orientada a Objetos (Etapa 4)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Modelagem conceitual de classes no Astah UML e mapeamento conceitual em C#.')
    pdf.add_bullet_point('Heranca e UML', 'Superclasse Usuario herdada por Aluno (com moedas/XP) e Tutor. Desenhado no Astah UML.')
    pdf.add_bullet_point('Encapsulamento e SOLID', 'Escrita privada (private set) nos saldos de Aluno. Mapeamento de SRP (Principio da Responsabilidade Unica) do SOLID.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'A arquitetura de POO (Programacao Orientada a Objetos) foi desenhada visualmente no software Astah UML e mapeada para o C# .NET 10. Criamos a classe base Usuario e aplicamos herança para estender as classes Aluno e Tutor, reaproveitando codigo. Para garantir a seguranca das regras de pontos, aplicamos encapsulamento limitando a escrita do XP e moedas via private set. E planejamos o SOLID isolando o SM-2 em ISm2Engine.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Onde e como voces criaram e planejaram essas classes do projeto?',
                   'Modelamos toda a arquitetura conceitual de classes visualmente no software **Astah UML** (Linguagem de Modelagem Unificada), definindo atributos, tipos de dados e heranca. Exportamos esse blueprint para o código C#.')
    pdf.add_defesa('Como o encapsulamento protege o saldo de moedas do Aluno no codigo?',
               'Os campos de saldo possuem escrita privada (private set). Outras classes nao conseguem alterar o saldo de moedas do aluno de fora; sao obrigadas a passar pelo metodo AdicionarMoedas().')

    # ==================== PÁGINA 5: SLIDE 5 ====================
    pdf.add_page()
    pdf.add_slide_title("5", "Desenvolvimento Web Responsivo (Etapa 5)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Projetagem de pagina unica (SPA), CSS Puro (Vanilla) e a monografia em HTML/CSS.')
    pdf.add_bullet_point('SPA Vanilla', 'Carregamento dinâmico sem frameworks via fetch com a API transferindo dados de flashcards em JSON.')
    pdf.add_bullet_point('Grid, Flexbox e ABNT', 'CSS Grid para a estrutura cartesiana (dashboard) e Flexbox para menus. Reset de impressao com @media print no CSS para ABNT.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Projetamos o frontend como SPA (Single Page Application - Aplicacao de Pagina Unica) em HTML (Linguagem de Marcacao) e CSS (Folha de Estilo) puro, garantindo carregamento sem atritos. Adotamos CSS Grid para a estrutura do dashboard e Flexbox para organizar os menus. O diferencial do grupo foi programar a monografia academica em index.html e style.css seguindo as normas ABNT via @media print.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Por que optaram por Vanilla JavaScript e nao frameworks como React ou Bootstrap?',
                   'Para garantir carregamento leve no celular e controle absoluto de design do portal. Isso nos permitiu configurar o reset de impressao @media print de forma nativa e sem interferencia externa.')
    pdf.add_defesa('Como Grid e Flexbox se dividem na responsividade do portal?',
                   'CSS Grid organiza a grade maior (dashboard e Mapa Neural) e Flexbox organiza menus e botoes. Nas media queries do style.css, empilhamos as colunas do Grid em telas pequenas para celulares.')

    # ==================== PÁGINA 6: SLIDE 6 ====================
    pdf.add_page()
    pdf.add_slide_title("6", "UX/UI Design & Heurísticas (Etapa 6)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Modelagem no Figma, jornada da persona e Heuristicas de usabilidade.')
    pdf.add_bullet_point('Modelagem Figma', 'Desenho das telas no Figma com Design System (--alura-cyan) e affordance (cards com sombra).')
    pdf.add_bullet_point('Heuristicas aplicadas', 'Cinco regras de Nielsen: Correspondencia (mapa Obsidian View), Consistencia, Controle do usuario, Feedback visual (hud de XP) e Prevencao de erros.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'A usabilidade e o prototipo de alta fidelidade das telas de Login, Cadastro e Dashboard foram desenhados no Figma. Focamos em uma persona de 18 a 20 anos iniciante em TI. No Figma, desenhamos telas de alta fidelidade e aplicamos Heuristicas de Nielsen. A principal delas e a Correspondencia com o mundo real no Mapa Neural (Obsidian View) para o progresso de estudos da persona.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Onde as telas de usabilidade do projeto foram desenhadas?',
                   'Modelamos toda a interface de usabilidade (UX - Experiencia do Usuario) e o prototipo interativo (UI - Interface do Usuario) das telas no software **Figma**, definindo a tipografia e cores.')
    pdf.add_defesa('Como as Heurísticas de Nielsen aparecem no visual do Figma?',
                   'Exemplos: Correspondencia (mapa mental Obsidian), Consistencia (cores e botoes unificados), Controle (botao Voltar sem barreiras), Feedback (HUD de moedas brilhando) e Prevencao de erros (confirmacao).')

    # ==================== PÁGINA 7: SLIDE 7 ====================
    pdf.add_page()
    pdf.add_slide_title("7", "Machine Learning & Dados (Etapa 7)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Algoritmo SM-2 combatendo a curva de esquecimento de Hermann Ebbinghaus.')
    pdf.add_bullet_point('Projetagem SM-2', 'Formula matematica do SM-2 (Algoritmo SuperMemo 2) calcula o intervalo de revisao em dias com base no feedback de facilidade (nota 0 a 5).')
    pdf.add_bullet_point('Machine Learning', 'Massa de dados de revisoes a ser salva na tb_flashcards_sm2 servira para treinar modelos de ML (Machine Learning - Aprendizado de Maquina) no futuro.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Para tornar o estudo ativo e eficiente, projetamos o algoritmo matematico SM-2, que combate cientificamente a Curva de Esquecimento de Ebbinghaus. Quando o aluno responde um flashcard e atribui nota de facilidade de 0 a 5, a formula calcula o Fator de Facilidade e o intervalo de dias. Nota 5 oculta o card por 6 dias e nota 1 faz reaparecer amanha. Planejamos esses dados para treinar modelos preditivos no futuro.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Como o algoritmo SM-2 funciona na modelagem conceitual do calculo?',
                   'O algoritmo usa a nota (0 a 5) dada pelo aluno para atualizar o Fator de Facilidade. Se a nota for alta (facil), o intervalo de revisao em dias aumenta; se for baixa (dificil), o card reaparece rapido.')
    pdf.add_defesa('Como voces pretendem usar esses dados para Machine Learning (ML)?',
                   'No proximo semestre (PIM IV), usaremos a tabela tb_flashcards_sm2 para treinar modelos preditivos de ML (Machine Learning - Aprendizado de Maquina) para alertar se o aluno corre risco de reprovacao.')

    # ==================== PÁGINA 8: SLIDE 8 ====================
    pdf.add_page()
    pdf.add_slide_title("8", "Acessibilidade & LIBRAS (Etapa 8)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Acessibilidade universal no portal, WAI-ARIA e VLibras.')
    pdf.add_bullet_point('Tags WAI-ARIA', 'Atributos (aria-label, role, aria-selected) na monografia index.html garantem leitura de botoes por leitores de tela.')
    pdf.add_bullet_point('VLibras e Zoom', 'CSS responsivo Grid/Flexbox suporta zoom de ate 200% sem quebras de layout. Planejada traducao para LIBRAS (Lingua Brasileira de Sinais) via VLibras (avatar 3D).')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'A acessibilidade digital foi projetada nos mockups do Figma e codificada no HTML5 semântico da monografia. Injetamos rotulos acessiveis WAI-ARIA (Aplicacoes de Internet Rica Acessiveis) nas acoes de controle, garantindo que deficientes visuais naveguem com leitores de tela. O layout responsivo Grid/Flexbox suporta zoom de 200% sem distorcer o site. E prevemos a traducao para LIBRAS com o VLibras.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('O que sao as etiquetas WAI-ARIA e onde estao aplicadas no site?',
                   'Atributos (Iniciativa de Acessibilidade da Web) que dizem a leitores de tela o que os botoes fazem. Exemplo: no botao de seta para passar o flashcard, colocamos aria-label="Passar para proximo flashcard" para leitores.')
    pdf.add_defesa('Como trataram a acessibilidade para pessoas com baixa visao?',
                   'Usamos cores com contraste WCAG (Diretrizes de Acessibilidade) e layouts flexiveis Grid/Flexbox. Se o usuario aumentar a fonte no navegador em ate 200%, as tabelas se reorganizam sem cortar textos.')

    # ==================== PÁGINA 9: SLIDE 9 ====================
    pdf.add_page()
    pdf.add_slide_title("9", "Integracao & Modelagem UML (Etapa 9)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Integracao conceitual e consistência lógica de diagramacao UML no Astah.')
    pdf.add_bullet_point('Diagramas no Astah', 'Diagrama de Classes (planta estatica de POO C#), Diagrama de Casos de Uso (limites) e Diagrama de Sequencia (tempo).')
    pdf.add_bullet_point('Consistencia Logica', 'UML (Linguagem de Modelagem Unificada) garante que o visual do Figma, a logica em C# e o banco SQL Server se comuniquem perfeitamente.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Para integrar e validar toda a consistência logica da plataforma, criamos os diagramas UML (Linguagem de Modelagem Unificada) no software Astah UML. O Diagrama de Casos de Uso delimita as fronteiras de acesso de Aluno, Tutor e Admin; o Diagrama de Classes planeja a modelagem conceitual estatica em C#; e o Diagrama de Sequencia desenha o fluxo dinâmico cronologico das requisicoes.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Qual a importância do Diagrama de Sequência UML no projeto?',
                   'Mostrar a ordem cronológica e a troca de mensagens entre o cliente web, a lógica do backend C# e as atualizações físicas no banco de dados SQL Server, provando a viabilidade de rotas.')
    pdf.add_defesa('Como Figma, Astah UML e banco de dados se relacionam no PIM III?',
                   'O Figma define a usabilidade das telas; o Astah UML planeja a arquitetura estática/dinâmica (Classes e Sequências); e o SQL Server e C# dão os modelos e rotinas que unificam o PIM III.')

    # ==================== PÁGINA 10: METODOLOGIA DE GRUPO ====================
    pdf.add_page()
    pdf.add_slide_title("10", "Metodologia Scrum & Escopo (Scrum)")
    pdf.ln(1)
    
    pdf.add_bullet_point('Conteudo do Slide', 'Rituais de sprints, manuais complementares e definicao realista de escopo.')
    pdf.add_bullet_point('Rituais Scrum', 'Sprints de 1 semana registradas em 10 atas. Kanban no Trello. Scrum Masters rotativos (Gabriel e Maciel).')
    pdf.add_bullet_point('Fronteira de Escopo', 'O 3º Semestre foca na prototipagem no Figma e modelagem lógica no Astah. Módulos complexos de simulados ENADE e loja sao escopo do PIM IV.')
    pdf.ln(2.0)
    
    pdf.add_script_fala(
        'Para concluir, organizamos nosso trabalho em Sprints de uma semana com rituais Scrum semanais registrados em 10 atas e Kanban no Trello, com lideranca rotativa de Scrum Master. Criamos manuais de Execucao, Pratico e Tecnico para a extensao. Delimitamos que a entrega do 3º semestre consiste nos prototipos do Figma e na modelagem logica do Astah, sendo o codigo funcional total escopo do PIM IV.'
    )
    
    pdf.add_defesa_divider()
    pdf.add_defesa('Como voces se organizaram e gerenciaram impedimentos no grupo?',
                   'Usamos sprints de 1 semana e reuniões semanais de Sprint Planning e Review no Discord para atualizar o Kanban do Trello, organizando tarefas por responsaveis de forma transparente.')
    pdf.add_defesa('Como definiram a divisao de escopo entre o PIM III e o PIM IV?',
                   'Delimitamos nos manuais e README que a programacao do banco relacional de simulados e loja e escopo do PIM IV (Projeto Integrado Multidisciplinar IV), entregando agora os prototipos Figma e modelagem UML no Astah.')

    # Salva o arquivo PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    print(f"PDF gerado com sucesso em: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        out = sys.argv[1]
    else:
        out = "docs/apresentação.pdf"
    gerar_apresentacao(out)

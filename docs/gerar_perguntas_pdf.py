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

class NexTIPerguntasPDF(FPDF):
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
        self.cell(0, 7, 'NEX_TI - GUIA DE PERGUNTAS E RESPOSTAS DA BANCA', 0, 1, 'C')
        
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

    def add_etapa_title(self, number, title):
        self.set_font('Helvetica', 'B', 12.5)
        self.set_text_color(15, 23, 42)
        
        # Caixa de fundo para o título da etapa (Slate 249/241/245)
        self.set_fill_color(241, 245, 249)
        self.cell(0, 8.0, f' ETAPA {number}: {title.upper()}', 0, 1, 'L', fill=True)
        self.ln(3.0)

    def add_pergunta_resposta(self, num_pergunta, question, answer):
        y_init = self.get_y()
        
        # Recuo para o texto, deixando espaço para a barra esquerda
        self.set_left_margin(19)
        self.set_x(19)
        
        # Pergunta (Fonte aumentada 10.5, Negrito, Cor Slate 900)
        self.set_font('Helvetica', 'B', 10.5)
        self.set_text_color(15, 23, 42)
        self.multi_cell(176, 4.8, f'P{num_pergunta}. {question}')
        self.ln(1.5)
        
        # Resposta (Fonte 10.0, Normal, Cor Slate 700 para contraste equilibrado)
        self.set_font('Helvetica', '', 10.0)
        self.set_text_color(51, 65, 85)
        self.set_x(19)
        self.multi_cell(176, 4.4, f'R: {answer}')
        
        y_final = self.get_y()
        
        # Restaura a margem padrão (15)
        self.set_left_margin(15)
        self.set_x(15)
        
        # Desenha a barra vertical lateral Teal na esquerda do bloco de texto
        self.set_fill_color(13, 148, 136) # Teal
        self.rect(15, y_init, 1.5, y_final - y_init, 'F')
        
        # Espaçador para o próximo bloco de pergunta
        self.set_y(y_final + 6.0)

def gerar_perguntas_pdf(output_path):
    pdf = NexTIPerguntasPDF()
    pdf.set_top_margin(36)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_auto_page_break(auto=True, margin=12)
    
    # Base de dados estruturada com as 30 perguntas e respostas
    etapas = [
        {
            "numero": "1",
            "titulo": "Caracterizacao do Negocio Ficticio",
            "perguntas": [
                {
                    "num": 1,
                    "q": "O que e a startup Nex_TI Educacional, qual o seu segmento de atuacao e qual oportunidade de mercado ela atende?",
                    "a": "A Nex_TI Educacional e uma startup ficticia de Tecnologia da Informacao (TI) voltada para o segmento de tecnologia educacional (EdTech), operando no modelo comercial SaaS (Software as a Service - Software como Servico), onde o faturamento e gerado por assinaturas recorrentes na nuvem. A oportunidade de mercado que identificamos baseia-se em uma dor real e cronica dos cursos superiores e tecnicos de TI (Tecnologia da Informacao): o altissimo indice de evasao de alunos logo nos primeiros semestres, motivado pelo medo e pela dificuldade de fixar a enorme quantidade de jargoes tecnicos e conceitos abstratos (como algoritmos, protocolos de rede e banco de dados). Resolvemos essa dor oferecendo um portal de estudo ativo baseado em flashcards interativos (cartoes de revisao rapida com pergunta na frente e resposta no verso) integrado ao algoritmo de repeticao espacada SM-2 (SuperMemo 2). Na pratica, a plataforma funciona como um nivelador academico interativo que ajuda o aluno iniciante a fixar conceitos complexos sem sobrecarga cognitiva."
                },
                {
                    "num": 2,
                    "q": "Quem e o publico-alvo da Nex_TI e qual a estrategia de comercializacao planejada?",
                    "a": "Nosso publico-alvo e dividido em duas frentes de mercado. A principal e o B2B (Business to Business - Empresa para Empresa), que atende instituicoes de ensino de tecnologia (faculdades e escolas tecnicas) que contratam a plataforma para nivelar turmas inteiras de calouros, recebendo paineis de estatisticas para que os coordenadores acompanhem o rendimento das salas. A segunda frente e o B2C (Business to Consumer - Empresa para Consumidor), voltada a estudantes e profissionais iniciantes em transicao de carreira de 18 a 20 anos que desejam estudar de forma autonoma para certificacoes e exames. A estrategia de comercializacao B2B funciona por assinaturas anuais com base na quantidade de licencas de estudantes ativos, enquanto o B2C opera no modelo de assinatura mensal direta no portal. Exemplo pratico: Uma faculdade de ADS (Analise e Desenvolvimento de Sistemas) contrata o sistema no inicio do semestre letivo e cria um 'torneio de nivelamento' para fazer os novos alunos aprenderem a logica de programacao de forma gamificada."
                },
                {
                    "num": 3,
                    "q": "Quais sao as principais regras de funcionamento (Regras de Negocio) definidas para manter a consistencia do sistema?",
                    "a": "Modelamos tres regras de negocio fundamentais (RNs) para regular o funcionamento e a integridade da plataforma:\n- RN01 (Atribuicao de Recompensas): O aluno so ganha as recompensas da sessao (pontos de XP (Pontos de Experiencia) e moedas virtuais) se responder e concluir 100% das perguntas do deck de flashcards selecionado. Se ele abandonar o deck no meio da rodada, nao recebe nada. Essa regra foi criada para evitar trapacas (cheating) e garantir que o ciclo de repeticao espacada exigido pelo algoritmo seja cumprido pelo cerebro.\n- RN02 (Perfis de Acesso): O Aluno apenas estuda e consome os flashcards. O Tutor tem acesso a area de cadastro para criar novas perguntas e alternativas. O Admin (Administrador) gerencia todos.\n- RN03 (Economia Virtual): As moedas adquiridas servem apenas para compras de itens cosmeticos na loja interna do site, como novos avatares ou temas de visual personalizados, aumentando o engajamento sem criar recompensas financeiras reais."
                }
            ]
        },
        {
            "numero": "2",
            "titulo": "Engenharia de Software Agil e LGPD (Lei Geral de Protecao de Dados)",
            "perguntas": [
                {
                    "num": 4,
                    "q": "Como o grupo dividiu e mapeou os requisitos tecnicos do sistema de forma estruturada?",
                    "a": "Dividimos o escopo do sistema de forma classica em Requisitos Funcionais (RF - Funcionalidades do Sistema) e Requisitos Nao Funcionais (RNF - Caracteristicas de Qualidade). Os Requisitos Funcionais especificam as acoes diretas do usuario na interface (ex: o login de usuarios, a criacao de decks pelo tutor e a visualizacao do Mapa Neural pelo aluno). Ja os Requisitos Nao Funcionais descrevem criterios de qualidade, desempenho e seguranca do sistema (ex: a responsividade estrita da interface para rodar em smartphones e computadores, e a conformidade com as regras de acessibilidade WCAG (Web Content Accessibility Guidelines - Diretrizes de Acessibilidade para Conteudo Web)). Exemplo pratico: O requisito funcional RF03 especifica a interface de flashcards onde o aluno vira a carta para ler a resposta. O requisito nao funcional RNF02 garante que essa mesma acao seja amigavel a leitores de tela usando etiquetas acessiveis e navegacao simples por teclado."
                },
                {
                    "num": 5,
                    "q": "O que e o backlog do produto e como a equipe estimou o esforco de desenvolvimento do projeto?",
                    "a": "O backlog do produto e a lista priorizada de todas as tarefas e funcionalidades que precisam ser construidas na plataforma, organizadas em blocos funcionais chamados Epicos (Autenticacao, Motor de Flashcards, Economia Virtual e Acessibilidade). Para estimar o esforco de cada tarefa, utilizamos o ritual de Planning Poker com a sequencia de Fibonacci nas reunioes do grupo. Exemplo pratico: Tarefas com escopo visual simples e de baixo atrito, como desenhar as telas de login e cadastro de usuarios no Figma, receberam peso de esforco 3. Tarefas de alta complexidade de logica relacional e matematica, como modelar as tabelas do algoritmo SM-2 (SuperMemo 2) e estruturar as variaveis em C#, receberam peso de esforco 8 devido a maior incerteza e regras envolvidas."
                },
                {
                    "num": 6,
                    "q": "Como a equipe organizou as Sprints semanais utilizando o Kanban e como garantiram a conformidade com a LGPD (Lei Geral de Protecao de Dados)?",
                    "a": "Usamos a plataforma Trello para implementar um quadro Kanban (Painel de Fluxo Visual), organizando o andamento das atividades em colunas claras: A Fazer (To Do), Em Andamento (Doing), Testes (Testing) e Concluido (Done), associando responsaveis a cada tarefa. Em conformidade estrita com a LGPD (Lei Geral de Protecao de Dados), planejamos na interface do Figma que, no momento do cadastro do usuario, seja exigido o consentimento explicito dos termos de uso. No modelo de banco de dados SQL (Structured Query Language - Linguagem de Consulta Estruturada) Server, especificamos que senhas nao sao armazenadas em texto limpo; elas passam obrigatoriamente por um algoritmo de hash criptografico SHA-256 (Algoritmo de Hash Seguro de 256 bits) no backend, garantindo que os dados dos usuarios permanecam confidenciais mesmo em caso de vazamento na base."
                }
            ]
        },
        {
            "numero": "3",
            "titulo": "Modelagem de Banco de Dados",
            "perguntas": [
                {
                    "num": 7,
                    "q": "Por que foi escolhido um banco de dados relacional (SQL Server) em vez de outros modelos como NoSQL (Nao Relacional)?",
                    "a": "A escolha do Microsoft SQL Server baseou-se nas garantias das propriedades ACID (Atomicidade, Consistencia, Isolamento e Durabilidade). Como a Nex_TI opera com uma economia de moedas virtuais acumuladas para desbloquear avatares na loja, precisamos de seguranca transacional rigorosa. Um banco de dados relacional com integridade referencial impede que moedas sejam geradas incorretamente em acessos simultaneos ou que um aluno excluido mantenha registros orfaos ativos. Exemplo pratico: O banco relacional com chaves estrangeiras (FK - Foreign Key) garante a consistencia do saldo. Si precisassemos escalar o sistema para logs temporarios de auditoria ou historico de cliques de milhoes de alunos, poderiamos adotar uma arquitetura hibrida usando NoSQL (Nao Relacional, como o MongoDB) de forma isolada para processamento de alto volume."
                },
                {
                    "num": 8,
                    "q": "Como foi aplicada a normalizacao de dados e qual a utilidade da regra de 'exclusao em cascata' nas tabelas do SQL Server?",
                    "a": "Aplicamos as Formas Normais (1FN, 2FN e 3FN - Primeira, Segunda e Terceira Formas Normais) para eliminar anomalias de insercao, exclusao e alteracao. Um exemplo e a tabela associativa tb_prova_questao, criada para resolver o relacionamento de muitos-para-muitos (N:N) entre Provas e Questoes. A regra de exclusao em cascata (ON DELETE CASCADE) foi implementada na chave estrangeira que liga a tabela tb_alternativas a tabela tb_questoes. Exemplo pratico: Se um Tutor excluir uma Questao na interface, o banco de dados SQL Server apaga automaticamente todas as alternativas correspondentes de forma transparente no script DDL (Data Definition Language - Linguagem de Definicao de Dados), garantindo que a base de dados permaneca limpa de dados inuteis e economizando processamento de limpeza manual."
                },
                {
                    "num": 9,
                    "q": "Como o historico de estudos do aluno e os parametros do algoritmo SM-2 (SuperMemo 2) sao persistidos no banco?",
                    "a": "Criamos a tabela especifica tb_flashcards_sm2 para persistir o estado das revisoes. Ela guarda a chave estrangeira do usuario (id_usuario), a frente e o verso da carta, e tres colunas cruciais para o algoritmo:\n- fator_facilidade (float, inicializado em 2.5): Determina o grau de facilidade de recordacao daquele cartao.\n- intervalo_dias (integer): Quantidade de dias que o sistema esperara ate reexibir o cartao para o aluno.\n- data_proxima_revisao (date): O dia em que o cartao reaparecera no dashboard do aluno. A cada rodada que o aluno estuda e da um feedback de nota (0 a 5), a API (Application Programming Interface - Interface de Programacao de Aplicacao) calcula o SM-2 e atualiza essas tres colunas no banco de dados."
                }
            ]
        },
        {
            "numero": "4",
            "titulo": "Desenvolvimento com POO (Programacao Orientada a Objetos) (C#)",
            "perguntas": [
                {
                    "num": 10,
                    "q": "Onde a modelagem conceitual das classes foi criada e como foi estruturada em C#?",
                    "a": "Toda a nossa arquitetura de classes foi modelada e desenhada visualmente utilizando o software Astah UML (Unified Modeling Language - Linguagem de Modelagem Unificada) (definindo propriedades, metodos de classe, multiplicidades e relacionamentos de heranca). A partir desse desenho logico, planejamos as classes estruturais em C# (.NET 10). Exemplo pratico: Criamos a classe base Usuario.cs contendo as propriedades comuns (ID, Nome, Email e Senha). Usando o pilar de Heranca, derivamos as subclasses Aluno.cs (que inclui a composicao de moedas e XP) e Tutor.cs (que adiciona funcoes de edicao). Isso evita redundancia de codigo e garante que qualquer mudanca em propriedades basicas de usuarios seja herdada automaticamente por todos os perfis do sistema."
                },
                {
                    "num": 11,
                    "q": "Como o conceito de protecao de dados (encapsulamento) e os principios SOLID foram planejados para as classes?",
                    "a": "Aplicamos o encapsulamento restringindo a modificacao direta de atributos criticos. Exemplo pratico: Os campos xp_acumulado e moedas_virtuais na classe Aluno.cs possuem modificador de escrita privada (private set). Isso impede que qualquer outra classe mude os pontos do aluno de forma indevida de fora. O saldo so e atualizado de forma controlada chamando metodos da propria classe, como AdicionarMoedas(int quantidade), que validam as regras de negocio. Adicionalmente, aplicamos o Principio da Responsabilidade Unica (SRP - Single Responsibility Principle) do SOLID (Principios de Engenharia de Software) ao isolar toda a formula matematica do algoritmo SM-2 na classe ISm2Engine em backend/Services/, impedindo que classes de dados ou controladores fiquem inflados com logica de calculo."
                },
                {
                    "num": 12,
                    "q": "O que e a classe Program.cs e como ela foi estruturada para manter a legibilidade do codigo?",
                    "a": "E o arquivo inicial e ponto de entrada da nossa API (Application Programming Interface - Interface de Programacao de Aplicacao) backend em C#. Em projetos com Minimal APIs do .NET, e comum que a configuracao de banco, injecao de dependencia e mapeamento de caminhos inflem o arquivo inicial. Para manter o codigo legivel e seguir boas praticas de engenharia, planejamos mover todos os caminhos e mapeamentos de endpoints para uma classe estatica de extensao separada chamada EndpointExtensions.cs, mantendo o Program.cs focado exclusivamente nas definicoes essenciais de inicializacao de servicos."
                }
            ]
        },
        {
            "numero": "5",
            "titulo": "Desenvolvimento Web Responsivo",
            "perguntas": [
                {
                    "num": 13,
                    "q": "O que significa desenvolver a interface como uma SPA (Single Page Application) e quais os beneficios?",
                    "a": "Significa que todo o portal funciona em uma pagina unica que e carregada apenas uma vez pelo navegador, e as atualizacoes de tela acontecem dinamicamente sem recarregar o site. Exemplo pratico: Quando o aluno clica para abrir uma sessao de flashcards, o JavaScript do frontend intercepta a acao, faz uma requisicao assintrona usando o comando fetch para a nossa API em C#, recebe as perguntas em formato JSON (JavaScript Object Notation - Notacao de Objetos JavaScript), e atualiza apenas a area de cartoes da tela. Isso elimina a necessidade de fazer o navegador piscar e baixar arquivos HTML (HyperText Markup Language - Linguagem de Marcacao de Hipertexto) pesados novamente, proporcionando uma transicao de tela instantanea."
                },
                {
                    "num": 14,
                    "q": "Por que foi escolhido HTML/CSS Puro (Vanilla) em vez de frameworks visuais?",
                    "a": "A escolha por Vanilla HTML5/CSS3 puro nos garante o maximo de desempenho, baixo consumo de dados moveis e controle absoluto sobre o codigo e formatacao academica. Exemplo pratico: No arquivo style.css, criamos regras de impressao estilizadas com @media print para que toda a monografia desenvolvida em HTML (HyperText Markup Language) seja impressa exatamente dentro das margens, fontes e especificacoes da ABNT (Associacao Brasileira de Normas Tecnicas) de forma nativa."
                },
                {
                    "num": 15,
                    "q": "Como funciona a adaptacao fluida de layout (responsividade) usando CSS Grid e Flexbox?",
                    "a": "Adotamos uma estrategia adaptativa no style.css. Usamos CSS Grid (Grade de Layout Bidimensional) para estruturar as areas principais e bidimensionais (como a divisao das colunas do dashboard (painel gerencial) de estudos) e CSS Flexbox (Caixa Flexivel Unidimensional) para alinhar elementos unidimensionais menores (como botoes, avatares e barras de navegacao). Exemplo pratico: Usamos media queries (consultas de midia) para fazer com que, em resolucoes de telas menores (celulares), as colunas horizontais do dashboard em CSS Grid se empilhem verticalmente de forma automatica e os botoes aumentem de area de clique para facilitar o toque com o polegar."
                }
            ]
        },
        {
            "numero": "6",
            "titulo": "UX (User Experience) e UI (User Interface) Design (Figma e Heuristicas)",
            "perguntas": [
                {
                    "num": 16,
                    "q": "Onde as interfaces de usuario foram projetadas e qual foi a base de estudo de usabilidade?",
                    "a": "Toda a interface do usuario (telas de login, dashboard de estudos e os cartoes) foi modelada e prototipada integralmente no software Figma. No Figma, criamos o nosso Design System (Sistema de Design) definindo uma paleta cromatica unificada (cor principal --alura-cyan para as acoes primarias) e tipografias de alta leitura. A usabilidade foi baseada na jornada de uma Persona: um jovem de 18 a 20 anos que busca nivelamento introdutorio em TI (Tecnologia da Informacao). Como esse usuario possui inseguranca com jargoes, as telas no Figma foram projetadas com botoes grandes, dicas visuais (affordance clara) e poucos textos para evitar medo ou sobrecarga cognitiva."
                },
                {
                    "num": 17,
                    "q": "Quais Heuristicas de Nielsen foram aplicadas no prototipo desenvolvido no Figma?",
                    "a": "Aplicamos cinco heuristicas fundamentais de usabilidade nas telas do Figma:\n- Correspondencia com o mundo real: O progresso do aluno e exibido na forma de um Mapa Neural de conexoes (Obsidian Neural View), simulando graficamente um mapa mental fisico de estudos familiares.\n- Consistencia e padroes: Todos os botoes primarios seguem o mesmo tamanho de cantos arredondados, cor ciano e efeitos visuais identicos, garantindo que o usuario aprenda a usa-los uma unica vez.\n- Controle e liberdade do usuario: Colocamos botoes claros de 'Voltar' ou 'Pausar estudos' em todas as telas, permitindo ao aluno abortar o estudo dos flashcards a qualquer momento sem barreiras ou perdas punitivas de moedas.\n- Feedback visual (Visibilidade do estado do sistema): A barra de progresso e o saldo de moedas no HUD (Heads-Up Display - Painel de Informacoes Flutuantes) do topo piscam e se atualizam dinamicamente no momento em que uma questao e respondida com sucesso.\n- Prevencao de erros: Adicionamos telas de confirmacao ('Deseja mesmo finalizar os estudos?') antes de fechar a rodada para evitar que toques involuntarios na tela apaguem o progresso atual do deck."
                },
                {
                    "num": 18,
                    "q": "Como a prototipagem no Figma e os conceitos de usabilidade garantem que o visual do site seja intuitivo?",
                    "a": "Passamos pelas etapas de Wireframes de Baixa Fidelidade (esbocos conceituais em tons de cinza para focar no fluxo) ate o Prototipo Interativo de Alta Fidelidade. Aplicamos o conceito de Affordance (Caracteristicas de Acao) e Signifiers (Sinalizadores): os cartoes de flashcards possuem sombras sutis e icones de 'virar' que sinalizam fisicamente que podem ser rotacionados. O Mapa Neural possui fisica visual de conexoes que guiam o olhar do aluno, mostrando que nos apagados representam materias ainda nao iniciadas e nos brilhantes representam topicos ja dominados no prototipo Figma."
                }
            ]
        },
        {
            "numero": "7",
            "titulo": "Machine Learning (Aprendizado de Maquina) e Analise de Dados",
            "perguntas": [
                {
                    "num": 19,
                    "q": "Qual a relacao matematica do algoritmo SM-2 (SuperMemo 2) com a aprendizagem ativa no projeto?",
                    "a": "O SM-2 (SuperMemo 2) e a formula usada para calcular o intervalo ideal de dias para o aluno rever cada flashcard com base no seu feedback. Apos o aluno visualizar a resposta de um flashcard, ele avalia a facilidade de recordacao dando uma nota de 0 a 5. A formula recalcula o Fator de Facilidade (EF - Easiness Factor) da seguinte forma:\nEF' = EF + (0.1 - (5 - nota) * (0.08 + (5 - nota) * 0.02))\nCom o novo EF, o sistema calcula o numero de dias de intervalo para a proxima revisao. Exemplo pratico: Se a nota dada for 5 (muito facil), o intervalo salta para 6 dias. Se for 1 (dificil), o card reaparece no dia seguinte, forcando o cerebro a resgatar ativamente a informacao de forma personalizada para cada estudante."
                },
                {
                    "num": 20,
                    "q": "Como os dados gerados nas sessoes sao gravados e como podem ser usados para Machine Learning no futuro?",
                    "a": "Gravamos os tempos de resposta, a taxa de erros e as notas fornecidas em cada flashcard na tabela tb_flashcards_sm2. Essa massa de dados estruturados gera relatorios de desempenho. Exemplo pratico: No PIM IV (4º Semestre), esses dados servirao para treinar modelos preditivos de inteligencia artificial baseados em ML (Machine Learning - Aprendizado de Maquina). A IA (Inteligencia Artificial) podera cruzar o tempo de estudo do aluno com suas notas de flashcards para prever de forma precoce quais estudantes estao em risco de reprovacao ou evasao, gerando alertas de intervencao para os tutores."
                },
                {
                    "num": 21,
                    "q": "O que e a Curva de Esquecimento de Hermann Ebbinghaus e como o SM-2 (SuperMemo 2) a resolve?",
                    "a": "E o estudo cientifico que prova que a memoria humana esquece informacoes novas de forma exponencial ao longo do tempo (a curva cai acentuadamente logo no primeiro dia). O algoritmo SM-2 resolve isso agendando as revisoes espacadas exatamente nos momentos em que a probabilidade de esquecimento e alta. A cada revisao bem-sucedida, a taxa de esquecimento diminui e a curva se torna mais 'plana', transferindo o conhecimento de TI da memoria de curto prazo para a memoria de longo prazo de forma cientifica."
                }
            ]
        },
        {
            "numero": "8",
            "titulo": "Comunicacao e Acessibilidade (LIBRAS - Lingua Brasileira de Sinais)",
            "perguntas": [
                {
                    "num": 22,
                    "q": "Como a acessibilidade digital e as boas praticas de desenvolvimento web foram aplicadas na plataforma?",
                    "a": "Foram pensadas desde os desenhos de interface no Figma e aplicadas no codigo HTML (HyperText Markup Language) do index.html. Empregamos HTML5 semantico e injetamos atributos de acessibilidade WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Applications) (role='tab', aria-label, aria-selected dinamicos). Exemplo pratico: Em botoes de acao do portal que contem apenas imagens ou icones visuais (como o botao de seta para avancar o flashcard), inserimos o atributo aria-label='Passar para proximo flashcard'. Assim, os softwares leitores de tela usados por pessoas com deficiencia visual conseguem ler em voz alta o que o botao faz."
                },
                {
                    "num": 23,
                    "q": "Como o projeto atende a padroes de contraste e controle de tamanho de tela?",
                    "a": "As cores selecionadas no Design System respeitam as taxas de contraste minimo estabelecidas pelas diretrizes WCAG (Web Content Accessibility Guidelines). Exemplo pratico: No CSS (Cascading Style Sheets), estruturamos os layouts de forma flexivel utilizando Grid e Flexbox com unidades de tamanho escalaveis. Se o usuario ampliar o zoom da tela do navegador para 200% devido a baixa visao, os elementos se reorganizam de forma fluida sem transbordar, sem sobrepor e sem quebrar o layout das telas."
                },
                {
                    "num": 24,
                    "q": "Como a plataforma pode ser adaptada para acessibilidade em LIBRAS (Lingua Brasileira de Sinais) no futuro?",
                    "a": "Projetamos a integracao conceitual do plugin VLibras. Exemplo pratico: Ficara visivel o icone flutuante do VLibras (uma maozinha). Ao clicar sobre ela e depois sobre um paragrafo de texto informativo de nivelamento, um avatar virtual interativo traduzira o texto em portugues para a Lingua Brasileira de Sinais (LIBRAS) por meio de animacao 3D de gestos em tempo real na tela."
                }
            ]
        },
        {
            "numero": "9",
            "titulo": "Integracao e Avaliacao Final (UML - Linguagem de Modelagem Unificada)",
            "perguntas": [
                {
                    "num": 25,
                    "q": "Como os diagramas UML garantem a integridade de todo o ecossistema Nex_TI?",
                    "a": "Os diagramas UML (Unified Modeling Language) (desenhados no software Astah UML) funcionam como o blueprint de engenharia do software. Eles provam que a nossa arquitetura foi pensada sem pontas soltas ou incoerencias estruturais antes do inicio da codificacao. Exemplo pratico: O Diagrama de Sequencia detalha a ordem exata em que as mensagens transitam (1. Clique do Aluno -> 2. Chamada da API em C# -> 3. Validacao do SM-2 -> 4. Gravacao de dados no SQL Server -> 5. Retorno de dados atualizados), garantindo que a logica que o usuario enxerga seja fisicamente viavel no banco de dados e no codigo."
                },
                {
                    "num": 26,
                    "q": "O que e o Diagrama de Classes e como ele se aplica na pratica?",
                    "a": "E o mapa conceitual estatico que planeja a estrutura das classes de codigo, desenhado no Astah UML. Ele descreve quais entidades de codigo vao existir (Usuario, Aluno, Tutor, XP, Moedas), quais sao seus atributos internos (tipos de dados e modificadores de acesso) e assinaturas de metodos. Exemplo pratico: O diagrama de classes especificou no Astah a relacao de heranca entre Usuario e suas derivadas, servindo de roteiro de implementação para que o grupo criasse o codigo C# correspondente sem improvisos."
                },
                {
                    "num": 27,
                    "q": "O que e o Diagrama de Sequencia UML e qual seu beneficio?",
                    "a": "E o diagrama dinamico que ilustra as interacoes e trocas de mensagens no tempo entre os componentes do sistema (navegador, backend em C# e banco SQL Server). Exemplo pratico: Ele mapeia o passo a passo de uma autenticacao de login ou o salvamento de um card de estudos, garantindo que a ordem logica das validacoes ocorra sem gargalos ou erros de projeto de software."
                }
            ]
        },
        {
            "numero": "10",
            "titulo": "Metodologia Scrum e Escopo",
            "perguntas": [
                {
                    "num": 28,
                    "q": "Como as reunioes Scrum nas atas ajudaram a provar a organizacao da equipe no semestre?",
                    "a": "Registramos 10 reunioes semanais de planejamento e revisao (Sprint Planning e Sprint Review) em atas formais. Elas provam as reunioes semanais, divisoes de tarefas em Kanban no Trello e a facilitacao rotativa por Gabriel Moreira e Maciel Silva. Exemplo pratico: Se a banca perguntar sobre conflitos tecnicos ou atrasos, explicamos que usavamos as reunioes de Daily Scrum diarias para identificar impedimentos de escopo e redistribuir cartoes rapidamente pelo quadro Kanban no Trello."
                },
                {
                    "num": 29,
                    "q": "Para que serviram os manuais tecnicos de extensão universitaria gerados no repositorio pratico?",
                    "a": "Escrevemos tres manuais complementares no repositorio de extensao: o Manual de Execucao (ensina a rodar a base SQL e o backend C# localmente), o Manual Pratico (guia de uso ilustrado para o usuario final aprender a rodar e usar as telas do portal) e o Manual Tecnico (que detalha as rotas de dados e seguranca do backend)."
                },
                {
                    "num": 30,
                    "q": "Como o grupo gerenciou a transicao conceitual para o PIM IV (4º semestre) e como os diagramas no Astah e as telas do Figma foram integrados no projeto academico do PIM III?",
                    "a": "Delimitamos formalmente que o 3º Semestre foca na prototipagem no Figma e modelagem logica no Astah. Modulos complexos como a logica real de banco de questoes do simulado ENADE e loja virtual estendida ja foram mapeados conceitualmente para manter a consistencia da documentacao de engenharia (como as tabelas no SQL Server e classes em UML), mas sua implementacao e programacao funcional de telas sao escopo futuro do PIM IV (4º semestre). Na integracao academica, o Figma definiu a usabilidade das telas, o Astah UML planejou a arquitetura estatica/dinamica (Classes e Sequencias), e o SQL Server/C# deram as estruturas e rotinas essenciais que unificam o PIM III (Projeto Integrado Multidisciplinar III)."
                }
            ]
        }
    ]

    for etapa in etapas:
        pdf.add_page()
        pdf.add_etapa_title(etapa["numero"], etapa["titulo"])
        for perg in etapa["perguntas"]:
            pdf.add_pergunta_resposta(perg["num"], perg["q"], perg["a"])

    # Salva o arquivo PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    print(f"PDF gerado com sucesso em: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        out = sys.argv[1]
    else:
        out = "docs/Perguntas_Banca_Nex_TI.pdf"
    gerar_perguntas_pdf(out)

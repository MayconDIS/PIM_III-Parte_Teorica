# Guia de Preparação para a Banca: PIM III (Projeto Integrado Multidisciplinar III) – Nex_TI (Modelagem com Astah, Figma e Prática)

Este guia reúne **30 perguntas e respostas com profunda riqueza teórica, técnica e prática** para a banca examinadora do PIM III (Projeto Integrado Multidisciplinar III) do Curso Superior de Tecnologia em ADS (Análise e Desenvolvimento de Sistemas). As respostas foram escritas em um tom didático, informal e com alta densidade de conteúdo relevante, projetadas para servir de roteiro de apoio para a sua fala na apresentação oral. Toda e qualquer sigla técnica possui o seu significado por extenso e tradução entre parênteses para demonstrar total domínio acadêmico diante dos avaliadores. 

As respostas destacam que a entrega atual do 3º Semestre foca na **modelagem conceitual e prototipagem** (com ferramentas como **Astah UML** (*Unified Modeling Language* - Linguagem de Modelagem Unificada) para classes e **Figma** para usabilidade), deixando claro que a codificação funcional completa é escopo do PIM IV (Projeto Integrado Multidisciplinar IV) no 4º Semestre.

---

## 📌 Etapa 1: Caracterização do Negócio Fictício

### P1. O que é a startup Nex_TI Educacional, qual o seu segmento de atuação e qual oportunidade de mercado ela atende?
**R:** A Nex_TI Educacional é uma startup fictícia de Tecnologia da Informação (TI) voltada para o segmento de tecnologia educacional (*EdTech*), operando no modelo comercial SaaS (*Software as a Service* - Software como Serviço), onde o faturamento é gerado por assinaturas recorrentes na nuvem. A oportunidade de mercado que identificamos baseia-se em uma dor real e crônica dos cursos superiores e técnicos de TI (Tecnologia da Informação): o altíssimo índice de evasão de alunos logo nos primeiros semestres, motivado pelo medo e pela dificuldade de fixar a enorme quantidade de jargões técnicos e conceitos abstratos (como algoritmos, protocolos de rede e banco de dados). Resolvemos essa dor oferecendo um portal de estudo ativo baseado em flashcards interativos (cartões de revisão rápida com pergunta na frente e resposta no verso) integrado ao algoritmo de repetição espaçada SM-2 (SuperMemo 2). Na prática, a plataforma funciona como um nivelador acadêmico interativo que ajuda o aluno iniciante a fixar conceitos complexos sem sobrecarga cognitiva.

### P2. Quem é o público-alvo da Nex_TI e qual a estratégia de comercialização planejada?
**R:** Nosso público-alvo é dividido em duas frentes de mercado. A principal é o B2B (*Business to Business* - Empresa para Empresa), que atende instituições de ensino de tecnologia (faculdades e escolas técnicas) que contratam a plataforma para nivelar turmas inteiras de calouros, recebendo painéis de estatísticas para que os coordenadores acompanhem o rendimento das salas. A segunda frente é o B2C (*Business to Consumer* - Empresa para Consumidor), voltada a estudantes e profissionais iniciantes em transição de carreira de 18 a 20 anos que desejam estudar de forma autônoma para certificações e exames. A estratégia de comercialização B2B funciona por assinaturas anuais com base na quantidade de licenças de estudantes ativos, enquanto o B2C opera no modelo de assinatura mensal direta no portal. Exemplo prático: Uma faculdade de ADS (Análise e Desenvolvimento de Sistemas) contrata o sistema no início do semestre letivo e cria um "torneio de nivelamento" para fazer os novos alunos aprenderem a lógica de programação de forma gamificada.

### P3. Quais são as principais regras de funcionamento (Regras de Negócio) definidas para manter a consistência do sistema?
**R:** Modelamos três regras de negócio fundamentais (RNs) para regular o funcionamento e a integridade da plataforma:
- **RN01 (Atribuição de Recompensas):** O aluno só ganha as recompensas da sessão (pontos de XP (Pontos de Experiência) e moedas virtuais) se responder e concluir 100% das perguntas do deck de flashcards selecionado. Se ele abandonar o deck no meio da rodada, não recebe nada. Essa regra foi criada para evitar trapaças (*cheating*) e garantir que o ciclo de repetição espaçada exigido pelo algoritmo seja cumprido pelo cérebro.
- **RN02 (Perfis de Acesso):** O Aluno apenas estuda e consome os flashcards. O Tutor tem acesso à área de cadastro para criar novas perguntas e alternativas. O Admin (Administrador) gerencia todos.
- **RN03 (Economia Virtual):** As moedas adquiridas servem apenas para compras de itens cosméticos na loja interna do site, como novos avatares ou temas de visual personalizados, aumentando o engajamento sem criar recompensas financeiras reais.

---

## 📐 Etapa 2: Engenharia de Software Ágil e LGPD (Lei Geral de Proteção de Dados)

### P4. Como o grupo dividiu e mapeou os requisitos técnicos do sistema de forma estruturada?
**R:** Dividimos o escopo do sistema de forma clássica em Requisitos Funcionais (RF - Funcionalidades do Sistema) e Requisitos Não Funcionais (RNF - Características de Qualidade). Os Requisitos Funcionais especificam as ações diretas do usuário na interface (ex: o login de usuários, a criação de decks pelo tutor e a visualização do Mapa Neural pelo aluno). Já os Requisitos Não Funcionais descrevem critérios de qualidade, desempenho e segurança do sistema (ex: a responsividade estrita da interface para rodar em smartphones e computadores, e a conformidade com as regras de acessibilidade WCAG (*Web Content Accessibility Guidelines* - Diretrizes de Acessibilidade para Conteúdo Web)). Exemplo prático: O requisito funcional **RF03** especifica a interface de flashcards onde o aluno vira a carta para ler a resposta. O requisito não funcional **RNF02** garante que essa mesma ação seja amigável a leitores de tela usando etiquetas acessíveis e navegação simples por teclado.

### P5. O que é o backlog do produto e como a equipe estimou o esforço de desenvolvimento do projeto?
**R:** O backlog do produto é a lista priorizada de todas as tarefas e funcionalidades que precisam ser construídas na plataforma, organizadas em blocos funcionais chamados Épicos (Autenticação, Motor de Flashcards, Economia Virtual e Acessibilidade). Para estimar o esforço de cada tarefa, utilizamos o ritual de *Planning Poker* com a sequência de Fibonacci nas reuniões do grupo. Exemplo prático: Tarefas com escopo visual simples e de baixo atrito, como desenhar as telas de login e cadastro de usuários no Figma, receberam peso de esforço 3. Tarefas de alta complexidade de lógica relacional e matemática, como modelar as tabelas do algoritmo SM-2 (SuperMemo 2) e estruturar as variáveis em C#, receberam peso de esforço 8 devido à maior incerteza e regras envolvidas.

### P6. Como a equipe organizou as Sprints semanais utilizando o Kanban e como garantiram a conformidade com a LGPD (Lei Geral de Proteção de Dados)?
**R:** Usamos a plataforma Trello para implementar um quadro Kanban (Painel de Fluxo Visual), organizando o andamento das atividades em colunas claras: A Fazer (*To Do*), Em Andamento (*Doing*), Testes (*Testing*) e Concluído (*Done*), associando responsáveis a cada tarefa. Em conformidade estrita com a **LGPD (Lei Geral de Proteção de Dados)**, planejamos na interface do Figma que, no momento do cadastro do usuário, seja exigido o consentimento explícito dos termos de uso. No modelo de banco de dados SQL (*Structured Query Language* - Linguagem de Consulta Estruturada) Server, especificamos que senhas não são armazenadas em texto limpo; elas passam obrigatoriamente por um algoritmo de hash criptográfico SHA-256 (Algoritmo de Hash Seguro de 256 bits) no backend, garantindo que os dados dos usuários permaneçam confidenciais mesmo em caso de vazamento na base.

---

## 💾 Etapa 3: Modelagem de Banco de Dados

### P7. Por que foi escolhido um banco de dados relacional (SQL Server) em vez de outros modelos como NoSQL (Não Relacional)?
**R:** A escolha do Microsoft SQL Server baseou-se nas garantias das propriedades **ACID** (Atomicidade, Consistência, Isolamento e Durabilidade). Como a Nex_TI opera com uma economia de moedas virtuais acumuladas para desbloquear avatares na loja, precisamos de segurança transacional rigorosa. Um banco de dados relacional com integridade referencial impede que moedas sejam geradas incorretamente em acessos simultâneos ou que um aluno excluído mantenha registros órfãos ativos. Exemplo prático: O banco relacional com chaves estrangeiras (**FK** - *Foreign Key*) garante a consistência do saldo. Se precisássemos escalar o sistema para logs temporários de auditoria ou histórico de cliques de milhões de alunos, poderíamos adotar uma arquitetura híbrida usando NoSQL (Não Relacional, como o MongoDB) de forma isolada para processamento de alto volume.

### P8. Como foi aplicada a normalização de dados e qual a utilidade da regra de "exclusão em cascata" nas tabelas do SQL Server?
**R:** Aplicamos as Formas Normais (1FN, 2FN e 3FN - Primeira, Segunda e Terceira Formas Normais) para eliminar anomalias de inserção, exclusão e alteração. Um exemplo é a tabela associativa `tb_prova_questao`, criada para resolver o relacionamento de muitos-para-muitos (N:N) entre Provas e Questões. A regra de **exclusão em cascata (ON DELETE CASCADE)** foi implementada na chave estrangeira que liga a tabela `tb_alternativas` à tabela `tb_questoes`. Exemplo prático: Se um Tutor excluir uma Questão na interface, o banco de dados SQL Server apaga automaticamente todas as alternativas correspondentes de forma transparente no script DDL (*Data Definition Language* - Linguagem de Definição de Dados), garantindo que a base de dados permaneça limpa de dados inúteis e economizando processamento de limpeza manual.

### P9. Como o histórico de estudos do aluno e os parâmetros do algoritmo SM-2 (SuperMemo 2) são persistidos no banco?
**R:** Criamos a tabela específica `tb_flashcards_sm2` para persistir o estado das revisões. Ela guarda a chave estrangeira do usuário (`id_usuario`), a frente e o verso da carta, e três colunas cruciais para o algoritmo:
- `fator_facilidade` (float, inicializado em 2.5): Determina o grau de facilidade de recordação daquele cartão.
- `intervalo_dias` (integer): Quantidade de dias que o sistema esperará até reexibir o cartão para o aluno.
- `data_proxima_revisao` (date): O dia em que o cartão reaparecerá no dashboard do aluno. A cada rodada que o aluno estuda e dá um feedback de nota (0 a 5), a API (*Application Programming Interface* - Interface de Programação de Aplicação) calcula o SM-2 e atualiza essas três colunas no banco de dados.

---

## 💻 Etapa 4: Desenvolvimento com POO (Programação Orientada a Objetos) (C#)

### P10. Onde a modelagem conceitual das classes foi criada e como foi estruturada em C#?
**R:** Toda a nossa arquitetura de classes foi modelada e desenhada visualmente utilizando o software **Astah UML** (*Unified Modeling Language* - Linguagem de Modelagem Unificada) (definindo propriedades, métodos de classe, multiplicidades e relacionamentos de herança). A partir desse desenho lógico, planejamos as classes estruturais em C# (.NET 10). Exemplo prático: Criamos a classe base `Usuario.cs` contendo as propriedades comuns (ID, Nome, Email e Senha). Usando o pilar de **Herança**, derivamos as subclasses `Aluno.cs` (que inclui a composição de moedas e XP) e `Tutor.cs` (que adiciona funções de edição). Isso evita redundância de código e garante que qualquer mudança em propriedades básicas de usuários seja herdada automaticamente por todos os perfis do sistema.

### P11. Como o conceito de proteção de dados (encapsulamento) e os princípios SOLID foram planejados para as classes?
**R:** Aplicamos o encapsulamento restringindo a modificação direta de atributos críticos. Exemplo prático: Os campos `xp_acumulado` e `moedas_virtuais` na classe `Aluno.cs` possuem modificador de escrita privada (`private set`). Isso impede que qualquer outra classe mude os pontos do aluno de forma indevida de fora. O saldo só é atualizado de forma controlada chamando métodos da própria classe, como `AdicionarMoedas(int quantidade)`, que validam as regras de negócio. Adicionalmente, aplicamos o **Princípio da Responsabilidade Única (SRP - *Single Responsibility Principle*) do SOLID** (Princípios de Engenharia de Software) ao isolar toda a fórmula matemática do algoritmo SM-2 na classe `ISm2Engine` em `backend/Services/`, impedindo que classes de dados ou controladores fiquem inflados com lógica de cálculo.

### P12. O que é a classe Program.cs e como ela foi estruturada para manter a legibilidade do código?
**R:** É o arquivo inicial e ponto de entrada da nossa API (*Application Programming Interface* - Interface de Programação de Aplicação) backend em C#. Em projetos com Minimal APIs do .NET, é comum que a configuração de banco, injeção de dependência e mapeamento de caminhos inflem o arquivo inicial. Para manter o código legível e seguir boas práticas de engenharia, planejamos mover todos os caminhos e mapeamentos de endpoints para uma classe estática de extensão separada chamada `EndpointExtensions.cs`, mantendo o `Program.cs` focado exclusivamente nas definições essenciais de inicialização de serviços.

---

## 🌐 Etapa 5: Desenvolvimento Web Responsivo

### P13. O que significa desenvolver a interface como uma SPA (Single Page Application) e quais os benefícios?
**R:** Significa que todo o portal funciona em uma página única que é carregada apenas uma vez pelo navegador, e as atualizações de tela acontecem dinamicamente sem recarregar o site. Exemplo prático: Quando o aluno clica para abrir uma sessão de flashcards, o JavaScript do frontend intercepta a ação, faz uma requisição assíncrona usando o comando `fetch` para a nossa API em C#, recebe as perguntas em formato JSON (*JavaScript Object Notation* - Notação de Objetos JavaScript), e atualiza apenas a área de cartões da tela. Isso elimina a necessidade de fazer o navegador piscar e baixar arquivos HTML (*HyperText Markup Language* - Linguagem de Marcação de Hipertexto) pesados novamente, proporcionando uma transição de tela instantânea.

### P14. Por que foi escolhido HTML/CSS Puro (Vanilla) em vez de frameworks visuais?
**R:** A escolha por Vanilla HTML5/CSS3 puro nos garante o máximo de desempenho, baixo consumo de dados móveis e controle absoluto sobre o código e formatação acadêmica. Exemplo prático: No arquivo `style.css`, criamos regras de impressão estilizadas com `@media print` para que toda a monografia desenvolvida em HTML (*HyperText Markup Language*) seja impressa exatamente dentro das margens, fontes e especificações da ABNT (Associação Brasileira de Normas Técnicas) de forma nativa.

### P15. Como funciona a adaptação fluida de layout (responsividade) usando CSS Grid e Flexbox?
**R:** Adotamos uma estratégia adaptativa no `style.css`. Usamos CSS Grid (Grade de Layout Bidimensional) para estruturar as áreas principais e bidimensionais (como a divisão das colunas do dashboard (*painel gerencial*) de estudos) e CSS Flexbox (Caixa Flexível Unidimensional) para alinhar elementos unidimensionais menores (como botões, avatares e barras de navegação). Exemplo prático: Usamos media queries (*consultas de mídia*) para fazer com que, em resoluções de telas menores (celulares), as colunas horizontais do dashboard em CSS Grid se empilhem verticalmente de forma automática e os botões aumentem de área de clique para facilitar o toque com o polegar.

---

## 🎨 Etapa 6: UX (User Experience) e UI (User Interface) Design (Figma e Heurísticas de Nielsen)

### P16. Onde as interfaces de usuário foram projetadas e qual foi a base de estudo de usabilidade?
**R:** Toda a interface do usuário (telas de login, dashboard de estudos e os cartões) foi modelada e prototipada integralmente no software **Figma**. No Figma, criamos o nosso *Design System* (Sistema de Design) definindo uma paleta cromática unificada (cor principal `--alura-cyan` para as ações primárias) e tipografias de alta leitura. A usabilidade foi baseada na jornada de uma **Persona**: um jovem de 18 a 20 anos que busca nivelamento introdutório em TI (Tecnologia da Informação). Como esse usuário possui insegurança com jargões, as telas no Figma foram projetadas com botões grandes, dicas visuais (affordance clara) e poucos textos para evitar medo ou sobrecarga cognitiva.

### P17. Quais Heurísticas de Nielsen foram aplicadas no protótipo desenvolvido no Figma?
**R:** Aplicamos cinco heurísticas fundamentais de usabilidade nas telas do **Figma**:
- **Correspondência com o mundo real:** O progresso do aluno é exibido na forma de um Mapa Neural de conexões (Obsidian Neural View), simulando graficamente um mapa mental físico de estudos familiares.
- **Consistência e padrões:** Todos os botões primários seguem o mesmo tamanho de cantos arredondados, cor ciano e efeitos visuais idênticos, garantindo que o usuário aprenda a usá-los uma única vez.
- **Controle e liberdade do usuário:** Colocamos botões claros de "Voltar" ou "Pausar estudos" em todas as telas, permitindo ao aluno abortar o estudo dos flashcards a qualquer momento sem barreiras ou perdas punitivas de moedas.
- **Feedback visual (Visibilidade do estado do sistema):** A barra de progresso e o saldo de moedas no HUD (*Heads-Up Display* - Painel de Informações Flutuantes) do topo piscam e se atualizam dinamicamente no momento em que uma questão é respondida com sucesso.
- **Prevenção de erros:** Adicionamos telas de confirmação ("Deseja mesmo finalizar os estudos?") antes de fechar a rodada para evitar que toques involuntários na tela apaguem o progresso atual do deck.

### P18. Como a prototipagem no Figma e os conceitos de usabilidade garantem que o visual do site seja intuitivo?
**R:** Passamos pelas etapas de *Wireframes de Baixa Fidelidade* (esboços conceituais em tons de cinza para focar no fluxo) até o *Protótipo Interativo de Alta Fidelidade*. Aplicamos o conceito de **Affordance** (Características de Ação) e **Signifiers** (Sinalizadores): os cartões de flashcards possuem sombras sutis e ícones de "virar" que sinalizam fisicamente que podem ser rotacionados. O Mapa Neural possui física visual de conexões que guiam o olhar do aluno, mostrando que nós apagados representam matérias ainda não iniciadas e nós brilhantes representam tópicos já dominados no protótipo Figma.

---

## 📐 Etapa 7: Machine Learning (Aprendizado de Máquina) e Análise de Dados

### P19. Qual a relação matemática do algoritmo SM-2 (SuperMemo 2) com a aprendizagem ativa no projeto?
**R:** O SM-2 (SuperMemo 2) é a fórmula usada para calcular o intervalo ideal de dias para o aluno rever cada flashcard com base no seu feedback. Após o aluno visualizar a resposta de um flashcard, ele avalia a facilidade de recordação dando uma nota de 0 a 5. A fórmula recalcula o **Fator de Facilidade (EF - *Easiness Factor*)** da seguinte forma: 
$$EF' = EF + (0.1 - (5 - \text{nota}) \times (0.08 + (5 - \text{nota}) \times 0.02))$$
Com o novo EF, o sistema calcula o número de dias de intervalo para a próxima revisão. Exemplo prático: Se a nota dada for 5 (muito fácil), o intervalo salta para 6 dias. Se for 1 (difícil), o card reaparece no dia seguinte, forçando o cérebro a resgatar ativamente a informação de forma personalizada para cada estudante.

### P20. Como os dados gerados nas sessões são gravados e como podem ser usados para Machine Learning no futuro?
**R:** Gravamos os tempos de resposta, a taxa de erros e as notas fornecidas em cada flashcard na tabela `tb_flashcards_sm2`. Essa massa de dados estruturados gera relatórios de desempenho. Exemplo prático: No PIM IV (4º Semestre), esses dados servirão para treinar modelos preditivos de inteligência artificial baseados em ML (*Machine Learning* - Aprendizado de Máquina). A IA (Inteligência Artificial) poderá cruzar o tempo de estudo do aluno com suas notas de flashcards para prever de forma precoce quais estudantes estão em risco de reprovação ou evasão, gerando alertas de intervenção para os tutores.

### P21. O que é a Curva de Esquecimento de Hermann Ebbinghaus e como o SM-2 (SuperMemo 2) a resolve?
**R:** É o estudo científico que prova que a memória humana esquece informações novas de forma exponencial ao longo do tempo (a curva cai acentuadamente logo no primeiro dia). O algoritmo SM-2 resolve isso agendando as revisões espaçadas exatamente nos momentos em que a probabilidade de esquecimento é alta. A cada revisão bem-sucedida, a taxa de esquecimento diminui e a curva se torna mais "plana", transferindo o conhecimento de TI da memória de curto prazo para a memória de longo prazo de forma científica.

---

## ♿ Etapa 8: Comunicação e Acessibilidade (LIBRAS - Língua Brasileira de Sinais)

### P22. Como a acessibilidade digital e as boas práticas de desenvolvimento web foram aplicadas na plataforma?
**R:** Foram pensadas desde os desenhos de interface no **Figma** e aplicadas no código HTML (*HyperText Markup Language*) do `index.html`. Empregamos HTML5 semântico e injetamos atributos de acessibilidade **WAI-ARIA** (*Web Accessibility Initiative - Accessible Rich Internet Applications*) (`role="tab"`, `aria-label`, `aria-selected` dinâmicos). Exemplo prático: Em botões de ação do portal que contêm apenas imagens ou ícones visuais (como o botão de seta para avançar o flashcard), inserimos o atributo `aria-label="Passar para próximo flashcard"`. Assim, os softwares leitores de tela usados por pessoas com deficiência visual conseguem ler em voz alta o que o botão faz.

### P23. Como o projeto atende a padrões de contraste e controle de tamanho de tela?
**R:** As cores selecionadas no Design System respeitam as taxas de contraste mínimo estabelecidas pelas diretrizes WCAG (*Web Content Accessibility Guidelines*). Exemplo prático: No CSS (*Cascading Style Sheets*), estruturamos os layouts de forma flexível utilizando Grid e Flexbox com unidades de tamanho escaláveis. Se o usuário ampliar o zoom da tela do navegador para 200% devido a baixa visão, os elementos se reorganizam de forma fluida sem transbordar, sem sobrepor e sem quebrar o layout das telas.

### P24. Como a plataforma pode ser adaptada para acessibilidade em LIBRAS (Língua Brasileira de Sinais) no futuro?
**R:** Projetamos a integração conceitual do plugin VLibras. Exemplo prático: Ficará visível o ícone flutuante do VLibras (uma mãozinha). Ao clicar sobre ela e depois sobre um parágrafo de texto informativo de nivelamento, um avatar virtual interativo traduzirá o texto em português para a Língua Brasileira de Sinais (LIBRAS) por meio de animação 3D de gestos em tempo real na tela.

---

## 📐 Etapa 9: Integração e Avaliação Final (UML - Linguagem de Modelagem Unificada)

### P25. Como os diagramas UML garantem a integridade de todo o ecossistema Nex_TI?
**R:** Os diagramas UML (*Unified Modeling Language*) (desenhados no software **Astah UML**) funcionam como o blueprint de engenharia do software. Eles provam que a nossa arquitetura foi pensada sem pontas soltas ou incoerências estruturais antes do início da codificação. Exemplo prático: O Diagrama de Sequência detalha a ordem exata em que as mensagens transitam (1. Clique do Aluno -> 2. Chamada da API em C# -> 3. Validação do SM-2 -> 4. Gravação de dados no SQL Server -> 5. Retorno de dados atualizados), garantindo que a lógica que o usuário enxerga seja fisicamente viável no banco de dados e no código.

### P26. O que é o Diagrama de Classes e como ele se aplica na prática?
**R:** É o mapa conceitual estático que planeja a estrutura das classes de código, desenhado no **Astah UML**. Ele descreve quais entidades de código vão existir (Usuario, Aluno, Tutor, XP, Moedas), quais são seus atributos internos (tipos de dados e modificadores de acesso) e assinaturas de métodos. Exemplo prático: O diagrama de classes especificou no Astah a relação de herança entre `Usuario` e suas derivadas, servindo de roteiro de implementação para que o grupo criasse o código C# correspondente sem improvisos.

### P27. O que é o Diagrama de Sequência UML e qual seu benefício?
**R:** É o diagrama dinâmico que ilustra as interações e trocas de mensagens no tempo entre os componentes do sistema (navegador, backend em C# e banco SQL Server). Exemplo prático: Ele mapeia o passo a passo de uma autenticação de login ou o salvamento de um card de estudos, garantindo que a ordem lógica das validações ocorra sem gargalos ou erros de projeto de software.

---

## 👥 Metodologia e Trabalho em Grupo (Scrum)

### P28. Como as reuniões Scrum nas atas ajudaram a provar a organização da equipe no semestre?
**R:** Registramos 10 reuniões semanais de planejamento e revisão (Sprint Planning e Sprint Review) em atas formais. Elas provam as reuniões semanais, divisões de tarefas em Kanban no Trello e a facilitação rotativa por Gabriel Moreira e Maciel Silva. Exemplo prático: Se a banca perguntar sobre conflitos técnicos ou atrasos, explicamos que usávamos as reuniões de Daily Scrum diárias para identificar impedimentos de escopo e redistribuir cartões rapidamente pelo quadro Kanban no Trello.

### P29. Para que serviram os manuais técnicos de extensão universitária gerados no repositório prático?
**R:** Escrevemos três manuais complementares no repositório de extensão: o **Manual de Execução** (ensina a rodar a base SQL e o backend C# localmente), o **Manual Prático** (guia de uso ilustrado para o usuário final aprender a rodar e usar as telas do portal) e o **Manual Técnico** (que detalha as rotas de dados e segurança do backend).

### P30. Como o grupo gerenciou a transição conceitual para o PIM IV (4º semestre) e como os diagramas no Astah e as telas do Figma foram integrados no projeto acadêmico do PIM III?
**R:** Delimitamos formalmente que o 3º Semestre foca na prototipagem no Figma e modelagem lógica no Astah. Módulos complexos como a lógica real de banco de questões do simulado ENADE e loja virtual estendida já foram mapeados conceitualmente para manter a consistência da documentação de engenharia (como as tabelas no SQL Server e classes em UML), mas sua implementação e programação funcional de telas são escopo futuro do PIM IV (4º semestre). Na integração acadêmica, o Figma definiu a usabilidade das telas, o Astah UML planejou a arquitetura estática/dinâmica (Classes e Sequências), e o SQL Server/C# deram as estruturas e rotinas essenciais que unificam o PIM III (Projeto Integrado Multidisciplinar III).

# Fase 3: Sincronização do Ecossistema Nex_TI (Três Repositórios)

Esta fase contemplou a sincronização profunda e padronização conceitual entre os três repositórios complementares que constituem o projeto **Nex_TI** para o PIM III da UNIP:
1. [PIM_III-Parte_Teorica](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica) (Monografia/Relatório)
2. [PIM_III-Parte_Pratica](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Pratica) (Sistema Fullstack)
3. [PIM_III-Documentacao_UML](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Documentacao_UML) (Diagramas e Atas)

---

## 📋 Plano de Implementação

O objetivo foi garantir a uniformidade das informações técnicas, dados de datas, nomes de autores e atas de reuniões Scrum para a banca avaliadora:
1. **Atas de Reuniões Informais (Meetings de 1 a 10)**: Unificar as atas baseadas em Scrum registradas de forma informal na pasta `.planning/meetings/` em todos os repositórios (incluindo as reuniões 9 e 10 realizadas em domingos).
2. **Sincronização de Backlog e Documentos**: Copiar os markdowns corrigidos de backlog do produto e atas de planejamento da Parte Teórica para a pasta `01_Documentacao_Teorica/` de UML, removendo os arquivos PDF obsoletos e desatualizados.
3. **Persistência de Git Limpa**: Finalizar todos os commits com a nomenclatura de *Conventional Commits* em português, garantindo um histórico limpo e profissional.

---

## 🛠️ Tasks Executadas

- [x] Atualizar o [ROADMAP.md](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica/.planning/ROADMAP.md) no repositório teórico
- [x] Criar a documentação de fase em [phase_03.md](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica/.planning/phases/phase_03.md)
- [x] Criar as atas Scrum [reuniao_09.md](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica/.planning/meetings/reuniao_09.md) (03/05/2026 - Domingo) e [reuniao_10.md](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica/.planning/meetings/reuniao_10.md) (24/05/2026 - Domingo)
- [x] Copiar as atas de reuniões Scrum (`reuniao_01.md` a `reuniao_10.md`) para o repositório prático em `PIM_III-Parte_Pratica/.planning/meetings/`
- [x] Copiar as atas de reuniões Scrum (`reuniao_01.md` a `reuniao_10.md`) para o repositório UML em `PIM_III-Documentacao_UML/.planning/meetings/`
- [x] Commitar as alterações e novas atas no repositório `PIM_III-Documentacao_UML` com commit convencional
- [x] Commitar as novas atas no repositório `PIM_III-Parte_Pratica` com commit convencional
- [x] Commitar as alterações de roadmap, fase e reuniões no repositório `PIM_III-Parte_Teorica` com commit convencional
- [x] Verificar o status git de todos os repositórios

---

## 🚀 Walkthrough de Desenvolvimento

### 1. Sincronização Física das Atas Scrum
As atas informais de reuniões Scrum (da reunião 1 à reunião 10) foram criadas originalmente no repositório teórico para documentar a rotina ágil da equipe. Elas foram replicadas integralmente para:
- `PIM_III-Parte_Pratica/.planning/meetings/`
- `PIM_III-Documentacao_UML/.planning/meetings/`

Isso inclui os registros dos encontros de domingo (reuniao_09 e reuniao_10), focados na estruturação de manuais técnicos de extensão universitária e refatoração SOLID de backend.

### 2. Sincronização de Backlog e Limpeza em UML
No repositório de modelagem UML, foram removidos os PDFs estáticos antigos e desatualizados em `01_Documentacao_Teorica/`, que continham datas divergentes de sprints e placeholders. Em substituição, foram sincronizados os markdowns válidos e formatados:
- `Ata_Sprint_Planning_Nex_TI.md`
- `Documentacao_Projeto_Nex_TI.md`
- `Product_Backlog_Nex_TI.md`

### 3. Commits Convencionais
As atualizações foram salvas e documentadas em cada repositório através de commits convencionais em português:
- **UML**: `docs(planning): sincroniza atas, backlog e reunioes Scrum com o repositorio teorico e remove PDFs obsoletos`
- **Prático**: `docs(planning): sincroniza atas de reunioes Scrum com o repositorio teorico`
- **Teórico**: `docs(planning): sincroniza roadmap, phase 03 e atas Scrum de domingo`

---

## 🧪 Validação dos Resultados

- **Uniformidade de Dados**: Verificado que as datas de entrega (`Julho / 2026`), lista de integrantes (Gabriel, Maciel, Maycon, Miguel e Rafael) e estimativas do Product Backlog (US01 a US15 com sequência Fibonacci de Story Points) batem 100% em todas as instâncias do projeto.
- **Estrutura de Diretórios**: Todas as pastas `.planning/meetings/` contêm os exatos 10 arquivos markdown das reuniões Scrum.
- **Delimitação de Escopo nos Manuais**: Verificado que a seção "Delimitação de Escopo de Semestre (Banca UNIP)" foi adicionada com sucesso no [README.md](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Pratica/README.md) e no [MANUAL_TECNICO.md](file:///C:/Users/mayco/Documents/GitHub/PIM_III-Parte_Pratica/MANUAL_TECNICO.md) do projeto prático, esclarecendo que os módulos de simulados ENADE e loja estão omitidos no front-end por ser escopo do próximo semestre (4º semestre), resguardando a avaliação de MVP atual do 3º semestre.
- **Git Status Limpo**: Executado o comando `git status` nos três repositórios, confirmando que não há arquivos untracked remanescentes e que as working trees estão totalmente consolidadas.


# Fase 1: Integração de Ativos Visuais e Abas Dinâmicas

Esta fase contemplou a consolidação dos diagramas de arquitetura, banco de dados e modelagem de casos de uso na documentação acadêmica interativa do PIM III.

---

## 🎯 Objetivos da Fase
* Integrar as três versões físicas de cada diagrama (Visão Geral Completa, Corte 1 e Corte 2) na estrutura do relatório.
* Corrigir as referências de imagens quebradas que geravam placeholders da web.
* Manter a paginação física do documento e a conformidade com as normas ABNT tanto na visualização web quanto na impressão para PDF.

---

## 🛠️ Alterações Realizadas

### 1. Estrutura de Abas no Front-end: [index.html](file:///c:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica/index.html)
* Substituição dos blocos simples de imagem por contêineres de classe `.diagrama-container` que utilizam uma barra de abas interativa (`.tabs-control`):
  * **Diagrama DER**: Imagens `DER_Nex_TI.png` (Geral), `DER_Nex_TI 01.png` (Corte 1: Gamificação e Usuários) e `DER_Nex_TI 02.png` (Corte 2: Questões).
  * **Diagrama de Casos de Uso**: Imagens `UseCase Diagrams Nex_TI.png` (Geral), `UseCase Diagrams Nex_TI 01.png` (Corte 1: Atores) e `UseCase Diagrams Nex_TI 02.png` (Corte 2: Fluxo Aluno).
  * **Diagrama de Classes**: Imagens `Class Diagram Nex_TI.png` (Geral), `Class Diagram Nex_TI 01.png` (Corte 1: Métodos) e `Class Diagram Nex_TI 02.png` (Corte 2: Atributos).
  * **Diagrama de Sequência**: Imagens `Sequence Diagram Nex_TI.png` (Geral), `Sequence Diagram Nex_TI 01.png` (Corte 1: Autenticação) e `Sequence Diagram Nex_TI 02.png` (Corte 2: Algoritmo SM-2).
* Implementação dos metadados de acessibilidade `WAI-ARIA` (`role="tablist"`, `role="tab"`, `aria-selected` e `role="tabpanel"`) para assegurar que leitores de tela compreendam a estrutura de abas.
* Inclusão de um script Vanilla JS antes do encerramento da tag `</body>` para gerenciar dinamicamente a alternância dos estados `.active` e `aria-selected` ao clicar nos botões de controle de abas de forma isolada para cada diagrama.

### 2. Estilização CSS: [style.css](file:///c:/Users/mayco/Documents/GitHub/PIM_III-Parte_Teorica/style.css)
* Desenvolvimento das classes `.tabs-control`, `.tab-btn` e `.tab-content` para suportar a interatividade da interface web.
* Adição de efeitos suaves de transição de opacidade (`transition: opacity 0.2s ease-in-out`).
* Configuração do comportamento sob a regra `@media print` para fins de geração de PDF / Impressão ABNT:
  * Ocultação dos botões de controle de abas.
  * Expansão automática de todos os conteúdos de abas para que sejam impressos sequencialmente em cascata com suas respectivas legendas originais.
  * Adição de `page-break-inside: avoid` para evitar que as imagens sejam cortadas ao meio na divisória de páginas do PDF.

---

## 🧪 Verificação de Funcionamento
* **Visualização Web**: Os botões no topo de cada diagrama alternam instantaneamente as imagens completas e cortes detalhados, reduzindo o espaço vertical e mantendo a interface limpa e navegável.
* **Impressão**: O fluxo de impressão (Ctrl + P) renderiza todas as imagens empilhadas de forma transparente, permitindo gerar o PDF final do trabalho de acordo com os requisitos teóricos da banca.

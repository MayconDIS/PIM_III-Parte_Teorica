*Read in: [English](#english-version) | [Português](#versao-em-portugues)*

---
## English Version

# Project: Structural and Semantic Refactoring of PIM_III Document

### What This Is
This project aims to refactor the academic document `index.html` (Nex_TI platform), focusing on separation of concerns (Clean Code) and semantic technical improvements, without altering the underlying text or existing design.

### Core Value
Ensure that the project documentation reflects technical professionalism, facilitating future editing by separating CSS and ensuring maximum accessibility standards (W3C/WAI-ARIA) in HTML.

### Requirements

#### Validated
- ✓ The original document structure (`index.html`) and its textual content.
- ✓ Current visual formatting and design.

#### Active
- [x] Extraction of the stylesheet (`<style>`) from `index.html` into an external `style.css` file.
- [x] Refactoring and enhancement of Semantic HTML5 tags.
- [x] Deep review of accessibility tags (WAI-ARIA).

#### Out of Scope
- Drastic UI alterations or color palette changes.
- Addition of new textual chapters.

### Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| CSS Separation | Externalizing into `style.css` keeps the HTML content-focused. | — Done |
| Semantic & Accessible Refinement | The code will become an educational showcase of Front-end best practices. | — Done |

---
## Versão em Português

# Projeto: Refatoração Estrutural e Semântica do Documento PIM_III

### What This Is
Este projeto visa a refatoração do documento acadêmico `index.html` (plataforma Nex_TI), focando na separação de responsabilidades (Clean Code) e melhoria técnica semântica do código, sem alterar a base textual ou o design existente.

### Core Value
Garantir que a documentação do projeto seja o reflexo do profissionalismo técnico, facilitando a edição futura com a separação do CSS e garantindo padrões máximos de acessibilidade (W3C/WAI-ARIA) no HTML.

### Requirements

#### Validated
- ✓ A estrutura original do documento (`index.html`) e seus conteúdos textuais.
- ✓ A formatação visual e design atual.

#### Active
- [x] Extração da folha de estilos (`<style>`) do `index.html` para um arquivo externo `style.css`.
- [x] Refatoração e aprimoramento das marcações HTML5 Semânticas.
- [x] Revisão profunda das tags de acessibilidade (WAI-ARIA).

#### Out of Scope
- Alterações drásticas de UI ou mudança de paleta de cores.
- Adição de novos capítulos textuais.

### Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Separação do CSS | Externalizar em `style.css` deixa o HTML focado no conteúdo. | — Done |
| Refino Semântico e Acessível | O código se tornará uma vitrine didática de boas práticas de Front-end. | — Done |

# Registro Scrum: Reunião 02 (12/03)

**Ritual**: Sprint Planning (Planejamento da Sprint 2)  
**Data**: 12 de Março de 2026  
**Facilitador (Scrum Master)**: Rafael Mesquita  
**Participantes**: Gabriel, Maciel, Maycon, Miguel, Rafael  

---

### 1. O que foi feito (Progresso)
* **Product Backlog no Trello**: Criamos e estimamos o tamanho de todas as tarefas de desenvolvimento do MVP usando a sequência de Fibonacci.
* **Esboço do Banco de Dados**: Definimos as principais tabelas relacionais do sistema (`tb_usuarios`, `tb_flashcards_sm2` e tabelas de simulado).
* **Modelagem POO**: Esboçamos a arquitetura de classes do back-end em C# (declarando a herança e propriedades de encapsulamento).

### 2. O que será feito (Planejamento)
* **Estudo de Acessibilidade**: Planejar o uso de WAI-ARIA nas telas.
* **Persona e UX**: Detalhar quem é o nosso usuário final e quais as heurísticas visuais que usaremos para as interfaces.

### 3. Impedimentos e Resoluções
* **Impedimento**: Como conectar de forma segura e limpa a tabela de usuários com o banco de questões na modelagem do SQL Server.
* **Resolução**: Criamos uma tabela intermediária associativa (`tb_prova_questao`) para isolar a estrutura das avaliações e assegurar integridade referencial.

### 4. Backlog da Sprint (Status)
- [x] Criação e pontuação do Product Backlog no Trello
- [x] Rascunho da modelagem lógica do banco de dados (tabelas e chaves)
- [x] Definição preliminar do diagrama de classes em C#

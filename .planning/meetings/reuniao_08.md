# Registro Scrum: Reunião 08 (17/04)

**Ritual**: Sprint Review & Retrospective (Encerramento da Sprint Final)  
**Data**: 17 de Abril de 2026  
**Facilitador (Scrum Master)**: Gabriel Alves Moreira  
**Participantes**: Gabriel, Maciel, Maycon, Miguel, Rafael  

---

### 1. O que foi feito (Progresso)
* **Revisão Geral do Banco**: Analisamos de ponta a ponta o Diagrama de Entidade-Relacionamento (DER). Como tínhamos muitas relações muitos-para-muitos (N:N), como a ligação de questões a provas, garantimos que a modelagem relacional estivesse o mais limpa e legível possível.
* **Script DDL Finalizado**: Fechamos o arquivo de criação física do banco no SQL Server, configurando chaves estrangeiras com exclusão em cascata (`ON DELETE CASCADE`) para manter o banco consistente.
* **Validação Geral**: Rodamos um pente-fino de testes de integridade no banco e conferimos os arquivos de código.

### 2. O que será feito (Próximos Passos)
* **Entrega do PIM**: Compilar a versão final do PDF e exportar o relatório do projeto para envio na plataforma acadêmica da UNIP.
* **Apresentação**: Preparar os slides e alinhar a fala do grupo sobre o MVP da EdTech Nex_TI.

### 3. Impedimentos e Resoluções
* **Impedimento**: A modelagem física do banco com muitas relações N:N estava ficando confusa de ler no diagrama completo.
* **Resolução**: Resolvemos fatiar a exibição do DER em "Cortes" menores (Foco em Usuários/Gamificação e Foco em Questões) nas abas interativas do HTML para facilitar a compreensão da banca avaliadora.

### 4. Backlog da Sprint (Status)
- [x] Ajustes e refações no diagrama DER
- [x] Escrita do Script SQL DDL finalizado e testado no SQL Server
- [x] Revisão ortográfica e formatação final de acordo com a ABNT

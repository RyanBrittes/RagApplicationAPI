# Dúvidas e problemas encontrados no desenvolvimento do projeto

- **Alucinação causada pela busca vetorial trazer informações que não condizem com o contexto da conversa atual**
    - Ajustar a temperatura para 0.1 ou 0.2

- **Tentar encontrar o melhor número de chunks e overlap para separar de maneira eficiente o documento de recuperação**
    - Fazer uma analise, não existe uma receita

- **Tentar encontrar o melhor dimensão do embedding vetorial para gerar melhores combinações de significados entre as palavras**
    - Usar 1526 dimensões

- **Explorar métodos diferentes de buscas e aferir se melhoram as respostas ofertadas pela IA**
    - Método por Cosseno (Coisas menos detalhadas) ou Método Euclidiano (Para coisas mais detalhadas)

- **Pesquisar Top K**
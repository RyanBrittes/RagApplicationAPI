# Utilizando RAG com uma API para realizar consultas e interações com uma Inteligência Artificial

## Resultados encontrados:
> Foram realizados testes com o algoritmo atual, que está utilizando o modelo "gemini-1.5-flash" para prover as respostas e o modelo "gemini-embedding-001" para criar os embeddings.
### Resultados sem utilizar RAG:
**Input: "Fale de maneira direta sobre Crispr"**

**Outputs:**

1. CRISPR-Cas9 é uma ferramenta de edição genética precisa e relativamente barata.  Funciona como um "corretor ortográfico" do DNA, permitindo cortar e substituir sequências de DNA defeituosas ou indesejadas.  Sua precisão e facilidade de uso revolucionaram a biologia, com aplicações promissoras em medicina (tratamento de doenças genéticas), agricultura (melhora de culturas) e pesquisa básica.  Apesar de seu grande potencial, existem preocupações éticas e de segurança associadas ao seu uso.

2. CRISPR-Cas9 é uma ferramenta de edição genética precisa e relativamente barata.  Funciona como "tesoura molecular", permitindo cortar e, em seguida, modificar o DNA de qualquer organismo. Isso abre portas para correções genéticas em doenças hereditárias, desenvolvimento de culturas resistentes a pragas e doenças, e muitas outras aplicações na biotecnologia e medicina.  Apesar de seu potencial, existem preocupações éticas e potenciais efeitos colaterais a serem considerados.

3. CRISPR-Cas9 é uma ferramenta de edição genética precisa e barata.  Funciona como uma tesoura molecular, permitindo cortar e modificar o DNA de forma altamente específica. Isso abre possibilidades para corrigir defeitos genéticos, desenvolver novos tratamentos para doenças e melhorar culturas agrícolas.  Apesar de seu potencial enorme, existem preocupações éticas e de segurança a serem consideradas.

---

### Resultados utilizando RAG:
**Input: "Persona" + "Responda com base nos seguintes documentos:" + "Contexto do RAG" + "Pergunta"**

- Persona: Fale de maneira direta
- Pergunta: Fale sobre Crispr
- Contexto do RAG: São realizadas buscas no Vecto Store, os 03 resultados (03 chunks) que forem mais parecidos com a pergunta feita são retornados.

**Outputs:**

1. CRISPR é uma técnica de edição de genes.  Seu funcionamento é simples.

2. CRISPR é uma técnica de edição genética.  Seu funcionamento é simples e utiliza um sistema baseado em nucleases, enzimas que cortam o DNA em locais específicos.

3. CRISPR é uma técnica de edição genética.  Seu funcionamento é simples e utiliza uma enzima para cortar o DNA em um local específico, permitindo a edição do genoma.

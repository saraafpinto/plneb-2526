### Descrição
Este script utiliza a biblioteca spaCy para realizar Reconhecimento de Entidades Nomeadas (NER) num texto do livro Harry Potter e a Pedra Filosofal.

O objetivo é identificar personagens (entidades do tipo "PER") e calcular quantas vezes cada par de personagens aparece na mesma frase.

### Funcionamento
O texto é processado com o modelo pt_core_news_sm do spaCy
- Para cada frase (doc.sents):
    - São extraídas todas as personagens presentes
    - São contabilizadas as coocorrências entre todas as personagens da frase

- Os resultados são armazenados num dicionário onde:
    - Cada personagem é uma chave
    - O valor é outro dicionário com o número de coocorrências com outras personagens

### Output
O resultado é guardado no ficheiro amigos.json com a seguinte estrutura:

{
  "Harry": {
    "Ron": 10,
    "Hermione": 8
  }
}
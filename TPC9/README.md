Este projeto demonstra a criação, treino e avaliação de modelos de Word Embeddings (Word2Vec) utilizando os textos dos dois primeiros livros da saga Harry Potter. O objetivo é explorar como diferentes hiperparâmetros influenciam a percepção semântica da IA sobre os personagens e o mundo bruxo.

## Tecnologias Utilizadas

* **Python 3.12**
* **Gensim**: Para a implementação do algoritmo Word2Vec e gestão de vetores.
* **spaCy**: Utilizado o modelo `pt_core_news_sm` para tokenização e pré-processamento de texto em Português.
* **Re (Regular Expressions)**: Para limpeza de caracteres especiais nos ficheiros de texto.

## Metodologia de Criação

O processo de treino, detalhado no ficheiro `tpc9.py`, segue um fluxo incremental:

1.  **Limpeza**: Remoção de quebras de página (`\f`) e ruído textual.
2.  **Pré-processamento**: O texto é dividido em frases onde apenas tokens alfabéticos (sem pontuação ou espaços) são mantidos e convertidos para minúsculas.
3.  **Treino Base**: O modelo é inicializado com o livro *"Harry Potter e a Pedra Filosofal"*.
4.  **Treino Incremental**: O vocabulário é atualizado e o modelo é re-treinado com o livro *"Harry Potter e a Câmara Secreta"*, permitindo que a IA acumule conhecimento de ambos os volumes.

## Comparação de Modelos

No notebook `tpc9.ipynb`, foram testadas quatro configurações distintas:

| Modelo | Tamanho do Vetor | Janela (Window) | Contagem Mínima | Algoritmo (SG) | Épocas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Modelo 1** | 100 | 5 | 2 | 0 (CBOW) | 5 |
| **Modelo 2** | 200 | 10 | 2 | 0 (CBOW) | 5 |
| **Modelo 3** | 200 | 10 | 3 | 0 (CBOW) | 10 |
| **Modelo 4** | 200 | 10 | 3 | 1 (Skip-Gram) | 10 |

### Diferenças Técnicas Principais:
* **CBOW vs Skip-Gram**: Os primeiros três modelos usam CBOW (arquitetura mais rápida), enquanto o Modelo 4 usa Skip-Gram, que é geralmente superior para capturar relações em datasets menores.
* **Janela de Contexto**: Aumentou-se a janela de 5 para 10 para capturar relações de longo alcance entre nomes de personagens e ações.

## 🔍 Análise de Resultados

### Similaridade de Personagens
* **Modelos 1, 2 e 3**: Apresentaram similaridades extremamente altas (ex: Harry e Hermione > 0.98), o que sugere uma baixa capacidade de distinção entre os contextos dos protagonistas.
* **Modelo 4**: Apresentou valores mais realistas e distribuídos (ex: Harry e Rony com 0.46), demonstrando uma compreensão mais fina das diferenças entre os personagens.

### Analogias Complexas
Ao realizar a operação `draco + grifinória - harry` (procurando o equivalente de Draco na Grifinória, ou vice-versa):
* O **Modelo 3** (CBOW) conseguiu identificar o termo `sonserina` como altamente relevante.
* O **Modelo 4** (Skip-Gram) foi o mais preciso em termos contextuais, retornando casas rivais como `corvinal` e `lufa-lufa`, além de termos desportivos como `capitão` e `time`.

## Conclusão

O **Modelo 4** é considerado o de melhor performance. Apesar de apresentar índices de similaridade numérica menores, a sua arquitetura **Skip-Gram** aliada a um maior número de épocas permitiu uma representação muito mais rica do vocabulário, evitando o "achatamento" semântico dos modelos CBOW e capturando melhor a essência das relações entre as casas e personagens de Hogwarts.
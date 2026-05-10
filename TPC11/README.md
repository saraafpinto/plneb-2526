Este TPC implementa um motor de busca simplificado capaz de ordenar documentos por relevância em relação a uma consulta (query) do utilizador. A implementação baseia-se nos conceitos teóricos de Information Retrieval (IR) apresentados na Aula 11.

### Objetivo
O objetivo deste trabalho é calcular a pontuação de relevância de uma coleção de documentos para a query "The bright sun", utilizando:
    - TF (Term Frequency): Frequência relativa de um termo num documento.
    - IDF (Inverse Document Frequency): Importância global de um termo no corpus (escala logarítmica).
    - TF-IDF: O produto dos dois anteriores para vetorização.
    - Similaridade do Cosseno: Medida de proximidade angular entre vetores para determinar o ranking.
    
### Metodologia
O pipeline de processamento segue os seguintes passos:
    1. Pré-processamento: Utilizando a biblioteca spaCy (modelo en_core_web_sm), os textos são normalizados através de:
        - Tokenização.
        - Conversão para minúsculas.
        - Remoção de pontuação e espaços.
        - Remoção de stop words (palavras gramaticais sem valor semântico como "the", "is", "in").
        
    2. Vetorização (Espaço Vetorial): Cada documento e a query são convertidos em vetores numéricos num espaço n-dimensional, onde n é o tamanho do vocabulário total do corpus.        
    - Fórmula TF: $$TF(t,d) = \frac{\text{contagem}(t,d)}{\text{total de termos em } d}$$
    - Fórmula IDF: $$IDF(t, D) = \log_{10}\left(\frac{N}{df_t}\right)$$
    
    3. Cálculo de Similaridade: Para evitar que documentos mais longos tenham vantagem apenas por terem mais palavras, utiliza-se a Similaridade do Cosseno para medir o ângulo entre o vetor da query (q) e o vetor do documento (d):
        $$\text{sim}(q, d) = \frac{\sum_{i=1}^{n} q_i d_i}{\sqrt{\sum_{i=1}^{n} q_i^2} \sqrt{\sum_{i=1}^{n} d_i^2}}$$
        
### Exemplo de Execução
Corpus:
    - "The sky is blue"
    - "The sun is bright"
    - "The sun in the sky"
    
Query: "The bright sun"

Resultados Obtidos:
    - D2 (The sun is bright): Similaridade 1.0000 (Máxima relevância).
    - D3 (The sun in the sky): Similaridade 0.2448.
    - D1 (The sky is blue): Similaridade 0.0000.
    
### Tecnologias Utilizadas
- Python 3.12
- spaCy: Processamento de Linguagem Natural.
- Math: Cálculos logarítmicos e algébricos.
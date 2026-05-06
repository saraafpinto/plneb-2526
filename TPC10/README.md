Este TPC demonstra o processo de fine-tuning do modelo BERTimbau (BERT base para Português) para a tarefa de identificação de entidades nomeadas, como pessoas, locais, organizações, datas e profissões.

### Estrutura do Projeto
O notebook está dividido em quatro etapas fundamentais:

1. Carregamento do Dataset: Utilizou-se o dataset lfcc/portuguese_ner via Hugging Face Datasets. Este conjunto de dados contém textos anotados com etiquetas NER seguindo o esquema IOB (Inside, Outside, Beginning).
    - Total de linhas (Treino): 3716
    - Total de linhas (Teste): 930
    - Categorias: Pessoa, Local, Organização, Data, Profissão.
    
2. Pré-processamento de Dados: Nesta fase, os dados brutos foram preparados para o modelo:
    - Tokenização: Utilização do neuralmind/bert-base-portuguese-cased.
    - Alinhamento de Labels: Implementação de uma função para alinhar as etiquetas originais com os sub-tokens gerados pelo tokenizer do BERT (atribuindo a label -100 a tokens especiais e sub-tokens subsequentes para serem ignorados no cálculo da perda).
    
3. Treino do ModeloO fine-tuning foi configurado com os seguintes parâmetros:
    - Modelo Base: BERTimbau (NeuralMind).
    - Épocas: 2.
    - Batch Size: 16.
    - Taxa de Aprendizagem: $2 \times 10^{-5}$.
    - Métricas de Avaliação: Precisão, Recall, F1-Score e Accuracy, calculadas através da biblioteca evaluate (seqeval).
    
    - Resultados obtidos na última época:
        - F1-Score: ~0.9546
        - Accuracy: ~0.9842
        
4. Inferência: Criação de um pipeline de classificação para aplicar o modelo treinado a textos reais (ex: notícias). O modelo demonstrou ser capaz de identificar corretamente entidades como "Donald Trump" (Pessoa), "Washington" (Local) e "presidente" (Profissão) num exemplo prático.

### Ferramentas Utilizadas
- Python 3.12
- Hugging Face Transformers: Para o modelo e o ciclo de treino.
- Datasets: Para gestão dos dados.
- Evaluate & Seqeval: Para métricas específicas de NER.
- PyTorch: Framework de deep learning.
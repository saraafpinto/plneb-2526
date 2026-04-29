from gensim.models import Word2Vec
import re
import spacy

nlp = spacy.load("pt_core_news_sm")

f = open("Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf8") 
texto = f.read()

texto = re.sub(r'\f', '', texto)

doc = nlp(texto)
sentences = []
for sent in doc.sents:
    # Get the text of each token, lowercased, filtering out punctuation
    tokens = [token.text.lower() for token in sent if not token.is_punct and not token.is_space]
    if len(tokens) > 0:
        sentences.append(tokens)

model = Word2Vec(sentences, vector_size=200, window=10, min_count=3, sg=1, epochs=10, workers=3)

f = open("Harry_Potter_Camara_Secreta-br.txt", "r", encoding="utf8") 
texto2 = f.read()

texto2 = re.sub(r'\f', '', texto2)

doc = nlp(texto2)
more_sentences = []
for sent in doc.sents:
    # Get the text of each token, lowercased, filtering out punctuation
    tokens = [token.text.lower() for token in sent if not token.is_punct and not token.is_space]
    if len(tokens) > 0:
        more_sentences.append(tokens)

model.build_vocab(more_sentences, update=True)
model.train(more_sentences, total_examples=model.corpus_count, epochs=model.epochs)

word_vectors = model.wv
word_vectors.save("word2vec4.wordvectors")

model.wv.save_word2vec_format('model_harry4.txt', binary=False)
#http://projector.tensorflow.org/
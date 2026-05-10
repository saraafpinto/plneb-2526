import spacy
import math

nlp = spacy.load("pt_core_news_sm")

collection = ["The sky is blue",
              "The sun is bright",
              "The sun in the sky"]

#remover stop words, tirar pontuacao e por tudo letras minuscula, tokenizar
"""def pre_processamento(colection):
    new_collection = []
    for doc in collection:
        s_doc = nlp(doc)
        ...
    new_collection = [
        ["sky","blue"],
        ["sun","bright"],
        ["sun","sky"]
    ]
    return new_collection"""

#tf(t,d) = count(t)/total words(d)
def tf(doc):
    N = len(doc)
    res = {}
    for term in doc:
        if term in res:
            res[term] += 1
        else:
            res[term] = 1

    res = {k: v/N for k,v in res.items()}
    return res #{"termo": freq}

#idf(t,D) = log(N,df)
def idf(collection):
    N = len(collection)
    res = {}
    unique_terms = set([term for d in collection for term in d])
    for term in unique_terms:
        counter = 0
        for doc in collection:
            if term in doc:
                counter += 1
        rarity = math.log(N/counter,10)
        res[term] = rarity
    return res #{termo: rarity}

# tf_idf(t,d,D) = tf(t,d) * idf(t,D)
#por os 0 nos vetores tambem
def tf_idf(collection):
    res = []
    idf_values = idf(collection)
    for doc in collection:
        doc_tf_idf = []
        tf_values = tf(doc)
        for term in tf_values:
            tf_idf = tf_values[term]*idf_values[term]
            doc_tf_idf.append(tf_idf)
        res.append(doc_tf_idf)
    return res

#fazer a parte da query (fazer o mesmo pre processamento, fazer o tf e usar o idf do corus e multiplicar) e depois fazer o cosseno para ver qual o documento ta mais similar
collection = [
        ["sky","blue"],
        ["sun","bright"],
        ["sun","sky"]
    ]

print(tf_idf(collection))
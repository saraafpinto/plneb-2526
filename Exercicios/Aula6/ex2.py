import spacy

nlp = spacy.load("pt_core_news_sm")
#nlp = spacy.load("pt_core_news_lg")

f = open(r"C:\Users\saraa\Documents\1ano mestrado\2semestre\PLN\plneb-2526-stor\Dados\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf8")
texto = f.read()

doc = nlp(texto)

print("="*20, "Tokens", "="*20)

dic = {}
for token in doc:
    if token.pos_ in ["VERB", "AUX"]:
        if token.lemma_ in dic:
            dic[token.lemma_] += 1
        else:
            dic[token.lemma_] = 1

sorted_verbs = sorted(dic.items(), key= lambda x: x[1])
print(sorted_verbs)


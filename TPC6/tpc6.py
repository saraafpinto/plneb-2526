import spacy
import json

nlp = spacy.load("pt_core_news_sm")
#nlp = spacy.load("pt_core_news_lg")

f = open(r"C:\Users\saraa\Documents\1ano mestrado\2semestre\PLN\plneb-2526-stor\Dados\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf8")
texto = f.read()
doc = nlp(texto)

dic = {}

for sent in doc.sents:
    pessoas_na_frase = []

    for entity in sent.ents:
        if entity.label_ == "PER":
            if entity.text not in pessoas_na_frase:
                pessoas_na_frase.append(entity.text)

    for amigo1 in pessoas_na_frase:
        if amigo1 not in dic:
            dic[amigo1] = {}
        
        for amigo2 in pessoas_na_frase:
            if amigo2 != amigo1:
                if amigo2 not in dic[amigo1]:
                    dic[amigo1][amigo2] = 1
                else:
                    dic[amigo1][amigo2] += 1
    
f_out = open("amigos.json", "w", encoding="utf8")
json.dump(dic, f_out, indent=4, ensure_ascii=False)
f_out.close()
import spacy

nlp = spacy.load("./models/model-best")

f = open(r"C:\Users\saraa\Documents\1ano mestrado\2semestre\PLN\plneb-2526-stor\Dados\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf8")
texto = f.read()

config = {
    "overwrite_ents": True,
}

ruler = nlp.add_pipe("entity_ruler", last=True)

patterns = [
    {"label": "Pessoa", "pattern": "Dumbledore"},
    {"label": "Pessoa", "pattern": "Hagrid"},
    {
        "label": "Pessoa", 
        "pattern": [{"LOWER": "albus"}, {"LOWER": "dumbledore"}]
    }
]

ruler.add_patterns(patterns)

doc = nlp(texto)

for ent in doc.ents:
    print(ent, ent.label_)
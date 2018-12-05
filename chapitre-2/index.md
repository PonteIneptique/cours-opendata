
Linked Open Data
================

Chapitre 2 : La question de la modélisation et du choix des ontologies

---

# Résultats des devoirs :

151 triplets conservés sur l'ensemble fourni

---

# Erreurs communes

## 1 Attention à l'ordre des triplets

http://dbpedia.org/ontology/residence

> Place of residence of a person.

| Propriété | Définition |
| -- | -- |
| rdfs:domain | dbo:Person |
| rdfs:isDefinedBy | http://dbpedia.org/ontology/ |
| rdfs:label | residence (en) |
| rdfs:range | dbo:Place |

domain = Person, range = Place signifie que la personne sera sujet

---

# Erreurs communes

## 2 Le problème de normalisation des dates

| Valide | Sujet  | Prédicat | Objet |
| ------ | ------ | -------- | ----- |
| Oui | viaf:100226923 | schema:deathDate | 120 |
| Oui | viaf:286265178 | schema:deathDate | 12/120|
| Oui | viaf:286265178 | schema:deathDate | 12/-120|
| Oui | viaf:286265178 | schema:deathDate | 15/12/-120 |
| Non | viaf:286265178 | schema:deathDate | Déc 120 |

---

# Erreurs communes

## 3 Utilisation d'objet en propriété

schema:Occupation -> schema:hasOccupation

| Sujet  | Prédicat | Objet |
| ------ | -------- | ----- |
| viaf:100219060 | wikidataProp:P53 | wikidata:Q221312 |

https://www.wikidata.org/wiki/Property:P53

---

# Erreurs communes

## 5 Utilisation de chaînes en objet ou en sujet

| Sujet  | Prédicat | Objet |
| ------ | -------- | ----- |
| viaf:100219060 | foaf:knows | "Cicéron" |

https://www.wikidata.org/wiki/Property:P53

---

# Résultat

https://ponteineptique.github.io/latin-lod/2018

---

# Modéliser

## Quel référentiel utiliser ?

### Pleiades ou Geonames ?

L'un est spécialisé dans les lieux anciens. En modélisation, on essaye d'être le plus proche des concepts abordés, tout comme en histoire.

On ne dit pas que César a conquis la France mais la Gaule. De la même manière, on va avoir tendance à traiter avec Pleiades plutôt que Geonames dans un contexte d'histoire antique.

---

# Modéliser

## Quels prédicats utiliser ?

### Choix d'équipe 

#### Vocabulaire
foaf:publications, dc:author, schema:author ?
foaf:birthday, schema:birthDate ?

#### Précision
relationships:siblingsOf, foaf:knows ?

--- 

# Modéliser

## Que faire d'un-e inconnu-e ?

| Sujet | Prédicat | Objet |
| ----- | -------- | ----- |
| viaf:90637919 | relationship:spouseOf | Pauline |
| Pauline | relationship:childOf | wikidata:Q581899 |

1. Regarder sur d'autres sources 

>Later in life Seneca was married to a woman younger than himself, Pompeia Paulina. [ wikidata:Q459183 ]

2. Créer.

https://www.wikidata.org/wiki/Special:NewItem

---

# Exercice

## Compléter Wikidata avec des informations trouvées

- Exemple : Ajouter épouse de Sénèque https://www.wikidata.org/wiki/Q2054
- https://www.wikidata.org/w/index.php?search=relationship%20person&title=Special%3ASearch&fulltext=1

---

# Visualiser un réseau LOD

http://en.lodlive.it/?https://www.wikidata.org/entity/Q2054

---

# Interroger un réseau

https://query.wikidata.org/

```sparql
SELECT ?objet ?objetLabel WHERE {
  SERVICE wikibase:label { 
  bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". 
  }
  ?objet wdt:P50 wd:Q2054.
}
LIMIT 100
```
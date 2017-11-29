Introduction aux *Linked Open data*
==============

D'après Blaney Jonathan, *Introduction to the Principles of Linked Open Data*, ProgrammingHistorian.org, eds. Adam Crymble


## Que sont les Linked open data

> Les LOD sont des informations structurées écrites dans un format pensé pour les machines, et pour cette raison ne sont pas nécessairement très agréables pour l'oeil humain.

Quand on visite un site web, on retrouve en effet beaucoup d'informations. Sil l'on allait sur la page de [Sénèque sur Wikipedia](https://fr.wikipedia.org/wiki/S%C3%A9n%C3%A8que), on verrait rapidement les informations suivantes : c'est un auteur, il est né vers 4 av. JC, il meurt en 65 et c'est un stoïcien. L'information est claire, lisible. Maintenant, je vais sur le site de la BNF pour lire une édition des [Lettres à Lucilius](http://gallica.bnf.fr/ark:/12148/bpt6k5499165x/f54.image). Puis je visite le [site de Perseus](http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a2007.01.0080) qui contient une édition de ce texte. Pour moi, humain, la connection entre ces différentes ressources est claire. Malheureusement, ce n'est pas le cas pour la machine qui doit s'efforcer d'extraire ce sens à grand coup d'apprentissage automatique. Et l'apprentissage automatique n'étant pas parfait, les développeurs ont prévu un autre système.

Les projets mettent dorénavant des données à disposition : les données sont structurées suivant les mêmes standards et sont disponibles à la lecture. On mets alors ces données en groupe : on appelle cela plus communément des *datasets* et les projets hébergeurs des silos d'informations.

Pour créer ces silos et sets de données, il faut respecter **trois principes** :

1. **Utiliser un format standard** de *linked open data*: pour que les macines puissent communiquer entre elles, les données doivent êtres structurées. Vous avez vu jusqu'ici la structuration du texte via par exemple le XML et une grammaire. Il s'agit ici de faire la même chose mais pour la description d'object.
2. **Utiliser des référentiels communs** : le principe des LOD est de fournir un ensemble d'informations sur les mêmes objets. Tout cela est rendu plus facile lorsque ces objets portent le même nom.
3. **Publier ses données de manière ouverte** : pour uqe les données soient liables, il ne faut pas avoir à se connecter ou à payer un abonnement pour pouvoir les lire.


### Video Europeana

Europeana est un projet européen de bibliotèque numérique en ligne. Cette bibliothèque n'héberge aucunes ressources mais sert de portail vers les bibliothèques nationales et locales grâce à l'usage de Linked Open Data et de standards d'échange de catalogue. On retrouve par exemple les ouvragres de Gallica.
 
https://youtu.be/oEuDaJjEFos

## Vous avez dit RDF ?

RDF : Resource Data Framework

Avant d'expliquer ce qu'est le RDF, pouvez-vous me dire quelle est la structure de phrase verbale complète la plus commune ? Sujet-Verbe-COD. C'est un peu de cette structure qu'est partie le concept de RDF où les choses sont structurées en sujet prédicat objet.

**Slide** 
- Sénèque a écrit Les Lettres à Lucilius
- Les lettres à Lucilius sont appelées Ad Lucilium

**Faire un exemple ensemble**

Le problème de ces exemples c'est qu'ils signifient quelque chose pour nous, personnes parlant le Français. A votre avis, que peut-on faire pour aider la machine à comprendre cela ?

La première chose, c'est évidemment d'utiliser un référentiel. Là pour le moment, on a 2 objets distincts : Sénèque et Les Lettres à Lucilius. Étant donné que l'on a à faire à des objets traditionnels des catalogues, il s'avère que des identifiants ont déjà été fournis : il s'agit des identifiants du VIAF (Virtual International Authority File). 

En l'occurrence, si on cherche Sénèque sur le VIAF on tombe sur cette page [https://viaf.org/viaf/90637919/#Seneca,_Lucius_Annaeus,_approximately_4_B.C.-65_A.D](Page) . Que pouvez-vous dire sur cette page ?
- Il y a des traductions du nom de l'auteur


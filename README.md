# BFA-1-Python-Evan-Lacan-Riviere
Réponses aux questions — Séance 1
Partie A — Premiers pas en Python
A.2 — Premier programme
1. C’est quoi Python ? À quoi sert ce langage ? Est-il compilé ou interprété ?
Python est un langage de programmation polyvalent, connu pour sa syntaxe simple et lisible. Il peut être utilisé pour créer des programmes, automatiser des tâches, manipuler des données ou encore communiquer avec des API. Python est principalement considéré comme un langage interprété : le code est exécuté par l’interpréteur Python.
2. Comment installe-t-on Python ? Comment vérifie-t-on qu’il est bien installé et quelle version on utilise ?
On installe Python depuis le site officiel de Python ou avec le gestionnaire de logiciels de son système. Pour vérifier l’installation, on ouvre un terminal et on utilise la commande python --version ou python3 --version. Cela affiche la version installée, par exemple Python 3.11.
3. Citez les différentes façons de lancer du code Python et un cas d’usage de chacune.
On peut lancer du code Python de plusieurs façons :
•	Dans un terminal avec python fichier.py : pratique pour exécuter un script complet.
•	Dans l’interpréteur interactif : utile pour tester rapidement des commandes ou des petits morceaux de code.
•	Avec un environnement de développement (IDE) : pratique pour écrire, organiser et déboguer des programmes plus importants.
A.3 — Les types de base
1. Quels sont les types de base en Python ? Que signifie « typage dynamique » ? Que donne "3" + 4 et pourquoi ?
Parmi les types de base, on trouve les entiers (int), les nombres décimaux (float), les chaînes de caractères (str), les booléens (bool), les listes (list) et les dictionnaires (dict).
Le typage dynamique signifie qu’on n’a pas besoin de préciser le type d’une variable lors de sa création : Python détermine automatiquement son type.
"3" + 4 provoque une erreur, car "3" est une chaîne de caractères alors que 4 est un entier. Python ne peut pas les additionner directement.
A.4 — Les opérations
1. Quelle est la différence entre un opérateur booléen et un opérateur logique ?
Un opérateur booléen permet de travailler avec des valeurs True ou False. Les opérateurs and, or et not permettent de combiner ou de modifier ces valeurs.
Dans le contexte de Python, les termes « opérateur booléen » et « opérateur logique » sont souvent utilisés pour désigner ces mêmes opérateurs : and, or et not.
A.6 — Les boucles
1. Quand utilise-t-on une boucle for et quand une boucle while ?
On utilise une boucle for lorsqu’on souhaite parcourir une collection ou répéter une action pour un nombre d’éléments connu.
On utilise une boucle while lorsqu’on souhaite répéter une action tant qu’une condition est vraie, sans forcément connaître à l’avance le nombre de répétitions.
Partie B — Git et GitHub
B.3 — Premier commit
1. C’est quoi Git ? C’est quoi GitHub ? Quelle est la différence entre les deux ?
Git est un outil de gestion de versions qui permet de suivre les modifications d’un projet et de revenir à des versions précédentes.
GitHub est une plateforme en ligne qui permet notamment d’héberger des dépôts Git et de travailler à plusieurs sur un projet.
La différence principale est donc que Git est l’outil de gestion de versions, tandis que GitHub est une plateforme qui permet notamment de stocker et partager des projets Git.
2. Pourquoi utiliser Git et GitHub ?
Git permet de conserver l’historique des modifications et de revenir en arrière en cas de problème. GitHub facilite le travail en groupe grâce au partage du projet, aux branches, aux commits et aux pull requests. Cela permet donc de travailler à plusieurs tout en gardant une trace des modifications.
Partie C — Découvrir les données, puis appeler l’API
C.1 — Explorer un dictionnaire
1. Quand on affecte une valeur à une clé qui existe déjà dans un dictionnaire, que se passe-t-il ? Un dictionnaire peut-il contenir deux fois la même clé ?
Si une clé existe déjà, lui affecter une nouvelle valeur remplace l’ancienne valeur.
Un dictionnaire ne peut donc pas avoir deux clés identiques. Chaque clé est unique et correspond à une seule valeur.
2. Après avoir copié un dictionnaire avec .copy() et modifié la copie, l’original est-il modifié ? Et si l’on modifie une partie imbriquée comme rates ?
Avec .copy(), on crée une copie superficielle. Si on modifie directement une valeur simple de la copie, l’original n’est pas modifié.
En revanche, pour une partie imbriquée comme rates, la copie et l’original peuvent partager le même objet. Modifier rates dans la copie peut donc également modifier l’original.
3. C’est quoi la mutabilité ? Quelle différence entre une copie superficielle et une copie profonde ? Comment fait-on une copie profonde en Python ?
La mutabilité désigne la possibilité de modifier un objet après sa création.
Une copie superficielle copie le dictionnaire mais conserve les mêmes objets imbriqués. Une copie profonde crée également des copies des objets imbriqués.
Pour réaliser une copie profonde, on utilise le module copy :
import copy
copie = copy.deepcopy(reponse)
4. Quels types de base sont mutables ? Lesquels sont immuables ? Donnez des exemples.
Les listes et les dictionnaires sont des exemples de types mutables, car on peut modifier leur contenu après leur création.
Les chaînes de caractères, les entiers, les nombres décimaux et les booléens sont immuables : leur valeur ne peut pas être modifiée directement. Une nouvelle valeur doit être créée.
C.2 — Appeler l’API pour de vrai
1. Qu’est-ce qu’une API ? Que signifie « envoyer une requête » pour récupérer une donnée ? Qu’est-ce que le format JSON, et en quels types Python se traduit-il ?
Une API est une interface qui permet à un programme de communiquer avec un autre service pour demander ou envoyer des données.
Envoyer une requête signifie transmettre une demande à l’API, généralement à une adresse précise, afin qu’elle renvoie les informations demandées.
JSON est un format permettant de représenter et d’échanger des données. En Python, un objet JSON peut notamment être traduit en dictionnaire, liste, chaîne de caractères, nombre, booléen ou None, selon les données contenues.
2. Pourquoi enregistrer la réponse de l’API dans un fichier (cache/) plutôt que de rappeler l’API à chaque exécution ?
Enregistrer la réponse permet de conserver les données déjà récupérées et d’éviter de refaire une requête à chaque exécution du programme. Cela permet de travailler plus rapidement, de limiter les appels au service et de pouvoir réutiliser les données même sans refaire immédiatement une requête réseau.

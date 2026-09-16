"""
Séance 2 - Partie A : les fonctions
Lecture du CSV produit en séance 1, calcul de la moyenne, du minimum et du maximum.
"""

import csv
from statistics import mean



def lire_csv(chemin):
    """Lit le fichier CSV et renvoie une liste de couples (date, taux)."""
    resultat = []                      # la liste vide que l'on va remplir
    with open(chemin, "r") as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)                  # on saute la ligne d'en-tete Date,Taux_USD
        for ligne in lecteur:
            date = ligne[0]            # 1re colonne : du texte
            taux = float(ligne[1])     # 2e colonne : on convertit le texte en nombre
            resultat.append((date, taux))
    return resultat                    # on renvoie la liste au programme appelant


def calculer_moyenne(taux):
    """Calcule la moyenne d'une liste de taux (somme divisee par le nombre)."""
    if len(taux) == 0:                 # protection : on ne divise jamais par zero
        return None
    somme = 0
    for t in taux:
        somme += t
    return somme / len(taux)


def min_max(taux):
    """Renvoie le taux le plus bas et le taux le plus haut d'une liste."""
    if len(taux) == 0:
        return None, None
    plus_bas = taux[0]                 # on part du 1er element comme reference
    plus_haut = taux[0]
    for t in taux:
        if t < plus_bas:
            plus_bas = t
        if t > plus_haut:
            plus_haut = t
    return plus_bas, plus_haut         # une fonction peut renvoyer deux valeurs


# ==========================================================
# Programme principal
# ==========================================================

donnees = lire_csv("donnees/taux_historique.csv")
print("Nombre de lignes lues :", len(donnees))
print("Premiere ligne :", donnees[0])
print("Derniere ligne :", donnees[-1])

# On extrait uniquement les taux (2e element de chaque couple)
liste_taux = []
for date, taux in donnees:
    liste_taux.append(taux)

moyenne_maison = calculer_moyenne(liste_taux)
print(f"\nMoyenne (notre fonction)   : {moyenne_maison:.4f}")

# A.2 - la meme chose avec la bibliotheque standard
moyenne_statistics = mean(liste_taux)
print(f"Moyenne (statistics.mean)  : {moyenne_statistics:.4f}")
print("Les deux resultats sont-ils identiques ?", moyenne_maison == moyenne_statistics)

bas, haut = min_max(liste_taux)        # on recupere les deux valeurs d'un coup
print(f"\nTaux minimum : {bas}")
print(f"Taux maximum : {haut}")
print(f"Amplitude    : {haut - bas:.4f}")

"""
Séance 2 - Partie B : gestion des erreurs (try/except) et journalisation (logging)
On reprend l'appel API de la seance 1, mais cette fois le programme ne plante plus.
"""

import urllib.request
import urllib.error
import json
import logging

# ==========================================================
# B.2 - Configuration du journal (a faire UNE SEULE FOIS, tout en haut)
# ==========================================================
logging.basicConfig(
    filename="logs/projet.log",                       # ou ecrire le journal
    level=logging.INFO,                               # niveau minimum enregistre
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

URL = "https://api.frankfurter.app/latest?from=EUR&to=USD"


def recuperer_taux(url):
    """Appelle l'API et renvoie le taux USD, ou None si l'appel echoue."""
    logging.info(f"Appel de l'API : {url}")

    try:
        with urllib.request.urlopen(url, timeout=10) as reponse:
            data = json.loads(reponse.read().decode())
            taux = data["rates"]["USD"]

    except urllib.error.HTTPError as e:
        # Le serveur a repondu, mais avec un code d'erreur (403, 404, 500...)
        logging.error(f"Le serveur a refuse la requete (code {e.code})")
        print(f"Erreur : le serveur a repondu {e.code}.")
        return None

    except urllib.error.URLError as e:
        # On n'a meme pas reussi a joindre le serveur (pas de connexion, DNS...)
        logging.error(f"Impossible de joindre le serveur : {e.reason}")
        print("Erreur : pas de connexion internet ou serveur injoignable.")
        return None

    except json.JSONDecodeError:
        # La reponse est arrivee mais ce n'est pas du JSON valide
        logging.error("La reponse recue n'est pas du JSON lisible")
        print("Erreur : reponse illisible.")
        return None

    except KeyError as e:
        # Le JSON est valide mais la cle attendue est absente
        logging.error(f"Cle absente dans la reponse : {e}")
        print("Erreur : la devise demandee n'est pas dans la reponse.")
        return None

    else:
        # Execute SEULEMENT si aucune erreur n'a eu lieu
        logging.info(f"Taux recupere avec succes : {taux}")
        if taux > 2 or taux < 0.5:
            logging.warning(f"Taux anormal detecte : {taux}")
        return taux

    finally:
        # Execute DANS TOUS LES CAS, erreur ou pas
        logging.info("Fin de la tentative d'appel API")


# ==========================================================
# Programme principal
# ==========================================================

print("--- Appel de l'API protege ---")
taux = recuperer_taux(URL)

if taux is None:
    print("Le programme continue malgre l'echec (il n'a pas plante).")
else:
    print(f"Taux EUR/USD du jour : {taux}")

# Demonstration volontaire d'une erreur reseau
print("\n--- Test avec une adresse volontairement fausse ---")
recuperer_taux("https://adresse-qui-nexiste-pas-du-tout.app/latest")

print("\nConsultez le fichier logs/projet.log pour voir le journal.")

"""
Séance 2 - Partie C : recursivite, memoisation et complexite
"""

import time
import sys
from functools import lru_cache


# ==========================================================
# C.1 - Deux fonctions recursives simples
# ==========================================================

def factorielle(n):
    """Calcule n! de facon recursive. Exemple : 4! = 4*3*2*1 = 24."""
    if n <= 1:                 # CAS DE BASE : il arrete la descente
        return 1
    return n * factorielle(n - 1)   # CAS RECURSIF : la fonction s'appelle elle-meme


def somme_liste(liste):
    """Somme des elements d'une liste, de facon recursive."""
    if len(liste) == 0:        # CAS DE BASE : liste vide, somme nulle
        return 0
    return liste[0] + somme_liste(liste[1:])   # 1er element + somme du reste


print("--- C.1 : recursivite simple ---")
print("factorielle(5) =", factorielle(5))
print("somme_liste([1.05, 1.08, 1.10]) =", somme_liste([1.05, 1.08, 1.10]))


# ==========================================================
# C.2 - Les trois versions de Fibonacci
# ==========================================================

def fib_naif(n):
    """Fibonacci recursif naif : recalcule sans arret les memes valeurs."""
    if n < 2:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)


@lru_cache(maxsize=None)       # decorateur : memorise les resultats deja calcules
def fib_memo(n):
    """Fibonacci recursif avec memoisation."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_iteratif(n):
    """Fibonacci avec une simple boucle : pas de recursion du tout."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b        # on ne garde que les deux dernieres valeurs
    return a


def mesurer(fonction, n):
    """Mesure le temps d'execution d'une fonction en secondes."""
    debut = time.perf_counter()
    resultat = fonction(n)
    fin = time.perf_counter()
    return resultat, fin - debut


print("\n--- C.2 : comparaison des trois versions ---")
print(f"{'n':>4} | {'naif (s)':>12} | {'memo (s)':>12} | {'iteratif (s)':>12}")
print("-" * 52)

for n in [10, 20, 25, 30, 32]:
    _, t_naif = mesurer(fib_naif, n)
    fib_memo.cache_clear()           # on vide le cache pour une mesure honnete
    _, t_memo = mesurer(fib_memo, n)
    _, t_iter = mesurer(fib_iteratif, n)
    print(f"{n:>4} | {t_naif:>12.6f} | {t_memo:>12.6f} | {t_iter:>12.6f}")

# Memoire utilisee par la memoisation
fib_memo.cache_clear()
fib_memo(30)
print("\nEtat du cache apres fib_memo(30) :", fib_memo.cache_info())


# ==========================================================
# C.3 - La limite de recursion
# ==========================================================

print("\n--- C.3 : la RecursionError ---")
print("Limite de recursion de Python :", sys.getrecursionlimit())

try:
    fib_memo.cache_clear()
    print(fib_memo(5000))
except RecursionError:
    print("RecursionError : la pile d'appels a ete depassee.")

print("Version iterative pour n = 5000 : aucun probleme,",
      len(str(fib_iteratif(5000))), "chiffres.")
# %%
"""
BUT: calculer la moyenne de n valeurs entières relatives saisies par l'utilisateur


0/ dans une cellule de test, trouver la fonction permettant de vérifier qu'une str soit convertible en entier

1/ saisir n valeurs entiers relatifs dans le clavier séparés par "," (ex: 1, 2, -3, 14, -33)
2/ on veut itérer sur les valeurs saisies, nettoyées des espaces à gauche et à droite pour vérifier
que ces valeurs sont des entiers relatifs (1er cas entier naturel ensuite 2ème cas négatif)
3/ si c'est convertible on ajoute la valeur convertie dans une nouvelle liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis cette nouvelle liste => trouver les fonctions qui travaillent directmement sur les listes
5/ présenter le résultat avec 2 décimales
"""

# %% ------------------------------- trouver la fonction pour convertir en int -------------------------------
# TIP: regarder si la fonciton est globale ou interne à str

s = ""
s.isnumeric()
# SI la str représente un entier naturel OU un entier négatif
#                                           ( commence par - ET les reste est numérique)
                                             # s[0] == "-"
if s.isnumeric()                         or (s.startswith("-")     and s[1:].isnumeric()):
    print("convertible en entier")

# %% --------------------- saisie en clavier -----------------

values = input("saisir n valeurs entiers relatifs séparés par ',':")
values

# %% ------------------------- itérer sur les valeurs -----------
# TIP: pass est une instruction "bouche trou" qui ne fait rien pour éviter l'erreur de syntaxe
# values = values.split(",")
# for value in values:
integers = []
for value in values.split(","):
    # nettoyer les espaces à gauche et à droite
    value = value.strip()
    if value.isnumeric() or (value.startswith("-") and value[1:].isnumeric()):
        integers.append(int(value))
    else:
        print(f"valeur {value} non convertible !")

# ----------------------------- calculer la moyenne à partir de la liste -----------
# if len(integers) != 0:
else:
    if integers:
        # arrondi dans la valeur : round
        avg = round(sum(integers) / len(integers), 2)
        # .2f: uniquement formatage
        print(f"moyenne de {integers}: {avg:.2f}")

# %%

# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer tous les slots ((xxxx))
par la clé correspondante si celle ci existe ou par N/A
"""

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": 500,
    "section": 30,
    "debit": 2
}

# %% ---------------- trouver le contenu entre les 1ers occurences de (( et )) ----------------------

start_index = _template.find("((") + 2
end_index = _template.find("))")
key = _template[start_index:end_index]

_template.replace("((" + key + "))", str(injections[key]))

# %% ------------------- itération selon les lignes de la str -----------------

lines = _template.splitlines()
injected_lines = []
for line in lines:
    if line:
        start_index = line.find("((") + 2
        end_index = line.find("))")
        key = line[start_index:end_index]

        injected_lines.append(line.replace("((" + key + "))", str(injections.get(key, "N/A"))))
print("\n".join(injected_lines))

# %% ------------------ for : variation -----------------------------------------------
lines = _template.splitlines()
for i in range(len(lines)):
    if lines[i]:
        start_index = lines[i].find("((") + 2
        end_index = lines[i].find("))")
        key = lines[i][start_index:end_index]

        lines[i] = lines[i].replace("((" + key + "))", str(injections.get(key, "N/A")))
print("\n".join(lines))

# %% ---------------------- for: dictionnaire -----------------------------------
for key, value in injections.items():
    _template = _template.replace("((" + key + "))", str(injections[key]))
print(_template)

# %% -------------------------- while: quelle est la condition de continuation/arrêt -----------

while "((" in _template:
    start_index = _template.find("((") + 2
    end_index = _template.find("))")
    key = _template[start_index:end_index]

    _template = _template.replace("((" + key + "))", str(injections.get(key, "N/A")))
_template

# %% ----- portage de la cellule précédente en fonction ----------
"""
technique
1/ entourer le code avec l'entête de def et ajouter le nom
2/ transformer le print ou affectation finale en return
3/ réféchir sur les paramètres d'entrée (positionnels / centraux, et optionnels => valeur par défaut) et de sortie
4/ refactorer le code pour utiliser les paramètres d'entrée et construire la sortie
5/ tester dans différents cas
1. _template et injections
2. "blabla {{param}}" et {"param": 100}
"""


# %%

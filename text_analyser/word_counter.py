# from text_cleaner import Cleaner # ERROR

# REGLE D'OR IMPORTS inter package
# les imports sont toujours calculés depuis le programme principal !!!

from text_analyser.text_cleaner import Cleaner

# ou à la rigueur avec un import relatif
# from .text_cleaner import Cleaner

class Counter:
    def __init__(self, text: str, min_len: int=3):
        # couplage fort ou composition(UML)
        self.text = Cleaner(text).clean(min_len=min_len)

    def get_occurences(self) -> dict:

        # générer un dictionnaie de forme {"mot": nb_occurence (int), ....}
        occurences = {}
        for word in self.text.split():
            ## soit le mot est déjà dans le dico ==> j'incrémente son occurence
            if word in occurences:
                occurences[word] += 1
            # soit non ==> le je crée la clé avec son occurence de base 1
            else:
                occurences[word] = 1

        # REM: trier un dictionnaire, en tant qu'itérable => trier la liste des clés
        # REM: on doit tier la liste de tuple ==> .items()
        # REM: trier un tuple par défaut ==> trie sur le premier élément [0] par défaut
        # REM: on a besoin de changer la fonction de tri pour trier sur [1]
        occurences = sorted(occurences.items(), key=lambda tup: tup[1], reverse=True)

        return dict(occurences[:5])

        

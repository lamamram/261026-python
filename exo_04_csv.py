# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

3. déplacer le fichier csv en dans data/dns.csv
4.. ne faire ce qui précède qui si ce n'est pas déjà fait
hint: module os et pathlib.Path


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""
# %% ---------------------------- télécharger une ressource distante (ici de type zip) avec requests -----------------
"""
HTTP: Hyper Text Transfer Protocol

protocole d'échange de données entre un client (requête HTTP) et un serveur distant qui délivre une réponse HTTP

requête HTTP
--------------
- version de http (1.1) / 2 / 3
- URL : Unified Resource Location: adresse d'une ressource 
protocole|://|nom de domaine|chemin(path) physique ou virtuel|resource (.html, .php, .zip, ...)          |query parameters    |hash données supplémentaires
https     :// www.afnic.fr  |/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip|?param=1&param2=truc|#tag

- Méthode ou verbe HTTP: mode d'accès à la ressource
  GET: lire la ressource
  POST: créer la ressource sur le serveur distant (formulaire)
  PUT/PATCH : modifier la ressource complètement ou partiellement
  DELETE: supprimer la ressource distante

- les entêtes de requêtes : métadonnées (infos contextuelles sur le client)

- données de la requête en cas de POST/PUT/PATCH


Réponse HTTP
------------

                                                     OK  | OK mais redirection| pb sur la requête| pb serveur
- Code de statut: entier répartie en famille de code 2XX | 3XX                | 4XX              | 5XX
- entête de réponse: infos sur le serveur
- le corps de la réponse (html, fichier sous forme de flux d'octets, json ... )
"""

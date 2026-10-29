# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.ZipFile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment
hint: pour extraire une pièce individuelle dans le zip => .namelist()

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
# %%

import requests
import os
from pathlib import Path

url = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
archive_name = url.split("/")[-1]
p_archive = Path(archive_name)

# if not os.path.exists(f"./{archive_name}"):
if not p_archive.exists():
   try:
      r = requests.get(url)

      # 1. vérifier le code de statut et 2. observer l'entête Content-Type
      if 200 <= r.status_code < 300 and "application/zip" in r.headers["content-type"]:
         # prendre le format de corps de réponse (.json() ou .text (HTML) ou .content (bytes))
         with open(f"./{archive_name}", mode="wb") as f:
            f.write(r.content)
      else:
         raise ValueError(f"pb: status: {r.status_code}, headers: {r.headers["content-type"]}")
   except (requests.ConnectionError, requests.HTTPError, ValueError) as e:
      print(e)

# %% ---------------------- décompresser le zip avec le module zipfile et sa classe ZipFile ------------------

from zipfile import ZipFile
from datetime import datetime

p_data = Path("./data")

# if not os.path.exists("./data"):
if not p_data.exists():
   os.mkdir(p_data)

# surcharge de l'opérateur / pour composer des chemins
p_dns = p_data / "dns.csv"

## usages du path
# print(p_dns, p_dns.absolute())
# print(p_dns.parent, p_dns.stem)
# meta = p_dns.lstat()
# print(datetime.fromtimestamp(meta.st_mtime))

# if not os.path.exists("./data/dns.csv"):
if not p_dns.exists():
   with ZipFile(f"./{archive_name}", mode="r") as z:
      csv_name = z.namelist()[0]
      z.extract(csv_name)
   os.rename(f"./{csv_name}", p_dns)

# %% ------------------ découper un gros csv ----------

"""
- BUT: extraire n=2 paquets de nb_line=100k lignes de donnée, sans le header
1/ ouvrir le fichier et lire les lignes de csv
2/ à chaque paquet de lignes <==> tous les multiples de 100k
    faire les opérations suivantes:
     - créér un nouveau fichier csv à nommer en fct du n° de ligne
     - insérer le header dans ce nouveau fichier
     - écrire le paquet de 100k de lignes
"""

nb_slice = 2
slice_size = 10**5

import csv

def write_slice(i: int, header: list, data: list):
   with open(p_data / f"dns_{i}.csv", mode="w", encoding="utf-8") as f:
      writer = csv.writer(f, delimiter=";", lineterminator="\n")
      writer.writerow(header)
      writer.writerows(data)
      # réaffectation dans une fonction ==> variable locale
      # data = []
      # opération muable => même id
      data.clear()


data = []
with open(p_dns, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for i, line in enumerate(reader, start=1):
      
      if i > nb_slice * slice_size: break
      
      data.append(line)
      # if not (i % slice_size):
      
      if i % slice_size: continue
      
      write_slice(i, header, data)




       
       
    




# %%

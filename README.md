# Data-pipeline


## I) Python et Data Engineering
### Execution
Pour exécuter le pipeline, suivez les étapes suivantes :

Installez les dépendances dans le fichier requirements.txt en utilisant la commande pip install -r requirements.txt
Exécutez le fichier src/main.py
Cette exécution génère un fichier json dans le dossier output/ et un fichier de log dans le dossier Logs

### Traitement ad-hoc:
Pour avoir le nom du journal qui mentionne le plus de médicaments différents, exécutez le fichier src/journal_analysis.py.

### Tests unitaires :
Pour lancer les tests unitaires que j'ai implémentés, exécutez le fichier src/test.py.

### Pour aller plus loin
Pour passer à l'échelle et gérer de grosses volumétries, une solution simple serait d'exécuter le pipeline dans le cloud. Dans main.py, j'ai commenté le bloc de code qui permettrait d'exécuter le pipeline sur Dataflow (GCP).

Un aspect à prendre en considération pour gérer de grosses volumétries serait également le stockage des fichiers. Mettre les fichiers sur le cloud, par exemple dans un bucket GCS ou S3, serait une solution. En phase de développement, il faudrait également travailler sur un échantillon réduit des données pour des itérations plus rapides. À cela s'ajoute le fait de paralléliser et d'automatiser au maximum.

## II) SQL
Retrouvez les requêtes SQL dans le fichier requetes/requetes.sql.

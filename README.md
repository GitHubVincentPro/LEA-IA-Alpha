# LEA-IA-Alpha
LEA-IA-Alpha

Voici La structure du projet en 5 dossiers:

1. api/
- __init__.py
- routes/
- messages.py

- Cette route de base fonctionne déjà et permet de tester la structure.

2. app/
- __init__.py
- models.py
- db.py

- Cela établit la connexion à MongoDB locale. Les collections pourront être définies ensuite.

3. chatbot/
- __init__.py
- predict.py
- train.py

- Cela pose les bases pour la prédiction et l'entraînement du chatbot.

4. tests/
- __init__.py
- test_api.py
- test_chatbot.py

- Cela crée:

- Un test basique de l'API avec Requests
- Un test unitaire du modèle de prédiction

5. config/
- __init__.py
- settings.py

- Les variables de environnement pourront être définies (ex: dans un fichier .env).

Ce fichier settings.py pourra ensuite être importé dans les autres modules pour accéder aux paramètres de configuration de manière centralisée.

Cette structure sépare les différentes parties du projet :

- L'API dans api/
- La logique métier dans app/
- Le chatbot dans chatbot/
- Les tests dans tests/
- La config dans config/

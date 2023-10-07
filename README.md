# LEA-IA-Alpha
LEA-IA-Alpha

### DEV V1

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

  ### DEV V2

  API:
- api/routes/messages.py
- Créer une fonction pour créer un message
- Créer une fonction pour récupérer tous les messages

Modèle de données:
- app/models.py
- Ajouter des validations avec Pydantic
- app/db.py
- Créer le schéma MongoDB
- Ajouter les fonctions de CRUD

Chatbot:
- chatbot/predict.py
- Utiliser un pipeline Transformer
- chatbot/data.py
- Fonction pour charger les données d'entraînement
- chatbot/train.py
- Ajouter l'appel à la fonction de chargement des données
- Ajouter l'entraînement personnalisé

Tests:
- tests/test_api.py
- Ajouter des tests pour les routes POST/GET
- tests/test_db.py
- Tester les fonctions de persistance

Configuration:
- config/settings.py
- Définir les variables d'environnement
- Dockerfile
- Construire l'image docker

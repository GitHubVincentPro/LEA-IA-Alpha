# chatbot/train.py
```python
from chatbot.data import load_data
from transformers import Trainer, TrainingArguments

MODEL_NAME = 'chatbot/model'

def train_model():

# Chargement des données
data = load_data()

# Initialisation du modèle
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Définition des arguments d'entraînement
training_args = TrainingArguments(
evaluation_strategy="epoch",
num_train_epochs=3
#...
)

# Entraînement
trainer = Trainer(
model=model,
args=training_args,
train_dataset=data['train'],
eval_dataset=data['valid']
)

trainer.train()

# Sauvegarde du modèle entraîné
trainer.save_model(MODEL_NAME)

if __name__ == '__main__':
train_model()
```
# chatbot/train.py
from chatbot.data import load_data
from transformers import Trainer, TrainingArguments

def train():
data = load_data()

trainer = Trainer(
model=model,
args=TrainingArguments("test"),
train_dataset=data['train'],
eval_dataset=data['valid']
)

trainer.train()
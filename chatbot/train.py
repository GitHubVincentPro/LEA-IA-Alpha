# Dans chatbot/train.py

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Dans chatbot/predict.py

from .train import model

def predict(message):
return model.predict([message])[0]
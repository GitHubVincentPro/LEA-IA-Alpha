```python
import os

# Database
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", 27017)
DB_NAME = os.environ.get("DB_NAME", "chatbot")

# API
API_HOST = os.environ.get("API_HOST", "0.0.0.0")
API_PORT = os.environ.get("API_PORT", 8000)

# Logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")

# JWT
JWT_SECRET = os.environ.get("JWT_SECRET", "super-secret")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")

# Chatbot model
MODEL_NAME = os.environ.get("MODEL_NAME", "chatbot/model")

class Config:
...
DB_CONFIG = {
"host": DB_HOST,
"port": DB_PORT,
"name": DB_NAME
}

API_CONFIG = {
"host": API_HOST,
"port": API_PORT
}

LOG_CONFIG = {
"level": LOG_LEVEL
}

AUTH_CONFIG = {
"secret": JWT_SECRET,
"algorithm": JWT_ALGORITHM
}

MODEL_CONFIG = MODEL_NAME

config = Config()
```
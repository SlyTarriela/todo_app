# commands

## how to setup environment

- create venv
```
python -m venv flask_mongodb
```

- activate environment
```
flask_mongodb\Scripts\Activate.ps1
```

- install dependencies
```
pip install -r requirements.txt
```

- create .env file
```
MONGODB_USERNAME = <your-username>
MONGODB_PASSWORD = <your-password>

SECRET_KEY = <your-secret-key-here>
```

- run the code
```
python run.py
```

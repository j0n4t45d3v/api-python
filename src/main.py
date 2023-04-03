from flask import Flask
from src.controllers.user_controller import user
from src.controllers.index_controller import index

app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(user)

if __name__ == '__main__':
    print(f"Server running port: {3000}")
    app.run(port=3000)

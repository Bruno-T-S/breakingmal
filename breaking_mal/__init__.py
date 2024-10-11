from flask import Flask
from .controllers import tarefas_controller as tc

app = Flask(__name__)
app.register_blueprint(tc)

if __name__ == "__main__":
    app.run(debug=True)
    
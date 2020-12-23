from flask import Flask
from main import algorithms as ee

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/erdil-ergin')
def run_erdil_ergin_algorithms():
    return ee.match()


if __name__ == '__main__':
    app.run()

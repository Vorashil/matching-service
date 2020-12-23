from flask import Flask, request, jsonify
from flask.wrappers import JSONMixin

from main.algorithms import erdil_ergin as ee
from main.domain.commoninput import CommonInput
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/erdil-ergin', methods=['POST'])
def run_erdil_ergin_algorithms():
    common_input = parse_input(request)
    return ee.match(common_input)


@app.route('/gale-shapley', methods=['POST'])
def run_gale_shapley():
    pass


@app.route('/check-input', methods=['POST'])
def check_input():
    common_input = parse_input(request)

    men_name = common_input.get_men_names()
    men_count = common_input.get_men_count()

    women_name = common_input.get_women_names()
    women_count = common_input.get_women_count()

    return "There are {} men and {} women. Men are [{}] and women are [{}].".format(men_count, women_count, men_name,
                                                                                    women_name)


def parse_input(payload: JSONMixin):
    j = json.dumps(payload.get_json())
    return CommonInput.from_json(json.loads(j))


if __name__ == '__main__':
    app.run()

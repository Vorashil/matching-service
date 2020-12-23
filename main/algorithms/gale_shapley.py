import main.domain.commoninput as ci
from main.exceptions.gale_shapley_exception import GaleShapleyException


def count_agents(common_input: ci.CommonInput):
    women_count = common_input.get_women_count()
    men_count = common_input.get_men_count()

    return men_count, women_count


def match(common_input: ci.CommonInput):
    return "matching"


def random_match(common_input: ci.CommonInput):
    validate(common_input)
    matching = dict()

    for i in range(common_input.get_men_count()):
        matching[common_input.men_list[i].get_name()] = common_input.women_list[i].get_name()

    return matching


def validate(common_input: ci.CommonInput):
    if common_input.get_men_count() != common_input.get_women_count():
        raise GaleShapleyException("There should be the same number of men and women")

import main.domain.commoninput as ci


def count_agents(common_input: ci.CommonInput):
    women_count = common_input.get_women_count()
    men_count = common_input.get_men_count()

    return men_count, women_count

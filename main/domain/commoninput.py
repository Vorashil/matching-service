from typing import List
from main.domain.man import Man
from main.domain.woman import Woman


class CommonInput:
    def __init__(self, men_list: List[Man], women_list: List[Woman]):
        self.men_list = men_list
        self.women_list = women_list

    def get_women_count(self):
        return len(self.women_list)

    def get_men_count(self):
        return len(self.men_list)

    def get_men_names(self):
        result = ""
        for man in self.men_list:
            result += man.get_name()
            result += ", "

        return result[:-2]

    def get_women_names(self):
        result = ""
        for woman in self.women_list:
            result += woman.get_name()
            result += ", "

        return result[:-2]

    @classmethod
    def from_json(cls, data):
        men_list = list(map(Man.from_json, data["men_list"]))
        women_list = list(map(Woman.from_json, data["women_list"]))
        return cls(men_list, women_list)

    def __str__(self):
        return "we have {} men and {} women".format(len(self.men_list), len(self.women_list))

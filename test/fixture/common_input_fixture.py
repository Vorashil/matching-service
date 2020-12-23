from main.domain.commoninput import CommonInput
from main.domain.man import Man
from main.domain.woman import Woman


def create_sample_input():
    m_1 = Man("m_1", ["w_2", "w_1", "w_3"])
    m_2 = Man("m_2", ["w_1", "w_2", "w_3"])
    m_3 = Man("m_3", ["w_1", "w_2", "w_3"])

    w_1 = Woman("w_1", ["m_1", "m_3", "m_2"])
    w_2 = Woman("w_2", ["m_3", "m_1", "m_2"])
    w_3 = Woman("w_3", ["m_1", "m_2", "m_3"])

    return CommonInput([m_1, m_2, m_3], [w_1, w_2, w_3])

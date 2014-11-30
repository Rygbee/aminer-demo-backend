__author__ = 'yxy'

from aminer.config import DefaultConfig
from datetime import datetime
import math


def get_pub_count(pub_list):
    return len(pub_list)


def get_citation_num(pub_list):
    citation_number = 0
    for p in pub_list:
        if p.citation_num >= 0:
            citation_number += p.citation_num
    return citation_number


def get_h_index(pub_list):
    sorted_pub_list = sorted(pub_list, key=lambda x: x.citation_num, reverse=True)
    h_index = 0
    for i in range(0, len(sorted_pub_list)):
        if sorted_pub_list[i].citation_num < i+1:
            break
        h_index = i+1
    return h_index


def get_g_index(pub_list):
    sorted_pub_list = sorted(pub_list, key=lambda x: x.citation_num, reverse=True)
    max_gindex = len(pub_list)
    g_index = 100
    sum_citation = 0
    for i in range(0, len(sorted_pub_list)):
        current_citation = sorted_pub_list[i].citation_num
        if current_citation is None:
            current_citation = 0
        elif current_citation < 0 :
            current_citation = 0
        sum_citation += current_citation
        if g_index < i+1:
            break
        g_index = int(math.floor(math.sqrt(sum_citation)))
    if g_index > max_gindex:
        g_index = max_gindex
    return g_index


def get_sociability(pub_list):
    name_set = set()
    for p in pub_list:
        for a in p.authors:
            name_set.add(a)
    return math.log(len(name_set) + 1)


def get_activity(pub_list, year_limit):
    conf_dict = AuthorFeatureCalculateData.read_code_file()
    sorted_pub_list = sorted(pub_list, key=lambda x: x.year, reverse=False)
    last_year = 0
    activity = []
    for i in year_limit:
        activity.append(0.0)
    #final
    ICWeight = 0.2  #due to not having page info in mongo
    alpha = 0.75

    #literate
    IS = 0.0
    for p in sorted_pub_list:
        if last_year != p.year:
            year_dist = datetime.now().year - p.year
            ISWeight = 1.0 + math.pow(alpha, year_dist)
            for i in range(0, len(year_limit)):
                if year_limit[i] == -1 or year_dist <= year_limit[i]:
                    activity[i] += ISWeight * IS
            IS = 0.0
            pass
        IC = 0.05
        if p.conf_name in conf_dict:
            IC = conf_dict.get(p.conf_name)
        IS += IC * ICWeight
    year_dist = datetime.now().year - p.year
    ISWeight = 1.0 + math.pow(alpha, year_dist)
    for i in range(0, len(year_limit)):
        if year_limit[i] == -1 or year_dist <= year_limit[i]:
            activity[i] += ISWeight * IS

    return activity


def get_activity_new_and_rising_star(pub_list):
    sorted_pub_list = sorted(pub_list, key=lambda x: x.year, reverse=True)
    activity = 0.0
    rising_star = 0.0
    new_star = 0.0

    if len(sorted_pub_list) == 0:
        return [0.0, 0.0, 0.0]

    year_dist = datetime.now().year - sorted_pub_list[len(sorted_pub_list)-1].year
    if year_dist > 12:
        result = get_activity(sorted_pub_list, [-1])
        activity = result[0]
    else:
        result = get_activity(sorted_pub_list, [-1, 3])
        activity = result[0]
        star_activity = result[1]
        rising_star_add_on = 0.0
        for p in sorted_pub_list:
            cur_year_dist = datetime.now().year - p.year
            if cur_year_dist > 5:
                break
            citation = p.citation_num
            if citation < 0:
                citation = 0
            rising_star_add_on += math.log(citation + 1)
        rising_star = star_activity + rising_star_add_on

        if year_dist <= 3:
            new_star = star_activity
    return [activity, rising_star, new_star]


def get_diversity(pub_list):
    conf_count = {}
    pub_count = 0.0
    for p in pub_list:
        if p.conf_id != -1:
            if p.conf_id not in conf_count:
                conf_count[p.conf_id] = 0
            conf_count[p.conf_id] += 1
            pub_count += 1
    diversity = 0.0
    if pub_count != 0.0:
        for key in conf_count:
            p_a_c = float(conf_count[key]) / pub_count
            diversity -= p_a_c * math.log(p_a_c)
    return diversity


class AuthorFeatureCalculateData:
    conf_dict = None

    def __init__(self):
        pass

    @staticmethod
    def read_code_file():
        if not AuthorFeatureCalculateData.conf_dict is None:
            return AuthorFeatureCalculateData.conf_dict
        import codecs
        f = codecs.open(DefaultConfig.APP_STATIC+'/misc/dict_pair_EN.dic', 'r', 'utf8')
        # utf8coder = codecs.getdecoder("utf-8")
        result = {}
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            x = line.split('\t')
            score = float(x[1])
            result[x[0]] = score
            # result[x[0]] = x[1].encode('gb2312')
        f.close()

        f = codecs.open(DefaultConfig.APP_STATIC+'/misc/dict_pair_ZH.dic', 'r', 'utf8')
        # utf8coder = codecs.getdecoder("utf-8")
        result = {}
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            x = line.split('\t')
            score = float(x[1]) * 4
            result[x[0]] = score
            # result[x[0]] = x[1].encode('gb2312')
        f.close()

        AuthorFeatureCalculateData.conf_dict = result
        return result


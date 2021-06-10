import random
from pprint import pprint

monsterstats_file = open('monsterstats.csv')
monsterstats_text = monsterstats_file.read()

def get_headers(s):
    s = s[:s.find("\n")]
    g = s.split(",")
    return g

def get_data(s):
    s = s[s.find("\n")+1:len(s)-1]
    data = s.split("\n")
    order = 0
    while order < len(data):
        data[order] = data[order].split(",")
        order += 1
    return data

def make_monster_dict(data):
    d = {}
    for x in data:
        y = x[0]
        sub_list = []
        order = 1
        while order < len(data[0]):
            sub_list.append(x[order])
            order += 1
        d[y] = sub_list
    return d
    
def combine_dict(d, headers):
    temp_dict = {}
    headers.remove(headers[0])
    for x in d:
        g = d[x]
        order = 0
        while order < len(g):
            temp_dict[headers[order]] = g[order]
            order += 1
        d[x] = temp_dict
        temp_dict = {}
    return d    

monster_headers = get_headers(monsterstats_text)
monster_data = get_data(monsterstats_text)
monster_dict = make_monster_dict(monster_data)
monster_combine = combine_dict(monster_dict, monster_headers)
pprint(monster_combine)

monster_list = []
for x in monster_data:
    monster_list.append(x[0])
pprint(monster_list)

monsternumber = 5
order = 0
monsters = []
while order < monsternumber:
    monsters.append(random.choice(monster_list))
    order += 1
    
def make_levels(dictionary, levels):
    answer = {}
    monster_list = []
    for x in monster_data:
        monster_list.append(x[0])
    for x in levels:
        answer[x] = dictionary[monster_list[x-1]]
    return answer
    
levels = [1,2,3,4]
pprint(make_levels(monster_combine, levels))

def make_levels2(dictionary, levels):
    answer = {}
    monster_list = []
    for x in monster_data:
        monster_list.append(x[0])
    print(monster_list)
    temp_dict = {}
    order = 0
    i = 0
    while order < len(levels):
        while i < 3:
            temp_dict[monster_list[i + (order * 3)]] = dictionary[monster_list[i + (order * 3)]]
            answer[levels[order]] = temp_dict
            i += 1
        temp_dict = {}
        order += 1
        print(order)
    return answer
    
levels = [1,2,3,4]
pprint(make_levels2(monster_combine, levels))
    
    

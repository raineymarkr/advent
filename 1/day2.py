import re

f = open('locationid.txt', 'r')
loc_ids = f.read()

regex = re.compile(r'\d{5}', re.IGNORECASE)
loc_id_list = re.findall(regex, loc_ids)

locs_left = []
locs_right = []
total_distance = 0
i = 0
for i in range(0, len(loc_id_list)-1, 2):
    locs_left.append(int(loc_id_list[i]))
    locs_right.append(int(loc_id_list[i+1]))

locs_left.sort()
locs_right.sort()

dict = {}
for i in range(len(locs_left)):
    number_to_check = locs_left[i]
    multiplicity = 0
    for j in range(len(locs_right)):
        if locs_right[j] == number_to_check:
            multiplicity += 1
    dict[number_to_check] = multiplicity

similarity_score = 0

for key in dict:
    sim = key * dict[key]
    similarity_score += sim
print(similarity_score)
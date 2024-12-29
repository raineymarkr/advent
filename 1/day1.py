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
    locs_left.append(loc_id_list[i])
    locs_right.append(loc_id_list[i+1])

locs_left.sort()
locs_right.sort()

for i in range(len(locs_right)):
    dist = abs(int(locs_left[i]) - int(locs_right[i]))
    total_distance += dist

print(total_distance)


import csv
# getting map from csv and using value to get image
with open('try_again/tile_try/level_1s.csv',mode ='r') as f:
    reader = csv.reader(f)
    l_map1 = list(reader)


for i in range(len(l_map1)):
#     print(l_map1[i])
    for o in range(len(l_map1[i])) :
        if l_map1[i][o] == "34":
#             print(l_map1[i][o])
            l_map1[i][o] = "c"
        if l_map1[i][o] == "19":
            l_map1[i][o] = "y" 
        if l_map1[i][o] == "163":
            l_map1[i][o] = "e" 
        if l_map1[i][o] == "291":
            l_map1[i][o] = "d" 
        if l_map1[i][o] == "133":
            l_map1[i][o] = "w" 
        if l_map1[i][o] == "335":
            l_map1[i][o] = "dr"
            # dragon 
        

#  change value 0 to c - coins

l_map = l_map1.copy()
print(l_map)

# print(l_map)
screen_tile = 64
screen_width = 1200
screen_height = len(l_map1) * screen_tile

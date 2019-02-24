from fuzzywuzzy import fuzz
import copy 

all_data = ['aditya','adit',"adity",'kuma','kumar','kumara']
tem_list = copy.deepcopy(all_data)
limit = 90
for i in range(0, len(all_data)):
    flag = False
    for j in range(i+1, len(all_data)):
        if fuzz.ratio(all_data[i], all_data[j]) > limit or fuzz.token_set_ratio(all_data[i], all_data[j]) > limit or fuzz.token_sort_ratio(all_data[i], all_data[j]) > limit or fuzz.partial_ratio(all_data[i], all_data[j]) > limit:
            all_data[j] = ""
print(list(set(all_data)))

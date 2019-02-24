import json

host_global = ["aditya", "kumar"]
winners_global = {"a":["123"], "b":["234"]}
presenters_global = {"a":["3","4"],"b":["5","6"]}
nominee_global = {"a":["7","8"], "b":["9","10"]}
best_dressed_global = ["ajsbd sdfsd", "asd sdfsdf"]
worst_dressed_global = ["kfjgk sdfsdf", "shdfjb sdfsd"]
c_dressed_global = ["asdfiuh jsjd","bhdsf jkbdsf"]
m_disscussed = ["jsbhdf sjbdhf", "ajbhd kajbsd"]


# award = {}
# final = {"Host":host_global, "award_data":award}

# for key, value in winner.items():
#     award[key] = dict()
#     award[key]["nominees"] = nomines[key]
#     award[key]["presenters"] = presenters[key]
#     award[key]["winner"] = value
# with open('result.json', 'w') as fp:
#     json.dump(final, fp)


f= open("results.txt","w")
f.write("Host:"+",".join(host_global)+"\n")
f.write("\n")
for key, value in winners_global.items():
     f.write("Award:"+key+"\n")
     f.write("Presenters:"+",".join(presenters_global[key])+"\n")
     f.write("Nominees:"+",".join(nominee_global[key])+"\n")
     f.write("Winner:"+value[0]+"\n")
     f.write("\n")

f.write("Most Disscussed:"+",".join(m_disscussed)+"\n")
f.write("Best Dressed:"+",".join(best_dressed_global)+"\n")
f.write("Worst Dressed:"+",".join(worst_dressed_global)+"\n")
f.write("Most Controversially Dressed:"+",".join(c_dressed_global)+"\n")
f.close()
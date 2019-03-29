def findItinerary(tickets):
    d = {}
    for e in tickets:
        if e[0] in d:
            d[e[0]].append(e[1])
        else:
            d[e[0]] = [e[1]]
    # Construnct Output
    o = ["JFK"]
    while True:
        if o[len(o)-1] in d and d[o[len(o)-1]]:
            temp = d[o[len(o)-1]]
            temp.sort(reverse = True)                
            if len(temp)>1:
                if temp[len(temp)-1] in d:
                    o.append(temp.pop())
                else:
                    count = len(temp) - 1
                    while count != -1:
                        if temp[count] not in d:
                            count -= 1
                        else:
                            o.append(temp.pop(count))
                            break
            else:
                o.append(temp.pop())
        else:
            break  
    return o

print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
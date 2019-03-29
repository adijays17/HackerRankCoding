# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    if len(intervals) < 2:
        return intervals
    final_list = []
    intervals.sort(key=lambda x: (x.start, x.end))
    i = [intervals[0].start , intervals[0].end] 
    for e in range(1, len(intervals)):
        if int(intervals[e].start) <= int(i[1]):
            i = [min(intervals[e].start, i[0]), max(intervals[e].end, i[1])]
        else:
            if i not in final_list:
                final_list.append(i)
            i = [intervals[e].start, intervals[e].end]
        if i not in final_list:
            final_list.append(i)
    out = []
    for each in final_list:
        out.append(Interval(each[0], each[1]))
    return out

print(merge([Interval(2,3), Interval(4,5),Interval(6,7),Interval(8,9), Interval(1,10)]))
#print()
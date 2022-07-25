from const import *


def dicsum(dics):
    ret={catagories[0]:{},catagories[1]:{},catagories[2]:{}}
    for dic in dics:
        for cat in catagories:
            for ref,lst in dic[cat].items():
                if ref not in ret[cat]:
                    ret[cat][ref]=[]
                ret[cat][ref].extend(lst)
    return ret
            

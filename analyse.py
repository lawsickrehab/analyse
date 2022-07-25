import re

catagory=['刑法','刑事訴訟法','其他']

def str2list(ditiao):
#    assert re.search('^第.*條。$',ditiao),'str2list not expected format'
    return ditiao.split('、')

def cut(d):
    end=['法','條例','公約']
    d=d.replace(' ','')
#    assert d.endswith('。'),'string does not end with\'。\''
    assert any([re.search(ed,d) for ed in end]),d+'=> Input not end with \''+'\' or \''.join(end)+'\''

    cutIdx=d.find('第')
    cata=d[:cutIdx]
    if cata!=catagory[0] and cata!=catagory[1]:
        cata=catagory[2]
    return cata,str2list(d[cutIdx:])
     

def analyse(zp):
    dic={catagory[0]:{},catagory[1]:{},catagory[2]:{}}
    for c,rs in zp:
        for r in rs:
            main,lst=cut(r) 
            for lt in lst:
                lt=main+lt
                if lt not in dic[main]:
                    dic[main][lt]=[]
                dic[main][lt].append(c)
    return dic

    
        

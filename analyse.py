import re

def str2list(ditiao):
#    assert re.search('^第.*條。$',ditiao),'str2list not expected format'
    return ditiao.split('、')

def analyse(data):
    end=['法','條例','公約']
    catagory=['刑法','刑事訴訟法','其他']
    dic={catagory[0]:{},catagory[1]:{},catagory[2]:{}}
    for d in data:

        d=d.replace(' ','')
#        assert d.endswith('。'),'string does not end with\' 。\''
        assert any([re.search(ed,d) for ed in end]),d+'Input not expected format'

        cutIdx=d.find('第')
        main=d[:cutIdx]
        if main!=catagory[0] and main!=catagory[1]:
            main=catagory[2]
        
        lst=str2list(d[cutIdx:])
        for lt in lst:
            lt=d[:cutIdx]+lt
            dic[main][lt]=dic[main].get(lt,0)+1
    
     
    return dic

    
        

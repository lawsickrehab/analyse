import re

def pure(s,dirt):
    for d in dirt:
        s=s.replace(d,'')
    return s

def find_by_regex(str):
    # 總總好可愛
    str=pure(str,' \n\t')
    regex = r'參考法條：(.*?[一二三四五六七八九十百千]+、)?'
    matches = re.findall(regex, str, re.DOTALL)
    ret = []
#    print(matches)
    for i, match in enumerate(matches):
#        print(match)
        if i == len(matches)-1:
            match=match[:match.find('裁判字號')]
        match = match.split('。')
        match = match[:-1]
        ret.append(match)
 
    # print(ret)
    return ret

def contents(str):
#    print(repr(str))
    regex = r'目錄[\n\t ]+裁判要旨[\n\t ]+(.*?)裁判全文'
#    regex = r'((.*)目錄[\n\t ]+裁判要旨[\n\t ]+)(.*)'
    matches = re.findall(regex, str, re.DOTALL)
#    print("line 31",matches)
    if(len(matches)!=1):
        print(matches)
    assert len(matches)==1, "more than one content found"
    matches=pure(matches[0],' \n\t.　')
#    print("-----")
#    print(repr(matches))
#    print("-----")
#    matches=matches.splitlines()
    matches=re.split(r'([一二三四五六七八九十百千]+、)',matches)
    matches=[matches[i][:matches[i].find('號')+1] for i in range(2,len(matches),2)]
    
    return matches

def prec(s):
    year=s[0:3]
    type=s[5:7]
    num=re.search('(.*)第([0-9]*)號$',s).group(2)
    return year+','+type+','+num

    

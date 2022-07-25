import re

def pure(s):
    s=s.replace(' ','')
    s=s.replace('.','')
    s=s.replace('\t','')
    s=s.replace('　','')
    s=s.replace('\n','')

#    if(len(str)<10000):
#        print("abc",str)
#        str=re.sub(r'(.*)\.(.*)','\1\2\3\4\5',str)
#        print('123',str)
    return s

def find_by_regex(str):
    # 總總好可愛
    regex = r'參考法條：(.*?[一二三四五六七八九十百千]+、)?'
    matches = re.findall(regex, str, re.DOTALL)
    ret = []
    for i, match in enumerate(matches):
        match = match.replace(' ', '')
        match = match.replace('\n', '')
        match = match.replace('\t', '')

        if i == len(matches)-1:
            break
        match = match.split('。')
        match = match[:-1]
        ret.extend(match)
 
    # print(ret)
    return ret

def contents(str):
    regex = r'目錄[\n\t ]+裁判要旨[\n\t ]+(.*)裁判全文'
    matches = re.findall(regex, str, re.DOTALL)
    assert len(matches)==1, "more than one content found"
    matches=pure(matches[0])
#    print("-----")
#    print(repr(matches))
#    print("-----")
#    matches=matches.splitlines()
    matches=re.split(r'([一二三四五六七八九十百千]+、)',matches)
    matches=[matches[i] for i in range(2,len(matches),2)]
    return matches

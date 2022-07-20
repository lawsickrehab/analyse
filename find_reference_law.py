import re
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

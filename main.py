import os
import re
from colorama import Fore
from pprint import pprint


from const import *
import utils
from trans import pdf2txt,dic2csv
from analyse import analyse
from filters import find_by_regex,contents

dataPath='./data/'
ls=os.listdir(dataPath)

ans={}
ans={catagories[0]:{},catagories[1]:{},catagories[2]:{}}
# 
broken=["105年度刑事具有參考價值之裁判要旨暨裁判全文.pdf","最高法院刑事具有參考價值之裁判要旨暨裁判全文（109年度11月）.pdf"]

# content count failed
strange=["109年度（6月）刑事具有參考價值之裁判要旨暨裁判全文.pdf","109年度（7月）刑事具有參考價值之裁判要旨暨裁判全文.pdf"]

fouts=[]

for fname in ls:
    if fname in broken or fname in strange:
        print(Fore.RED+   "File not expected "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname)
        continue
    try:
        text=pdf2txt(dataPath+fname) 
        print(Fore.GREEN+ "Read successful   "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname)
    except KeyboardInterrupt:
        print("KeyboardInterrupted")
        break
    except:
        print(Fore.YELLOW+"Read failed       "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname)
        continue
    
    cnts=contents(text)

    refs=find_by_regex(text)

    fouts.append(analyse(zip(cnts,refs)))
    

#pprint(fouts)
ans=utils.dicsum(fouts)
#print(ans)

exit(0)

resultPath='./result/'
for k,v in ans.items():
    v=dict(sorted(v.items(),key=lambda item:len(item[1])))
    dic2csv(v,resultPath+k+'.csv')
    



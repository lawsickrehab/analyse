import os
import re
import json

from colorama import Fore
from pprint import pprint
from tqdm import tqdm

import filters

from const import *
import utils
from trans import pdf2txt,dic2csv
from analyse import analyse
from filters import find_by_regex,contents

dataPath='./data/'
ls=os.listdir(dataPath)
logfile=open("log",'w')

# 
broken=["105年度刑事具有參考價值之裁判要旨暨裁判全文.pdf","最高法院刑事具有參考價值之裁判要旨暨裁判全文（109年度11月）.pdf"]

# content count failed
strange=["109年度（6月）刑事具有參考價值之裁判要旨暨裁判全文.pdf","109年度（7月）刑事具有參考價值之裁判要旨暨裁判全文.pdf"]

st=set()
st={"109,台上,1478","109,台上,1479","109,台上,2076","109,台上,2077"}

for fname in tqdm(ls):
    if fname in broken or fname in strange:
        print(Fore.RED+   "File not expected "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname,file=logfile)
        continue
    try:
        text=pdf2txt(dataPath+fname) 
        print(Fore.GREEN+ "Read successful   "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname,file=logfile)
    except KeyboardInterrupt:
        print("KeyboardInterrupted")
        break
    except:
        print(Fore.YELLOW+"Read failed       "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname,file=logfile)
        continue
    
    cnts=contents(text)
    cts=[filters.prec(c) for c in cnts if c!="NIL"]
    st.update(cts)


judgePath='../judgements/最高法院_刑事/'
jls=os.listdir(judgePath)
outfile=open("precisetest.txt",'w')

for jname in tqdm(jls):
    with open(judgePath+jname,'r') as jfile:
        cur=json.load(jfile)
        assert "no" in cur, "judgement number lost"
        if cur["no"] in st:
            st.remove(cur["no"])
            print(jname,file=outfile)

print("st reamins",len(st))
print(st)

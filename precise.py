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

dataPath='../logic-graph/txt/'
ls=os.listdir(dataPath)
logfile=open("log",'w')

# 
broken=["最高法院刑事具有參考價值之裁判要旨暨裁判全文（109年度11月）.txt"]

st=set()
st={"109,台上,1478","109,台上,1479","109,台上,2076","109,台上,2077"}

for fname in tqdm(ls):
    if fname in broken or 0:
        print(Fore.RED+   "File not expected "+Fore.LIGHTBLACK_EX+"|"+Fore.RESET,fname)
        continue
    text=open(dataPath+fname,'r').read()
    
    cnts=contents(text)
    cts=[filters.prec(c) for c in cnts if c!="NIL"]
    st.update(cts)


judgePath='../judgements/最高法院_刑事/'
jls=os.listdir(judgePath)
outfile=open("precise.txt",'w')

print(len(st),"found in st")

for jname in tqdm(jls):
    with open(judgePath+jname,'r') as jfile:
        cur=json.load(jfile)
        assert "no" in cur, "judgement number lost"
        if cur["no"] in st:
            st.remove(cur["no"])
            print(jname,file=outfile)

print("st still reamins",len(st))
print(st)

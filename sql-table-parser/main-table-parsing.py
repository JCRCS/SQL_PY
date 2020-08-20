#%%
import sqlparse
import mmap
import base64
import re
from bs4 import BeautifulSoup
from copy import deepcopy
#%%
with open('txtVistaBANKIT', 'rb') as f1: 
    content = f1.read().decode("utf-8")
    
# %%
content_fixed = content.replace('\r',"")
content_fixed = content_fixed.replace('\n',"")
content_fixed = content_fixed.replace("select",";select")
contents = content_fixed.split(";")
# %%
contents[0][0:150]
#%% Get an Statement object from parsed
for icontent in contents:
    parsed = sqlparse.parse(icontent)
    stmt = parsed[0]
    try:
        print(str(stmt.tokens[-3]))
    except: pass

# %%
txt = deepcopy(content[0:1000])

def select2where(self, txt, i):
    self.m_res = []
    while flag:
        if 

def from2where (self, txt, i):
    self.m_res = []
    while flag:
        if (txt[i]) = 'select':
            from2where(txt,i)
        elif (txt[i]) = 'where':
            return self.m_res
            break
        else 


replace_list = ['\n', '(', ')', '*', '=']
for i in replace_list:
    txt = txt.replace(i, ' ')
txt = txt.split()
res = []
for i in range(1, len(txt)):
    print (f"txt[i], {txt[i-1]}")
    print (f"txt[i], {txt[i]}")
    if txt[i-1] in ['from', 'join'] and txt[i] != 'select': 
        print("append")
        res.append(txt[i])
print(res)
# %%

# %%

# %%

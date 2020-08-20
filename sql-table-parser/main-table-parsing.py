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
    content.replace(r'\"',"")

#%% sqlparse flatten preview
content_fixed = content[0:1000].replace(r'\r',"")
content_fixed = content_fixed.replace(r'\n',"")
# content_fixed = content_fixed.replace("select",";select")
sqlParse_contents = sqlparse.split(content_fixed)
# %%
for iSqlParse_contents in sqlParse_contents:
    parsed_tuple = sqlparse.parse(iSqlParse_contents)
    statement = parsed_tuple[0]
    tokens = statement
    # def recursion (tokens = parent_token ):
    for token in tokens:
        # print (sqlparse.sql.Parenthesis(token))
        # print(f"type: {token.ttype}, value: {token.value}, the token has a child?: {token.is_group}.")
        if token.ttype != sqlparse.tokens.Whitespace and token.ttype != sqlparse.tokens.Punctuation:
            print("hola")
            if token.is_group:
                if token.is_group and token.ttype == None:
                    print ("is true and is group")
                for itoken in token:
                    if (itoken.ttype != sqlparse.tokens.Whitespace and 
                    itoken.ttype != sqlparse.tokens.Punctuation and 
                    itoken.ttype != sqlparse.tokens.Whitespace.Newline):
                        print(f"I type: {itoken.ttype} value: {itoken.value}, the token has a child?: {itoken.is_group}.")
                        if itoken.is_group:
                            for iitoken in itoken:
                                if (iitoken.ttype != sqlparse.tokens.Whitespace and 
                                iitoken.ttype != sqlparse.tokens.Punctuation and 
                                iitoken.ttype != sqlparse.tokens.Whitespace.Newline):
                                    print(f"II type: {iitoken.ttype} value: {iitoken.value}, the token has a child?: {iitoken.is_group}.")
                            # if itoken.is_group:
                            #     if itoken.is_group and itoken.ttype == None:
                            #         print ("I is true and is group")
# %%

# print(str(stmt.tokens))
#%%
aux = sqlparse.split(content_fixed)
print (content_fixed)
for i in range (5):
    print (len(aux))
    # print (aux )
    aux = sqlparse.split(aux[0])
    

#%%
import pandas as pd
name_counts = pd.DataFrame()
for parsed in sqlparse.parse(content_fixed):
    for token in parsed.flatten():
        print (token)

        


# %%
update_names(content_fixed)
print(name_counts)
# %%

# %%
content_fixed = content.replace('\r',"")
content_fixed = content_fixed.replace('\n',"")
content_fixed = content_fixed.replace("select",";select")
contents = content_fixed.split(";")

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

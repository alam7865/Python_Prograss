# from trac import trac

# import json
# with open ("./trac.json",'r') as f:
#     data=json.load(f)

# text=data["text"]  


# def solve(text,chunk_Size,Overlap):
#     text1=text.split()
#     step_size=chunk_Size-Overlap
#     chunks=[]
#     # for x in range(0,len(text1)-Overlap,step_size):
#     for x in range(0,len(text1)-chunk_Size+1,step_size):
#         txt1=text1[x:x+chunk_Size]
#         str=" ".join(txt1)
#         # print(str)
#         chunks.append(str)

#     with open("./trac1.json",'w') as f:
#         # f.loads(chunks)
#         json.dump(chunks,f,indent=4)
            

# solve(text,5,2)


# //////////////////////////// for 12 chunks ////////////////////////


# import json
# with open("./trac.json",'r') as f:
#     data=json.load(f)

# text=data["text"]

# def solve(text,chunk,overlap):
#     step_size=chunk-overlap
#     text1=text.split()
#     chunks=[]
#     for x in range(0,len(text1)-chunk+1,step_size):
#         str=text1[x:x+chunk]
#         str1=" ".join(str)
#         # print(str1)
#         chunks.append(str1)

#     with open("./trac2.json",'w') as f:
#         json.dump(chunks,f,indent=4)    

# solve(text,10,2)


# /////////////////// Sentence Based Chunking //////////////

# import json

# with open("./trac.json",'r') as f:
#     data=json.load(f)

# text=data["text"]

# def solve(text,chunk,overlap):
#     step_size=chunk-overlap
#     sentence=text.split(". ")
#     chunks=[]
#     for x in range(0,len(sentence)-chunk+1,step_size):
#         sentence1=sentence[x:x+chunk]
#         chunks.append(sentence1)
#     with open("./trac3.json",'w') as f:
#         json.dump(chunks,f,indent=4)
# solve(text,1,0)


# ///////////////////// Paragraph based chunking /////////////////

# import json

# with open("./trac.json",'r') as f:
#     data=json.load(f)

# text ="""
#            I love Python. It is easy to learn.

#            It is used in data science, AI, and web development.
#     """

# def paragraph_chunking(text, chunk_size=2, overlap=1):
#     paragraphs = text.split("\n\n")
    
#     chunks = []

#     text1=text.split("\n\n")
#     for i,par in enumerate(text1,1):
#         print(i)
#         print(par)

# chunks = paragraph_chunking(text, chunk_size=2, overlap=1)



# ///////////////////// Pages by Chunking ////////////////////////

# text = """
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Line 11
# """

# def solve(text):
#     chunk=[]
#     line=text.strip().split("\n")
#     for x in range(0,len(line)-5+1,5):
#         str=line[x:x+5]
#         str1=" ".join(str)
#         print(str1)
#     # print(line)
# solve(text)


# //////////////////// chunk by characters /////////////////

# import json
# text="Python is great for data science."

# def solve(text,chunk,Overlap):
#     step_size=chunk-Overlap
#     chunks=[]

#     for x in range(0,len(text),chunk):
#         str=text[x:x+chunk]
#         # print(str)
#         chunks.append(str)

#     with open("./trac4.json",'w') as f:
#         json.dump(chunks,f,indent=4)    
# solve(text,10,2)


# /////////////// Sliding Window chunking /////////////////////

# import json
# text="I love learning Python because it is easy."

# def solve(text,chunk,overLap):
#     step_size=chunk-overLap
#     text1=text.split()
#     chunks=[]
#     for x in range(0,len(text1)-chunk+1,step_size):
#         str=text1[x:x+chunk]
#         str1=" ".join(str)
#         chunks.append(str1)

#     with open("./trac5.json",'w') as f:
#         json.dump(chunks,f,indent=4)    
        



# solve(text,5,2)

# ///////////////////////// Token Based Chunking /////////////////

import json
import regex as re

def solve(text,chunk,overLap):
    step_size=chunk-overLap
    text1=re.findall(r"\w+|[^\w\s]", text)
    chunks=[]
    for x in range(0,len(text1)-chunk+1,step_size):
        str=text1[x:x+chunk]
        str1=" ".join(str)
        chunks.append(str1)

    with open("./trac6.json",'w') as f:
        json.dump(chunks,f,indent=4)    

# text="Hello how are you?"

import json

with open("./corpus.jsonl", 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

text=data[0]["text"]

solve(text,128,2)
# print(data1)

# words="I love learning Python because it is powerful and easy to use."

# def solve(words,chunk,overlap):
#     str=words.split()
#     step=chunk-overlap
#     res=[]

    
#     for x in range(0,len(str)-overlap,step):
#         str1=str[x:x+chunk]
#         print(str1)

# solve(words,5,2)



# //////////////////////////// Excessing text ////////////////

def solve(text, chunk, overlap):
    words = text.split()
    step_size = chunk - overlap
    for i in range(0, len(words) - chunk+1, step_size):
        chunk_words = words[i:i + chunk]
        print(" ".join(chunk_words))


# import yaml

# with open("./config2.yaml",'r') as f:
#     str=yaml.safe_load(f)

# data=str["text"]

# idx=1
# for val in data:
#     print(f"{idx} :")
#     solve(val,5,2)


# /////////////////////// Sliding Window on Multiple Sentence ////////////////

# texts=[
#     "Hello my name is Sabaz Alam",
#     "I love learning Python",
#     "Let's explore new things every day"
# ]


# for idx,str in enumerate(texts,1):
#     print(f"Text: {idx}")
#     solve(str,3,1)


# ////////////////// Character Based Sliding Window //////////////////////

# def solve(word,chunks,overlap):
#     step_size=chunks-overlap

#     for idx in range(0,len(word)-chunks+1,step_size):
#         text=word[idx:idx+chunks]
#         print(text)

# word="HELLO_WORLD"

# solve(word,5,2)


# ////////////////// Sentence Chunking in words /////////////////////////

# paragraph = "Data Science is fun. Machine Learning is the future. AI is transforming the world."

# sentence=paragraph.split(". ")
# len1=len(sentence)

# for x in range(1,len1,1):
#     print(sentence[x-1]," ",sentence[x])


# /////////////////// Slighting window on array

def solve(nums,chunk,overlap):
    len1=len(nums)
    step_size=chunk-overlap
    for x in range(0,(len1-chunk)+1,step_size):
        subarray=nums[x:x+chunk]
        print(subarray)


nums = [10, 20, 30, 40, 50, 60, 70]
window = 3
step = 1

solve(nums,window,step)
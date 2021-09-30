import json
import random

# some JSON:
with open(r'data.json', 'r', encoding='utf-8') as dt:
    dataQA = json.load(dt)
    cauhoi=False
    cautl=""
    print(dataQA)
    for dataLine in dataQA:
        if type(dataLine["question"]) == list:
            for question in dataLine["question"]:
                if question in "ăn cơm":
                    print('Câu hỏi có Data')
                    cauhoi=True
        else:
            if dataLine["question"] in "ăn cơm":
                print('Câu hỏi có Data')
                cauhoi=True
        if cauhoi==True:
            if type(dataLine["answer"]) == list:
                print(dataLine["answer"])
                size = len(dataLine["answer"])
                num = random.randint(0,size-1)
                cautl = dataLine["answer"][num]
                print(cautl)
                cauhoi=False
            else:
                cautl = dataLine["answer"]
                print(cautl)
                cauhoi=False
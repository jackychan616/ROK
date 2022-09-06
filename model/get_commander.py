import json

def check(words):
    temp = {}
    fp = open("src/commanders.json")
    data = json.load(fp)
    commanders = [list(data)[i].lower() for i in range(len(data))]
    if len(words) <= 1:
        return 
    for i in commanders:
        score = 0
        try:
            for j in range(len(words)):
                if i[j] == words.lower()[j]:
                    score += 1
                    print(i[j])
            if score in temp:
                temp[score].append(i)
            else:
                temp[score] = [i]
        except: pass
    return temp[max(temp)][0]

#done 
''' issus
Alexander nevsky and Alex
''' 
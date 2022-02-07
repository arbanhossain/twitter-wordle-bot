res = []
with open('wordle-answers-alphabetical.txt') as f:
    for line in f:
        res.append(line.strip())
print(res)
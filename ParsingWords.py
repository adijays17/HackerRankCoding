def WordParser(input_lines):
    count = 0
    out = "words\n"
    wordCount = {}
    letterCount =  dict([(chr(i),0) for i in range(97,123)])
    for everyLine in input_lines:
        words = everyLine.split()
        for word in words:
            count += 1
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] = wordCount[word] + 1
        for letter in everyLine:
            if letter is " ":
                continue
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] = letterCount[letter] + 1
    for key in wordCount:
        out = out + key + " " + str(wordCount[key]) +"\n"
    out  = out + "letters\n"
    for key in sorted(letterCount.keys()):
        out = out + key + " " + str(letterCount[key]) +"\n"
    out = str(count) + " \n" + out
    return out

print(WordParser(["test case"]))
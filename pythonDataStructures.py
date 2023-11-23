############### 2D List and Dictionary ###############
myDictionary = {}
index = 0
list = [["a","b","c"],
        ["d","e","f"],
        ["g","h","i"],
        ["j","k","l"],
        ["m","n","o"]]

for i in range(0,len(list),1): 
    for j in range(0,len(list[i]),1): 
        myDictionary[list[i][j]] = index = index+1
        
if "o" in myDictionary:
    myDictionary["o"] = 100 # The value of "o" is now 100
############### 2D List and Dictionary ###############



############### if a list contains ###############
listOfString = ["abc", "ab", "aac", "zsx", "hhc"]
if "abc" in listOfString:
    index = listOfString.index("abc")
    listOfString[index] = "aaa"
############### if a list contains ###############



#################### Substring ####################
boolContains = None
stringBig = "My name is Mohammad"
if "Mohammad" in stringBig:
    boolContains=True
else:
    boolContains=False
#################### Substring ####################



#################### String array ####################
newSentence = ""
sentence = [["I "] , ["go "], ["to "], ["school "], ["at "], ["Texas "]]
for i in range(len(sentence)):
    for j in range(len(sentence[i])):
        newSentence += sentence[i][j]
#################### String array ####################



############### Reverse For Loop ###############
palindromeCheck = None
actualText = "repaper"
tempText = ""
for i in range(len(actualText)-1,-1,-1):
    tempText+=actualText[i]
if tempText == actualText:
    palindromeCheck=True
else:
    palindromeCheck=False
############### Reverse For Loop ###############



# May 8, 2017 - Anagram function

def anagram(word1,word2):
    word1Dict = {}
    word2Dict = {}
    if len(word1) != len(word2):
        print("No, not an anagram!")
    else:
        for letter in word1:
            word1Dict[letter] = 0
            for key in word1Dict.keys():
                word1Dict[key] = word1Dict[key]+1
        for lett in word2:
            word2Dict[lett] = 0
            for key2 in word2Dict.keys():
                word2Dict[key2]=word2Dict[key2]+1
        if word1Dict.keys() != word2Dict.keys():
            print("No, not an anagram!")
        elif word1Dict == word2Dict:
            print("Yes, anagram!")
        else:
            print("No, not an anagram!")
            

anagram("annoy", "annoy")

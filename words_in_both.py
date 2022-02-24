#Name: Lilliana Parra
#Date: 2/23/2022
#Github user: ParraL1
#Description: sees what words are in both strings

def words_in_both(s1, s2):
    words1 = s1.lower().split(" ")
    words2 = s2.lower().split(" ")
    result = []
    for x in words1:
        if (x in words2) and (x not in result):
            result.append(x)
    return result

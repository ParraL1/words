#Name: Lilliana Parra
#Date: 2/23/2022
#Github user: ParraL1
#Description: sees what words are in both strings

def words_in_both(a,b):
    words1 = set(a.lower().spilit())
    words2 = set(b.lower().split())
    return words1.intersection(words2)
    common_words = words_in_both("jack of all trades",'His name is Jack')



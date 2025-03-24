def  is_anagram(word_one, word_two):
  """ This function receives two words and verify if it are an anagram """
    word_one = word_one.lower()
    word_two = word_two.lower()
     if len(word_one) == len(word_two):
        _size = len(word_one)
        for l in range(_size):
            if word_one[:1] == word_two[-1:]:
                word_one = word_one[1:]
                word_two = word_two[:-1]
                
            else:
                break
        return True
             
     return False
     
print(is_anagram("AMOR", "ROMA"))
print(is_anagram("AMA", "AMA"))
print(is_anagram("HORA", "ora"))

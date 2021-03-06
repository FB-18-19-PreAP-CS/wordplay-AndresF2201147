def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if len(word) >= 20:
                    print(word)

def has_no_e(word):
    '''
    >>> has_no_e('texas')
    False
    
    >>> has_no_e('longhorn')
    True
    
    >>> has_no_e('UTEP')
    False
    '''
    if 'e' in word.lower():
        return False
    else:
        return True


def no_e():
    count_e = 0
    count_word = 0
    with open('words.txt') as file:
        for line in file:
            for word in line.split():
                count_word += 1
                if has_no_e(word):
                    count_e += 1
    percent =(count_e / count_word) * 100
    print(f'{percent:.3f}% of words contain "e"')

def avoids(word, letters):
    '''
    >>> avoids('Texas','tpr')
    False
    
    >>> avoids('Texas','bcd')
    True
    
    >>> avoids('LONGHORNS','lgh')
    False
    
    >>> avoids('longhorns','LGH')
    False
    
    >>> avoids('flourbluff','  FL  ')
    False
    '''
    for i in letters.lower():
        if i in word.lower():
            return False
        else:
            pass
    else:
        return True

        
def count_avoids():
    lets = input('Give the exclusion letters: ')
    word_count = 0
    with open('words.txt') as files:
        for line in files:
            for word in line.split():
                if avoids(word, lets):
                    word_count += 1
        print(word_count)
        
def uses_only(word, letters):
    '''
    >>> uses_only('test','ets')
    True
    
    >>> uses_only('longhorns','zyxt')
    False
    
    >>> uses_only('flourbluff','fule')
    False
    
    >>> uses_only('reproachful','acefhlo')
    False
    '''
    for let in word:
        if let not in letters:
            return False
    else:
        return True
    
def words_with_only(letters):
    count_word = 0
    with open('words.txt') as files:
        for line in files:
            for word in line.split():
                if uses_only(word, letters):
                    count_word += 1
        print(count_word)
                
def uses_all(word, letters):
    '''
    >>> uses_all('hello','ha')
    False
    
    >>> uses_all('hello','hl')
    True
    
    >>> uses_all('Texas','t')
    True
    
    >>> uses_all('Texas','tAx')
    True
    
    >>> uses_all('NOveMber','noberz')
    False
    '''
    for i in range(len(letters)):
        if letters[i].lower() not in word.lower():
            return False
    else:
        return True
        
def how_many_uses_all(letters):
    count_word = 0
    with open('words.txt') as files:
        for line in files:
            for word in line.split():
                if uses_all(word,letters):
                    count_word += 1
        print(count_word)

def is_abecedarian(word):
    for let in word:
        pass
    # 'a' < 'b' returns true - so each letter is already assigned to a value :)


if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    #print(avoids('longhorns','LGH'))
    #print(uses_only('test', 'ets'))
    #count_avoids()
    #print(uses_only('reproachful','acefhlo'))
    #how_many_uses_all('aeiou')
    
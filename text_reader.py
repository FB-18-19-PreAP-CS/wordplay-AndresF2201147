def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if len(word) >= 20:
                    print(word)

def no_e():
    count_e = 0
    count_word = 0
    with open('words.txt') as file:
        for line in file:
            for word in line.split():
                count_word += 1
                for i in word:
                    if i == 'e':
                        count_e += 1
    percent = round((count_e / count_word) * 100, 2)
    
    print(f'{percent}% of words contain "e"')

def avoids(word, letters):
    pass
    

if __name__ == "__main__":
    no_e()
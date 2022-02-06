from all_words import all_words

initial_guesses = ["ouija", "fetch", "greed"]

def get_subtracted_list(l):
    res = []
    for i in l:
        if i not in [0,1,2,3,4]:
            res.append(i)
    return res

def guess(guess, word):
    result_tiles = []
    word_list = list(word)
    guess_list = list(guess)
    for i, letter in enumerate(word_list):
        # print(idx)
        if letter in guess_list:
            if word_list.count(letter) > 1:
                if word_list[i] == guess_list[i]:
                    result_tiles.append('G')
                else: result_tiles.append('Y')
            elif guess_list.index(letter) == word_list.index(letter):
                result_tiles.append('G')
            else: result_tiles.append('Y')
        else: result_tiles.append('B')
    return result_tiles

def can_take_word(letter_list, rejected, word, dic):
    for x in rejected:
        if x in word:
            return False
    for x in range(len(letter_list)):
        if letter_list[x] not in word:
            return False
        else:
            if letter_list[x] in dic:
                #print(dic[letter_list[x]])
                if len(dic[letter_list[x]]) == 1:
                    if word.index(letter_list[x]) != dic[letter_list[x]][0]: return False
                else:
                    boolean = False
                    for idx in dic[letter_list[x]]:
                        if word[idx] == letter_list[x]:
                            boolean = True
                    if boolean == False: return False

    return True

def solver(word):
    all_words = aw
    rejected = []
    accepted = []
    guessed = []
    current_guess = ''
    dic = {}
    i = 0
    while True:
        if current_guess == word:
            print("Found word:", current_guess, i)
            return current_guess, i
        all_words = [w for w in all_words if can_take_word(accepted, rejected, w, dic)]
        if current_guess in all_words: all_words.remove(current_guess)
        current_guess = all_words[0]
        if i==0:
            current_guess = initial_guesses[i]
        new_guess = guess(word, current_guess)
        for idx in range(len(new_guess)):
            if new_guess[idx] == 'G':
                dic[current_guess[idx]] = [idx]
                if current_guess[idx] not in accepted: accepted.append(current_guess[idx])
            elif new_guess[idx] == 'Y':
                if current_guess[idx] in dic:
                    if len(dic[current_guess[idx]]) > 1 and idx in dic[current_guess[idx]]: dic[current_guess[idx]].remove(idx)
                else:
                    dic[current_guess[idx]] = [item for item in [0,1,2,3,4] if item!=idx]
                if current_guess[idx] not in accepted: accepted.append(current_guess[idx])
            else:
                if current_guess[idx] not in rejected: rejected.append(current_guess[idx])
        print(dic, i, current_guess, new_guess, accepted, rejected)
        
        i += 1

def valid_word(word, dic):
    for i in range(len(word)):
        if word[i] not in dic[i]: return False
    return True


def sanitize_all_words(wordlist, dic, current_guess, guess_result):
    for i in range(len(current_guess)):
        if guess_result[i] == 'Y':
            if current_guess[i] in dic[i]:
                dic[i].remove(current_guess[i])
        elif guess_result[i] == 'G':
            dic[i] = current_guess[i]
        else:
            for key in dic:
                if current_guess[i] in dic[key]:
                    dic[key].remove(current_guess[i])
    
    for word in wordlist:
        if not valid_word(word, dic):
            wordlist.remove(word)
    return wordlist, dic


def solver2(word, wlist):
    dic = {
        0: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        1: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        2: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        3: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        4: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    }
    guess_count = 0
    current_guess = ''
    while True:
        guess_count += 1
        if current_guess == '': current_guess = initial_guesses[0]
        guess_result = guess(word, current_guess)
        if ''.join(guess_result) == 'GGGGG':
            return current_guess, guess_count
        print(current_guess, guess_result)
        wlist, dic = sanitize_all_words(wlist, dic, current_guess, guess_result)
        current_guess = wlist[0]
        input()

if __name__ == '__main__':
    # guess and word are reversed
    # for word in all_words:
    #     print(solver2(word,all_words.copy()))
    print(solver2("order", all_words.copy()))
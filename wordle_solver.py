from all_words import all_wordle_words as all_words

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
    # for i, letter in enumerate(word_list):
    #     # print(idx)
    #     if letter in guess_list:
    #         print(word_list.count(letter))
    #         if word_list.count(letter) > 1:
    #             print(word_list[i], guess_list[i])
    #             if word_list[i] == guess_list[i]:
    #                 result_tiles.append('G')
    #             else: result_tiles.append('Y')
    #         elif guess_list.index(letter) == word_list.index(letter):
    #             result_tiles.append('G')
    #         else: result_tiles.append('Y')
    #     else: result_tiles.append('B')
    for i in range(len(guess_list)):
        if guess_list[i] == word_list[i]:
            result_tiles.append('G')
        elif guess_list[i] in word_list:
            result_tiles.append('Y')
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
    # print(wordlist)
    for i in range(len(current_guess)):
        if guess_result[i] == 'Y':
            if current_guess[i] in dic[i]:
                dic[i].remove(current_guess[i])
        elif guess_result[i] == 'G':
            dic[i] = [current_guess[i]]
        else:
            for key in dic:
                if current_guess[i] in dic[key]:
                    dic[key].remove(current_guess[i])
    newlist = []
    for word in wordlist:
        if valid_word(word, dic) == True:
            newlist.append(word)
    return newlist, dic

def create_guess(letter_array, wordlist):
    result_array = []
    for word in wordlist:
        for char in word:
            if char not in letter_array: break
    return result_array

def solver2(word, workinglist, initial_guess):
    wlist = workinglist.copy()
    dic = {
        0: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        1: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        2: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        3: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        4: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    }
    guess_count = 0
    current_guess = ''
    steps_array = []
    while True:
        guess_count += 1
        if current_guess == '': current_guess = initial_guess
        guess_result = guess(current_guess, word)
        steps_array.append(guess_result)
        # print(guess_result, steps_array)
        # input()
        if ''.join(guess_result) == 'GGGGG':
            return current_guess, guess_count, steps_array
        wlist, dic = sanitize_all_words(wlist.copy(), dic.copy(), current_guess, guess_result)
        # print(current_guess, guess_result)
        # print(wlist, dic)
        # input()
        dic_one_items = [key for key in dic if len(dic[key]) == 1]
        dic_len_one_items = len(dic_one_items)
        temp_guess = []
        if dic_len_one_items >= 4 and len(wlist) > 1:
            letter_array = [dic[key] for key in dic if len(dic[key]) > 1][0]
            letter_array.extend(dic_one_items)
            letter_array.pop()
            temp_guess = create_guess(letter_array.copy(), workinglist.copy())
        if len(temp_guess) > 0:
            current_guess = temp_guess[0]
        else: current_guess = wlist[0]

def Sort_Tuple(tup): 
      
    # getting length of list of tuples
    lst = len(tup) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 
            if (tup[j][1] > tup[j + 1][1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup

if __name__ == '__main__':
    init = ["adieu"]

    results = []
    morethan6cnt = 0
    for word in all_words:
        i = 0
        guesses = []
        for i in range(len(init)):
            result = solver2( word, all_words.copy(), init[i] )
            guesses.append(result)
        
        guesses = Sort_Tuple(guesses)
        results.append(guesses[0])
        
        # results.append(solver2(word,all_words.copy()))
        if guesses[0][1] > 6:
            morethan6cnt += 1
            print(result)
    print(morethan6cnt)

    # print( solver2( "aback", all_words.copy(), init[0] ) )

    # new_result = [x for x in results if x[1] > 6]
    # print( solver2( "fight", all_words.copy(), init[i] ) )
    # print(guess("ouija", "their"))
# leetcode problem 520.

class detect_capital:
    def detectCapitalUse(self, word):
        count = 0
        flag = False
        if(word[0].isupper()):
            flag = True
        for letter in word[1:]:
            if(letter.isupper()):
                count = count + 1
        if count >= 1:
            flag = False
        if word.isupper() or flag:
            return True
        elif word.islower():
            return True
        else:
            return False


if __name__ == '__main__':
    output = detect_capital("flaG")
    print(output)

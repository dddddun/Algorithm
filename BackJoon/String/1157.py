if __name__ == "__main__":
    word = input().upper()
    word_dict = {string: 0 for string in word}

    for wd in word_dict:
        word_dict[wd] = word.count(wd)

    answer = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)

    if len(answer) == 1:
        print(answer[0][0])
    elif answer[0][1] == answer[1][1]:
        print("?")
    else:
        print(answer[0][0])
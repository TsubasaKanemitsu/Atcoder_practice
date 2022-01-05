n = int(input())

ans = []
for _ in range(n):
    word_num = int(input())
    bigrams = input().split()
    # 文字数がbigrams数より少ないとき
    # 圧縮する
    if word_num < len(bigrams) * 2:
        # 圧縮回数
        comp_num = len(bigrams) * 2 - word_num
        word = ''
        for bigram in bigrams:
            # 圧縮できるときは、圧縮し、できないときは圧縮しない
            if len(word) > 0 and word[-1] == bigram[0] and comp_num > 0:
                word += bigram[1]
                comp_num -= 1
            else:
                word += bigram
    elif word_num > len(bigrams) * 2:
        word = ''.join(bigrams)
        if word[-1] == 'a':
            word += 'b'
        else:
            word += 'a'
    else:
        word = ''.join(bigrams)
    ans.append(word)

for a in ans:
    print(a)
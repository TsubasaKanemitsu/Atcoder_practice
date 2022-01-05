# 鳩ノ巣原理
# やり直し

k = int(input())

# 77...77がKで割り切れるのは何項目なのかという話で
# modを考えればいいのはわかった

# できなかったこと
# 最大の777...がなんぼまでなのかという理論 -> 鳩ノ巣原理らしい
# 漸化式を立式できなかったこと
# 7の項が増えつつKで割りながら見ていくということがどういうことなのかがわかっていなかった。
# -> 項の数が1つ増えるということは、現在の余りの桁が1つあがるということ(×10)
# -> 更に項の数が1つ増えているので、7を足すことになる。

a = 7

for i in range(k + 1):
    a = a % k
    if a == 0:
        print(i + 1)
        exit()
    a = 10 * a + 7
print(-1)
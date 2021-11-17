int_, dec_ = list(input().split('.'))
if 0 <= int(dec_[0]) < 5:
    print(int_)
else:
    print(int(int_) + 1)
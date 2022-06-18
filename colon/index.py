x = 'the quick brown fox jumps over the lazy dog'

print('start|stop|step \n')
print(x[:1:] + '\n' + 't')
print(x[:-1:] + '\n' + 'the quick brown fox jumps over the lazy do')
print(x[1::] + '\n' + 'he quick brown fox jumps over the lazy dog')
print(x[-1::] + '\n' + 'g')
print(x[::1] + '\n' + 'the quick brown fox jumps over the lazy dog')
print(x[::-1] + '\n' + 'god yzal eht revo spmuj xof nworb kciuq eht')

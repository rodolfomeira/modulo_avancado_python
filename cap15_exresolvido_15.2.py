def funcao_fatorial():
    num, fat = 0, 1
    while True:
        yield num, fat
        num += 1
        fat *= num

N = int(input('Digite a quantidade: '))
gen = funcao_fatorial()
for i in range(N):
    print(next(gen))

# remova o comentário desde código e veja o que acontece
#print('\n\nParte 2')
#for ret in funcao_fatorial():
#    print(ret)

print('\nFim do Programa')

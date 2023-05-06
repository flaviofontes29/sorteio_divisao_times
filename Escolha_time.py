import random

nomes = ["nome1","nome2","nome3","nome4","nome5","nome6","nome7","nome8","nome9","nome10","nome11","nome12","nome13","nome14","nome15"]
qtd_times = 3
sorteio = [nomes[i::qtd_times] for i in range(qtd_times)]
random.shuffle(sorteio)
times = list(enumerate(sorteio))
indice = 1
for time in times:
    print(f" Time {indice}: {time[1]}")
    indice +=1
import random

nomes = ["nome1","nome2","nome3","nome4","nome5","nome6","nome7","nome8","nome9","nome10","nome11","nome12","nome13","nome14","nome15"]
qtd_times = 3
random.shuffle(nomes)
separar_times = [nomes[i::qtd_times] for i in range(qtd_times)]

times = list(separar_times)
indice = 1
for time in times:
    print(f" Time {indice}: {time}")
    indice +=1
modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY',
                 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr', 'StELLa']
indices = []
characters = []
temp = []
for index, item in enumerate(modern_family):
    indices.append(index)
    characters.append(item.lower().replace("_", "-"))
    temp.append(len(item))

indices = [sum(i) for i in zip(indices, temp)]
indices.sort(reverse=True)
Phew_finally = {indices[i]: characters[i] for i in range(len(indices))}
print(Phew_finally)

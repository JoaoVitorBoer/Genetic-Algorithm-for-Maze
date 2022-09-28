def remove_espacos(arquivo):
    slice_arquivo = arquivo[1:]
    vet = []
    for linha in slice_arquivo:
        for char in linha:
            if char != ' ':
                if char != "\n":
                    vet.append(char)
    return vet

def cria_matriz(arquivo):
   
    arquivo_fixed = remove_espacos(arquivo)
                    
    tamanho_matriz = int(arquivo[0])
    matriz = []
    while arquivo_fixed != []:
        matriz.append(arquivo_fixed[:tamanho_matriz])
        arquivo_fixed = arquivo_fixed[tamanho_matriz:]

    return tamanho_matriz, matriz
#Verificar a disponibilidade

def verifica(labsala, data, lista_dados):
    for v in lista_dados:
        if v.labsala == labsala and v.data == data:
            return False
    return True
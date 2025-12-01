resultados = {

}
votos_crudos = "candidatoA_30,candidatoB_50,candidatoA_10,candidatoC_20,candidatoB_5"
votos = votos_crudos.split(",")
for i in votos:
    lista_votos = i.split("_")
    candidato = lista_votos[0]
    cantidad = lista_votos[1]
    int_cant = int(cantidad)
    if candidato in resultados:
        resultados[candidato]+=int_cant
    else:
        resultados[candidato] = int_cant
print(resultados)
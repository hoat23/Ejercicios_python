N = int (input("Ingrese el numero de plantas a evaluar:"))
meses = ["enero","febrero","marzo"]
informacion = {}
for i in range(0,N):
    ventas_por_mes = []
    departamento = input("Ingre el departamento donde se ubica la planta: ")
    for mes in meses:
        variable_temporal = float( input("Ingrese las ventas del mes de " + mes + "[S/] :") )
        ventas_por_mes.append( variable_temporal )
    informacion.update( {departamento: ventas_por_mes} )
#Calculando la suma total de cada planta
venta_total_por_planta = {}
for name_planta in informacion:
    suma = 0
    ventas_por_mes = informacion[name_planta]
    for ventas_por_mes in ventas_por_mes:
        suma = suma + ventas_por_mes
    venta_total_por_planta.update( {name_planta:suma} )
#Calculando el promedio, minimo y maximo
planta_vendio_menos = None
planta_vendio_mas = None
suma_total = 0
for key in venta_total_por_planta:
    if planta_vendio_mas==None:
        planta_vendio_mas = key
    if planta_vendio_menos==None:
        planta_vendio_menos = key
    
    if venta_total_por_planta[key]>=venta_total_por_planta[planta_vendio_mas]:
        planta_vendio_mas = key
    if venta_total_por_planta[key]<=venta_total_por_planta[planta_vendio_menos]:
        planta_vendio_menos = key
    suma_total = suma_total + venta_total_por_planta[key]
#Identificando plantas por encima del promedio
promedio = suma_total/len(venta_total_por_planta)
plantas_por_encima_del_promedio = []
for key in venta_total_por_planta:
    if venta_total_por_planta[key]>promedio:
        plantas_por_encima_del_promedio.append(key)
#Mostrando resultado:
print("Promedio de venta de ventas : " + str(promedio))
print("Planta que vendio menos: " + planta_vendio_menos)
print("                     S/: " + str( venta_total_por_planta[planta_vendio_menos] ))
print("Planta que vendio mas  : " + planta_vendio_mas)
print("                     S/: " + str( venta_total_por_planta[planta_vendio_mas]))
print("Plantas por encima del promedio:")
for key in plantas_por_encima_del_promedio:
    print("  " + key + "     S/" + str(venta_total_por_planta[key]) )

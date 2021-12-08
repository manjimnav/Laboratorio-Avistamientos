#-*- coding:utf-8 -*-
'''
Created on 9 dic. 2020

@author: alfonso.bengoa
'''
from ovnis import *


def test_número_avistamientos_de_una_fecha():
    fecha = date(2011,12,26)
    print("\nEl día {} se produjeron {} avistamientos".
          format(fecha,número_avistamientos_en_una_fecha (datos, fecha)))  

def test_número_diferentes_formas_en_estados():
    estados={'nm','pa','in','wa'}
    print ("\nSe observaron {} diferentes formas en los estados: {}".
           format(número_diferentes_formas_en_estados(datos,estados),estados))

def test_duración_total():
    estado='in'
    print ("\nDuración total de los avistamientos en {}: {:,d} segundos".
           format(estado, duración_total (datos, estado)))
    estado='wa'
    print ("Duración total de los avistamientos en {}: {:,d} segundos".
           format(estado, duración_total (datos, estado)))
    
def test_avistamientos_cercanos_coordenada(): 
    ubicación=Coordenada(38.26, -77.18)
    radio=.25
    print ("\nAvistamientos cercanos a {} a menos de {}:\n{}".
           format(ubicación,radio,
                  avistamientos_cercanos_coordenada (datos,ubicación,radio)))

def test_avistamiento_mayor_duración():
    forma="circle"
    print ("\nEl avistamiento en de forma {} de mayor duración es: {} ".
           format(forma,avistamiento_mayor_duración(datos,forma)))
    
def test_avistamientos_entre_fechas():
    fecha1=date(2005,5,1)
    fecha2=date(2005,5,2)
    print("\nAvistamientos entre el {} y el {}:".
      format(fecha1.strftime("%d de %B de %Y"), fecha2.strftime("%d de %B de %Y"))) 
    for a in avistamientos_entre_fechas(datos, fecha1, fecha2):
        print("--->",a)
    
def test_avistamiento_comentario_más_largo_del_año():
    palabra="Object"
    print('\nAvistamiento con la palabra "{}" de cualquier año con el comentario más largo: \n{}'.
          format(palabra,avistamiento_comentario_más_largo_del_año(datos,palabra)))
    año=2009
    print('\nAvistamiento con la palabra "{}" del año {} con el comentario más largo: \n{}'.
          format(palabra,año,avistamiento_comentario_más_largo_del_año(datos,palabra,año)))

def test_duración_total_por_fechas():
    print ("\nDuración por fechas:\n{}".
           format(sorted(list(duración_total_por_fechas(datos).items()))[-5:]))

def test_avistamientos_por_fechas():
    print ("\nAvistamientos por fechas:\n{}".
           format(sorted(list(avistamientos_por_fechas(datos).items()))[-2:]))

def test_formas_por_mes():
    print ("\nFormas por mes:\n{}".
           format(formas_por_mes(datos)))

def test_número_de_avistamientos_por_mes():
    print ("\nNúmero de avistamientos por mes:\n{}".
           format(número_de_avistamientos_por_mes(datos)))

def test_coordenadas_más_avistamientos():
    print ("\nLa coordenada con más avistamiento es: {}".
           format(coordenadas_más_avistamientos(datos)))

def test_horas_con_más_duración_avistamientos():
    n=5
    formas={'circle', 'cylinder', 'triangle'}
    print ("\nLas {} horas con más duración con formas {}: \n{}".
           format(n,formas,horas_con_más_duración_avistamientos(datos,formas,n)))

def test_longitud_media_comentarios_por_estado():
    fecha1=date(2008,1,1)
    fecha2=date(2009,12,31)
    print("\nLongitud media de comentarios por estados entre {} y {}:\n{}".
          format(fecha1,fecha2,
                 longitud_media_comentarios_por_estado(datos,fecha1,fecha2))) 
   

def test_porcentaje_avistamientos_por_forma():  
    print ("\nPorcentaje según las formas:\n{}".
           format(porcentaje_avistamientos_por_forma(datos))) 
    
def test_porcentaje_avistamientos_por_forma_ordenada():  
    print ("\nPorcentaje según las formas:\n{}".
           format(porcentaje_avistamientos_por_forma_ordenada(datos)))
    
def test_avistamientos_mayor_duración_por_estado():
    n=2
    print ("\nLos {} avistamientos de mayor duración en cada estado es:\n{}".
           format(n,avistamientos_mayor_duración_por_estado(datos,n)))

def test_primer_avistamiento_por_forma():
    estado="wa"
    print ("\nEl primer avistamiento de {} ha sido:\n{}".
           format(estado,primer_avistamiento_por_forma(datos,estado)))
#Lectura
datos=lee_avistamientos('../data/ovnis.csv')
print("Número de registros leídos: {:,d}".
      format(len(datos)))
print ("Los 2 primeros registros: {}".
       format(datos[:3]))
print ("Los 2 últimos registros: {}".
       format(datos[-3:]))

# Resto de funciones

#test_número_avistamientos_de_una_fecha()
#test_número_diferentes_formas_en_estados()
#test_duración_total()
#test_avistamientos_cercanos_coordenada()
#test_avistamiento_mayor_duración()
#test_avistamientos_entre_fechas()
#test_avistamiento_comentario_más_largo_del_año()
#test_duración_total_por_fechas()
#test_avistamientos_por_fechas()
#test_formas_por_mes()
#test_número_de_avistamientos_por_mes()
#test_coordenadas_más_avistamientos()
#test_horas_con_más_duración_avistamientos()
#test_longitud_media_comentarios_por_estado()
#test_porcentaje_avistamientos_por_forma()
#test_porcentaje_avistamientos_por_forma_ordenada()
#test_avistamientos_mayor_duración_por_estado()
#test_primer_avistamiento_por_forma()


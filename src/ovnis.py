#-*- coding:utf-8 -*-
'''
@author: alfonso.bengoa
'''

from collections import namedtuple
from datetime import datetime, date
import csv
from math import sqrt

Coordenada = namedtuple("coord","latitud, longitud")
Avistamiento = namedtuple('avistamiento', 'fechahora, ciudad, estado, forma, duración, comentarios, coordenada')

def lee_avistamientos(fichero):
    res=list()
    with open(fichero,"rt", encoding='utf-8') as f:
        lineas=csv.reader(f,delimiter=',')
        next(lineas)
        for l in lineas:
            l[0]=datetime.strptime(l[0],"%m/%d/%Y %H:%M")
            res.append(Avistamiento(l[0],
                                    l[1],
                                    l[2],
                                    l[3],
                                    int(l[4]),
                                    l[5],
                                    Coordenada(float(l[6]),float(l[7])))) 
    return res

def número_avistamientos_en_una_fecha (registros, fecha):
    return len([r.fechahora.date() for r in registros
                if r.fechahora.date()==fecha])

def número_diferentes_formas_en_estados(registros, estados):
    return len({r.forma for r in registros
                if r.estado in estados})

def duración_total (registros, estado):
    return sum(r.duración for r in registros if r.estado==estado)

def avistamientos_cercanos_coordenada (registros,coordenada,radio):
    return [(r.fechahora.date(),r.ciudad,r.estado,r.coordenada) for r in registros
             if distancia(coordenada, r.coordenada)<radio]
  
def distancia(c1, c2):
    return sqrt(pow(c2.latitud-c1.latitud,2) +
                pow(c2.longitud-c1.longitud,2))
    
def avistamiento_mayor_duración(registros,forma):
    lista_aux=[(r.fechahora,r.ciudad,r.duración) for r in registros
                if r.forma==forma]
    return max(lista_aux,key=lambda e:e[2])  


def avistamientos_entre_fechas(registros, fec1=None, fec2=None):
    return sorted([r for r in registros 
                   if  (fec1==None or fec1<=r.fechahora.date()) and 
                       (fec2==None or r.fechahora.date()<=fec2)],
                   key=lambda r:r.fechahora, reverse=True)
    
def avistamiento_comentario_más_largo_del_año (registros,palabra,año=None):
    lista_aux=[r for r in registros 
                if palabra.upper() in r.comentarios.upper() and
                (año==None or año==r.fechahora.date().year)]
    return max(lista_aux,key=lambda e:len(e.comentarios))

def duración_total_por_fechas(registros):
    res=dict()
    for r in registros:
        clave=r.fechahora.date()
        if clave not in res:
            res[clave]=r.duración
        else:
            res[clave]+=r.duración
    return res    


def avistamientos_por_fechas(registros):
    res=dict()
    for r in registros:
        clave=r.fechahora.date()
        if clave not in res:
            res[clave]={r}
        else:
            res[clave].add(r)
    return res


             
def formas_por_mes (registros): 
    meses = ["Enero", "Febrero", "Marzo", 
             "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", 
             "Octubre", "Noviembre", "Diciembre"]
    res=dict()
    for r in registros:
        clave=meses[r.fechahora.date().month-1]
        if clave not in res:
            res[clave]={r.forma}
        else:
            res[clave].add(r.forma)
    return res

def número_de_avistamientos_por_mes(registros): 
    meses = ["Enero", "Febrero", "Marzo", 
             "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", 
             "Octubre", "Noviembre", "Diciembre"]
    res=dict()
    for r in registros:
        clave=meses[r.fechahora.date().month-1]
        if clave not in res:
            res[clave]=1
        else:
            res[clave]+=1
    return res

def coordenadas_más_avistamientos(registros):
    aux=dict()
    for r in registros:
        clave=(int(r.coordenada.latitud),int(r.coordenada.longitud))
        if clave not in aux:
            aux[clave]=1
        else:
            aux[clave]+=1
    
    return max(aux.items(),key=lambda e:e[1])[0]

def horas_con_más_duración_avistamientos(registros,formas,n=3):
    aux=dict()
    for r in registros:
        if r.forma in formas:
            clave=r.fechahora.time().hour
            if clave not in aux:
                aux[clave]=r.duración
            else:
                aux[clave]+=r.duración
    
    return sorted(aux.items(),key=lambda e:e[1], reverse=True)[:n]
   
def longitud_media_comentarios_por_estado(registros, f1=None, f2=None):
    aux=dict()
    for r in registros:
        if ((f1==None or f1<=r.fechahora.date()) and
           (f2==None or r.fechahora.date()<=f2)):
            if r.estado not in aux:
                aux[r.estado]=[len(r.comentarios)]
            else:
                aux[r.estado]+=[len(r.comentarios)]
    res=dict()
    for clave,valor in aux.items():
        res[clave]=sum(valor)/len(valor)
    return res

def porcentaje_avistamientos_por_forma(registros):
    aux=dict()
    for r in registros:
        if r.forma not in aux:
            aux[r.forma]=1
        else:
            aux[r.forma]+=1

    res=dict()
    total_avistamientos=len(registros)
    for clave,valor in aux.items():
        res[clave]=100*valor/total_avistamientos
    return res

def porcentaje_avistamientos_por_forma_ordenada(registros):
    return sorted(porcentaje_avistamientos_por_forma(registros).items())

def avistamientos_mayor_duración_por_estado(registros, límite=3):
    aux=dict()
    for r in registros:
        if r.estado not in aux:
            aux[r.estado]=[(r.fechahora,r.duración,r.ciudad)]
        else:
            aux[r.estado]+=[(r.fechahora,r.duración,r.ciudad)]
    
    res=dict()
    for clave,valor in aux.items():
        res[clave]=sorted(valor,key=lambda e:e[1], reverse=True)[:límite]
    return res

def primer_avistamiento_por_forma(registros, estado=None):
    aux1=dict()
    for r in registros:
        if estado==None or estado==r.estado:
            if r.forma not in aux1:
                aux1[r.forma]=[r]
            else:
                aux1[r.forma]+=[r]
    
    aux2=dict()
    for clave,valor in aux1.items():
        aux2[clave]=min(valor,key=lambda e:e.fechahora)
    return sorted(aux2.items())
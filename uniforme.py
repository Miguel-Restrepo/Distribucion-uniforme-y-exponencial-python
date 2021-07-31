import random
#Dos personas llegan a una estacion de tren siguiendo una distribucion
#unirofme entre las 10:00 a.m. y las 11:00 a.m. de forma independiente
#la una de la otra.
#Se pide calcular la probabilidad de que la primera persona que llegue
#deba de esperar cuanto mucho 10 minutos a la siguiente persona en lllegar

#A~uniforme(0,0,60.0)#el primer cero es el minimo y el 60 es el maximo
#B~uniforme(0,60)+
#P(|A-B|<=10.0)#10 me representa el Maximo de espera

i=0
s=0
while(i<1000000):#Iteramos un millon de veces
    A= 0.0 +((60.0-0.0)*random.random())# el primero cero es el minimo mas el maximo menos el minimo por radon
    B= 0.0+ ((60.0-0.0))*random.random()
    if(0.0<=A-B<=10.0):
        s=s+1
    if(0.0<=B-A<=10.0):
        s=s+1
    i=i+1
print("P(|A-B|<=10.0) = {}".format(str(float(s)/1000000)))

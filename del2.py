# UPORABA --> ./dodatna5b [dolzina bitov] [kodna zamenjava]


import math
import numpy
import sys

l = int(sys.argv[1]) #dolzina bitov za preverjanje
k = 2**l-1-l #Hammingov pogoj
#print(k)
i = k + l # stevilo stolpcev matrike H 
j = l # stevilo vrstic matrike H
M = 2**k #stevilo informacijskih blokov
H = numpy.zeros((j,i))
H = numpy.array(H)
for x in range(2**j):
    b1 = bin(x)[2:]
    l1 = len(b1)
    b1 = str(0) * (j - l1) + b1
    b_arr1 = [int(i) for i in b1]
    if b_arr1 != 0:
        H[:,x-1] = b_arr1

print('\nH=:')
print(H)

print('\nHammingov pogoj:')
print( str((2**i)/(1+i)) + " => " + str(2**k) )
if ((2**i)/(1+i) >= 2**k):
    print("Potreben pogoj,da bi kod popravljal še vse enkratne napake je izpolnjen")
else: 
    print("Enkratne napake se ne dekodirajo pravilno")
    
    
print('\nVse mozne kodne zamenjave:')

# Binarna števila N števk
for x in range(2**k):
    b1 = bin(x)[2:]
    l1 = len(b1)
    b1 = str(0) * (k - l1) + b1 # stevila od 0 do k, prave dolzine

    for y in range(2**l):
        b2 = bin(y)[2:]
        l2 = len(b2)
        b2 = str(0) * (l - l2) + b2
        #kodno zamenjavo pretvorimo v array (*)
        b_arr = [int(n) for n in b2+b1]
        
        prva = numpy.dot(H[0], b_arr)%2
        druga = numpy.dot(H[1], b_arr)%2
        tretja = numpy.dot(H[2], b_arr)%2
        if prva==0:
            if druga==0:
                if tretja==0:
                    print(str(x)+" : " + str(b2) + str(b1))
                    break

input = sys.argv[2] #kodna zamenjava
print("\nVnesli ste kodno zamenjavo: " + input + " ;dolžine " + str(len(input)) + " bit")

input_arr =  [int(i) for i in input]
prva_IN = numpy.dot(H[1,:], input_arr)%2
druga_IN = numpy.dot(H[2,:], input_arr)%2
tretja_IN = numpy.dot(H[3,:], input_arr)%2

if prva_IN==0:
    if druga_IN==0:
        if tretja_IN==0:
            print("V vnesenem zaporedju ni napake!")

for x in range(i):
    if prva_IN == H[1,x]:
        if druga_IN == H[2,x]:
            if tretja_IN == H[3,x]:
                x_napaka = [0,0,0,0,0,0,0]
                for y in range(i):
                    if x == y:
                        x_napaka[y] = 1
                    else: 
                        x_napaka[y] = 0

                x_pravi = [0,0,0,0,0,0,0]
                for z in range(i):
                    if x_napaka[z]==1:
                        if input_arr[z]==1 :
                            x_pravi[z] = 0
                        else:
                            x_pravi[z] = 1
                    else:
                        x_pravi[z] = input_arr[z]
                print("Veljavna kodna zamenjava: ")
                print(''.join(map(str, x_pravi)))
                print("Napaka je na bitu: " + str(x+1))


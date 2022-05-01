#
#  
#  @version 1.0
# 
# Linearni bločni kod. UPORABA --> ./vaja5b [kodna zamenjava]

import math
import numpy
import sys

#H(7,4)
H = ( [1,0,0,0,1,1,1] , [0,1,0,1,0,1,1] , [0,0,1,1,1,0,1] )
H_prva = [1,0,0,0,1,1,1]
H_druga = [0,1,0,1,0,1,1]
H_tretja = [0,0,1,1,1,0,1]

m = 3 # stevilo vrstic matrike H
n = 7 # stevilo stolpcev matrike H 
k = n - m #dolzina koda
l = n - k #dolzina bitov za preverjanje

M = 2**k #stevilo informacijskih blokov

print('\nHammingov pogoj:')
print( str((2**n)/(1+n)) + " => " + str(2**k) )
if ((2**n)/(1+n) >= 2**k):
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
        
        prva = numpy.dot(H_prva, b_arr)%2
        druga = numpy.dot(H_druga, b_arr)%2
        tretja = numpy.dot(H_tretja, b_arr)%2
        if prva==0:
            if druga==0:
                if tretja==0:
                    print(str(x)+" : " + str(b2) + str(b1))
                    break
    
input = sys.argv[1]
print("\nVnesli ste kodno zamenjavo: " + input + " dolžine " + str(len(input)) + " bit")

input_arr =  [int(n) for n in input]
prva_IN = numpy.dot(H_prva, input_arr)%2
druga_IN = numpy.dot(H_druga, input_arr)%2
tretja_IN = numpy.dot(H_tretja, input_arr)%2

if prva_IN==0:
    if druga_IN==0:
        if tretja_IN==0:
            print("V vnesenem zaporedju ni napake!")

for x in range(n):
    if prva_IN == H_prva[x]:
        if druga_IN == H_druga[x]:
            if tretja_IN == H_tretja[x]:
                x_napaka = [0,0,0,0,0,0,0]
                for y in range(n):
                    if x == y:
                        x_napaka[y] = 1
                    else: 
                        x_napaka[y] = 0

                x_pravi = [0,0,0,0,0,0,0]
                for j in range(n):
                    if x_napaka[j]==1:
                        if input_arr[j]==1 :
                            x_pravi[j] = 0
                        else:
                            x_pravi[j] = 1
                    else:
                        x_pravi[j] = input_arr[j]
                        #>>> ' '.join(sentence)
                print("Veljavna kodna zamenjava: ")
                print(''.join(map(str, x_pravi)))
                print("Napaka je na bitu: " + str(x+1))


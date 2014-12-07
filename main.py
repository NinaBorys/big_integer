#! /usr/bin/python3.3
import random
import time
from my_library import *


def main():
    first_hex='2413475dcad12'
    second_hex='aaaff'

    big_int=Big_Int() #init class

    arr1=big_int.transform(first_hex)
    arr2=big_int.transform(second_hex)

    print(first_hex)
    big_int.print_final_arr(arr1)
    print(second_hex)
    big_int.print_final_arr(arr2)


    # # # k=big_int.multiplication_simple(arr1, arr2)

    print("=========== mod ==============")   
    print(big_int.re_tranform(big_int.Barretts_module(arr1,arr2)), 'barrett')
    print(big_int.re_tranform(big_int.remainder_simple(arr1 ,arr2)), 'simple')
    # print("correct result: {}".format(float.hex(float(int(first_hex,16)/int(second_hex,16))) [2:]))   #float
    print("correct result: {}", (hex(int(first_hex,16)%int(second_hex,16)) [2:]))
    print(' ')
   


    # print("===========Division==============")   
    # print(big_int.re_tranform(big_int.division(arr1 ,arr2)))
    # # print("correct result: {}".format(float.hex(float(int(first_hex,16)/int(second_hex,16))) [2:]))   #float
    # print("correct result: {}".format(hex((int(int(first_hex,16)/int(second_hex,16)))) [2:])) 
    # print("correct result: {}".format(((int(int(first_hex,16)/int(second_hex,16)))) )) 
    # print(' ')
   
    # print(big_int.division(arr1,arr2))  
    # print("correct result: {}".format(float.hex(float(int(first_hex,16)/int(second_hex,16))) [2:]))   #works here!)
    #print(float(int(first_hex,16)/int(second_hex,16)))
    

    # print(big_int.re_tranform(big_int.multiplication_simple(arr1,arr2)))
    # print("correct result: {}".format(hex(int(second_hex,16)*int(first_hex,16))[2:]))


    # b=777
    # print(big_int.re_tranform(big_int.mult_on_cell(arr2,b)))
    # print("correct result: {}".format(hex(int(second_hex,16)*b)  [2:]   )   )


    # big_int.print_final_arr(big_int.addittion(arr1, arr2))
    # print(big_int.re_tranform(big_int.addittion(arr1, arr2)))
    # print("correct result: {}".format(hex(int(first_hex,16)+int(second_hex,16))[2:]))

    # big_int.print_final_arr(big_int.substraction(arr1, arr2))
    # print(big_int.re_tranform(big_int.substraction(arr1, arr2)))
    # print("correct result: {}".format(hex(int(first_hex,16)-int(second_hex,16))[2:]))

    # big_int.print_final_arr(big_int.multiplication_karatsuba(arr1, arr2),)
    # print(big_int.re_tranform(big_int.multiplication_karatsuba(arr1, arr2)))
    # print("correct result: {}".format(hex(int(first_hex,16)*int(second_hex,16))[2:]))
    #print("working")
    # now = time.time()

   
    # for i in range(10000):
    #   first = hex(random.randint(10 ** 50,10 ** 70))[2:]
    #   second = hex(random.randint(10 ** 50,10 ** 70))[2:]
    #   if int(second, 16) > int(first, 16):
    #     continue
    #   arr1=big_int.transform(first)
    #   arr2=big_int.transform(second)

    #   result = big_int.re_tranform(big_int.remainder_simple(arr1, arr2))
    #   correct_result = hex(int(first,16)%int(second,16)) [2:]
    #   if result == correct_result:
    #       pass
    #   else:
    #       print ("num1: {0}. num2: {1}. Class answer: {2}. Correct: {3}. Iteration: {4}".format(first,second,result,correct_result,i))
    
    # print("Karatsuba: {}s".format(time.time()-now))

    # now = time.time()
    # for i in range(100):
    #   first = hex(random.randint(0,10))[2:]
    #   second = hex(random.randint(0,1000))[2:]
    #   arr1=big_int.transform(first)
    #   arr2=big_int.transform(second)
    #   result = big_int.re_tranform(big_int.power(arr1, 2))
    #   correct_result = hex(abs(int(first,16)**3))[2:]
    #   if result == correct_result:
    #       pass
    #   else:
    #       print ("num1: {0}. num2: {1}. Class answer: {2}. Correct: {3}. Iteration: {4}".format(first,second,result,correct_result,i))

    # print("Simple: {}s".format(time.time()-now))


if __name__ == '__main__':
    main()
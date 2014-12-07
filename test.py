#! /usr/bin/python3.3
import random

def High_Bit(arr):

    res=0

    int_num = int(re_tranform(arr),16)

    while (int_num!=0):
        int_num>>=1
        res+=1
    return res


    

def print_final_arr( arr):
    print_string=''
    for i in range(0,len(arr),1):
        print_string=str(arr[i])+"   "+print_string

    print(print_string)

def transform(x):
    temp_arr=''
    final_arr = []
    for i in range(len(x)-1,-1,-1):
        if len(temp_arr)==4:
            final_arr.append(temp_arr)
            temp_arr=x[i]
            if i == 0: 
                final_arr.append(temp_arr)
        elif i == 0:
            temp_arr=x[i]+temp_arr
            final_arr.append(temp_arr)
            temp_arr=''
        else:
            temp_arr=x[i]+temp_arr
    for i in range(0,len(final_arr),1):
        final_arr[i]=int(final_arr[i],16)
    return final_arr

def re_tranform(x):
    x = [hex(x[k])[2:] for k in range(len(x)-1,-1,-1)]
    if x[0] == '0' and len(x) > 1:
        x.pop(0)
    for e in range(0,len(x)):
        if len(x[e]) < 4 and e != 0:
            while len(x[e]) < 4: x[e] = '0' + x[e]
    return ''.join(x)

# def shift_right(a, k):
#     a = list(map(lambda x: list(str(x))*5 if x == 0 else list(str(x)) , a))
#     for x in range(k): a[0].insert(0,'0')

#     if len(a[0]) <= 5:
#         while len(a[0]) <= 5:
#             a[0].insert(0,'0')

#     e = 0
#     while True:
#         if e + 1 == len(a) and len(a[e]) > 5:
#             a.append(list())
#         elif e + 1 == len(a)  and len(a[e]) < 5:
#             break
#         while len(a[e]) > 5:
#             a[e+1].insert(0,a[e].pop())
#         e += 1

#     if a[-1] == ['0']: a.pop()

#     return list(map(lambda x: int(''.join(x)), a))

# def shift_left( a, k):
#     a = list(map(lambda x: list(str(x)) , a))
#     for x in range(k): a[-1].append('0')

#     e = len(a) - 1
#     while True:
#         if e == 0 and len(a[e]) > 5:
#             a.insert(0, list())
#             e += 1
#         elif e == 0:
#             break
#         while len(a[e]) > 5:
#             a[e-1].append(a[e].pop(0))
#         e -= 1




#     return list(map(lambda x: int(''.join(x)), a))
def shift_right_with_zeros( a, k):
    a = list(map(lambda x: list(str(x))*5 if x == 0 else list(str(x)) , a))
    for x in range(k): a[0].insert(0,'0')

    if len(a[0]) <= 5:
        while len(a[0]) <= 5:
            a[0].insert(0,'0')

    e = 0
    while True:
        if e + 1 == len(a) and len(a[e]) > 5:
            a.append(list())
        elif e + 1 == len(a)  and len(a[e]) <= 5:
            break
        while len(a[e]) > 5:
            a[e+1].insert(0,a[e].pop())
        e += 1

    if a[-1] == ['0']: a.pop()

    print(list(map(lambda x: int(''.join(x)), a)))

    return list(map(lambda x: int(''.join(x)), a))

def shift_right( a, kkk):
    a = a[::-1]
    hex_num = re_tranform(a)
    num_after = int(hex_num,16) >> kkk
    final_arr = transform(hex(num_after)[2:])

    return final_arr[::-1]


def shift_left( a, kkk):
    a = a[::-1]
    hex_num = re_tranform(a)
    num_after = int(hex_num,16) << kkk
    final_arr = transform(hex(num_after)[2:])

    return final_arr[::-1]


def first_more_than_second( arr1, arr2):       #>

    zero_index=0
    for e in range(0,len(arr1),1):
        if arr1[e] != 0:
            zero_index = e
            break

    if zero_index!=0:
        arr1=arr1[zero_index:]


    if (len(arr1)>len(arr2)):
        return True
    elif (len(arr1)<len(arr2)):
        return False
    else:
        b = False
        for i in range(0,len(arr1),1):
            if arr1[i]>arr2[i]:
                b = True
                break
            elif arr1[i]<arr2[i]:
                break

        if b:
            return True
        else:
            return False


def substraction_stright(arr1,arr2):
    sub_result=[]

    for i in range(0,len(arr1)-len(arr2),1):
        arr2.insert(0,0)

    for i in range(len(arr1)-1,-1,-1):
        if arr1[i]>=arr2[i]:
            sub_result.insert(0,arr1[i]-arr2[i])
        else:
            sub_result.insert(0,arr1[i]+65536-arr2[i])
            arr1[i-1]-=1
    return sub_result

def addittion( arr1, arr2):
    add_result=[]

    if len(arr1)>len(arr2):
        for i in range(0,len(arr1)-len(arr2),1):
            arr2.append(0)
    elif len(arr2)>len(arr1):
        for i in range(0,len(arr2)-len(arr1),1):
            arr1.append(0)

    for i in range(0,len(arr1),1):
        add_result.append(arr1[i]+arr2[i])
    add_result.append(0)
    for i in range(0,len(add_result),1):
        if add_result[i]>65535:
            add_result[i]-=65536
            add_result[i+1]+=1

    zero_index=0
    for e in range(len(add_result)-1,-1,-1):
        if add_result[e] != 0:
            zero_index = e
            break
    if zero_index!=0:
        add_result=add_result[:zero_index+1]

    return add_result

      

def addition_stright(arr1,arr2):
    add_result=[]

    if len(arr1)>len(arr2):
        for i in range(0,len(arr1)-len(arr2),1):
            arr2.insert(0,0)
    elif len(arr2)>len(arr1):
        for i in range(0,len(arr2)-len(arr1),1):
            arr1.insert(0,0)

    for i in range(len(arr1)-1,-1,-1):
        add_result.append(arr1[i]+arr2[i])
    #add_result.insert(0,0)
    for i in range(len(arr1)-1,-1,-1):
        if add_result[i]>65535:
            add_result[i]-=65536
            # print (i,add_result[i])
            # print (add_result[i+1])
            add_result[i+1]+=1
            


    return add_result[::-1]



def substraction( arr1, arr2):

    sub_result=[]

    if len(arr1)>len(arr2):
        for i in range(0,len(arr1)-len(arr2),1):
            arr2.append(0)
    
        for i in range(0,len(arr1),1):
            if arr1[i]>=arr2[i]:
                sub_result.append(arr1[i]-arr2[i])
            else:
                sub_result.append(arr1[i]+65536-arr2[i])
                arr1[i+1]-=1


    elif len(arr2)>len(arr1):
        for i in range(0,len(arr2)-len(arr1),1):
            arr1.append(0)

        for i in range(0,len(arr1),1):
            if arr2[i]>=arr1[i]:
                sub_result.append(arr2[i]-arr1[i])
            else:
                sub_result.append(arr2[i]+65536-arr1[i])
                arr2[i+1]-=1

    else:
        b = False
        for i in range(len(arr1)-1,-1,-1):
            if arr1[i]>arr2[i]:
                b = True
                break
        if b:
            for i in range(0,len(arr1),1):
                if arr1[i]>=arr2[i]:
                    sub_result.append(arr1[i]-arr2[i])
                else:
                    sub_result.append(arr1[i]+65536-arr2[i])
                    arr1[i+1]-=1
        else:
            for i in range(0,len(arr1),1):
                if arr2[i]>=arr1[i]:
                    sub_result.append(arr2[i]-arr1[i])
                else:
                    sub_result.append(arr2[i]+65536-arr1[i])
                    arr2[i+1]-=1

    zero_index=0
    for e in range(len(sub_result)-1,-1,-1):
        if sub_result[e] != 0:
            zero_index = e
            break

    if zero_index!=0:
        sub_result=sub_result[:zero_index+1]

    return sub_result


def mult_on_cell( arr, b):
    mult_on_cell_result=[]

    for i in range(0,len(arr),1):
        mult_on_cell_result.append(arr[i]*b)
    mult_on_cell_result.append(0)
    for i in range(0,len(mult_on_cell_result)-1,1):
        while mult_on_cell_result[i]>65535:
            mult_on_cell_result[i]-=65536
            mult_on_cell_result[i+1]+=1
    if mult_on_cell_result[-1] == 0: mult_on_cell_result.pop()

    return mult_on_cell_result

def shift_right( a, kkk):
    a = a[::-1]
    hex_num = re_tranform(a)
    num_after = int(hex_num,16) >> kkk
    final_arr = transform(hex(num_after)[2:])

    return final_arr[::-1]


def shift_left( a, kkk):
    a = a[::-1]
    hex_num = re_tranform(a)
    num_after = int(hex_num,16) << kkk
    final_arr = transform(hex(num_after)[2:])

    return final_arr[::-1]

def bit_and( a):
    a = a[::-1]
    hex_num = re_tranform(a)
    
    res = int(hex_num,16) & 1


    return res



def multiplication_simple( arr1, arr2):
    temp_result=[]

    for i in range(0,len(arr2),1):
        x=mult_on_cell(arr1, arr2[i])
        if len(x)<(len(arr1)+1): x.append(0) # for all items to have the same length
        temp_result.append(x)


    for i in range(0,len(temp_result)):   # shift
        for j in range(0,i):
            temp_result[i].insert(0,0)
            temp_result[len(temp_result)-1-i].append(0) # 0 in begining


    mul_s_res=temp_result[0]

    for i in range(1,len(temp_result),1):
        mul_s_res = addittion(temp_result[i], mul_s_res)       

    zero_index=0
    for e in range(len(mul_s_res)-1,-1,-1):
        if mul_s_res[e] != 0:
            zero_index = e
            break

    if zero_index!=0:
        mul_s_res=mul_s_res[:zero_index+1]

    return mul_s_res


def Gorners_power(a ,n ):
    result=[1]

    while(re_tranform(n)!='0'):

        if (bit_and(n)):
            result=multiplication_simple(result, a)
            n=substraction(n, [1])
        else:
            a=multiplication_simple(a, a)
            n=shift_right(n, 1)

    return result 



first_hex='11111'
second_hex='a'

arr1=transform(first_hex)
arr2=transform(second_hex)



# print(first_hex)
# print(arr1)
# print_final_arr(arr1)
# print(second_hex)
# print_final_arr(arr2)




t=[1]

re=re_tranform(Gorners_power(arr1,arr2) )
print  (re)

print(hex ( int(first_hex,16)**int(second_hex,16)   ))


# k=(High_Bit(arr1))
# arr1=shift_left(arr1, k)
# print(arr1)


# for i in range(100):
#     first = hex(random.randint(0,1000000000))[2:]
#     second = hex(random.randint(0,100000000))[2:]
#     arr1=transform(first)[::-1]
#     arr2=transform(second)[::-1]
#     result = re_tranform(substraction_stright(arr1, arr2)[::-1])
#     correct_result = hex(abs(int(first,16)-int(second,16)))[2:]
#     #print(result, correct_result)
#     if result == correct_result:
#       pass
#     else:
#       print ("num1: {0}. num2: {1}. Class answer: {2}. Correct: {3}. Iteration: {4}".format(first,second,result,correct_result,i))


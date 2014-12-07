#! /usr/bin/python3.3
import random


class Big_Int(object):
    def __init__(self):
        pass


    def transform(self, x):
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


    def re_tranform(self,x):
        x = [hex(x[k])[2:] for k in range(len(x)-1,-1,-1)]
        if x[0] == '0' and len(x) > 1:
            x.pop(0)
        for e in range(0,len(x)):
            if len(x[e]) < 4 and e != 0:
                while len(x[e]) < 4: x[e] = '0' + x[e]
        return ''.join(x)


    def print_final_arr(self, arr):
        print_string=''
        for i in range(0,len(arr),1):
            print_string=str(arr[i])+"   "+print_string

        print(print_string)


    def addition_stright(self,arr1,arr2):
        add_result=[]

        if len(arr1)>len(arr2):
            for i in range(0,len(arr1)-len(arr2),1):
                arr2.insert(0,0)
        elif len(arr2)>len(arr1):
            for i in range(0,len(arr2)-len(arr1),1):
                arr1.insert(0,0)

        for i in range(len(arr1)-1,-1,-1):
            add_result.append(arr1[i]+arr2[i])
        add_result.append(0)
        for i in range(len(arr1)-1,-1,-1):
            if add_result[i]>65535:
                add_result[i]-=65536
                # print (i,add_result[i])
                # print (add_result[i+1])
                add_result[i+1]+=1  

        add_result=add_result[::-1]
        zero_index=0
        for e in range(0,len(add_result),1):
            if add_result[e] != 0:
                zero_index = e
                break

        if zero_index!=0:
            add_result=add_result[zero_index:]           

        return add_result


    def addittion(self, arr1, arr2):
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

      
    def mult_on_cell(self, arr, b):
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
  

    def multiplication_simple(self, arr1, arr2):
        temp_result=[]

        for i in range(0,len(arr2),1):
            x=self.mult_on_cell(arr1, arr2[i])
            if len(x)<(len(arr1)+1): x.append(0) # for all items to have the same length
            temp_result.append(x)


        for i in range(0,len(temp_result)):   # shift
            for j in range(0,i):
                temp_result[i].insert(0,0)
                temp_result[len(temp_result)-1-i].append(0) # 0 in begining


        mul_s_res=temp_result[0]

        for i in range(1,len(temp_result),1):
            mul_s_res = self.addittion(temp_result[i], mul_s_res)       

        zero_index=0
        for e in range(len(mul_s_res)-1,-1,-1):
            if mul_s_res[e] != 0:
                zero_index = e
                break

        if zero_index!=0:
            mul_s_res=mul_s_res[:zero_index+1]

        return mul_s_res

    def normalize(self, arr):

        for i in range(0,len(arr),1):
            if (i+1)==len(arr):
                arr.append(0)
            while arr[i]>65535:
                arr[i]-=65536
                arr[i+1]+=1

        zero_index=0
        for e in range(len(arr)-1,-1,-1):
            if arr[e] != 0:
                zero_index = e
                break

        if zero_index!=0:
            arr=arr[:zero_index+1]
        return arr  


    def multiplication_karatsuba(self, arr, brr):
        mul_k_res=[]

        # zero_index_a=0
        # zero_index_b=0
        # for e in range(len(arr)-1,-1,-1):
        #     if arr[e] != 0:
        #         zero_index_a = e
        #         break 

        # for e in range(len(brr)-1,-1,-1):
        #     if brr[e] != 0:
        #         zero_index_b = e
        #         break

        
        # if zero_index_a!=0:
        #     arr=arr[:zero_index_a+1]
        # if zero_index_b!=0:
        #     brr=brr[:zero_index_b+1]

                
        if len(arr)==1 and len(brr)!=1:
            mul_k_res=self.mult_on_cell(brr,arr[0])

        elif len(brr)==1 and len(arr)!=1:
            mul_k_res=self.mult_on_cell(arr,brr[0])
            
        elif len(brr)==1 and len(arr)==1:
            mul_k_res.append(arr[0]*brr[0])
            mul_k_res=self.normalize(mul_k_res)

        else: 

            if len(arr)>len(brr):
                for j in range(0,len(arr)-len(brr),1):
                    brr.insert(0,0)
            elif len(brr)>len(arr):
                for j in range(0,len(brr)-len(arr),1):
                    arr.insert(0,0)

            arr_0=[]
            arr_1=[]

            brr_0=[]
            brr_1=[]



            k=int((len(arr)+1)/2)
            
            for i in range(0,k,1):
                arr_0.append(arr[i])
            for i in range(k,len(arr),1):
                arr_1.append(arr[i])

            for i in range(0,k,1):
                brr_0.append(brr[i])
            for i in range(k,len(brr),1):
                brr_1.append(brr[i])

            sum_of_arr1_arr0=self.addittion(arr_1, arr_0)   #a1+a0
            sum_of_brr1_brr0=self.addittion(brr_0 ,brr_1)   #b0+b1

            
            mul_of_sum_of_parts=self.multiplication_karatsuba(sum_of_arr1_arr0,sum_of_brr1_brr0)    #(a1+a0)(b1+b0)

            arr1_on_brr1=self.multiplication_karatsuba(arr_1,brr_1) #a1*b1
            arr0_on_brr0=self.multiplication_karatsuba(arr_0,brr_0) #a0*b0

            sum_of_arr1_on_brr1_and_arr0_on_brr0=self.addittion(arr0_on_brr0, arr1_on_brr1)     #a1*b1+a0*b0 

            part_on_base_k=self.substraction(mul_of_sum_of_parts, sum_of_arr1_on_brr1_and_arr0_on_brr0)     #(a1+a0)(b1+b0)-(a1*b1+a0*b0)
            
            part_on_base_2k=arr1_on_brr1
            
            for i in range(0,k,1):
                part_on_base_k.insert(0,0)

            for i in range(0,2*k,1):
                part_on_base_2k.insert(0,0)

            temp_sum=self.addittion(part_on_base_2k,part_on_base_k)        


            mul_k_res=self.addittion(temp_sum, arr0_on_brr0)


        zero_index=0
        for e in range(len(mul_k_res)-1,-1,-1):
            if mul_k_res[e]!= 0:
                zero_index = e
                break

   
        if zero_index!=0:
            mul_k_res[:zero_index+1]

        return mul_k_res


    def power(self, arr, n):

        if (n==0): return self.mult_on_cell(arr,1)
        if (n==1): return arr
        else:   
            res = arr
            for e in range(n):
                res = self.multiplication_simple(arr,res)

        zero_index=0
        for e in range(len(res)-1,-1,-1):
            if res[e]!= 0:
                zero_index = e
                break
   
        if zero_index!=0:
            res=res[:zero_index+1]
 
        return res


    def first_more_than_second(self, arr1, arr2):       #>=
        x = self.re_tranform(arr1[::-1])
        y = self.re_tranform(arr2[::-1])

        if int(x,16) >= int(y,16):
            return True
        else:
            return False


    def shift_right_with_zeros(self, a, k):
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

        result_array=list(map(lambda x: int(''.join(x)), a))

        for i in range(len(result_array)-1,-1,-1):
            if result_array[i]>65535:
                result_array[i]-=65536
                # print (i,add_result[i])
                # print (add_result[i+1])
                result_array[i-1]+=1  
        return result_array



    def shift_left_with_zeros( self,a, k):
        a = list(map(lambda x: list(str(x)) , a))
        for x in range(k): a[-1].append('0')

        e = len(a) - 1
        while True:
            if e == 0 and len(a[e]) > 5:
                a.insert(0, list())
                e += 1
            elif e == 0:
                break
            while len(a[e]) > 5 :
                a[e-1].append(a[e].pop(0))
            e -= 1


        result_array = list(map(lambda x: int(''.join(x)), a))

        # for i in range(len(result_array)-1,-1,-1):
        #     if result_array[i]>65535:
        #         result_array[i]-=65536
        #         # print (i,add_result[i])
        #         # print (add_result[i+1])
        #         result_array[i-1]+=1  

        return result_array

    def High_Bit(self,arr):

        arr = arr[::-1]
        res=0

        int_num = int(self.re_tranform(arr),16)

        while (int_num!=0):
            int_num>>=1
            res+=1
        return res



    def shift_right(self, a, kkk):
        a = a[::-1]
        hex_num = self.re_tranform(a)
        num_after = int(hex_num,16) >> kkk
        final_arr = self.transform(hex(num_after)[2:])

        return final_arr[::-1]


    def shift_left(self, a, kkk):
        a = a[::-1]
        hex_num = self.re_tranform(a)
        num_after = int(hex_num,16) << kkk
        final_arr = self.transform(hex(num_after)[2:])

        return final_arr[::-1]

    def bit_and(self, a):
        a = a[::-1]
        hex_num = self.re_tranform(a)
        
        res = int(hex_num,16) & 1
  

        return res


    def division(self, arr, brr):
        arr=arr[::-1]
        brr=brr[::-1]
        t=self.High_Bit(brr)
        q=[0]

        while (self.first_more_than_second(arr,brr)):
            k=self.High_Bit(arr)
            c=brr
            c=self.shift_left(c,(k-t))
            while (self.first_more_than_second(c,arr)):
                k=k-1
                c=self.shift_right(c,1)
                  
            temp=[1]
            temp=self.shift_left(temp,(k-t))
            q=self.addition_stright(q, temp)
            arr=self.substraction_stright(arr,c)

        r=arr   
        q=q[::-1]
        
        return q

    def remainder_simple(self, arr, brr):
        arr=arr[::-1]
        brr=brr[::-1]
        t=self.High_Bit(brr)
        q=[0]

        while (self.first_more_than_second(arr,brr)):
            k=self.High_Bit(arr)
            c=brr
            c=self.shift_left(c,(k-t))
            while (self.first_more_than_second(c,arr)):
                k=k-1
                c=self.shift_right(c,1)
                  
            temp=[1]
            temp=self.shift_left(temp,(k-t))
            q=self.addition_stright(q, temp)
            arr=self.substraction_stright(arr,c)

        r=arr   
        r=r[::-1]
        print(r)
        return r


    def Barretts_module(self, x,n):
        r=[]


        b=self.transform('ffff')
        k=int(len(x)/2)

        mu=self.division(self.Gorners_power(b, self.transform(hex(2*k)[2::]))  , n) #GP!!   2*k -try
        # print(x, b,len(x), k,(k-1), hex(k-1), self.Gorners_power(b, self.transform(hex(k-1) [2::] ) ))

        q1=self.division(x, self.Gorners_power(b, self.transform(hex(k-1)[2::] ) ) )

        q2=self.multiplication_simple(mu, q1)

        q3=self.division(q2, self.Gorners_power(b, self.transform(hex(k+1)[2::]) ) )

        q3n=self.multiplication_simple(q3, n)
        
        r=self.substraction(x, q3n)



        while (self.first_more_than_second(r[::-1],n[::-1])):
            r=self.substraction(r,n)


        zero_index=0
        for e in range(len(r)-1,-1,-1):
            if r[e] != 0:
                zero_index = e
                break


        r=r[:zero_index+1]

        print(r)

        return r



    def Gorners_power(self,a ,n ):
        result=[1]

        while(self.re_tranform(n)!='0'):

            if (self.bit_and(n)):
                result=self.multiplication_simple(result, a)
                n=self.substraction(n, [1])
            else:
                a=self.multiplication_simple(a, a)
                n=self.shift_right(n, 1)


        zero_index=0
        for e in range(len(result)-1,-1,-1):
            if result[e] != 0:
                zero_index = e
                break

        result=result[:zero_index+1]

        return result 

    """
        int binpow (int a, int n) {
            int res = 1;
            while (n)
                if (n & 1) {
                    res *= a;
                    --n;
                }
                else {
                    a *= a;
                    n >>= 1;
                }
            return res;
        }
    """


    def substraction_stright(self,arr1,arr2):
        sub_result=[]


        for i in range(0,len(arr1)-len(arr2),1):
            arr2.insert(0,0)

        for i in range(len(arr1)-1,-1,-1):
            if arr1[i]>=arr2[i]:
                sub_result.append(arr1[i]-arr2[i])
            else:
                sub_result.append(arr1[i]+65536-arr2[i])
                arr1[i-1]-=1

        sub_result=sub_result[::-1]
        zero_index=0
        for e in range(0,len(sub_result),1):
            if sub_result[e] != 0:
                zero_index = e
                break

        if zero_index!=0:
            sub_result=sub_result[zero_index:]

        return sub_result

  
   
    def substraction(self, arr1, arr2):

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







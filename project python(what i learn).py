#mini  project

# option
def option():
    print("1)Addition of two number :")
    print("2)Addition of three number :")
    print("3)Addition of n number :")
    print("4)subtraction of two number :")
    print("5)mutliplication of two number :")
    print("6)divition of two number :")
    print("7)power of  number :")
    print("8)odd or even  number check :")
    print("9)print n number with odd even:")
    print("10)student number grade : ")
    print("11)A to Z print : ")
    print("12)n factorial print : ")
    print("13)n fibonacci print : ")
    print("14)n sorting array and max and min element : ")
    print("15)mirron string like abc ->> zyx")
    print("16)string is palindrome or not ?? ")
    print("17)string substring present if present find first occurance ?? ")
    print("18)the number is prime or not ?? ")
    print("19)search item usig binary search ?? ")
    print("20)array operation ")
    print("21)pattern print if n = 3")
    print("\n***\n***\n***")
    print("22)pattern print if n = 3")
    print("\n*\n**\n***")
    print("23)decimal to binary")
    print("24)find total digit summation ?? like 131 ans is 5")
    print("25)Guessing the number GAME")
    print("26)circle redius")
    print("27)leap year check")
    print("28)is it power of 2 check")
    print("click this number : \n")

option()
operator = int(input())

match operator:
    case 1:
        a = int(input("enter a : "))
        b = int(input("enter b : "))
        print("a + b  = ",a+b)
           
    case 2:
        a = int(input("enter a : "))
        b = int(input("enter b : "))
        c = int(input("enter c : "))
        print("a + b + c = ",a+b+c)
    
    case 3:
        num = []
        n = int(input("enter n "))

        for i in range(0,n): 
            val = int(input("value :"))
            num.append(val)

        sum = 0 

        for i in num: 
            sum+=i
    
        print(sum)
    
    case 4:
        a = int(input("enter a : "))
        b = int(input("enter b : "))
        print("a - b  = ",a-b)
        
    case 5:
        a = int(input("enter a : "))
        b = int(input("enter b : "))
        print("a * b  = ",a*b)
    
    case 6:
        a = int(input("enter a : "))
        b = int(input("enter b : "))
        print("a / b  = ",a/b)
    case 7:
        base = int(input("enter base :"))
        power = int(input("enter poewer :"))
        ans = base**power
        print("a^b is :  ",ans)
    case 8:
        a = int(input("enter a : "))
        if(a%2==0):
            print("EVEN NUMBER")
        else :
            print("ODD NUMBER")
    case 9:
        listeven =[]
        listodd = [] 
        listnum = []
        n = int(input("enter n : "))
        for i in range(1,n+1):
            listnum.append(i)
            if(i%2==0):
                listeven.append(i)
            else :
                listodd.append(i)
    
        print("1 to n number is : ",listnum)
        print("1 to n odd number is : ",listodd)
        print("1 to n even number is : ",listeven)
        
    case 10 :
        n = int(input("enter student number : "))
        if(n>=80):
            print("A+")
        elif(n>=70):
            print("A")
        elif(n>=60):
            print("A-")
        elif(n>=50):
            print("B")
        elif(n>=40):
            print("C")
        else:
            print("F")
            
    case 11:
        ch = 65
        for i in range(0,26):
            print(chr(ch),end="  ")
            ch = ch+1
            
    case 12:
        def fact(n):
            if (n==1 or n==0):
                return 1
            ans = n*fact(n-1)
            return ans 


        n = int(input("enter n :"))
        ans = fact(n)
        print("ans  =  ",ans)
        
    case 13:
        def fibo (n):
            if(n==1):
              return 0
            elif(n==2):
              return 1
            else:
                return fibo(n-1)+fibo(n-2)
            print(n,end=" ")
    

        n = int(input("enter n :"))

        for i in range(1,n+1):
           print(fibo(i),end=" ")
    
    case 14:
        
        lst = []
        n = int(input("enter n : "))
        for _ in range(n):
            val = int(input("enter val"))
            lst.append(val)  
        print("Assending Order")
        lst.sort()
        print (lst)
        
        print("Dessending Order")
        for i in range(0,n):
            print(lst[n-i-1])
            
        print("MAX value is = ",lst[n-1])
        print("MIN value is = ",lst[0])
        
    case 15:
        
        s = input("inpur the string : ")
        alpha = "abcdefghijklmnopqrstuvwxyz"
        revalpha = alpha[::-1]
        dic = dict(zip(alpha,revalpha))
        ans = ""
        for i in range(0,len(s)):
           ans+=dic[s[i]]
        print("mirror strig is :",ans)
    
    case 16:
        s = input("inpur the string : ")
        revs = s[::-1]
        if(s==revs):
            print("string are plaindrome")
        else :
            print("string are not palidrome")
    
    case 17:
        s = input("inpur the string : ")
        sub = input("inpur the substring : ")
        ans = s.find(sub)
        if(ans==-1):
            print("not present in the stirnger")
        else :
            print("present in the string")
            print("frist occurance index is : ",ans)
    case 18 : 
        
        def isprime(n):
            
            p = n
            for i in range(2,int(n**(0.5))+5) :
                if (p%i==0):
                    return 0
                    
            return 1
        n =int(input("enter n : "))
        if(isprime(n)==1):
            print("prime number  ")
        else :
            print("not prime number ")
            
    case 19 :
        def binary_search(lis,s,e,item):
            while(s<=e): 
                mid = int((s+e)/2)
        #print("mid = ",mid)
                if(lis[mid]==item):
                    return 1
                elif(lis[mid]>item):
                    e = mid-1
                else:
                    s = mid+1 
        
            return 0
    
        lis = []

        n = int(input("enter the element number "))

        for i in range(0,n):
            val = int(input("enter value : "))
            lis.append(val)

#print(lis)

        item = int(input("enter the element which you want search in the array: "))
        s = 0
        e = n-1
        ans = binary_search(lis,s,e,item)
        if(ans==1):
            print("YES FIND THIS ITEM")
        else:
            print("NO FIND")
    
    case 20 :
        lis = []
        n = int(input("enter the element"))
        for i in range(0,n):
            val = int(input("enter value : "))
            lis.append(val)       
        print("what are you want ??")
        print("1)if you want delete one element")
        print("2)if you want add one element")
        q = int(input("enter 1 or 2 :"))
        if(q==1):
            item = int(input("enter the item"))
            print("before remove :")
            print(lis)
            list.remove(item)
            print("after remove : ")
            print(lis)
        elif(q==2):
            item = int(input("enter the item"))
            ind = int(input("enter the ind"))
            print("before adding element :")
            print(lis)
            lis.insert(ind,item)
            print("after adding element :")
            print(lis)
        else :
            print("INVALID INPUT :}")
    case 21:
        n = int(input("enter n "))
        for i in range(0,n):
            for j in range(0,n):
                print(" * ",end=" ")
            print("\n")   
    case 22:
        
        n = int(input("enter n "))
        for i in range(0,n):
            for j in range(0,i+1):
                print(" * ",end=" ")
            print("\n")  
    
    case 23:
        n = int(input("enter n "))
        lis = []
        while(n>0):
            rem = n%2
            lis.append(rem)
            n = n//2
    

        sz = len(lis)
        print("n binary is  : ",end="  ")
        for i in range(0,len(lis)):
            print(lis[sz-i-1],end="")
            
    case 24 :
        n = int(input("enter n "))
        ans = 0 
        while(n>0):
            ans = ans+(n%10)
            n = n//10
    
        print("total digit summation is : ",ans)
    case 25 :
        lis = [1,4,9,7,10]  
        done = 0
        n = int(input("enter 1 to 10  any number "))  
        for i in range(0,len(lis)):
            if(lis[i]==n):
                print("YOU WIN")
                done = 1
        if(done==0):
            print("YOU LOSE")
    case 26:
        r = int(input("enter circle redius  : "))
        ans  = float(3.1416*r*r)
        print("Circle redius is : ",ans)
    case 27 :
        n = int(input("enter year :"))
        if(n%400 == 0 or(n%100!=0 and n%4==0)):
            print("YES LEAP YEAR")
        else :
            print("NOT LEAP YEAR")
    
    case 28:
        n = int(input("enter n "))
        lis = []
        while(n>0):
            rem = n%2
            lis.append(rem)
            n = n//2
    
        #print(lis)
        sz = len(lis)
        
        cnt = 0
        for i in range(0,len(lis)):
            if(lis[i]==1):
                cnt = cnt+1
        if(cnt ==1):
            print("POWER OF 2")
        else :
            print("NOT POWER OF 2")
            
    case _:
        print("INVLID INPUT  :}")
        
 
    
    
        
        



print("Never Give up!!")
def greeting():
    print("Hello ullas , welcome to python !!")
greeting()
------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sum(a,b):
    print(f"the sum of {a} and {b} is : {a+b}")
sum(10,20)
--------------------------------------------------------------------------------------------------------------------------------------------------------
def even_odd():
    a=int(input("Enter the number : "))
    if a%2==0:
        print(f"the {a} is even number")
    else:
        print(f"the {a} is odd ")
even_odd()
----------------------------------------------------------------------------------------------------------------------------------------------------------
def count_vowel(s):
    count=0
    for i in s:
      if i in "aeiouAEIOU":
         count+=1
    return count

s=str(input("Enter the string : "))
result=count_vowel(s)
print("number of vowels is  :",result)




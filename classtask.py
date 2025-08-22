''''prices=[120,250,300,150,200]
sum=0
for price in prices:
    sum+=price
print("sum of prices =",sum)
'''

''''lst1=[10,25,30,47,52,61]
count_even=0 
count_odd=0
even_lst=[]
odd_lst=[]
for num in lst1:
   if num%2==0:
      even_lst+=[num] #even_lst=even_lst+[num]
      count_even+=1
   else:
      odd_lst+=[num]
      count_odd+=1
print(count_even,even_lst)
print(count_odd,odd_lst)
      '''
            

''''pass_word="admin@123"
user_name="admin"
for i in range(3):
     user_input=input("enter the password:")  
     user_input1=input("enetr the username: ")
     if pass_word==user_input and user_name==user_input1 :
         print("Access granted")
         break 
     else:
          print('Try again' )
else:   
     print("Locked out")'''

''''seat_numbers=[5,25,13,15,27,55,11,30]
for num in seat_numbers:
    if num%3==0 and num%5==0:
        print("discount of 100 to",num, "seatnumber:",discount)'''

''''items = ["apples", "banana", "caps", "capsicums", "bread", "onions"]

item = input("Enter the item: ").lower()

if item in items:
    print("Item is available")
else:
    print("Not available")'''

items = ["apples", "banana", "caps", "capsicums", "bread", "onions"]
item = input("Enter the item: ").lower()
for i in items:
    if i == item:
        print("item is available")
        break
else:
    print("not available")


    




  
        






    
    



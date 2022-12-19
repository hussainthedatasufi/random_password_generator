import random
values_password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()+>?:{}"
length_password=int(input("Enter the length of the desired password"))
rand_password="".join(random.sample(values_password,length_password))
print("Your Password is : ",rand_password)
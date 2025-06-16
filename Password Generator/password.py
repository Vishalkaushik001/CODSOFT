import string 
import random 
total = string.ascii_letters + string.digits + string.punctuation 
length = 10
password = "".join(random.sample(total , length))
print(password)

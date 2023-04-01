import random
import string


symbols = "£$%^&**"
length = 16
source = string.ascii_letters + string.digits + symbols
password = "".join(random.sample(source,length))
print("Your new random password is: " + password)


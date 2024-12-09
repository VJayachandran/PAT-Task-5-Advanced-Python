import re
#validate Email address
email_address = "Jayachandran_90@gmail.com"

def validate_email_address(data):
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"
    if re.match(pattern, data):
        return True
    else:
        return False

print("Validate Email  : ", validate_email_address(email_address))
#validate Bangladesh Mobile number
data = "1512345678"
#code = "+880"
def validate_Bangladeshi_mobile_number(number):
    pattern = r"^[1789]\d{9}$"
    if re.match(pattern, data):
        return True
    else:
        return False
print("Validate Mobile Number: ", validate_Bangladeshi_mobile_number(data))

#validate America TelePhone number
Phone = "4855558789"
#code = "+1"
def validate_American_Telephone_number(number):
    pattern = r"^[145789]\d{9}$"
    if re.match(pattern, Phone):
        return True
    else:
        return False
print("Validate Telephone Number: ", validate_American_Telephone_number(Phone))



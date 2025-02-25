import re

password = input("Şifrenizi giriniz: ")

pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"


def check_password(password):
    # pattern neyi kontrol ediceğini belirler
    # password kontrol edilecek şifre
    # bu kod şifrenin gücünü belirler
    if re.match(pattern, password): 
        print("Stronger Password")
    else:
        print("Weak Password")
    
check_password(password)
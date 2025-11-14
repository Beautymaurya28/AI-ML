#convert into temperature
#celcius to kelvin
#celcius to fahrenheit\

def cal_to_fahr(c):
    return (c*9/5)+32
def cal_to_kel(c):
    return c+273.15
 
temp=25
print(cal_to_kel(temp))
print(cal_to_fahr(temp))

    
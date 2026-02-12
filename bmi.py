def get_user_input():
    weight=float(input("enter your weight(kg):"))
    height=float(input("enter your height(m):"))
    return weight,height
def calculat_bmi(weight,height):
    return weight//(height**2)

def get_bmi_result(bmi):
    if bmi < 18.5:
        print("you have under weight.")
    elif 18.5 < bmi <25:
        print("you are normal.")
    elif 25 < bmi < 30:
        print("you are Overweight")
    elif 30 < bmi <35:
        print("you are fat.")
    else:
        print("you are very fat")

def main():
    weight,height=get_user_input()
    bmi=calculat_bmi(weight,height)
    get_bmi_result(bmi)
if __name__=="__main__":
    main( )
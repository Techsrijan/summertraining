try:  # risky code 
    a=int(input("enetr any number"))
    b=int(input("enetr any number"))

    d=a/b
    print("div=",d)


except  ValueError:
    print("You have enetrd a character")

except  ZeroDivisionError:
    print("b cant be zero")

except Exception:
    print("hum to sabke papa hi sab solve kar lenege")


finally:  # always executes
    print("thank u")
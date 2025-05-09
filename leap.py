year = int(input("Enter year:"))

def is_leap(year) -> bool:
    if(year % 4) ==0:
        #If it's divisible by 4 and also by 100 do this tests
        if (year % 100) ==0:
            #If it's divisible by 4, 100 and 400 it's a leap year
            if (year % 400) ==0:
                leap_year = True
                #If it's divisible by 4, 100 and not 400 -> not leap
            else:
                leap_year = False
            #If it's divisible by 4 only -> not leap
        else:
            leap_year = True
    else:
        leap_year =False

# Call the function and print the result
if is_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
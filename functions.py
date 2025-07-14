# WAP to find how many days you have left till age 90 


def life_in_weeks(age = int(input("what is your age :"))):
    weeks_in_a_year = 1
    years_left= 0
    for life in range(age,90):
        years_left += 1
    weeks_left = years_left * weeks_in_a_year
    print(f"You have {weeks_left} year left. ")
    
        
life_in_weeks()

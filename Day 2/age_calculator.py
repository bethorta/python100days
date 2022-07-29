# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
years_remaining = 90 - int(age) 
#print (years_remaining) 
days = years_remaining *365
#print(days)
weeks = years_remaining * 52 
months = years_remaining * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left." )
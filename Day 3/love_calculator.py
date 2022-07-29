# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
combined_names = name1 + name2
lower_name = combined_names.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e
l= lower_name.count("l")
o= lower_name.count("o")
v= lower_name.count("v")
e= lower_name.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if score <10 or score >90: 
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50: 
    print(f"Your score is {score}, you are alright together.")
else: print(f"Your score is {score}.")
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

love = name1.lower() + name2.lower()



(love.count('t'))
(love.count('r'))
(love.count('u'))
(love.count('e'))

first_total = (love.count('t')) +(love.count('r')) + (love.count('u')) + (love.count('e'))

(love.count('l'))
(love.count('o'))
(love.count('v'))
(love.count('e'))

second_total = (love.count('l')) + (love.count('o')) + (love.count('v')) + (love.count('e'))

love_score = str(first_total) + str(second_total)
total_love_score = int(love_score)

if total_love_score < 9 or total_love_score > 90:
    print(f"Your score is {total_love_score}, you go together like coke and mentos.")

elif total_love_score >= 40 and total_love_score <= 50:
    print(f"Your score is {total_love_score}, you are alright together.")

else:
    print(f"Your love score is {total_love_score}.")
    


# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

#  Angela Yu
#  Jack Bauer
#  should be nothing, just  score of 53

#  Kanye West
#  Kim Kardashian
#  your alright together score of 42

#  Catherine Zeta-Jones
#  Michael Douglas
#  great score of 99
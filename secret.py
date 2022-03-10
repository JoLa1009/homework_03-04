# homework 1.2: Guess the secret number

import random, json, datetime
secret = random.randint(1,30)
attempts = 0
wrong_guess = []

player = input("Please enter your name: ")
print()

with open("score_list.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores:")
    for score_dict in score_list:
        print(str(score_dict["name"]) +": " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
print()

while True:
    guess = int(input("Choose a number between 1 and 30! "))
    attempts += 1
    if guess != secret:
        wrong_guess.append(guess)
        print("Sorry! You haven't found the secret number!")
        if guess < secret:
            print("The secret number is bigger. Try it again!")
        else:
            print("The secret number is smaller. Try it again!")
    else:
        print("Congratulations! You have found the secret number! It is " + str(secret) + "!")
        score_data ={"attempts": attempts, "date": str(datetime.datetime.now()), "name": player,
                     "secret number":str(secret), "wrong guesses": wrong_guess}
        score_list.append(score_data)

        from operator import itemgetter
        score_list.sort(key=itemgetter("attempts"))
        score_list.pop(3)


        with open("score_list.txt","w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Attempts needed: "+ str(attempts))
        print("Wrong guesses: " + str(wrong_guess))
        break
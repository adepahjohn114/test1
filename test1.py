current_users = ['john', 'mary', 'alex', 'anna', 'tom']
new_users = ['Alex', 'sarah', 'mike', 'John', 'emily']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, {user} is already taken. Please enter a new username.")
    else:
        print(f"Congratulations, {user} is available!")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

# Exercise 1 
for num in range(1, 11):
    print(num ** 3)

for num_cubed in (num ** 3 for num in range(1, 11)):
    print(num_cubed)
                            #not sure which one would be best 



# Exercise 2 
for num in range(1, 101):
    counter = 0
    for num2 in range(1, 101):
        if num % num2 == 0:
            counter += 1
    if counter == 2:
        print(num)



# Exercise 3
go_again = True
while go_again:
    age = input("Enter your age: ")
    
    while age.isalpha():
        print("Enter a numerical value...")
        age = input("Enter your age: ")
    
    if age < '18':
        print("Kids")
    
    elif age >= '18' and age <= '65':
        print("Adults")
    
    else:
        print("Seniors")
    
    run_again = input("Would you like to enter another age? (Y/N): ")
    
    while run_again.upper() not in ['Y', 'N']:
        print("Enter Y to go again or N to terminate...")
        run_again = input("Would you like to enter another age? (Y/N): ")
    
    if run_again.upper() == 'N':
        go_again = False
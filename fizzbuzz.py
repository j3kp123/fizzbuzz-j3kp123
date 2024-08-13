## Iterate through numbers from 0 to 100 using the range function
for fizzbuzz in range(101):
    # Check if the number is divisible by both 3 and 5
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        # If divisible by both 3 and 5, print "fizzbuzz" 
        print("fizzbuzz")
        continue
    # Check if the number is divisible only by 3
    elif fizzbuzz % 3 == 0:
        # If divisible only by 3, print "fizz"
        print("fizz")
        continue
    # Check if the number is divisible only by 5
    elif fizzbuzz % 5 == 0:
        # If divisible only by 5, print "buzz"
        print("buzz")
        continue
    # If the number is neither divisible by 3 nor 5, print the number
    print(fizzbuzz) 

 


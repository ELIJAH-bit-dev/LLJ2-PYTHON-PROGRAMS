def is_prime(n): 
if n <= 1: 
return False   
if n == 2: 
return True   
if n % 2 == 0: 
        return False   
    for i in range(3, int(n**0.5) + 
1, 2): 
        if n % i == 0: 
            return False   
    return True   
def main(): 
    try: 
        num = int(input("Enter a 
number to check if it's prime: 
")) 
        if is_prime(num): 
print(f"{num} is a prime 
number.") 
else: 
print(f"{num} is not a 
prime number.") 
except ValueError: 
print("Invalid input! 
Please enter a valid integer.") 
if __name__ == "__main__": 
main() 
def calculate_sum(n): 
return n * (n + 1) // 2  
def print_pattern(n): 
for i in range(1, n + 1): 
for j in range(1, i + 1): 
print(j, end=" ")   
print()   
if __name__ == "__main__": 
n = int(input("Enter a 
natural number (n): ")) 
     
    if n <= 0: 
        print("Please enter a 
positive integer.") 
    else: 
         
        total_sum = 
calculate_sum(n) 
        print(f"The sum of the 
first {n} natural numbers is: 
{total_sum}") 
         
        print("\nPattern:") 
print_pattern(n) 
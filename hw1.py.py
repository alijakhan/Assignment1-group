#User search for “near misses”
#hw1.py
#Date 20-09-2024
#Names of the programers: Ali Ajaz Khan Mohammed and Radhavaram Harini
#email adress: aliajazkhanmohammed04@gmail.com
#email adress: Hariniradhavaram@lewisu.edu
#roll numbers: Ali Ajaz Khan Mohammed(L30093968) 
#roll numbers: Radhavaram Harini(L30094111) 
#Course is software engineering in person

def findnearmisses(n, k):
    smallest_relative_miss = float('inf')
    best_combination = None

    #Here we are Iterate through all combinations
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            sum_power = x**n + y**n
            
            # Here we are Finding the z 
            z = int(round(sum_power ** (1/n)))
            
            # Here we are Calculating 
            zn = z**n
            z1n = (z + 1)**n
            
            # Here we are Determining which is closer to sum_power
            if zn < sum_power < z1n:
                miss = min(abs(sum_power - zn), abs(z1n - sum_power))
                relative_miss = miss / sum_power
                
                if relative_miss < smallest_relative_miss:
                    smallest_relative_miss = relative_miss
                    best_combination = (x, y, z, miss, relative_miss)
                    print(f"New smallest relative miss found: x={x}, y={y}, z={z}, "
                          f"actual miss={miss}, relative miss={relative_miss:.6f}")

    return best_combination

def main():
    print("Fermat's Last Theorem Near Miss Finder")
    
    # Here we are taking User input
    n = int(input("Enter a value for n (2 < n < 12): "))
    while n <= 2 or n >= 12:
        print("Invalid input. Please enter a value for n (2 < n < 12): ")
        n = int(input())
    
    k = int(input("Enter a value for k (k > 10): "))
    while k <= 10:
        print("Invalid input. Please enter a value for k (k > 10): ")
        k = int(input())
    
    # Here we are Finding near misses
    best_combination = findnearmisses(n, k)
    
    if best_combination:
        x, y, z, miss, relative_miss = best_combination
        print(f"\nFinal smallest relative miss: x={x}, y={y}, z={z}, "
              f"actual miss={miss}, relative miss={relative_miss:.6f}")
    else:
        print("No near misses found.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time, n):
    compound_amount = principal * (1 + (rate / (n * 100))) ** (n * time)
    compound_interest = compound_amount - principal
    return compound_interest

def main():
    print("Welcome to the Interest Calculator")
    
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    n = int(input("Enter the number of times interest is compounded per year: "))

    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"\nSimple Interest Calculation:")
    print(f"Principal Amount: {principal:.2f}")
    print(f"Rate of Interest: {rate:.2f}%")
    print(f"Time Period: {time:.2f} years")
    print(f"Simple Interest: {simple_interest:.2f}")


    compound_interest = calculate_compound_interest(principal, rate, time, n)
    compound_amount = principal + compound_interest
    print(f"\nCompound Interest Calculation:")
    print(f"Principal Amount: {principal:.2f}")
    print(f"Rate of Interest: {rate:.2f}%")
    print(f"Time Period: {time:.2f} years")
    print(f"Times Compounded per Year: {n}")
    print(f"Compound Interest: {compound_interest:.2f}")
    print(f"Total Amount after {time} years: {compound_amount:.2f}")

if __name__ == "__main__":
    main()

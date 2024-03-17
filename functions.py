def fibonacci(n):
    """3
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 1:
        return [n]  # Base case: return [0] for n=0 and [0, 1] for n=1
    else:
        fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two terms
        a, b = 0, 1  # Initialize variables for Fibonacci sequence
        for _ in range(2, n + 1):
            c = a + b  # Calculate the next Fibonacci number
            fib_sequence.append(c)
            a, b = b, c  # Update variables for next iteration
        return fib_sequence

def main():
    # Get the number of terms from the user
    num_terms = int(input("Enter the number of terms: "))
    
    # Generate the Fibonacci sequence
    fibonacci_sequence = fibonacci(num_terms)
    
    # Print the Fibonacci sequence
    print("Fibonacci sequence up to term", num_terms, ":")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()

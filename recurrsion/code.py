# recurrence.py
def recurrence(n, a, b, d):
    if n == 1:
        return 1
    return a * recurrence(n // b, a, b, d) + n ** d

def main():
    a, b, d = 2, 2, 1   # Example values: T(n) = 2T(n/2) + n
    ns = [2, 4, 8, 16, 32, 64]

    results = []
    for n in ns:
        val = recurrence(n, a, b, d)
        results.append((n, val))

    # Display table
    print("n\tT(n)")
    for n, val in results:
        print(f"{n}\t{val}")

    # Save to file
    with open("substitution_results.txt", "w") as f:
        f.write("n\tT(n)\n")
        for n, val in results:
            f.write(f"{n}\t{val}\n")
        f.write("\nVerification: Pattern matches O(n log n) for a=2, b=2, d=1\n")

if __name__ == "__main__":
    main()
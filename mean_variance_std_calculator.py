import numpy as np

def calculate_statistics(data):
    """Function to calculate the mean, variance, and standard deviation of a dataset."""
    mean = np.mean(data)
    variance = np.var(data)
    std_dev = np.std(data)
    
    return mean, variance, std_dev

def main():
    # Input: A list of numbers
    data = input("Enter a list of numbers (comma-separated): ")
    data = list(map(float, data.split(',')))  # Convert input string to a list of floats
    
    # Calculate statistics
    mean, variance, std_dev = calculate_statistics(data)
    
    # Output results
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

if __name__ == "__main__":
    main()

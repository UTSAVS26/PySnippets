# Statistics and Probability Module: statistics_operations.py

def mean(data):
    """Returns the mean of the data."""
    return sum(data) / len(data)

def median(data):
    """Returns the median of the data."""
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    if len(sorted_data) % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def mode(data):
    """Returns the mode of the data."""
    frequency = {}
    for number in data:
        frequency[number] = frequency.get(number, 0) + 1
    mode_value = max(frequency, key=frequency.get)
    return mode_value

def standard_deviation(data):
    """Returns the standard deviation of the data."""
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return variance ** 0.5

def variance(data):
    """Returns the variance of the data."""
    avg = mean(data)
    return sum((x - avg) ** 2 for x in data) / len(data)

def random_normal_samples(mean, std_dev, size):
    """Generates random samples from a normal distribution (simple method)."""
    samples = []
    for _ in range(size):
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)
        z0 = (-2 * math.log(u1)) ** 0.5 * math.cos(2 * math.pi * u2)
        samples.append(z0 * std_dev + mean)
    return samples

# Example usage
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
    print("Standard Deviation:", standard_deviation(data))
    print("Variance:", variance(data))

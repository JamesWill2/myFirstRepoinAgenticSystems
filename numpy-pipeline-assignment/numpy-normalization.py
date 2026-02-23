import numpy as np


def main():
    #create NumPy array
    data = np.array([40, 50, 60, 70])

    #find mean and std
    mean = np.mean(data)
    std = np.std(data)

    #Data Normalization
    normalized = (data - mean) / std

    #reshape into 2D array
    reshaped = normalized.reshape(2, 2)

    #print results
    print("Original data:", data)
    print("Mean:", round(mean, 2))
    print("Standard Deviation:", round(std, 2))
    print("Normalized data:", np.round(normalized, 2))
    print("Reshaped data shape:", reshaped.shape)


if __name__ == "__main__":
    main()
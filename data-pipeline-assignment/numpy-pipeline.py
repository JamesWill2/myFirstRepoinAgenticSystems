import numpy as np

def main():
    #random seed
    np.random.seed(42)

    #generate 2d dataset
    data = np.random.randn(150,2)

    #find mean and std for features
    mean = np.mean(data,axis = 0)
    std = np.std(data,axis = 0)

    normalized = (data - mean) / std

    #split into training and testing (80:20 ration)
    split_index = int(0.8 * normalized.shape[0])

    train_data = normalized[:split_index]
    test_data = normalized[split_index:]

    #check results
    original_value = normalized[0,0]
    train_data[0,0] = 999

    #printing outputs
    print("Original data shape:", data.shape)
    print("Mean shape:", mean.shape)
    print("Training data shape:", train_data.shape)
    print("Test data shape:", test_data.shape)
    print("Note: Modifying the slice affected the original array")

if __name__ == "__main__":
    main()
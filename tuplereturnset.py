def containing_unique_values(input_list):
    unique_values = set(input_list)
    return unique_values

dataset_list = [100, 200, 300, 400, 700, 200, 300, 800, 900, 1000]
print("Dataset values:", dataset_list)
print("Unique values in the dataset:", containing_unique_values(dataset_list))
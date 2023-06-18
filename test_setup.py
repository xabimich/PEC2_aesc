import csv
import random

def split_dataset(csv_file, test_file, train_file, test_size):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) 
        header_without_quality = header[:-1]
        data = list(reader)  

    random.shuffle(data) 

    test_data = [row[:-1] for row in data[:test_size]]
    train_data = data[test_size:]

    with open(test_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header_without_quality)
        writer.writerows(test_data)

    with open(train_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(train_data)

    print(f"Test set saved to: {test_file}")
    print(f"Train set saved to: {train_file}")


csv_file = 'wine.csv'
test_file = 'test.csv'
train_file = 'train.csv'
test_size = 70

split_dataset(csv_file, test_file, train_file, test_size)
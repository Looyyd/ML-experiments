import csv

# open the CSV file and text file
with open('spam.csv', 'r', encoding='utf-8', errors='replace') as csv_file, open('spam.txt', 'w') as txt_file:
    # create a csv reader object
    csv_reader = csv.reader(csv_file)

    # iterate over the csv file
    for row in csv_reader:
        # row is a list representing each row in the csv
        # we access the second column with row[1]
        # (indices start at 0 in Python, so 1 is the second column)
        txt_file.write(row[1] + '\n')  # write the second column to the text file

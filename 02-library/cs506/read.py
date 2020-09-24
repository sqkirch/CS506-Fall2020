import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, newline='') as csvfile:
        csvread = csv.reader(csvfile, delimiter=' ')
        matrix = []
        for row in csvread:
            newrow = []
            for r in row[0].split(','):
                if r.isnumeric():
                    newrow += [int(r)] #want int or float??
                else:
                    newrow += [r]
            matrix += [newrow]
        return matrix

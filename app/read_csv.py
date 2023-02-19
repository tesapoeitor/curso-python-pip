import csv


def read_csv(path):
  data = []

  with open(path, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    header = next(reader)

    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)

  return data


if __name__ == "__main__":
  data = read_csv("./app/data.csv")
  # print(data[0])

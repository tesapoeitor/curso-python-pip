import utils
import read_csv
import charts
import pandas as pd

def bar_chart():
  data = read_csv.read_csv("./data.csv")
  search = input("Escribe el pais => ")
  country = utils.population_by_country(data, search)
  try:
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(search, labels, values)
  except AttributeError:
    print(country)


def pie_chart():
  # data = read_csv.read_csv("./data.csv")
  # # filtrar solos paises de sudamerica
  # data = list(filter(lambda row: row["Continent"] == "South America", data))

  # labels, values = utils.get_worl_population_percentage(data)
  
  df = pd.read_csv("./data.csv")
  df = df[df["Continent"] == "Africa"]

  countries = df["Country/Territory"].values
  percentages = df["World Population Percentage"].values

  charts.generate_pie_chart(countries, percentages)


if __name__ == "__main__":
  bar_chart()
  pie_chart()

def population_by_country(countries, search_value):
  result = list(
    filter(
      lambda country: country["Country/Territory"].lower() == search_value.
      lower(), countries))

  if len(result) == 0:
    return "Ese pais no esta en la lista, intenta con otro"
  else:
    return result[0]


def get_population(country):
  population = {
    year[:4]: int(population)
    for (year, population) in country.items()
    if "Population" in year and not "Worl" in year
  }
  labels = population.keys()
  values = population.values()
  return labels, values


def get_worl_population_percentage(data):
  labels = []
  values = []
  for row in data:
    labels.append(row["Country/Territory"])
    values.append(float(row["World Population Percentage"]))

  return labels, values
import random

limit = 100
years = list(range(1970, 2013)) * 3
for year, forename, surname in zip(random.sample(years, limit), random.sample(forenames, limit), random.sample(surnames, limit)):
    name = "{0} {1}".foramt(forename, surname)
    fh.write("{0:.<25}{1}\n".format(name, year))
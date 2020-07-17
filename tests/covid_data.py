import covid

from covid import Covid
# initializing
covid = Covid()
# printing data for the world
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())
# getting data according to country wise
cases = covid.get_status_by_country_name("india")
print(cases)
for x in cases:
    print(x, ":", cases[x])
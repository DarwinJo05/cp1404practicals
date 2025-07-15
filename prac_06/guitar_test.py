from prac_06.guitar import Guitar

name1 = "Gibson L-5 CES"
year1 = 1922
cost1 = 16035.40

name2 = "Another Guitar"
year2 = 2013
cost2 = 500.00

guitar1 = Guitar(name1, year1, cost1)
guitar2 = Guitar(name2, year2, cost2)

print(f"{guitar1.name} get_age() - Expected around 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected around 9. Got {guitar2.get_age()}")

print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

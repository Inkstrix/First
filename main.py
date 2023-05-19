#Anthony Tomes CIS 245-T302
interest = int(input("Please enter the interest rate as a whole number. E.g. for 6% type 6: "))
investment = float(input("Please enter the amount for the initial investment as a whole number. E.g. for an initial investment of $5000 type 5000: "))
year = 0
interest = interest *.01
total = investment
double = investment * 2
while total < double:
  total += total * interest
  year += 1
  print(f"Year number: {year} Investment amount: {total}")
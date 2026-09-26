def main():
  # Get an odometer value in U.S. miles from the user.
  # Get another odometer value in U.S. miles from the user.
  # Get a fuel amount in U.S. gallons from the user.
  # Call the miles_per_gallon function and store
  # the result in a variable named mpg.
  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  # Display the results for the user to see.


  first_odometer = float(input("Enter the first odometer reading (miles): "))
  second_odometer = float(input("Enter the second odometer reading (miles): "))
  fuel_amount = float(input("Enter the amount of fuel used (gallons): "))

  mpg = miles_per_gallon(first_odometer, second_odometer, fuel_amount)
  lp100k = lp100k_from_mpg(mpg)

  print(f"{mpg:.1f} miles per gallon")
  print(f"{lp100k:.2f} liters per 100 kilometers")

def miles_per_gallon(start_miles, end_miles, amount_gallons):

  mpg = (end_miles - start_miles) / amount_gallons
  return mpg

def lp100k_from_mpg(mpg):
 
  lp100k = 235.215/mpg
  return lp100k

# Call the main function so that
# this program will start executing.
main()


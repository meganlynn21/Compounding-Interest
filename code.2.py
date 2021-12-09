#Code Compounding Interest Loops Assignment
#Megan Keyes

#Keep asking until the user puts in a positive numeric value using loops
fDeposit = 0
while fDeposit <= 0:
  try:
    fDeposit = float(input('What is the original deposit (positive value): '))
    if fDeposit <= 0:
      print("Input must be a positive numerical value: ")
  except ValueError:
    print("Input must be a numeric value")

fInterest = 0
while fInterest <= 0:
  try:
    fInterest = float(input('What is the Interest Rate (positive value): '))
    if fInterest <= 0:
      print("Input must be a positive numerical value: ")
  except ValueError:
    print("Input must be a numeric value")

iMonths = 0
while iMonths <= 0:
  try:
    iMonths = int(input('What is the number of months (positive value): '))
    if iMonths <= 0:
      print("Input must be a positive numerical value: ")
  except ValueError:
    print("Input must be a numeric value")

fGoal = None
while fGoal == None:
  try:
    fGoal = float(input('What is the goal amount (Can enter 0 but not negative): '))
    if fGoal < 0:
      print("Input must be a positive numerical value: ")
      fGoal = None
  except ValueError:
    print("Input must be a numeric value")

# Calculate Interest. First convert the variable to a decimal by dividing by 100 then divide that by 12
fMonthlyInterest= (fInterest/100/12)

#Output the number of months the user has supplied and get account balance

i = 1
fAccountBalance = fDeposit
while i <= 12:
  if fAccountBalance >= fGoal:
    break
  fInterestForMonth = (fAccountBalance * fMonthlyInterest)
  #Add the interest for the month to the deposit to get the new Account Balance
  fAccountBalance += fInterestForMonth 
  print('Month: ',i, 'Account Balance is: $',format(fAccountBalance, ",.2f"))
  i += 1
# Calculate how many months it will take of compounding to reach the goal amount
GoalFormatted = "{:.2f}".format(fGoal)
CompoundedSavingsAccountBalance = fMonthlyInterest + fAccountBalance
while CompoundedSavingsAccountBalance < fGoal:
  iMonths += 1 
print('It will take: ',i-1, 'months to reach the goal of $', GoalFormatted)
  

   






  


  

##

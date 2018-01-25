#Shawn Simko
#Collaborators: Mayo Clinic Website
#Created: 1/25/18
#Answers a series of questions using relational operators
#with true or false answers to the questions.

# Overtime pay is mandatory when a worker exceeds 40 hours of work per week
# Did I work overtime?

def madeOvertime(hours):
    return hours > 40
    

# Profit is any amount remaining after you have paid your expenses.
# Did I make a profit?

def makeProfit(earnings, expenses):
    return (earnings - expenses) > 0  

# The normal body temperature is 98.6, but some variations exist.
# The patient has a fever if the body temperature is greater than 100 degrees
# Does the patient have a fever?

def hasFever(temp):
    return temp > 100

# "I took a quiz and I want to know how I did"
# "Did I get the wrong answer?"

def answerWrong(myAns, correctAns):
    return myAns == correctAns

# 60% and above is considered a "passing" grade
# Did I pass? Grades are given as percents.

def PassingGrade (GradeInPercent):
    return GradeInPercent >= 60

# Is my letter a capital letter?

def CapitalLetter (myletter):
    return myletter < 'a'

# Even numbers are evenly disible by 2.
# Is this number even?

def EvenNumber (mynum):
    return (mynum % 2) == 0

#GMR is a very important measurement
#the normal values for GMR are between 15 and 48.
# is my GMR abnormal?

def GMRnormal (myGMR):
    return (15 >= myGMR) or (myGMR >= 48)

#Students are classified according to the number of
#credits that they have completed. A Freshman is any
#student with less than 8 credits.  With every 8 credits
#students are successively ranked as Sophomores,
#Juniors. Students with 24 or more credits are Seniors.
# Is this student a Sophomore?

def Sophmore (Credits):
    return 8 <= Credits < 16

# The best days for golf are influenced by the weather.
# Golfing in the rain is no fun, and it is better if it
# isn't too windy (windspeed less than 20 mph).   The
# ideal temperature is between 60 and 85 degrees
# Is it a good day to golf?

def Good2Golf (Precip, windspeed, temp):
    return Precip != 'rain' and windspeed < 20 and 60 <= temp <= 85

# IPERS is the Iowa Public Employees Retirement System
# To be eligible to collect pay from IPERS (i.e. to retire),
# you must meet one of three requirements.  a) The sum of the age and
# years of service equals or exceeds 88; b) age is at least 62
# and years service is at least 20; c) age is 65 or more.
# Can I retire?

def Retirement (YearsofService, Age):
    return Age + YearsofService >= 88 or (Age >= 62 and YearsofService >= 20) or Age >= 65

#Normal Blood sugar levels are 70-100 when fasting, but 70-140 otherwise.
# Is my blood sugar level ok?

def BloodSugarLevel (Fasting, BloodSugar):
    return (Fasting == ('Yes' or 'yes') and (70 >= BloodSugar or BloodSugar >= 100) or (Fasting == ('No' or 'no') and ((70 >= BloodSugar) or (BloodSugar >= 140))))

#Cholesterol levels can put people at risk for heart disease.
#Problems occur when LDL (bad cholesterol) is too high (above 190),
#HDL (good cholesterol) is too low (below 40), triglycerides are
#too high (above 250).   Patients should also be concerned if their
#overall cholesterol is too high (HDL+LDL +20% of triglycerides is
#above 250).
# Do my cholesterol levels indicate that I am at risk?
                                                                                        
def CholesterolDanger (LDL, HDL, Triglycerides):
    return LDL > 190 or HDL < 40 or Triglycerides > 250 or LDL + HDL + (.2 * Triglycerides) > 250

# I know that blood pressure is a combined measure of systolic and diastolic readings.
# Is my blood pressure ok?

def BloodPressure (systolic, diastolic):
    return 90 <= systolic <= 120 or 60 <= diastolic <= 80

def main ():
    print("The following are True statements:")
    print ("Made Overtime, Hours= 41: ", madeOvertime(41))
    print("The following are False statements:")
    print ("Made Overtime, Hours= 40: ", madeOvertime(40))

    print("The following are True statements:")
    print ("Profit, earnings=50, expenses=49: ", makeProfit(50, 49))
    print("The following are False statements:")
    print ("Profit, earnings=30, expenses=50: ", makeProfit(30, 50))

    print("The following are True statements:")
    print ("Has Fever, temp= 100.1 Farenheit: ", hasFever(100.1))
    print("The following are False statements:")
    print ("Has Fever, temp= 99.7 Farenheit: ", hasFever(99.7))

    print("The following are True statements:")
    print ("Answer Wrong, My Answer= A, Correct Answer = A: ", answerWrong('A', 'A'))
    print("The following are False statements:")
    print ("Answer Wrong, My Answer= B, Correct Answer = C: ", answerWrong('B', 'C'))

    print("The following are True statements:")
    print ("Passing Grade, Grade = 90%: ", PassingGrade(90))
    print("The following are False statements:")
    print ("Passing Grade, Grade= 59%: ", PassingGrade(59))

    print("The following are True statements:")
    print ("Capital Letter, My Letter= Z: ", CapitalLetter('Z'))
    print("The following are False statements:")
    print ("Capital Letter, My Letter= b: ", CapitalLetter('b'))

    print("The following are True statements:")
    print ("Even Number, my number= 4: ", EvenNumber(4))
    print("The following are False statements:")
    print ("Even Number, my number= 3: ", EvenNumber(3))

    print("The following are True statements:")
    print ("GMR normality, my GMR= 49: ", GMRnormal(49))
    print("The following are False statements:")
    print ("GMR normality, my GMR= 16: ", GMRnormal(16))

    print("The following are True statements:")
    print ("Sophmore, credits= 10: ", Sophmore(10))
    print("The following are False statements:")
    print ("Made Overtime, Hours= 30: ", Sophmore(30))

    print("The following are True statements:")
    print ("Good Golfing, Precipitation= none, wind= 2mph, temp= 65 Farenheit: ", Good2Golf('Sunny', 2, 65))
    print("The following are False statements:")
    print ("Good Golfing, Precipitation= rain, wind= 7mph, temp= 74 Farenheit: ", Good2Golf('rain', 7, 74))
    print ("Good Golfing, Precipitation= none, wind= 5mph, temp= 90 Farenheit: ", Good2Golf('sunny', 5, 90))
    print ("Good Golfing, Precipitation= none, wind= 24mph, temp= 79 Farenheit: ", Good2Golf('cloudy', 24, 79))
        
    print("The following are True statements:")
    print ("Made Overtime, Hours= 41: ", madeOvertime(41))
    print("The following are False statements:")
    print ("Made Overtime, Hours= 40: ", madeOvertime(40))

    print("The following are True statements:")
    print ("Made Overtime, Hours= 41: ", madeOvertime(41))
    print("The following are False statements:")
    print ("Made Overtime, Hours= 40: ", madeOvertime(40))

    print("The following are True statements:")
    print ("Made Overtime, Hours= 41: ", madeOvertime(41))
    print("The following are False statements:")
    print ("Made Overtime, Hours= 40: ", madeOvertime(40))

    print("The following are True statements:")
    print ("Made Overtime, Hours= 41: ", madeOvertime(41))
    print("The following are False statements:")
    print ("Made Overtime, Hours= 40: ", madeOvertime(40))
    
main ()

print("I'm trying to complete this letter. Will you help me? Read the letter below, then answer some questions to fill in those capital letter words. Thanks for your help")

proseString = """

Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
"""
print(proseString)

print("Please provide me with the following words:") 

print("Give me your least liked Occupation?")
newjob=input()
proseString = proseString.replace("OCCUPATION", newjob)

print("Country?")
newCountry=input()
proseString = proseString.replace("COUNTRY", newCountry)

print("What is your new Passion (one-word only)?")
newPassion=input()
proseString = proseString.replace("PLURAL_NOUN", newPassion)

print("Give me a verb that depicts an action")
newVerb=input()
proseString = proseString.replace("VERB", newVerb)

print("Deescribe your level of interest?")
newLevel=input()
proseString = proseString.replace("ADJECTIVE", newLevel)

print("Identify your favorite cherished item")
oldItem=input()
proseString = proseString.replace("PERSONAL_ITEM", oldItem)

print("Your least favorite holiday?")
oldHoliday=input() 
proseString = proseString.replace("HOLIDAY", oldHoliday)

print("Type Your Name Please")
newName=input() 
proseString = proseString.replace("NAME", newName)

print(proseString)

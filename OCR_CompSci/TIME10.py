import datetime
currYear = int(datetime.date.today().year)

def ageproblem():
    global currYear
    name = input('What is your name? ').title()
    year = input('What year was you born? ')
    while year == '' or year.upper() != year.lower():
        year = input('Must enter birth year, What year was you born? ')
        if year.upper() != year.lower() or ' ' in year:
            year = ''
    print(f'Hi {name}.')
    age = currYear - int(year)
    print(f'I think you are {age} years old.')
    if age < 18:
        print('That means you are a child')
    else:
        print('GO BUY ME A BEER!')
#-> ageproblem()

def Palindrome(statement):
    i = 0
    j = len(statement) - 1
    statement = statement.upper()
    palindrome = True
    while i != j:
        if statement[i] == ' ':
            i += 1
        elif statement[j] == ' ':
            j -= 1
        elif statement[i] == statement[j]:
            i += 1
            j -= 1
        else:
            palindrome = False
            break
    return palindrome
print(Palindrome('Was it a car or a cat I saw'))

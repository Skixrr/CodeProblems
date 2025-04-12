singles = {
    '0':'',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'}
teens = {
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen'}
tens = {
    '0':'',
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety'}

numbers = []
for i in range(1,1001):
    temp = ''
    n = str(i)
    if len(n) == 4:
        temp = temp + singles[n[0]] + 'thousand'
        n = n[1:]
        if n == '000':
            n = ''
    if len(n) == 3:
        temp = temp + singles[n[0]] + 'hundred'
        n = n[1:]
        if n != '00':
            temp = temp + 'and'
    if len(n) == 2:
        if n[0] == '1':
            temp = temp + teens[n]
        else:
            temp = temp + tens[n[0]]
            n = n[1:]
    if len(n) == 1:
        temp = temp + singles[n]
    numbers.append(temp)

Ans = 0
for i in numbers:
    print(i)
    Ans += len(i)
print(Ans)
    
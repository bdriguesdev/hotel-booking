from backend.exceptions import CustomException

def textValidator(text, maxLen, minLen = 1):
    #returns text that only contains 0-9 / a-z / A-Z or raise a Exception

    if not(isinstance(text, str)):
        raise Exception('Send a valid text. -1')
    if len(text) > maxLen or len(text) < minLen:
        raise Exception('Send a valid text. -2')
    for x in range(0, len(text)):
        asciinum = ord(text[x])
        #33(!) #44(,) #46(.) #63(?) #32(space) #48-57(0-9) #65-90(A-Z) 97-122(a-z)
        if asciinum < 32:
            raise Exception('Send a valid text. 1')
        elif asciinum > 33 and asciinum < 44:
            raise Exception('Send a valid text. 2')
        elif asciinum > 44 and asciinum < 46:
            raise Exception('Send a valid text. 3')
        elif asciinum > 46 and asciinum < 48:
            raise Exception('Send a valid text. 4')
        elif asciinum > 57 and asciinum < 63:
            raise Exception('Send a valid text. 5')
        elif asciinum > 63 and asciinum < 65:
            raise Exception('Send a valid text. 6')
        elif asciinum > 90 and asciinum < 97:
            raise Exception('Send a valid text. 7')
        elif asciinum > 122:
            raise Exception('Send a valid text. 8')
    
    return text

def passwordValidator(passw):
    for x in range(0, len(passw)):
        asciinum = ord(passw[x])
        #48-57(0-9) 65-90(A-Z) 97-122(a-z)
        if asciinum < 48:
            raise CustomException('You need to send a valid password.')
        elif asciinum > 57 and asciinum < 65:
            raise CustomException('You need to send a valid password.')
        elif asciinum > 90 and asciinum < 97:
            raise CustomException('You need to send a valid password.')
        elif asciinum > 122:
            raise CustomException('You need to send a valid password.')
    return passw

def birthdayValidator(birth):
    day = []
    month = []
    year = []

    if len(birth) != 10 or not(isinstance(birth, str)):
        return Exception
    
    for x in range(0, len(birth)):
        asciinum = ord(birth[x])

        if asciinum < 47 or asciinum > 57:
            return Exception

        if x < 2:
            day.append(birth[x])
        elif x > 2 and x < 5:
            month.append(birth[x])
        elif x > 5:
            year.append(birth[x])
    
    day = int("".join(day))
    month = int("".join(month))
    year = int("".join(year))

    return [day, month, year]

def emailValidator(email):
    indexOfSign = -1 #index of -> @ <-

    if len(email) > 50 or not(isinstance(email, str)) or len(email) < 5: 
        raise CustomException('You need to send a valid email.')

    # 46(.) 48-57(0-9) 65-90(A-Z) 95(_) 97-122(a-z)
    for x in range(0, len(email)):
        asciinum = ord(email[x])
        if email[x] == '@':
            indexOfSign = x
        elif asciinum < 48:
            if asciinum != 46:
                raise CustomException('You need to send a valid email.')
        elif asciinum > 57 and asciinum < 65:
            raise CustomException('You need to send a valid email.')
        elif asciinum > 90 and asciinum < 97:
            if asciinum != 95:
                raise CustomException('You need to send a valid email.')
        elif asciinum > 122:
            raise CustomException('You need to send a valid email.')

    if indexOfSign == -1:
        raise CustomException('You need to send a valid email.')

    return email

def stateValidator(state):
    states_dict = { "RJ": "Rio de Janeiro", "RS": "Rio Grande do Sul", "SP": "São Paulo" }

    if not(state in states_dict):
        raise CustomException("You need to choose one of these states: RJ, SP or SP.")

    return state

def cityValidator(city):
    return city

def numValidator(num, max=1000, min=0):
    num = float(num)
    if not(isinstance(num, float)) and not(isinstance(num, int)):
        raise Exception('Send a valid number.')
    if num > max or num < min:
        raise Exception('Send a valid number.')

    return num

def intValidator(num):
    if not(isinstance(num, int)):
        raise Exception
    return num

def reviewValueValidator(num):

    if not(isinstance(num, float)) and not(isinstance(num, int)):
        raise Exception('Send a valid number.')
    if num != 1 and num != 1.5 and num != 2 and num != 2.5 and num != 3 and num != 3.5 and num != 4 and num != 4.5 and num != 5:
        raise Exception('Send a valid number.')

    return num
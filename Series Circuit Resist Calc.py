# Series Circuit Total Resistance Calc

r = 0
newRes = []

while r != 10 or later == 'done' or later == 'Done':
    r = r + 1
    print('What is the value of resistor ' + str(r) + '?')
    value = float(input())
    newRes.append(value)
    print('\nIf there is no more resistors, please type done and hit enter, otherwise just hit enter')
    later = input()
    
    if later == 'done' or later == 'Done':
        Rt = sum(newRes)
        if Rt >=0 and Rt <= 1.0:
           print('Your total resistance is: ' + str(Rt) + ' ohm')
        elif Rt > 1.0:
            print('Your total resistance is: ' + str(Rt) + ' ohms')
        break

input()


# def series_resistance(lst):
#	Rt = sum(lst)
#	if Rt <= 1.0:
#			return str(Rt) + " ohm"
#	else:
#			return str(Rt) + " ohms"

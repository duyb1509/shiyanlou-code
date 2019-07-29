#!/usr/bin/env python3

import sys

salary = sys.argv[1]

try:
    salary2 = int(salary)
    salary1 = salary2 - 5000
    if salary1 <= 0:
        tax = 0
    elif salary1 <= 3000:
        tax = salary1 * 0.03
    elif salary1 <= 12000:
        tax = salary1 * 0.1 - 210
    elif salary1 <= 25000:
        tax = salary1 * 0.2 - 1410
    elif salary1 <= 35000:
        tax = salary1 * 0.25 - 2660
    elif salary1 <= 55000:
        tax = salary1 * 0.3 - 4410
    elif salary1 <= 80000:
        tax = salary1 * 0.35 - 7160
    elif salary1 > 80000:
        tax = salary1 * 0.45 - 15160
    print('your tax is: %.2f' % tax)
except:
    print('Parameter Error')


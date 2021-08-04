# from https://wwcodemanila.github.io/WWCodeManila-Python/#/basic_concepts/variables?id=challenge

""" The Challenge
Author: keopijane
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

# Build your code below
bill = input('How much is your total bill? ')
payment = input('How much is your payment? ')
change = float(payment) - float(bill)
format_change = "{:.2f}".format(change)
print('Hi! your change is {}'.format(format_change))
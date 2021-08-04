""" Aling Nena's Reward System Challenge
Author:
Description: This summer, Aling Nena’s Sari-sari store wants to implement a
reward system where customers can redeem a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>

>> Please enter text: 1 nicole i. tibay f

The system will then reply the following:
Hi <Customer’s name first letters upper case>! You have successfully redeem
reward #<reward number> - <reward>! Thank you for choosing Aling Nena’s
Sari-sari store.

>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank you for choosing Aling Nena’s Sari-sari store.
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
import string

rewards = [
    "Coke sakto",  # index 0
    "Boy Bawang",  # index 1
    "15pcs. Yucky candy",  # index 2
    "15pcs. Pintura candy",  # index 3
    "15PHP load",  # index 4
    "3 pcs. Dove conditioner",  # index 5
    "Cottonbuds",  # index 6
    "One sheet of Biogesic",  # index 7
    "100mL Pepper/Pintura",  # index 8
]

# Build your code below
description ='''
This summer, Aling Nena’s Sari-sari store wants to implement a
reward system where customers can redeem a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>'''
print(description)
response = input('Please enter text: ')
customer_name = response[2:-2]
reward_number = response[0]
reward = int(reward_number)
reward = rewards[reward-1]
customer_name = string.capwords(customer_name)
print('Hi {}! You have successfully redeem reward #{} - {}! Thank you for choosing Aling Nena’s Sari-sari store.'.format(customer_name, reward_number, reward))


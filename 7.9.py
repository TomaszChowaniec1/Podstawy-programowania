
import random
dice_roll_1 = random.randint(1,6)
special = dice_roll_1 ==1 or dice_roll_1 ==6

print(f'This is your roll {dice_roll_1}')
print(f'You rolled a special number: {special}')
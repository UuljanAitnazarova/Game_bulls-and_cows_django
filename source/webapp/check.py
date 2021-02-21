class Check:
    def __init__(self, user_numbers):
        self.user_numbers = user_numbers
        self.my_list = [3, 1, 6, 4]


    def check_values(self):
        bulks = 0
        cows = 0
        for i in range(len(self.my_list)):
            if self.my_list[i] == self.user_numbers[i]:
                bulks += 1
            elif self.my_list[i] in self.user_numbers:
                cows +=1

        if bulks ==4:
            return 'You got it right!'
        elif cows or bulks:
            return f'You got {bulks} bulks and {cows} cows!'
        else:
            return 'No identical numbers'


def track_errors(numbers):
    if len(numbers) != 4:
        return 'The amount of integers should equal to 4!'
    for i in numbers:
        if i >= 11 or i < 0:
            return 'The values should be less than 10!'
    if len(numbers) > len(set(numbers)):
        return 'The values should be unique!'
number = 10
number +=5 #присвоение
print(number)
first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(round(third_number)) #0.40002000000000004, но мы округляем с помощью road, у нас получается 0
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4)) #округляется до 4 после знака(2.1001)


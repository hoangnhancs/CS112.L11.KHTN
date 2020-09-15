def reversed_string_to_string(string_convert, seperator = ''):
    #convert string to a revesed list by reversed() function
    return seperator.join(reversed(string_convert))
    #it is a base function, and I write it for reference purposes only

#palindromic number always divisible by 11

max = 0
for i in range (990, 109, -11):
    for j in range (999, 99, -1):
        if str(i*j)==str(i*j)[::-1]:
            if(max<i*j):
                max=i*j
print(max)


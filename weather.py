november = [+9, +7, +4, +4, +4, +8, +5, +5, +5, +6, 0, 0, 0, +1, 0, -5, -4, -3, 0, 0, -1, -1, -2, -8, -7, -1, +4, +1,
            -1, +1, +1]
max_november = november.copy()
max_november.sort()
print(november)
# print(max_november)
solution = 0
v = len(november) - 1
maximum = november[v]
max_temp = november[v]
output = ['None']
days = 0
maximum_id = len(november) - 1
for i in range(1, len(november)):
    #print(november[- i - 1], november[- i])
    if november[- i - 1] >= maximum:
        output.append('None')
        maximum = november[- i - 1]
        maximum_id = - i - 1
    elif november[- i - 1] < november[- i]:
        max_temp = november[- i]
        days = 1
        output.append(str(days))
    elif november[- i - 1] < max_temp:
        days += 1
        output.append(str(days))
    elif november[- i - 1] < maximum:
        output.append(str(maximum_id + i + 1))
    else:
        output.append(november[- i - 1])
    '''if i + 1 < len(november):
        c = len(november)
        a = len(november) - i - 2
        b = len(november) - i - 1
        if november[b] >= maximum and november[b] > november[a]:
            maximum = november[b]
            november[b] = 'None'
            november
        elif november[b] > november[a]:
            november[b] = 'None'
        elif november[b] >= maximum:
            maximum = november[b]
            november[b] = 'None' '''
output.reverse()
print(output)
print(len(output), len(november))
print(str(2))

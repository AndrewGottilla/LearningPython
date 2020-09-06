months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# printing a list while concatenating requires you to use the str() function
print('months: ' + str(months))

# print('First month: ' + months[0])
# print('First month (fixed): ' + months[0].title())

msg = 'I was born in ' + months[9].title() + '.'
print(msg)
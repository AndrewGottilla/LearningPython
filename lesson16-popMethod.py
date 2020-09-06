### 2020-09-06
### Author: Andrew Gottilla
### Lesson 16: Using the pop() method

subscribers = ['chris@example.com', 'mary@test.com', 'andrew_gottilla@yahoo.com']
print('Subscribers:\n' + str(subscribers))
print()

# pop() method without parameters will remove last element of list and return value
popped_sub = subscribers.pop()
print('Last sub popped off:\n' + str(subscribers))
print('Last subscriber was ' + popped_sub)
print()

# put popped sub back into list
subscribers.append(popped_sub)
print('Subscriber put back:\n' + str(subscribers))
print()

# pop() method can pop at speceified index
first_sub = subscribers.pop(0)
print('First sub popped off:\n' + str(subscribers))
print('First subscriber was ' + first_sub)
print()

# remove element from list
subscribers.remove('mary@test.com')
print('Subscriber removed from list:\n' + str(subscribers))
print()

subscribers = ['chris@example.com', 'mary@test.com', 'andrew_gottilla@yahoo.com']
subbed_by_mistake = 'mary@test.com'
print('Subscriber list refreshed:\n' + str(subscribers))
print()

subscribers.remove(subbed_by_mistake)
print('Subscriber removed from list (again):\n' + str(subscribers))
print()
### 2020-09-09
### Author: Andrew Gottilla
### Lesson 42: Using while loop with list

# list of clients waiting
queue = ['frank', 'tom', 'andrew', 'mary', 'tony', 'chris', 'kevin']
# list that holds clients served
served = []

print("- - CLIENT SERVICE TERMINAL - -")

# serve all the clients
# NOTE: using the pop() method stops the while loop from being continuous
while queue:
    current = queue.pop()
    print("SERVING: " + current.title())
    served.append(current)
print()

# print all the users who have been served
print("The following clients have been served:")
for client in served:
    print("- " + client.title())
print()

# let's say Andrew put a bunch of tickets in, but the first solution solved
#   all the other problems that Andrew put tickets in for. So now we just
#   have to take the rest of Andrew's tickets out of the queue

# list of ticket queue
ticket_queue = ['andrew', 'frank', 'tom', 'andrew', 'mary', 'tony', 'chris', 'kevin', 'andrew', 'milton', 'erica', 'andrew', 'erica', 'tom', 'andrew']

print("CURRENT TICKET QUEUE:\n" + str(ticket_queue) + '\n')

# loop through ticket_queue while 'andrew' is still there and remove the instance
print("REMOVING ANDREW FROM QUEUE:")
while 'andrew' in ticket_queue:
    ticket_queue.remove('andrew')
print(ticket_queue)
print()

sandwich_orders = ['chicken sandwich','bacon sandwich','fish sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print('I made your' + ' ' + sandwich_order.title())
    finished_sandwiches.append(sandwich_order)
print('\nI have made this sandwich for you:\n')
for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())

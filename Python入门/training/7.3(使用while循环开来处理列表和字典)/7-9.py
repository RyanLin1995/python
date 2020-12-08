sandwich_orders = ['pastrami sandwich','chicken sandwich','pastrami sandwich',
                    'bacon sandwich','fish sandwich','pastrami sandwich']
finished_sandwiches = []

print('Pastrami Sandwich' + ' ' + ' had been sold out.\n')

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print('I made your' + ' ' + sandwich_order.title())
    finished_sandwiches.append(sandwich_order)
print('\nI have made this sandwich for you:\n')
for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())

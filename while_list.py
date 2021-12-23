sandwich_orders = ['cheese burger','mashed potatoes','tuna']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order.title() + " sandwich")
    
    finished_sandwiches.append(current_order)
print("Your " + current_order.title() + " sandwich has been made.")
    
    

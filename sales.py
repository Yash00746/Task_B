import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    if current_day % 7 != 0:
        # Process daily sales for non-restocking days

        max_unit_sells = min(200, available_items)  # Maximum units that can be sold based on inventory
        todays_sales = random.randint(1, 200)        # Randomly determine today's sales within the limit
        available_items = available_items - todays_sales    # Update available items after sales
        
        # Record the inventory details for the day

        inventory_records.append([current_day, todays_sales, 0, available_items])

    
    return available_items
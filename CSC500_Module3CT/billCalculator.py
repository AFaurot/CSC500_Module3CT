import numpy as np

def main():

    #quantity_items will be used to create the array based on user input
    quantity_items = int(input('How many items are on the bill? : '))
    #food_price array len = quantity of items. dtype = Float allows for decimal point precision.
    food_price = np.arange(quantity_items, dtype=float)
    #item_incrementer will store a variable used to iterate over the array
    item_incrementer = 0
    for i in range(quantity_items) :
        print('Enter item #', item_incrementer + 1 ,' price' )
        food_price[item_incrementer]= float(input())
        item_incrementer += 1
    #numpy sum is used to total the food before tax and tip
    before_total= np.sum(food_price)
    #variable to calculate tax and tip. Note that with_tip is calculated before adding tax
    with_tax=0.07 * before_total
    with_tip=0.18 * before_total
    #Calculate total bill
    final_bill=float(with_tax + with_tip + before_total)
    print('The total before tax and tip is:', round(before_total, 2))
    print('The final total after 18% tip and 7% tax is:', round(final_bill, 2))


if __name__ == '__main__': main()
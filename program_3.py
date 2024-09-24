def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    if weight <= 2:
        shippingCost = 1.50
    else:
        if weight <= 6:
            shippingCost = 3.00
        else:
            if weight <= 10:
                shippingCost = 4.00
            else:
                if weight > 10:
                    shippingCost = 4.75

    ######################
    # WRITE YOUR CODE HERE
    ######################

    return shippingCost


shippingCost = 0


#### you only need to worry about the actual shipping
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))




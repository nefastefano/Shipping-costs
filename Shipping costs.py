import time
import sys

cost_ground_premium = 125.00

weight_input = input("Please specify the weight (pounds) ")
weight = int(weight_input)

print("The weight is", weight, " lbs")

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

for _ in range(1, 35):
    content = f'\r{next(spinner)} Calculating the shipment costs...'
    print(content, end="")
    time.sleep(0.1)
    print('\r\033[K', end="")

print("Ground Premium Shipping ", cost_ground_premium, " USD")

# Ground Shipping
if weight <= 2:
    ground_shipping = 20+(1.5*weight)
    print("Ground shipping = ", ground_shipping, " USD")
elif weight <=6:
    ground_shipping = 20+(3*weight)
    print("Ground shipping = ", ground_shipping, " USD")
elif weight <=10:
    ground_shipping = 20 + (4 * weight)
    print("Ground shipping = ", ground_shipping, " USD")
else:
    ground_shipping = 20+(4.75*weight)
    print("Ground shipping = ", ground_shipping, " USD")

  # Drone Shipping
if weight <=2:
    drone_shipping = 4.5 * weight
    print("Drone shipping = ", drone_shipping, " USD")
elif weight <=6:
    drone_shipping = 9 * weight
    print("Drone shipping = ", drone_shipping, " USD")
elif weight <=10:
    drone_shipping = 12 * weight
    print("Drone shipping = ", drone_shipping, " USD")
else:
    drone_shipping = 14.25 * weight
    print("Drone shipping = ", drone_shipping, " USD")

# add a fancy loading spinning thingy

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

for _ in range(1, 35):
    content = f'\r{next(spinner)} Lemme see what is the cheapest shipment for you...'
    print(content, end="")
    time.sleep(0.1)
    print('\r\033[K', end="")

# end spinning thingy

if min(cost_ground_premium, ground_shipping, drone_shipping) == cost_ground_premium:
    print("The shipment that will cost you the least is = Cost Ground Premium, for a total of ", cost_ground_premium, " USD")
elif min(cost_ground_premium, ground_shipping, drone_shipping) == ground_shipping:
    print("The shipment that will cost you the least is = Ground Shipping, for a total of ", ground_shipping, " USD")
elif min(cost_ground_premium, ground_shipping, drone_shipping) == drone_shipping:
    print("The shipment that will cost you the least is = Drone Shipping, for a total of ", drone_shipping, " USD")


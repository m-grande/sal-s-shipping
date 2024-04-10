weight = 8.4

# Ground Shipping
if weight <= 2:
  cost_ground = 1.50 * weight + 20.00
elif weight > 2 and weight < 6:
  cost_ground = 3.00 * weight + 20.00
elif weight > 6 and weight < 10:
  cost_ground = 4.00 * weight + 20.00
elif weight >= 10:
  cost_ground = 4.75 * weight + 20.00
else:
  print('Error the weight is not correct')

print('Ground Shipping: $', cost_ground)

# Ground Shipping Premium
cost_ground_premium = 125.00
print('Ground Shipping Premium: $', cost_ground_premium)

# Drone Shipping
if weight <= 2:
  cost_drone_shipping = 4.50 * weight
elif weight > 2 and weight <= 6:
  cost_drone_shipping = 9.00 * weight
elif weight > 6 and weight <= 10:
  cost_drone_shipping = 12.00 * weight
elif weight > 10:
  cost_drone_shipping = 14.25 * weight
else:
  print('Error the weight is not correct')

print('Drone Shipping Premium: $', cost_drone_shipping)

#enter weight in lbs
weight = 41.5

#Ground Shipping 

if weight <= 2:
  cost = 20 + weight * 1.5
  print("Ground Shipping Cost= $" + str(cost))
elif weight >= 2 and weight <= 6:
  cost = 20 + weight * 3
  print("Ground Shipping Cost= $" + str(cost))
elif weight >= 6 and weight <= 10:
  cost = 20 + weight * 4
  print("Ground Shipping Cost= $" + str(cost))
elif weight > 10:
  cost = 20 + weight * 4.75
  print("Ground Shipping Cost= $" + str(cost))

#Premium Ground Shipping 

premium_shipping_cost = 125
print("Premium Shipping Cost= $" + str(premium_shipping_cost))

#Drone Shipping

if weight <= 2:
  cost = weight * 4.5
  print("Drone Shipping Cost= $" + str(cost))
elif weight >= 2 and weight <= 6:
  cost = weight * 9
  print("Drone Shipping Cost= $" + str(cost))
elif weight >= 6 and weight <= 10:
  cost = weight * 12
  print("Drone Shipping Cost= $" + str(cost))
elif weight > 10:
  cost = weight * 14.25
  print("Drone Shipping Cost= $" + str(cost))

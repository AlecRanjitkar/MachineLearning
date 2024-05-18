# Define probabilities
P_Car = 0.30
P_Bus = 0.10
P_Plane = 0.60
P_Death_Car = 0.00000271 / 100
P_Death_Bus = 0.00000004 / 100
P_Death_Plane = 0.00000003 / 100

# Total probability of death
P_Death = (P_Death_Car * P_Car) + (P_Death_Bus * P_Bus) + (P_Death_Plane * P_Plane)

# Probability of having taken a plane given death
P_Plane_Death = (P_Death_Plane * P_Plane) / P_Death

# Print the result as a percentage
print(f"The probability it was from travelling by plane given the person died is: {P_Plane_Death * 100:.4f}%")

a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of y^2 (b): "))
c = float(input("Enter the constant term (c): "))

# Solve for the intersection point (x, y)
intersection_x = (c * b) / (a + b)
intersection_y = (c * a) / (a + b)

# Calculate the distance from the origin to the intersection point
radius_inner_circle = (intersection_x**2 + intersection_y**2)*0.5

print(f"The radius of the inner circle is approximately {radius_inner_circle:.4f}")

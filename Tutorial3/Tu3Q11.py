def main(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "Y-axis"
    else:
        return "X-axis"
x = float(input("Enter x: "))
y = float(input("Enter y: "))
print("The point is in:", main(x, y))

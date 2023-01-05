def catAndMouse(x, y, z):
    dist_catA = abs(z-x)
    dist_catB = abs(z-y)
    if dist_catA != dist_catB:
        if dist_catA < dist_catB:
            return "Cat A"
        else:
            return "Cat B"
    elif dist_catA == dist_catB:
        return "Mouse C"

print(catAndMouse(1,2,3))
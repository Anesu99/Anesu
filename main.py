def join_calculation():
    import math
    DataY1 = float(input("Enter Y1 coordinate: "))
    DataY2 = float(input("Enter Y2 coordinate: "))
    DataX1 = float(input("Enter X1 coordinate: "))
    DataX2 = float(input("Enter X2 coordinate: "))
    DX = DataX2 - DataX1
    DY = DataY2 - DataY1
    Distance = math.sqrt(DX**2 + DY**2)
    A = DY/DX
    angle = math.degrees(math.atan(A))
    #quadrants
    quad1 = angle
    quad2 = 180 - angle
    quad3 = 180 + angle
    quad4 = 360 - angle
    #putting conditions after calculating the angle
    if DX > 0 and DY > 0:
        print(Distance, quad1)
    elif DX > 0 and DY < 0:
        print(Distance, quad2)
    elif DX < 0 and DY < 0:
        print(Distance, quad3)
    else:
        print(Distance, quad4)
join_calculation()


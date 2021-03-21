import math

def SetSailSpeed(ship):
    x_coord, y_coord = ship.x_coord, ship.y_coord
    x_dest, y_dest = ship.x_destination, ship.y_destination
    max_speed = ship.max_speed
    x_move = x_dest-x_coord
    y_move = y_dest-y_coord
    x_speed = 0
    y_speed = 0
    if x_move and y_move != 0:
        if y_move < 0 and x_move < 0:
            angle = math.atan(y_move / x_move)
            x_speed = math.cos(angle) * -max_speed
            y_speed = math.sin(angle) * max_speed
        elif y_move < 0 and x_move > 0:
            angle = math.atan(y_move / x_move)
            x_speed = math.cos(angle) * max_speed
            y_speed = math.sin(angle) * max_speed
        elif y_move > 0 and x_move < 0:
            angle = math.atan(x_move / y_move)
            x_speed = math.sin(angle) * -max_speed
            y_speed = math.cos(angle) * max_speed
        elif y_move > 0 and x_move > 0:
            angle = math.atan(x_move / y_move)
            x_speed = math.sin(angle) * max_speed
            y_speed = math.cos(angle) * max_speed
        else:
            x_speed = max_speed

    ship.x_speed = x_speed
    ship.y_speed = y_speed


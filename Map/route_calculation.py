import math

def RouteCalculation(SonarList, Goal_Angle, ship_x, ship_y):
    close_direction = []
    for sonar in SonarList:
        if sonar.angle == Goal_Angle:
            if sonar.change_y != 0 and sonar.change_x != 0:
                output_coordinates = [ship_x + math.cos(Goal_Angle) * 1000, ship_y + math.sin(Goal_Angle)]
                return output_coordinates
        if Goal_Angle-20 < sonar.angle < Goal_Angle + 20:
            close_direction.append(sonar)
    current_sonar = close_direction[0]
    for sonar in close_direction:
        if sonar.counter > current_sonar.counter:
            current_sonar = sonar
    output_coordinates = [ship_x + math.cos(current_sonar.angle) * current_sonar.counter * 100, ship_y + math.sin(current_sonar.angle) * current_sonar.counter * 100]
    return output_coordinates
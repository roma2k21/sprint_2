class PointsForPlace:
    place = 0

    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            place = 101 - place
            return place


class PointsForMeters:
    points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            meters *= 0.5
            return meters


class TotalPoints(PointsForPlace, PointsForMeters):

    @staticmethod
    def get_total_points(meters, place):
        total = PointsForPlace.get_points_for_place(place) + TotalPoints.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))
points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))
total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))

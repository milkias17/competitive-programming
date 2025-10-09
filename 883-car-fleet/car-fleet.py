class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        car_times = [(target - position) / speed for position, speed in cars]
        fleets = 0
        while len(car_times) > 1:
            leading_car = car_times.pop()
            if leading_car < car_times[-1]:
                fleets += 1
            else:
                car_times[-1] = leading_car
        
        if len(car_times) == 0:
            return fleets
        else:
            return fleets + 1
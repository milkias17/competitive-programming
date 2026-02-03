class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        f = (celsius * 1.8) + 32.0
        k = celsius + 273.15
        return [k, f]
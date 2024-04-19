from temperature import Temperature

class Calorie:
    """
    Represents the amount of calories calculated with:
    BMR = 10*weight + 6.25*height - 5*age + 5- 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.age = age
        self.height = height
        self.temperature = temperature
        self.weight = weight

    def calculate(self):
        return 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10


if __name__ == "__main__":
    country = "bosnia-herzegovina"
    city = "sarajevo"

    temp = Temperature(country, city).get()
    print(temp)
    # temp = 3
    calorie = Calorie(weight=70, height=170, age=39, temperature=temp)
    print(calorie.calculate())

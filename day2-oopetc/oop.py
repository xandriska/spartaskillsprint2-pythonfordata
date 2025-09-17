class GradeBook:
    def __init__ (self, grades):
        self.grades = grades

    def calculate_average(self):
        total = sum(self.grades)
        return total / len(self.grades)

    def display_average(self):
        average = self.calculate_average()
        print('average grade: ', average)


def main():
    gradebook = GradeBook([2, 3, 4, 5, 6])

    gradebook.display_average()


main()

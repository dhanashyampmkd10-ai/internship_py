def cal_avg(mark1: float, mark2: float, mark3: float) -> float:
    return (mark1 + mark2 + mark3) / 3
def get_grade(average: float) -> str:
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        return "D"
def display_res(name: str, average: float, grade: str) -> None:
    print("\n--- Result ---")
    print("Name:", name)
    print("Average:", average)
    print("Grade:", grade)
def main() -> None:
    name: str = input("Enter student name: ")
    mark1: float = float(input("Enter mark 1: "))
    mark2: float = float(input("Enter mark 2: "))
    mark3: float = float(input("Enter mark 3: "))
    average: float = cal_avg(mark1, mark2, mark3)
    grade: str = get_grade(average)
    display_res(name, average, grade)
main()
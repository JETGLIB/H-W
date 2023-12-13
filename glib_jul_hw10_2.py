import csv
def get_top_performers(file_path, number_of_top_students=2):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        students_data = list(reader)
    students_data.sort(key=lambda x: float(x[2]), reverse=True)
    top_performers = [student[0] for student in students_data[:number_of_top_students]]

    return top_performers
print(get_top_performers("students.csv"))

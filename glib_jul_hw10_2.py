def get_top_performers(file_path, number_of_top_students=5):  
    student = {}  
    import csv
    with open(file_path, newline='') as file:  
        for line in file:
            *name, _, marcks = line.split()
 #           name = " ".join(name).split()            
  #          marcks = int(marcks)
            student = zip(name, marcks)
            print(dict(student))
            
        
    return student
print(get_top_performers("students.csv"))
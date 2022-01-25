with open("grades.txt") as data:
    school = {}
    for inpts in data:
        temp = inpts.split(":")
        for i in temp:
            if temp[1][:-1] == "\\n": 
                school[temp[0]] = int(temp[1][:-1])
            else: school[temp[0]] = int(temp[1])        
highest_note, lowest_grade, avg_grade = 0, 101, 0    
for student,note in school.items():
    if note > highest_note: 
        highest_note = note
    if note < lowest_grade: 
        lowest_grade = note
    avg_grade += note
with open("class_stats.txt","w") as output:
    for student,note in school.items(): 
        if note == highest_note:
            output.write(f"Highest note: {student} {note}\n")
    for student,note in school.items():
        if note == lowest_grade: 
            output.write(f"lowest grade: {student} {note}\n")
    output.write("avg grade: {}\n".format(avg_grade/len(school)))
    
        
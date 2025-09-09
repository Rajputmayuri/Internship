"""Q148. Store marks of 5 different subjects in a
dictionary. Ask subject name as an input from the
user. Print the marks of that subject entered by
User. If subject does not exist, print "Invalis"."""

sub_marks = {"math": 89, "science": 60, "history": 45, "english": 90, "computer": 99}

sub_name = input("Enter Subject name=")
if sub_name in sub_marks:
    print(f"Marks for {sub_name}", sub_marks[sub_name])
else:
    print("Invalid Subject")

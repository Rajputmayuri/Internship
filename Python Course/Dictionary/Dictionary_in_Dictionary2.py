student_data = {
    "mayuri": {
        "roll_number": 1,
        "gedner": "female",
        "marks": [34, 54, 76, 90, 56],
    },
    "gayatri": {
        "roll_number": 2,
        "gedner": "female",
        "marks": [85, 96, 14, 65, 84],
    },
    "nayan": {
        "roll_number": 31,
        "gedner": "male",
        "marks": [85, 96, 12, 37, 85],
    },
}

for name, details in student_data.items():
    total = sum(details["marks"])
    print(f"{name} has scored {total} marks")

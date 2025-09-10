student_data = {
    "mayuri": {
        "roll_number": 12,
        "gender": "female",
        "physics": 78,
        "chemistry": 99,
        "maths": 90,
    },
    "gayatri": {
        "roll_number": 13,
        "gender": "female",
        "physics": 90,
        "chemistry": 45,
        "maths": 93,
    },
    "nayan": {
        "roll_number": 14,
        "gender": "male",
        "physics": 45,
        "chemistry": 89,
        "maths": 100,
    },
}

# print(student_data["mayuri"]["gender"])

for name, details in student_data.items():
    total = details["physics"] + details["chemistry"] + details["maths"]
    print(f"{name} -> {total}")

"""Q142. Write a program that converts a string in camelCase to snake_case.
For example, converting "helloWorldHowAreYou" should result in
"hello_world_how_are_you"."""

my_string = "helloWorldHowAreYou"


result = "".join(["_" + ch.lower() if ch.isupper()
                  else ch for ch in my_string])
print(result)

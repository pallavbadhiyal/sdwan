# Extract/parse India is Great! for the given string
# str_var = "I%^&n**^^d89i665a#$ i89s &*G5r789e%^a*((t!"
str_var = input("Enter your string:")

temp_var = ""
for char in str_var:
    if char.isalpha() or char == " ":
        temp_var = temp_var + char

print(temp_var)
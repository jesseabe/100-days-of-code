def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("angela", "ANGELA"))



# Function using the results the other functionm
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

def format_name():
    """Take a first and last name and format it to return
    the title case version of the name.---> This is a docstring"""
    first_name = f_name.title()
    last_name = l_name.title()
    # print(f"{first_name} {last_name}")
    return f"{first_name} {last_name}"

formated_name = format_name("SWAPnil", "AgRaWaL")
print(formated_name)
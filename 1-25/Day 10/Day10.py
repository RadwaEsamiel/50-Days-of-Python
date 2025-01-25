def format_name(f_name, l_name) :
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name} {formated_l_name}")
    return (f"{formated_f_name} {formated_l_name}")


format_name("radwa","esmaiel")



______________________________________________________________________________________________________________


def format_name(f_name, l_name) :
    if f_name == "" or l_name == "" :
        return "input is empty"
    else :
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"


print(format_name(input("what is your First name?"),input("what is your last name?")))
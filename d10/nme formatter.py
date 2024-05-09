first = input("give me your first name: ")
last = input("give me your last name: ")
def format_name(first, last):
    first_title = first.title()
    last_title = last.title()
    all_name = first_title + " " + last_title
    return all_name

result = format_name(first, last)
print(result)

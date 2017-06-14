my_dict = {
    "first_name": "I-vann",
    "last_name": "Cllaud",
    "email": "vano@gmail.com",
    "age": 26
}
print("Step 2 result is:", my_dict)
new_list = []
new_filtered_list = []

my_list = my_dict.values()
print("Step 3 before processing:", my_list)

for value in my_list:
    if isinstance(value, str) and len(value) > 5 and value.find("a") >= 0:
        new_list.append(value)
    elif isinstance(value, int) and 40 > value > 25:
        # value =
        new_list.append(str(value))
print("Step 3 result is:", new_list)


for itm in new_list:
    if "n" not in itm and "m" not in itm:
        new_filtered_list.append(itm)
print("Step 4 result is:", new_filtered_list, type(new_filtered_list))

new_filtered_list.sort(reverse=True)
print("Step 5 result is:", new_filtered_list, type(new_filtered_list))

new_str = ",".join(new_filtered_list)
print("Step 6 result is:", new_str, type(new_str))

new_list = new_str.split(",")
print("Step 7 result is:", new_list, type(new_list))
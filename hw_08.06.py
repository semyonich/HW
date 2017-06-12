my_dict = {
    "first_name" : "I-vann",
    "last_name" : "McCloud",
    "email" : "vano@gmail.com",
    "age" : 26
}
print("Step 2 result is:", my_dict)
new_list = []

my_list = my_dict.values()
print("Step 3 before processing:", my_list)

for itm in my_list:
    if isinstance(itm,str) and len(itm) > 5 and itm.find("a") != -1:
        new_list.append(itm)
    elif isinstance(itm,int) and itm > 25 and itm < 40:
        itm = str(itm)
        new_list.append(itm)
    # else :
print("Step 3 result is:", new_list)

# Here must be logical sequence, but i haven't written it
print("Step 4 result is:", "none")

new_list.sort(reverse=True)
print("Step 5 result is:", new_list)

new_str = ""
for itm in new_list: new_str += itm + ","
print("Step 6 result is:", new_str, type(new_str))

for itm in new_list:
    itm = itm.split(",")
print("Step 7 result is:", new_list, type(new_list))
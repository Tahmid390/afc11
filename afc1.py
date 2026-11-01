file_name = "shopping_list.txt"

shopping_file = open(file_name,"w")

shopping_file.write("Shopping List\n")
shopping_file.write("1. Milk \n")
shopping_file.write("2. Bread \n")
shopping_file.write("3. Eggs \n")
shopping_file.write("4. Apples \n")

shopping_file.close()

shopping_file = open(file_name, "r")

print("\n Full Shopping List")
content = shopping_file.read()
print(content)

shopping_file.close()

shopping_file = open(file_name, "a")

shopping_file.write("5. Rice \n")
shopping_file.write("6. Butter \n")

shopping_file.close()

shopping_file = open(file_name,"r")

print("updated Shopping list")
updated_content = shopping_file.read()
print(updated_content)

shopping_file.close()
from prettytable import PrettyTable

table = PrettyTable()
print(table)
onetable = PrettyTable(["Pokemon Name","Type"])
print(onetable)
table.add_column("Pokemon Name",["Pokédex ","Squirtle","Charmander"])
table.add_column("Type",[" Electric "," Water ","Fire"])
print(table)

print(table.align)

table.align = 'l'
print(table)

print(table.align)
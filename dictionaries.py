example_dict = {
	"class"  :      "Astro 119",
	"prof"  :       "Brant",
	"awesomeness"   :       10
}                                                        #there is two tabs between the first 2 and one tab after awesomness, does that matter?

print(type(example_dict))

course = example_dict["class"]
print(course)

example_dict["awesomeness"] += 1        #adds 1 to the value defined as awesomeness

print(example_dict)

for x in example_dict.keys():                 #print dictionary element by element
	print(x, example_dict[x])


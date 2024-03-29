#Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames alone. 
#For this question, you must use a for loop to create the list. 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename.replace(".hpp", ".h"))
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]





# List Comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = [filename.replace(".hpp", ".h") if filename.endswith("hpp") else filename for filename in filenames]

print(new_filenames) 

# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]




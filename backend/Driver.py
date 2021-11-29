from Problems import *
from timeit import default_timer as timer

print("Starting...")

val1 = input("Enter input 1: ")
# val2 = input("Enter input 2: ")
# print("Input: " + val1 + " : " + val2)

start = timer()
result = solve_001(int(val1))
end = timer()

print("Result: " + str(result))
print("This took " + '{:f}'.format(end - start) + " seconds to complete.")

# input("Press enter to end.")

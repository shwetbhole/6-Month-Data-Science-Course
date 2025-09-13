# Check if a number is a power of 2

num = int(input("Enter number: "))
if num>0 and (num & (num-1)==0):
    print("Power of 2")
else:
    print("Not a power of 2")

# Explaining:

# We check two conditions here:
#
# 1. num > 0
#
# Just makes sure the number is positive.
#
# (Because negative numbers and 0 can’t be powers of 2.)
#
# 2. (num & (num - 1) == 0)
#
# This is the trick.
# To understand it, think about binary form (0s and 1s).
#
# Key idea:
#
# A power of 2 in binary always looks like:
#
# 1, 10, 100, 1000, 10000, …
# (one 1 followed by only 0s).
#
# Example:
#
# 2 → 10
#
# 4 → 100
#
# 8 → 1000
#
# 16 → 10000
#
# What happens with num - 1?
#
# Subtracting 1 flips that single 1 into 0, and all lower bits become 1.
#
# Example:
#
# num = 8 → 1000
#
# num-1 = 7 → 0111
#
# Now do num & (num-1) (bitwise AND):
#
# 8 (1000)
# AND 7 (0111)
# = 0000 → 0
#
# So if a number is power of 2 → the AND result will always be 0.
#
# But if it’s not a power of 2:
#
# num = 10 → 1010
#
# num-1 = 9 → 1001
#
# 1010 & 1001 = 1000 → not 0
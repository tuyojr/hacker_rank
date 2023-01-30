# You are given four points A, B, C and D in a 3-dimensional Cartesian 
# coordinate system. You are required to print the angle between 
# the plane made by the points A, B, C and B, C, D in degrees(not radians). 
# Let the angle be PHI.
# Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD.

# Here, X.Y means the dot product of X and Y, and AB x BC means the cross
# product of vectors AB and BC. Also, AB = B - A.

# Input Format

# One line of input containing the space separated floating number values
# of the X, Y and Z coordinates of a point.

# Output Format

# Output the angle correct up to two decimal places.

# Sample Input

# 0 4 5
# 1 7 6
# 0 5 9
# 1 7 2

# Sample Output

# 8.19
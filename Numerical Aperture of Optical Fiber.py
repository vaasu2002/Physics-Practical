d = 2
r = 0.65

sina = r/((r**2 + d**2)**0.5)

import math
ans = math.asin(sina)
print(f"{ans*57.2958} degree")

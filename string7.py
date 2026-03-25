s1 = "Hello Python World"

if s1.startswith("Hello") and s1.endswith("World"):
    print("correct")
else:
    print("wrong")

import re

s2 = "Data123Science"
s3 = re.sub(r'[^a-zA-Z]', '', s2)
print(s3)

s4 = "python"
rev = s4[::-1]
print("Reversed string:", rev)
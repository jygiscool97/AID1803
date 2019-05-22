import re
print(re.search(r'8{1,4}(ab)*','88ababab,5abababab,888ababab').group())

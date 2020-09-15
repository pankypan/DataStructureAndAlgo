import re

content = "Xiaoshuaib has 100 bananas"
res = re.match('^Xi.*(\d+)\s.*s$', content)
print(res.group(1))
res = re.match('^Xi.*?(\d+)\s.*s$', content)
print(res.group(1))

content = """Xiaoshuaib has 100 
bananas
"""
res = re.match('^Xi.*?(\d+)\s.*s$', content, re.S)
print(res.group(1))


content = """Xiaoshuaib has 100 
bananas
"""
res = re.search('Xi.*?(\d+)\s.*s', content, re.S)
print(res.group(1))

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
print(re.findall('Xi.*?(\d+)\s.*?s;', content))


content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
content = re.sub('\d+', '200', content)
print(content)


content = "Xiaoshuaib has 100 bananas"
pattern = re.compile('Xi.*?(\d+)\s.*s', re.S)
res = re.match(pattern, content)
print(res.group(1))
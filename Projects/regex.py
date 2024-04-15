# regex
import re

# users = [
#     ['riya', 'riya@gmail.com'],
#     ['julia', 'julia@julia.me'],
#     ['julia', 'sjulia@gmail.com'],
#     ['julia', 'julia@gmail.com'],
#     ['samantha', 'samantha@gmail.com'],
#     ['tanya', 'tanya@gmail.com']
# ]

users = [
    ['riya', 'riya@gmail.com'],
    ['julia', 'julia@julia.me'],
    ['julia', 'sjulia@gmail.com'],
    ['julia', 'julia@gmail.com'],
    ['samantha', 'samantha@gmail.com'],
    ['tanya', 'tanya@gmail.com'],
    ['riya', 'ariya@gmail.com'],
    ['julia', 'bjulia@julia.me'],
    ['julia', 'csjulia@gmail.com'],
    ['julia', 'djulia@gmail.com'],
    ['samantha', 'esamantha@gmail.com'],
    ['tanya', 'ftanya@gmail.com'],
    ['riya', 'riya@live.com'],
    ['julia', 'julia@live.com'],
    ['julia', 'sjulia@live.com'],
    ['julia', 'julia@live.com'],
    ['samantha', 'samantha@live.com'],
    ['tanya', 'tanya@live.com'],
    ['riya', 'ariya@live.com'],
    ['julia', 'bjulia@live.com'],
    ['julia', 'csjulia@live.com'],
    ['julia', 'djulia@live.com'],
    ['samantha', 'esamantha@live.com'],
    ['tanya', 'ftanya@live.com'],
    ['riya', 'gmail@riya.com'],
    ['priya', 'priya@gmail.com'],
    ['preeti', 'preeti@gmail.com'],
    ['alice', 'alice@alicegmail.com'],
    ['alice', 'alice@gmail.com'],
    ['alice', 'gmail.alice@gmail.com']
]

items = []
for u in users:
    if re.search(r'@gmail\.com\b', u[1], re.IGNORECASE):
        items.append(u[0])
sorted(items)
print(items)

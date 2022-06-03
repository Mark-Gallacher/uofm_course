import re

def logs():
    with open("../datasets/logdata.txt", "r") as file:
        logdata = file.read()

    pattern = """
        (?P<host>\d*.\d*.\d*.\d*)
        (\ -\ )
        (?P<user_name>[\w]*)
        (\s*\[)
        (?<=\[)(?P<time>[^\]]*)(?=\])
        (\]\s["])
        (?<=\")(?P<request>[^\]]*)(?=\")
        (["][\s*]\d*\s\d*\\n)"""

    result = []

    for item in re.finditer(pattern, logdata, re.X):
        group = item.groupdict()
        if group['user_name'] == '':
            group['user_name'] = '-'

        result.append(group)

    return(result)


print(logs())



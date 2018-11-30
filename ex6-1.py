import random,string
src = string.ascii_letters + string.digits
count = input ('请确认要生成几条密码: ')
list_passwds = []
for i in range(int(count)):
    list_passwds_all =random.sample(src,5)
list_passwds_all.extend(random.sample(string.digits, 1))
list_passwds_all.extend(random.sample(string.ascii_lowercase, 1))
list_passwds_all.extend(random.sample(string.ascii_uppercase, 1))
random.shuffle(list_passwds_all)
str_passwds = ' '.join(list_passwds_all)

if str_passwds not in list_passwds:
        list_passwds.append(str_passwds)
print(list_passwds)

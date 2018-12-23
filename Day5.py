"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example : the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import string
keys = range(1, 27)
values = list(string.ascii_lowercase)
d = dict(zip(keys, values))
print(d)
decode_msg = input('Enter the message to be decoded : ')
if len(decode_msg) != 3:
    print('Expected code format is nnn !')
    quit()
code = [list(decode_msg[0:3]), decode_msg[0:2], decode_msg[1:3]]
for i in range(1,3):
    if int(code[i]) > 26:
        code[i] = ''
a = [d[int(code[0][0])], d[int(code[0][1])], d[int(code[0][2])], d[int(code[1])], d[int(code[2])]]
print('%s%s%s, %s, %s' % (a[0], a[1], a[2], a[3], a[4]))

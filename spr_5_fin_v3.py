"""
Yandex Practicum, Python-developer
Yandex contest:
11 мар 2024, 23:41:11 109432653 53ms 4.14Mb
Program converts encrypted commands
example: 3[a]2[bc] - > 3aa2bcbc
"""


def decypher(command_str):
    """Encrypted commands are decrypted here"""
    curr_num = ''
    curr_str = ''
    stack = []
    # Commands are stored as: (curr_num, curr_str)
    for cmd in command_str:
        match cmd:
            case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
                curr_num += cmd
            case '[':
                stack.append((int(curr_num), curr_str))
                curr_num = ''
                curr_str = ''
            case ']':
                prev_num, prev_str = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            case _:
                curr_str += cmd
    return curr_str


def main():
    with open('input.txt', 'r') as f:
        command_encrypted = f.readline().rstrip()
    print(decypher(command_encrypted))


if __name__ == '__main__':
    main()

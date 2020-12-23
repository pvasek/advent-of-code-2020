from typing import List, Tuple

from typing_extensions import Protocol

Policy = Tuple[int, int, str]

def parse_password_policy(s: str) -> Policy:
    # expected input: <number1>-<number2> <char> 
    n, w = s.split()
    n1, n2 = n.split("-")
    return (int(n1), int(n2), w)

def parse_line(s: str) -> Tuple[Policy, str]:
    # expected input: <password policy>: <password>
    policy_def, psw = s.split(": ")
    return (parse_password_policy(policy_def), psw)

def load_data(file_name: str) -> List[Tuple[Policy, str]]:
    with open(file_name) as f:
        return [parse_line(i) for i in f.readlines()]

def is_valid(policy: Policy, psw: str) -> bool:
    min, max, char = policy
    c = psw.count(char)
    return min <= c <= max

def is_valid2(policy: Policy, psw: str) -> bool:
    i1, i2, char = policy
    return (psw[i1 - 1] == char) ^ (psw[i2 - 1] == char)

print(len([psw for policy, psw in load_data("./day02.data") if is_valid(policy, psw) == True]))
print(len([psw for policy, psw in load_data("./day02.data") if is_valid2(policy, psw) == True]))
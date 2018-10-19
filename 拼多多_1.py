# coding:utf-8


def min_HuiHe(HP, normAttack, buffedAttack):
    if HP % normAttack == 0:
        norm_number = HP / normAttack
    else:
        norm_number = HP / normAttack + 1
    cishu = int(HP / buffedAttack)
    if (HP - (buffedAttack * cishu)) / normAttack == 0:
        buffed_number = cishu * 2 + 1
    else:
        buffed_number = cishu * 2 + min(2, (HP - (buffedAttack * cishu)) / normAttack)
    return min(norm_number, buffed_number)


if __name__ == '__main__':
    HP = int(input())
    normAttack = int(input())
    buffedAttack = int(input())
    print min_HuiHe(HP, normAttack, buffedAttack)

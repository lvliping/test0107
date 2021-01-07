import random
import string


def rand_userName():
    userName = ''.join(random.sample(string.ascii_letters + string.digits, 3))
    return userName


def rand_newPwd():
    newPwd = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    # print(newPwd)
    return newPwd


def rand_phone():
    prelist = ["15", "18", "13"]
    phone = random.choice(prelist) + "".join(random.sample("0123456789", 9))
    # print(phone)
    return phone


def rand_email():
    email_suffix = ["@163.com", "@qq.com", "@gmail.com", "@mail.hk.com", "＠yahoo.co.id", "mail.com"]

    email_font = ''.join(random.sample(string.ascii_letters + string.digits, 5))

    email = email_font + random.choice(email_suffix)
    return email


def rand_userCnName():
    userCnName = ''.join(random.sample(string.ascii_letters + string.digits, 3))
    # print(userCnName)
    return userCnName


def rand_teamName():
    # 团队先固定
    teamName = "test1124"
    return teamName


def rand_teamCode():
    # 团队先固定
    teamCode = "test1124"
    return teamCode


def rand_roleCode():
    roleCode = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    return roleCode


def rand_roleName():
    roleName = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    return roleName


if __name__ == '__main__':
    # rand_userName()
    # rand_phone()
    # rand_newPwd()
    # rand_email()
    rand_userCnName()

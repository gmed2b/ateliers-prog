def is_mail(str_arg: str) -> (int, int):
    is_valid = (1, 0)
    len_arg = len(str_arg)

    if len_arg == 0:
        is_valid = (0, 0)
    elif '@' not in str_arg:
        is_valid = (0, 2)
    else:
        local_domain = str_arg.split('@')
        local = local_domain[0]
        domain = local_domain[1]
        if len(local) < 1 or (local.startswith('.') or local.endswith('.')) or ('..' in local):
            is_valid = (0, 1)
        if '.' not in domain:
            is_valid = (0, 4)
        elif len(domain) < 1 or (domain.startswith('.') or domain.endswith('.')) or ('..' in domain) or '_' in domain:
            is_valid = (0, 3)
    return is_valid


def test():
    str_variable2test = "bisgambiglia_paul@univ.corse.fr"
    print(is_mail(str_variable2test), end=" - ")
    print("doit renvoyer (1,0)")
    str_variable2test = "bisgambiglia_paulOuniv-corse.fr"
    print(is_mail(str_variable2test), end=" - ")
    print("doit renvoyer (0,2)")
    str_variable2test = "bisgambiglia_paul@univ-corsePOINTfr"
    print(is_mail(str_variable2test), end=" - ")
    print("doit renvoyer (0,4)")
    str_variable2test = "@univ-corse.fr"
    print(is_mail(str_variable2test), end=" - ")
    print("doit renvoyer (0,1)")


test()

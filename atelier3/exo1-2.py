def is_mail(str_arg: str) -> (int, int):
    """
    Retourne un tuple composé des codes suivants : (validité, code erreur)\n
    - (1, 0) le mail est valide
    - (0, 1) le corp n’est pas valide
    - (0, 2) il manque l’@
    - (0, 3) le domaine n’est pas valide
    - (0, 4) il manque le .
    :param str_arg: (str) email à valider
    :returns: (1, 0) si valide, (0, x) sinon
    """
    is_valid = (1, 0)
    if len(str_arg) == 0:
        is_valid = (0, 0)
    else:
        local_domain = str_arg.split('@')
        if len(local_domain) < 2:
            is_valid = (0, 2)
        else:
            local = local_domain[0]
            domain = local_domain[1]
            if len(local) < 1 or (local.startswith('.') or local.endswith('.')) or ('..' in local):
                is_valid = (0, 1)
            elif '.' not in domain:
                is_valid = (0, 4)
            elif len(domain) < 1 or (domain.startswith('.') or domain.endswith('.')) or (
                    '..' in domain) or '_' in domain:
                is_valid = (0, 3)
    return is_valid


def test():
    test_cases = [
        ("bisgambiglia_paul@univ.corse.fr", (1, 0)),
        ("bisgambiglia_paulOuniv-corse.fr", (0, 2)),
        ("bisgambiglia_paul@univ-corsePOINTfr", (0, 4)),
        ("@univ-corse.fr", (0, 1))
    ]
    for i, (input_str, expected_output) in enumerate(test_cases):
        result = is_mail(input_str)
        if result == expected_output:
            print(f"Test case `{input_str}` passed")
        else:
            print(f"Test case {i + 1} failed: got {result}, expected {expected_output}")


test()

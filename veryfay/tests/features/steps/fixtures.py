class SomeClass(object):
    pass


class OtherClass(object):
    pass


class SomeOtherClass(object):
    pass


class OtherSomeOtherClass(object):
    pass


class PrincipalClass(object):
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username


class OtherPrincipalClass(object):
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Admin(metaclass=Singleton):
    def contains(self, principal, *extra_info):
        return principal.username == 'admin'


class Supervisor(metaclass=Singleton):
    def contains(self, principal, *extra_info):
        return (principal.username == 'supervisor' or 
                principal.username == 'supervisor-commiter')


class Commiter(metaclass=Singleton):
    def contains(self, principal, *extra_info):
        return (principal.username == 'commiter' or 
                principal.username == 'supervisor-commiter')


class Contributor(metaclass=Singleton):
    def contains(self, principal, *extra_info):
        return (principal.username == 'contributor' or 
                principal.username == 'contributor-reader')


class Reviewer(metaclass=Singleton):
    def contains(self, principal, *extra_info):
        return (principal.username == 'contributor' or 
                principal.username == 'commiter')


class Reader(metaclass=Singleton):
    def contains(self, principal, *extra_info):
        return (principal.username == 'reader' and 
                extra_info[0] == 1234)


class NoContainsRole(metaclass=Singleton):
    pass


class ContainsNoParamsRole(metaclass=Singleton):
    def contains(self):
        pass

class ContainsReturnNoBoolRole(metaclass=Singleton):
    def contains(self, principal):
        pass

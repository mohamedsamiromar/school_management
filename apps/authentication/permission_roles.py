def is_student(user):
    if user.is_anonymous:
        return False
    return user.profile.is_student or is_teacher()


def is_teacher(user):
    if user.is_anonymous:
        return False
    return user.profile.is_teacher or is_manager()


def is_manager(user):
    if user.is_anonymous:
        return False
    return user.profile.is_manager or user.is_superuser
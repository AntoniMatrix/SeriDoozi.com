"""
RBAC helpers:
- staff role = belongs to at least one group OR superuser
- permissions = standard Django permissions + custom perms (seeded)
"""


def is_staff_role(user) -> bool:
    return bool(
        user.is_authenticated
        and (user.is_superuser or user.groups.exists() or user.is_staff)
    )


def has_perm(user, perm_codename: str) -> bool:
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return user.has_perm(f"orders.{perm_codename}")

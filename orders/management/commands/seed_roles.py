from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from orders.models import Order


class Command(BaseCommand):
    help = "Seed roles and permissions"

    def handle(self, *args, **kwargs):
        ct = ContentType.objects.get_for_model(Order)

        permissions = {
            "view_all_orders": "Can view all orders",
            "change_order_status": "Can change order status",
            "set_pricing": "Can set pricing",
        }

        perm_objs = {}
        for code, name in permissions.items():
            perm, _ = Permission.objects.get_or_create(
                codename=code,
                name=name,
                content_type=ct,
            )
            perm_objs[code] = perm

        roles = {
            "Workshop Manager": permissions.keys(),
            "Order Operator": ["view_all_orders"],
        }

        for role, perms in roles.items():
            group, _ = Group.objects.get_or_create(name=role)
            for p in perms:
                group.permissions.add(perm_objs[p])

        self.stdout.write(self.style.SUCCESS("✅ Roles seeded"))

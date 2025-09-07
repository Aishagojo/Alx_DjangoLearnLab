from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == "bookshelf":
        Book = apps.get_model("bookshelf", "Book")

        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                try:
                    perm = Permission.objects.get(
                        codename=codename, content_type__app_label="bookshelf"
                    )
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    continue


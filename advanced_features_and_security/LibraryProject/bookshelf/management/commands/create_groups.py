from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Define groups
        groups = {
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
            "Editors": ["can_create", "can_edit"],
            "Viewers": ["can_view"],
        }

        content_type = ContentType.objects.get_for_model(Book)

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                permission, _ = Permission.objects.get_or_create(
                    codename=perm_codename,
                    name=f"Can {perm_codename.replace('can_', '')} book",
                    content_type=content_type,
                )
                group.permissions.add(permission)
            group.save()

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully!"))


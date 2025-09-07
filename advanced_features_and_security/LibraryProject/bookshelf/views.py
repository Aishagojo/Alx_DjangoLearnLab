# Run in Django shell: python3 manage.py shell
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Create groups
groups = ["Admins", "Editors", "Viewers"]
for name in groups:
    Group.objects.get_or_create(name=name)

# Get permissions
book_ct = ContentType.objects.get_for_model(Book)
can_view = Permission.objects.get(codename="can_view", content_type=book_ct)
can_create = Permission.objects.get(codename="can_create", content_type=book_ct)
can_edit = Permission.objects.get(codename="can_edit", content_type=book_ct)
can_delete = Permission.objects.get(codename="can_delete", content_type=book_ct)

# Assign permissions to groups
Group.objects.get(name="Admins").permissions.set([can_view, can_create, can_edit, can_delete])
Group.objects.get(name="Editors").permissions.set([can_create, can_edit])
Group.objects.get(name="Viewers").permissions.set([can_view])


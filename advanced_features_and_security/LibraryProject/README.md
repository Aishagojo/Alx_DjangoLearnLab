## Permissions and Groups Setup

### Custom Permissions
The `Book` model in `bookshelf/models.py` defines custom permissions:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

### Groups
In the Django admin panel, create groups and assign permissions:
- **Viewers**: `can_view`
- **Editors**: `can_create`, `can_edit`
- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`

### Views
Permission checks are enforced in `bookshelf/views.py` using `@permission_required`:
- `view_books` → requires `can_view`
- `create_book` → requires `can_create`
- `edit_book` → requires `can_edit`
- `delete_book` → requires `can_delete`

### Testing
1. Create test users in Django admin.
2. Assign users to different groups.
3. Try accessing views — permissions should restrict access accordingly.


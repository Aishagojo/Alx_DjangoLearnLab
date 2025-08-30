# ALX Submission Checklist

## ✅ Completed Requirements

### Project Setup
- [x] Django project created: social_media_api
- [x] Django app created: accounts
- [x] rest_framework and accounts added to INSTALLED_APPS

### User Authentication  
- [x] Custom user model extends AbstractUser
- [x] Added bio field (Text, max_length=500, blank=True)
- [x] Added profile_picture field (CharField, max_length=255, blank=True, null=True)
- [x] Added followers field (ManyToMany to self, symmetrical=False)
- [x] Token authentication configured
- [x] AUTH_USER_MODEL = 'accounts.CustomUser' set

### API Functionality
- [x] UserRegistrationSerializer implemented
- [x] UserLoginSerializer implemented  
- [x] UserProfileSerializer implemented
- [x] register_user view implemented
- [x] user_login view implemented
- [x] user_profile view implemented

### URL Configuration
- [x] accounts/urls.py with routes for register, login, profile
- [x] Main urls.py includes accounts URLs at api/auth/

### Testing
- [x] Custom user model tested and working
- [x] Serializers tested and validating correctly
- [x] All migrations applied successfully

### Documentation
- [x] README.md created with setup instructions
- [x] requirements.txt created with dependencies

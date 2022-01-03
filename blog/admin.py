from django.contrib import admin

from .models import Post

from django.contrib.auth.models import User

admin.site.register(Post)
admin.site.register(User, UserAdmin)

def create_superuser(username, password=None):
        user = self.create_user(
            username=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


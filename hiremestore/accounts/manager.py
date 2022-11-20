from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number,password=None,**extra_feilds):
        if not phone_number:
            raise ValueError('Phone Number Is required...')

        user=self.model(phone_number=phone_number,**extra_feilds)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,phone_number,password,**extra_feilds):
        extra_feilds.setdefault('is_staff',True)
        extra_feilds.setdefault('is_superuser',True)
        extra_feilds.setdefault('is_active',True)

        return self.create_user(phone_number,password,**extra_feilds)
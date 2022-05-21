from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOISE = (
        ('MALE', 'male'),
        ('FEMALE', 'female')
    )
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(
        max_length=55,
        unique=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=25,
        unique=True,
    )
    password = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOISE, null=True)
    email = models.EmailField(max_length=64, unique=True, null=True, blank=True)
    place = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def imageURL(self):
        if self.image:
            return self.image.url
        return ''

    @classmethod
    def create_user(cls, phone_number, password):
        user: cls = cls.objects.filter(phone_number=phone_number)
        if user:
            return 'This phone number is busy'
        else:
            user.objects.create(
                phone_number=phone_number,
                password=password
            )
            user.set_password(password)
            user.save()
        return user

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.phone_number


class Language(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserLanguages(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='languages')
    degree = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return f'{self.user}`s knowledge of {self.language} is {int(self.degree * 100)}%'


class Profession(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class UserProfessions(models.Model):
    profession = models.ForeignKey('account.Profession', on_delete=models.CASCADE, related_name='professions')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='professions')

    def __str__(self):
        return f'{self.user}`s job is a {self.profession} '


class Specialization(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserSpecialization(models.Model):
    special = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='specials')
    degree = models.FloatField(null=True, blank=True)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='specials')

    def __str__(self):
        return f'{self.user}`s knowledge of {self.special} is {int(self.degree * 100)}%'


class Additional(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserAdditional(models.Model):
    additional = models.ForeignKey(Additional, on_delete=models.CASCADE, related_name='additionals')
    is_active = models.BooleanField(default=False, null=True, blank=True)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='additionals')

    def __str__(self):
        if self.is_active:
            return f'{self.user} knows {self.additional} technology'
        else:
            return f'{self.user} doesn`t knows {self.additional} technology'



from django.db     import models

class User(models.Model):
    social_id         = models.CharField(max_length=100, null=True)
    nickname          = models.CharField(max_length=45)
    mobile            = models.CharField(max_length=50, null=True)
    password          = models.CharField(max_length=200, null=True)
    birth             = models.IntegerField(null=True)
    gender            = models.IntegerField(null=True)
    email             = models.EmailField(max_length=100, null=True)
    profile_image_url = models.URLField(max_length=2000, null=True)
    library_image_url = models.URLField(max_length=2000, null=True)
    usertype          = models.ForeignKey('UserType', on_delete = models.CASCADE)
    subscribe         = models.ManyToManyField('Subscribe', through ='UserSubscribe', related_name = 'users')
    review            = models.ManyToManyField('book.Review', through='book.ReviewLike', related_name='users')

    class Meta:
        db_table = 'users'

class UserType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'usertypes'

class Subscribe(models.Model):
    name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'subscribes'

class UserSubscribe(models.Model):
    user       = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'subscribes')
    subscribe  = models.ForeignKey(Subscribe, on_delete = models.CASCADE, related_name = 'subscribes')
    started_at = models.DateField(auto_now_add = True)
    expired_at = models.DateField(null=True)
    free       = models.BooleanField(default=False)

    class Meta:
        db_table = "users_subscribes"

class PhoneCheck(models.Model):
    check_id     = models.CharField(max_length = 50)
    check_number = models.CharField(max_length = 20)

    class Meta:
        db_table = "phone_checks"
# Generated by Django 3.1.5 on 2021-01-27 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_id', models.CharField(max_length=50)),
                ('check_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'phone_checks',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'subscribes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_id', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=45)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('birth', models.IntegerField(null=True)),
                ('gender', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('profile_image_url', models.URLField(max_length=2000, null=True)),
                ('library_image_url', models.URLField(max_length=2000, null=True)),
                ('library', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='library.library')),
                ('review', models.ManyToManyField(related_name='users', through='book.ReviewLike', to='book.Review')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'usertypes',
            },
        ),
        migrations.CreateModel(
            name='UserSubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateField(auto_now_add=True)),
                ('expired_at', models.DateField(null=True)),
                ('free', models.BooleanField(default=False)),
                ('subscribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribes', to='users.subscribe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribes', to='users.user')),
            ],
            options={
                'db_table': 'users_subscribes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='subscribe',
            field=models.ManyToManyField(related_name='users', through='users.UserSubscribe', to='users.Subscribe'),
        ),
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usertype'),
        ),
    ]

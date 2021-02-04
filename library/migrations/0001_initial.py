from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='나의 서재', max_length=45)),
            ],
            options={
                'db_table': 'libraries',
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelves', to='library.library')),
            ],
            options={
                'db_table': 'shelves',
            },
        ),
    ]

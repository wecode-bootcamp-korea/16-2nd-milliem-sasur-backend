from django.db     import models

class Library(models.Model):
    name = models.CharField(max_length=45, default='나의 서재')

    class Meta:
        db_table = 'libraries'

class Shelf(models.Model):
    name    = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='shelves')

    class Meta:
<<<<<<< HEAD
        db_table = 'shelves'
=======
        db_table = 'shelves'
>>>>>>> 7d1eec5b17691b3ccf74b0211fbf5017380dd500

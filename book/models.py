from django.db import models


class Book(models.Model):
    title            = models.CharField(max_length=45)
    summary          = models.TextField(null=True)
    translator       = models.CharField(max_length=20, null=True)
    sub_title        = models.CharField(max_length=200, null=True)
    description      = models.TextField(null=True)
    page             = models.PositiveIntegerField(null=True)
    capacity         = models.IntegerField(null=True)
    pub_date         = models.DateField()
    launched_date    = models.DateField()
    contents         = models.TextField(null=True)
    publisher_review = models.TextField(null=True)
    image_url        = models.URLField(max_length=2045, null=True)
    purchase_url     = models.URLField(max_length=2045, null=True)
    author           = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")
    category         = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books")
    publisher        = models.ForeignKey("Publisher", on_delete=models.CASCADE, related_name="books")
    shelf            = models.ManyToManyField("library.Shelf", related_name="books")
    class Meta:
        db_table = "books"

class Review(models.Model):
    user        = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    book        = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    pub_date    = models.DateField()
    body_text   = models.TextField()
    class Meta:
        db_table = "reviews"

class ReviewLike(models.Model):
    user    = models.ForeignKey("users.User", on_delete=models.CASCADE)
    review  = models.ForeignKey("Review",      on_delete=models.CASCADE)
    class Meta:
        db_table = "review_likes"

class Author(models.Model):
    name              = models.CharField(max_length=20)
    description       = models.TextField()
    profile_image_url = models.URLField(max_length=2000, null=True)
    class Meta:
        db_table = "authors"

class Publisher(models.Model):
    name        = models.CharField(max_length=20)
    description = models.TextField()
    class Meta:
        db_table = "publishers"

class Subcategory(models.Model):
    name     = models.CharField(max_length=45)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="subcategories")
    class Meta:
        db_table = "subcategories"

class Category(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = "categories"


from django.db import models

TEXT_LEN_MIN = 400


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/blog', default=None)
    text = models.TextField()

    def __str__(self):
        return self.title

    def short_text(self):
        if len(self.text) > TEXT_LEN_MIN:
            return self.text[:TEXT_LEN_MIN]
        else:
            return self.text


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/shop/', default=None)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta():
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comments(models.Model):
    class Meta():
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_article = models.ForeignKey(Article)

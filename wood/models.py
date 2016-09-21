from django.db import models
from django.utils import timezone

TEXT_LEN_MIN = 200


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/blog', default=None)
    text = models.TextField()

    def __str__(self):
        return self.title

    def short_text(self):
        short = self.text[:TEXT_LEN_MIN].split(' ')[:-1]
        return ' '.join(short) + ' >>>'


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/shop/', default=None)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    # Нужно ли поле "amount" для каждого товара?


class Category(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    def __str__(self):
        return self.comments_text[:30]

    comments_text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(default=timezone.now)
    comments_article = models.ForeignKey(Article)


class Purchase(models.Model):
    product = models.ForeignKey(Product)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=13)
    address = models.CharField(max_length=200, blank=True)
    comment = models.TextField(blank=True)
    buy_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name + " " + self.product.name

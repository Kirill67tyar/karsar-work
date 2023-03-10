from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

from common.utils import custom_slugify


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Наименование товара'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(custom_slugify(str(self.name)))
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse_lazy(
    #         'catalog:list_category',
    #         kwargs={
    #             'category_slug': self.slug,
    #         }
    #     )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        to='catalog.Category',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True
    )
    photo = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        verbose_name='Изображение'
    )
    description = models.TextField(
        blank=True
    )
    available = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    # created = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name='Создан'
    # )
    # updated = models.DateTimeField(
    #     auto_now=True,
    #     verbose_name='Изменён'
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (
            ('id', 'slug',),  # индекс по двум полям (не заменяет id или pk)
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(custom_slugify(str(self.name)))
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse_lazy(
    #         'catalog:detail_product',
    #         kwargs={
    #             'pk': self.pk,
    #             'slug': self.slug,
    #         }
    #     )

    def __str__(self):
        return self.name


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория (напр., MP3-плееры)")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Бренд (Sony, Apple, Nintendo)")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    CONDITION_CHOICES = [
        ('mint', 'Идеальное (Как новый/В пленке)'),
        ('good', 'Отличное (Минимальные следы использования)'),
        ('used', 'Хорошее (Есть царапины/потертости)'),
        ('refurbished', 'Восстановленный (Заменен аккумулятор/экран)'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name="Производитель")
    title = models.CharField(max_length=200, verbose_name="Название (напр., iPod Classic 5G)")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-слаг")
    
    release_year = models.PositiveIntegerField(verbose_name="Год выпуска модели", blank=True, null=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='good', verbose_name="Состояние")
    battery_life = models.CharField(max_length=100, blank=True, verbose_name="Состояние аккумулятора")
    bundle_includes = models.TextField(blank=True, verbose_name="Комплектация")
    
    storage_capacity = models.CharField(max_length=50, blank=True, verbose_name="Объем памяти")
    megapixels = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, verbose_name="Мегапиксели (для фотиков)")
    
    description = models.TextField(blank=True, verbose_name="Описание гаджета")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Главное фото")
    stock = models.PositiveIntegerField(default=1, verbose_name="Количество в наличии")
    is_available = models.BooleanField(default=True, verbose_name="Доступен для покупки")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Гаджет"
        verbose_name_plural = "Гаджеты"

    def __str__(self):
        return f"{self.brand} {self.title} ({self.release_year})"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/', verbose_name="Фото дефекта/ракурса")
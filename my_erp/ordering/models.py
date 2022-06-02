from django.db import models


class Customers(models.Model):
    customers_mame = models.CharField(max_length=150, verbose_name='Наименование заказчика')
    customers_contact_person = models.CharField(max_length=250, verbose_name='Контактное лицо')
    customers_address = models.CharField(max_length=150, verbose_name='Адрес заказчика')

    def __str__(self):
        return self.customers_mame

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['customers_mame']


class Orders(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.PROTECT, verbose_name='Заказчик')
    name_of_goods = models.CharField(max_length=150, verbose_name='Наименование товара')
    date_of_contract = models.DateField(verbose_name='Дата подписания договора')
    date_of_delivery = models.DateField(verbose_name='Дата поставки')
    contract_status = models.CharField(max_length=150, verbose_name='Состояние заказа')

    def __str__(self):
        return self.name_of_goods

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_of_contract']


class Requirements(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.PROTECT, verbose_name='Заказ')
    docs = models.FileField(upload_to='docs/%Y/%m/%d/', verbose_name='Документы', blank=True)
    text = models.CharField(max_length=250, verbose_name='Тех. требования кратко', blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Тех. требования'
        verbose_name_plural = 'Тех. требования'
        ordering = ['id']


class Comments(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.PROTECT, verbose_name='Заказ')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')
    author = models.CharField(max_length=150, verbose_name='Автор комментария')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']



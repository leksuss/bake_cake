# Generated by Django 4.2.3 on 2023-07-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakeshopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='decor',
            options={'verbose_name': 'Оформление', 'verbose_name_plural': 'Оформление'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'Начинка', 'verbose_name_plural': 'Начинки'},
        ),
        migrations.AlterField(
            model_name='berry',
            name='name',
            field=models.CharField(blank=True, choices=[('WITHOUT', 'Без ягод'), ('RASPBERRY', 'Малина'), ('BLUEBERRY', 'Голубика'), ('BlACKBERRY', 'Ежевика'), ('STRAWBERRY', 'Клубника')], default='WITHOUT', max_length=256, verbose_name='Название ягоды'),
        ),
        migrations.AlterField(
            model_name='decor',
            name='name',
            field=models.CharField(blank=True, choices=[('WITHOUT', 'Без декора'), ('PISTACHIO', ' Фисташки'), ('HAZELNUT', ' Фундук'), ('MERINQUE', 'Безе'), ('PECAN', 'Пекан'), ('MARSHMALLOW', 'Маршмеллоу'), ('MARZIPAN', 'Марципан')], default='WITHOUT', max_length=256, verbose_name='Наименование декора'),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(blank=True, choices=[('ONE', 'Один'), ('TWO', 'Два'), ('THREE', 'Три')], default='EMPTY', max_length=256, verbose_name='Уровни торта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('NEW', 'Создан'), ('PAID', 'Оплачен'), ('COOKING', 'Готовится'), ('IN_DELIVERY', 'В доставке'), ('DELIVERED', 'Доставлен')], default='NEW', max_length=256, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='shape',
            name='name',
            field=models.CharField(blank=True, choices=[('CIRCLE', 'Круг'), ('SQUARE', 'Квадрат'), ('RECTANGLE', 'Прямоугольник')], default='CIRCLE', max_length=256, verbose_name='Наименование формы'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(blank=True, choices=[('WITHOUT', 'Без начинки'), ('WHITE_SOUCE', 'Белый соус'), ('CARAMEL', 'Карамельный'), ('MAPLE', 'Кленовый'), ('BILBERRY', 'Черничный'), ('WHITE_CHOCOLATE', 'Молочный шоколад'), ('STRAWBERRY', 'Клубничный')], default='WITHOUT', max_length=256, verbose_name='Наименование начинки'),
        ),
    ]
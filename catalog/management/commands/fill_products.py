from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Наушники',
             'description': 'Полноразмерные',
             'image': '',
             'category': 'Аудиотехника',
             'price_for_one': '5800'},
            {'name': 'Кофемашина',
             'description': 'Автоматическая',
             'image': '',
             'category': 'Техника для кухни',
             'price_for_one': '30000'},
            {'name': 'Робот-пылесос',
             'description': 'Для влажной уборки',
             'image': '',
             'category': 'Техника для дома',
             'price_for_one': '34000'},
            {'name': 'Датчик открытия дверей и окон',
             'description': 'Экосистема Яндекс',
             'image': '',
             'category': 'Умный дом',
             'price_for_one': '2000'},
        ]

        products_for_create = []
        for product in product_list:
            products_for_create.append(
                Product(**product)
            )

        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_create)

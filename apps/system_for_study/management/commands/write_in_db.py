from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.system_for_study.models import Product, Lesson, Group


class Command(BaseCommand):
    help = 'Populate models with initial data'

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(username='user', password='password')

        products_data = [
            {'name': 'Курс Python', 'start_date_time': timezone.now(), 'cost': 10.50},
            {'name': 'Курс Rust', 'start_date_time': timezone.now(), 'cost': 15.75},
            {'name': 'Course English', 'start_date_time': timezone.now(), 'cost': 20.00},
        ]

        lessons_data = [
            {'title': 'Lesson 1', 'video_link': 'https://example.com/video1'},
            {'title': 'Lesson 2', 'video_link': 'https://example.com/video2'},
            {'title': 'Lesson 3', 'video_link': 'https://example.com/video3'},
            {'title': 'Lesson 4', 'video_link': 'https://example.com/video1'},
            {'title': 'Lesson 5', 'video_link': 'https://example.com/video2'},
            {'title': 'Lesson 6', 'video_link': 'https://example.com/video3'},
        ]

        groups_data = [
            {'name': 'Group 1', 'min_users': 5, 'max_users': 10},
            {'name': 'Group 2', 'min_users': 3, 'max_users': 8},
            {'name': 'Group 3', 'min_users': 4, 'max_users': 7},
        ]

        # Создаем продукты
        for data in products_data:
            product = Product.objects.create(
                name=data['name'],
                start_date_time=data['start_date_time'],
                cost=data['cost'],
                creator=user
            )

        # Создаем уроки
        for data in lessons_data:
            lesson = Lesson.objects.create(
                product=Product.objects.first(),
                title=data['title'],
                video_link=data['video_link']
            )

        # Создаем группы
        for data in groups_data:
            group = Group.objects.create(
                product=Product.objects.first(),
                name=data['name'],
                min_users=data['min_users'],
                max_users=data['max_users']
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))

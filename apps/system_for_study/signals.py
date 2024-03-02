from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import AccessRequest, Group


@receiver(post_save, sender=AccessRequest)
def handle_access_request(sender, instance, created, **kwargs):
    if instance.status == 'approved':
        product = instance.product
        if product.start_date_time <= timezone.now():
            distribute_user_to_group_when_started(instance.user, product)
        else:
            redistribute_groups(product)


def distribute_user_to_group_when_started(user, product):
    groups = Group.objects.filter(product=product).annotate(num_students=Count('students')).order_by('num_students')
    if groups.exists():
        target_group = groups.first()
        for group in groups[1:]:
            if group.num_students < target_group.num_students:
                target_group = group
        if target_group.num_students < target_group.max_users:
            target_group.students.add(user)
        else:
            redistribute_groups(product)


def redistribute_groups(product):
    groups = Group.objects.filter(product=product).annotate(num_students=Count('students')).order_by('num_students')
    num_groups = groups.count()
    if num_groups > 1:
        students_per_group = sum(group.num_students for group in groups) // num_groups
        for i, group in enumerate(groups):
            if i == num_groups - 1:
                group_students = students_per_group + sum(group.num_students for group in groups[i + 1:])
            else:
                group_students = students_per_group
            while group.num_students > group_students:
                student_to_move = group.students.last()
                new_group = groups[i + 1] if i < num_groups - 1 else groups[i - 1]
                group.students.remove(student_to_move)
                new_group.students.add(student_to_move)

from django.db import migrations


def Order(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Order = apps.get_model('orders', 'Order')
    Order.objects.all()

def Order_Items(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Order_Items = apps.get_model('orders', 'Order_Items')
    Order_Items.objects.all()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_created_alter_order_items_created'),
    ]

    operations = [
        migrations.RunPython(Order),
        migrations.RunPython(Order_Items),
    ]

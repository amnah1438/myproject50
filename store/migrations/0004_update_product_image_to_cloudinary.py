from django.db import migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(
                verbose_name='صورة المنتج',
                folder='products',
                max_length=255,
                blank=True,
                null=True
            ),
        ),
    ]

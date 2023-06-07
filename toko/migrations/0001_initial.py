# Generated by Django 4.2.1 on 2023-06-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdukItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=100)),
                ('harga', models.FloatField()),
                ('harga_diskon', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('deskripsi', models.TextField()),
                ('gambar', models.ImageField(upload_to='product_pics')),
                ('label', models.CharField(choices=[('NEW', 'primary'), ('SALE', 'info'), ('BEST', 'danger')], max_length=4)),
                ('kategori', models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2)),
            ],
        ),
    ]

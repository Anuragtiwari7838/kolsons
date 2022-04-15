# Generated by Django 3.2.7 on 2022-04-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kolsons', '0005_merge_20220415_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Colour_Of_light',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Contact',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Contact_Material',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Front_Bezel_Colour',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Front_Bezel_Material',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Front_Dimension',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Front_Ring_Colour',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Front_Ring_Material',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Lens_Colour',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Lens_Material',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Lens_Optics',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Lens_Shape',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Mounting_Style',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Operating_Current',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Operating_Voltage',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Switching_Action',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='Terminal',
            field=models.CharField(blank=True, default='Not Available', max_length=200),
        ),
    ]

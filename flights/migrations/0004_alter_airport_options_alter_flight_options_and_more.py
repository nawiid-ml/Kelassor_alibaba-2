# Generated by Django 4.2 on 2023-12-14 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_flight_origin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airport',
            options={'verbose_name': 'Kelaasor Airport'},
        ),
        migrations.AlterModelOptions(
            name='flight',
            options={'verbose_name': 'Kelaasor Flight'},
        ),
        migrations.AddField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='destination_airport', to='flights.airport'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='no',
            field=models.CharField(max_length=10, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.FloatField(help_text='Price in Rial'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Client ID',default=1000)),
                ('name', models.CharField(max_length=100, verbose_name='Client')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='client_logos/', verbose_name='Logo')),
                ('on_board_date', models.DateField(verbose_name='On Board Date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('status', models.CharField(choices=[('on_boarded', 'On Boarded'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='on_boarded', max_length=20, verbose_name='Status')),
            ],
        ),
    ]

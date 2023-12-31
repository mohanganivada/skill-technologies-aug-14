# Generated by Django 4.2.4 on 2023-08-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Client ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('On Boarded', 'On Boarded'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='on_boarded', max_length=20, verbose_name='Status'),
        ),
    ]

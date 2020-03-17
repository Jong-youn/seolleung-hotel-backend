from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(null=True)),
                ('stay_night', models.IntegerField(null=True)),
                ('how_many_adults', models.IntegerField(null=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
                ('request', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=100)),
                ('confirmation_code', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Date')),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.Reservation')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Room')),
            ],
            options={
                'db_table': 'vacancies',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_point', models.IntegerField(null=True)),
                ('used_point', models.IntegerField(null=True)),
                ('total_point', models.IntegerField(null=True)),
                ('is_accumulated', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.Reservation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User')),
            ],
            options={
                'db_table': 'points',
            },
        ),
    ]

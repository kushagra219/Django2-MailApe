# Generated by Django 2.0.13 on 2020-03-02 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('confirmed', models.BooleanField(default=False)),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.MailingList')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together={('email', 'mailing_list')},
        ),
    ]

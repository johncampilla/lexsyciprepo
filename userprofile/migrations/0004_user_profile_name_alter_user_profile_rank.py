# Generated by Django 4.0.5 on 2022-06-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_user_profile_access_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='rank',
            field=models.CharField(choices=[('MANAGING PARTNER', 'MANAGING PARTNER'), ('PARTNER', 'PARTNER'), ('ASSOCIATES', 'ASSOCIATES'), ('SECRETARY', 'SECRETARY'), ('PARALEGAL', 'PARALEGAL'), ('MIS STAFF', 'MIS STAFF'), ('SYSTEM ADMIN', 'SYSTEM ADMIN'), ('ACCOUNTING STAFF', 'ACCOUNTING STAFF'), ('DATA ENCODER', 'DATA ENCODER'), ('FRONTEND DEVELOPER', 'FRONTEND DEVELOPER'), ('BACKEND DEVELOPER', 'BACKEND DEVELOPER'), ('SYSTEM DEVELOPER', 'SYSTEM DEVELOPER'), ('LOCAL CIENT', 'LOCAL CIENT'), ('FOREIGN CIENT', 'FOREIGN CIENT')], max_length=30, null=True),
        ),
    ]

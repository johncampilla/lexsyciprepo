# Generated by Django 4.0.4 on 2022-05-05 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0013_alter_applicant_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_detail',
            name='duecode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapps.duecode'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='category',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Inventor', 'Inventor'), ('Individual', 'Individual')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Months', 'In Months'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('PCT Publication Date', 'PCT Publication Date'), ('Publication Date', 'PublicationDate'), ('Registration Date', 'RegistrationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Priority Date', 'Priority Date'), ('Renewal Date', 'Renewal Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Application Date', 'Application Date'), ('Document Date', 'Document Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ip_matters',
            name='status',
            field=models.CharField(blank=True, choices=[('REGISTERED', 'REGISTERED'), ('ABANDONED', 'ABANDONED'), ('TRANSFERRED', 'TRANSFERRED'), ('CANCELLED', 'CANCELLED'), ('PENDING', 'PENDING'), ('RENEWAL', 'RENEWAL')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mailsin',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Personal', 'Personal'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(choices=[('Others', 'Others'), ('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Personal', 'Personal'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]

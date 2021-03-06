# Generated by Django 2.0 on 2019-03-17 08:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TasKManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('password', models.CharField(max_length=40)),
                ('confrom_pass', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='teamcreater',
            name='Users',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Descripton',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Team',
        ),
        migrations.AddField(
            model_name='task',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='task',
            name='Assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TasKManager.SignUp'),
        ),
        migrations.AlterField(
            model_name='task',
            name='Status',
            field=models.CharField(choices=[('INPROGRESS', 'Inprogress'), ('NOT ASSIGNED', 'Not assigned'), ('DONE', 'done'), ('PLANNED', 'Planned')], default='NOT ASSIGNED', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='Title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='Creator_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='TasKManager.SignUp'),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='TasKManager.SignUp'),
        ),
        migrations.DeleteModel(
            name='TeamCreater',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]

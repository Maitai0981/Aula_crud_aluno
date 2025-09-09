from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('serie', models.CharField(blank=True, max_length=50, null=True, verbose_name='Série')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('OUTRO', 'Outro')], max_length=10, null=True, verbose_name='Sexo')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='alunos/', verbose_name='Foto')),
                ('data', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Cadastro')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'db_table': 'tb_alunos',
                'ordering': ['nome'],
            },
        ),
    ]
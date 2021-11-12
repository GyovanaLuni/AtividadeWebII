# Generated by Django 3.2.3 on 2021-06-02 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoPesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500, verbose_name='descrição')),
                ('inicio', models.DateField(verbose_name='início')),
                ('fim', models.DateField()),
                ('aprovado', models.BooleanField(default=False, verbose_name='Está institucionalizado?')),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.projetopesquisa')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='ProjetoTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.projetopesquisa')),
            ],
        ),
        migrations.CreateModel(
            name='CoordenadorProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.professor')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.projetopesquisa')),
            ],
        ),
        migrations.CreateModel(
            name='ColaboradorProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.professor')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.projetopesquisa')),
            ],
        ),
    ]
# Generated by Django 3.2.4 on 2021-07-10 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000, unique=True)),
                ('city', models.CharField(blank=True, max_length=10000)),
                ('country', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000, unique=True)),
                ('author_id', models.BigIntegerField()),
                ('total_number_of_papers_in_field', models.BigIntegerField(default=0, null=True)),
                ('affiliation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webo_app.affliation')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorKeywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=10000, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('author_id', models.BigIntegerField()),
                ('total_number_of_papers_in_field', models.BigIntegerField(default=0, null=True)),
                ('affiliation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webo_app.affliation')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=10000, unique=True)),
                ('total_number_of_papers', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_no', models.CharField(blank=True, max_length=10000, null=True, unique=True)),
                ('fund_sponsor', models.CharField(blank=True, max_length=10000, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPaperDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('doi', models.CharField(max_length=10000)),
                ('eid', models.CharField(max_length=10000)),
                ('year', models.BigIntegerField(default=0)),
                ('document_type', models.CharField(max_length=10000)),
                ('link', models.CharField(max_length=10000)),
                ('cited_by', models.IntegerField(default=0)),
                ('open_access', models.IntegerField()),
                ('author_count', models.IntegerField()),
                ('affiliation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webo_app.affliation')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='webo_app.author')),
                ('author_keyword', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webo_app.authorkeywords')),
                ('co_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='co_author', to='webo_app.coauthor')),
                ('research_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webo_app.researchfield')),
                ('sponsor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webo_app.sponsor')),
            ],
        ),
    ]

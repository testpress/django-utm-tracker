# Generated by Django 3.2.12 on 2022-03-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utm_tracker", "0007_alter_leadsource_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leadsource",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="leadsource",
            name="medium",
            field=models.CharField(
                help_text="utm_medium: Identifies what type of link was used, such as cost per click or email.",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="leadsource",
            name="source",
            field=models.CharField(
                help_text="utm_source: Identifies which site sent the traffic, and is a required parameter.",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="leadsource",
            name="term",
            field=models.CharField(
                blank=True,
                help_text="utm_term: Identifies search terms.",
                max_length=100,
            ),
        ),
    ]

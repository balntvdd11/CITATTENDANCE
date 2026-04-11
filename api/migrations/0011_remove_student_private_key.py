from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_add_private_key_back"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="private_key",
        ),
    ]

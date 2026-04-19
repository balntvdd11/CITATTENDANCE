# Generated migration to add device_base_fingerprint field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_student_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='device_base_fingerprint',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

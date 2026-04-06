from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_process", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studymaterial",
            name="title",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="studymaterial",
            name="original_filename",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddIndex(
            model_name="studymaterial",
            index=models.Index(
                fields=["user", "uploaded_at"],
                name="fp_mat_user_uploaded",
            ),
        ),
        migrations.AlterModelOptions(
            name="studymaterial",
            options={"ordering": ["-uploaded_at"]},
        ),
    ]

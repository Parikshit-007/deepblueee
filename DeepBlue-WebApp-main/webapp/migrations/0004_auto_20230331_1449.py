from django.db import migrations

def set_default_user(apps, schema_editor):
    UserProfile = apps.get_model('webapp', 'UserProfile')
    for profile in UserProfile.objects.all():
        profile.user = None
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_userprofile_related_user_id_and_more'),
    ]

    operations = [
        migrations.RunPython(set_default_user),
    ]

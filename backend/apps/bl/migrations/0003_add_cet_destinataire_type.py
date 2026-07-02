from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl', '0002_remove_bonlivraison_bon_commande_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonlivraison',
            name='destinataire_type',
            field=models.CharField(
                choices=[
                    ('ELIMINATEUR', 'Éliminateur de déchets'),
                    ('VALORISATEUR', 'Valorisateur de déchets'),
                    ('CET', "Centre d'Enfouissement Technique"),
                ],
                max_length=20,
            ),
        ),
    ]

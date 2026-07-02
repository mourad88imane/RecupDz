import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recuperateurs', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BonCommande',
            fields=[
                ('id',             models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero',         models.CharField(blank=True, max_length=30, unique=True)),
                ('client_nom',     models.CharField(blank=True, max_length=300)),
                ('client_adresse', models.CharField(blank=True, max_length=500)),
                ('date_commande',  models.DateField()),
                ('lignes',         models.JSONField(blank=True, default=list)),
                ('tva_pct',        models.DecimalField(decimal_places=2, default=19, max_digits=5)),
                ('observations',   models.TextField(blank=True)),
                ('statut',         models.CharField(
                    choices=[
                        ('BROUILLON', 'Brouillon'),
                        ('EMIS',      'Émis'),
                        ('VALIDE',    'Validé'),
                        ('ARCHIVE',   'Archivé'),
                    ],
                    default='BROUILLON', max_length=15,
                )),
                ('created_at',     models.DateTimeField(auto_now_add=True)),
                ('created_by',     models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to=settings.AUTH_USER_MODEL,
                )),
                ('recuperateur',   models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='bons_commande',
                    to='recuperateurs.recuperateur',
                )),
            ],
            options={'ordering': ['-created_at'], 'verbose_name': 'Bon de Commande'},
        ),
    ]

from django.db import models
from django.conf import settings


class BonLivraison(models.Model):
    """Bon de Livraison — émis par le récupérateur à destination d'un
    éliminateur, d'un valorisateur ou d'un Centre d'Enfouissement Technique (CET).
    Les CET n'acceptent pas les déchets spéciaux (S) ni les déchets spéciaux
    dangereux (SD/DSD) — uniquement les déchets ménagers et assimilés."""

    DESTINATAIRE_CHOICES = [
        ('ELIMINATEUR',  'Éliminateur de déchets'),
        ('VALORISATEUR', 'Valorisateur de déchets'),
        ('CET',          "Centre d'Enfouissement Technique"),
    ]
    STATUT_CHOICES = [
        ('BROUILLON', 'Brouillon'),
        ('EMIS',      'Émis'),
        ('VALIDE',    'Validé'),
        ('ARCHIVE',   'Archivé'),
    ]

    numero               = models.CharField(max_length=30, unique=True, blank=True)
    recuperateur         = models.ForeignKey('recuperateurs.Recuperateur', on_delete=models.PROTECT,
                                              related_name='bons_livraison')
    destinataire_type    = models.CharField(max_length=20, choices=DESTINATAIRE_CHOICES)
    destinataire         = models.ForeignKey('operateurs.Operateur', on_delete=models.PROTECT,
                                              related_name='bons_livraison_recus')

    date_livraison        = models.DateField()

    # Lignes : [{description, quantite, unite, stockage}, ...]
    lignes               = models.JSONField(default=list, blank=True)

    chauffeur_nom          = models.CharField(max_length=200, blank=True)
    camion_immatriculation = models.CharField(max_length=50, blank=True)

    statut               = models.CharField(max_length=15, choices=STATUT_CHOICES, default='BROUILLON')
    observations         = models.TextField(blank=True)
    created_by           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                              null=True, blank=True)
    created_at           = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering     = ['-created_at']
        verbose_name = 'Bon de Livraison'

    def save(self, *args, **kwargs):
        if not self.numero:
            import uuid
            from datetime import date
            self.numero = f"PBL{date.today().strftime('%y')}{str(uuid.uuid4())[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero

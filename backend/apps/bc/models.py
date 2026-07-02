from django.db import models
from django.conf import settings


class BonCommande(models.Model):
    """Bon de Commande (BC) — document commercial émis par le récupérateur
    listant les déchets avec prix unitaires, TVA et total TTC."""

    STATUT_CHOICES = [
        ('BROUILLON', 'Brouillon'),
        ('EMIS',      'Émis'),
        ('VALIDE',    'Validé'),
        ('ARCHIVE',   'Archivé'),
    ]

    numero         = models.CharField(max_length=30, unique=True, blank=True)
    recuperateur   = models.ForeignKey('recuperateurs.Recuperateur', on_delete=models.PROTECT,
                                        related_name='bons_commande')
    client_nom     = models.CharField(max_length=300, blank=True)
    client_adresse = models.CharField(max_length=500, blank=True)
    date_commande  = models.DateField()

    # Lignes : [{description, quantite, unite, prix_unitaire}]
    lignes         = models.JSONField(default=list, blank=True)

    tva_pct        = models.DecimalField(max_digits=5, decimal_places=2, default=19)
    observations   = models.TextField(blank=True)
    statut         = models.CharField(max_length=15, choices=STATUT_CHOICES, default='BROUILLON')
    created_by     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                        null=True, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering     = ['-created_at']
        verbose_name = 'Bon de Commande'

    def save(self, *args, **kwargs):
        if not self.numero:
            import uuid
            from datetime import date
            self.numero = f"PBC{date.today().strftime('%y')}{str(uuid.uuid4())[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero

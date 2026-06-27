from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import io

MOIS_FR = [
    '', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
    'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre',
]

DOTS = '.' * 45


def _texte_date(date_str):
    """Convertit une date ISO (YYYY-MM-DD) en 'le JJ du mois de MOIS AAAA'."""
    if not date_str:
        return DOTS, DOTS
    try:
        annee, mois, jour = str(date_str).split('-')[:3]
        mois_nom = MOIS_FR[int(mois)]
        return f"{int(jour)}", f"{mois_nom} {annee}"
    except Exception:
        return DOTS, DOTS


def generate_pv_pdf(data: dict) -> bytes:
    """
    Procès-verbal d'incinération des Déchets Spéciaux (DS) / Déchets Spéciaux
    Dangereux (DSD) — document officiel délivré par l'installation d'incinération
    (éliminateur) certifiant la destruction des déchets remis par un récupérateur.
    """
    buffer = io.BytesIO()
    BLACK = colors.black

    def st(name, **kw):
        return ParagraphStyle(name, **kw)

    TITLE  = st('TITLE',  fontName='Helvetica-Bold', fontSize=11, alignment=TA_CENTER, leading=14)
    OBJET  = st('OBJET',  fontName='Helvetica-Bold', fontSize=9.5, leading=13)
    LABEL  = st('LABEL',  fontName='Helvetica', fontSize=9.5, leading=16)
    BODY   = st('BODY',   fontName='Helvetica', fontSize=9.5, leading=15, alignment=TA_JUSTIFY)
    TH     = st('TH',     fontName='Helvetica-Bold', fontSize=9, leading=12)
    TD     = st('TD',     fontName='Helvetica', fontSize=9, leading=12)

    def remplir(valeur):
        v = str(valeur).strip() if valeur else ''
        return DOTS if not v else f"<b>{v}</b>"

    def champ(label, valeur, suite=''):
        return Paragraph(f"{label} {remplir(valeur)}{suite}", LABEL)

    doc = SimpleDocTemplate(buffer, pagesize=A4,
        topMargin=2*cm, bottomMargin=2*cm, leftMargin=2.5*cm, rightMargin=2.5*cm)
    story = []

    # ── En-tête — identité de l'installation d'incinération ──────────────────
    story.append(champ('Raison Sociale', data.get('raison_sociale')))
    story.append(Spacer(1, 6))
    story.append(champ("Agrément d'exploitation N° :", data.get('agrement_exploitation')))
    story.append(Spacer(1, 6))
    story.append(champ('Adresse :', data.get('adresse')))
    story.append(Spacer(1, 6))
    story.append(champ('RC :', data.get('rc')))
    story.append(Spacer(1, 6))
    story.append(champ('NIF :', data.get('nif')))
    story.append(Spacer(1, 6))
    story.append(champ('ART :', data.get('art')))
    story.append(Spacer(1, 6))
    story.append(champ('Téléphone :', data.get('telephone')))
    story.append(Spacer(1, 18))

    story.append(Paragraph(
        'Objet : Incinération des Déchets Spéciaux (DS) / Déchets Spéciaux Dangereux (DSD)', OBJET))
    story.append(Spacer(1, 14))

    pv_numero = data.get('pv_numero') or DOTS
    story.append(Paragraph(
        f"Procès-verbal d'incinération n° <b>{pv_numero}</b> du <b>{data.get('date_inspection') or DOTS}</b>",
        TITLE))
    story.append(Spacer(1, 16))

    jour, mois_annee = _texte_date(data.get('date_inspection'))
    societe = data.get('raison_sociale') or DOTS
    site    = data.get('site_incineration') or data.get('adresse') or DOTS
    story.append(Paragraph(
        f"L'an deux mille, le {jour} du mois de {mois_annee}, il a été procédé par "
        f"la société : {societe} sur son site d'incinération situé à : {site}",
        BODY))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        'à la destruction par procédé d\'incinération des déchets suivants :', BODY))
    story.append(Spacer(1, 8))

    dechets = data.get('dechets') or [{
        'designation': data.get('designation_dechet') or data.get('designation') or '',
        'quantite':    data.get('quantite') or '',
    }]
    rows = [[Paragraph('Désignation', TH), Paragraph('Quantité', TH)]]
    for d in dechets:
        rows.append([Paragraph(str(d.get('designation') or ''), TD), Paragraph(str(d.get('quantite') or ''), TD)])
    table = Table(rows, colWidths=[11*cm, 4*cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.6, BLACK),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(table)
    story.append(Spacer(1, 16))

    qte_totale = data.get('quantite_totale')
    if not qte_totale and data.get('quantite'):
        qte_totale = f"{data.get('quantite')} {data.get('unite_display') or data.get('unite') or ''}".strip()
    story.append(champ('Une quantité totale de', qte_totale, suite=f" récupérée par {remplir(data.get('recuperateur_nom'))}"))
    story.append(Spacer(1, 6))
    story.append(champ('Sise :', data.get('recuperateur_adresse')))
    story.append(Spacer(1, 6))
    story.append(champ('Agrément n°', data.get('recuperateur_agrement'), suite=f" du {remplir(data.get('recuperateur_agrement_date'))}"))
    story.append(Spacer(1, 14))

    story.append(champ('Les déchets proviennent de :', data.get('generateur_nom')))
    story.append(Spacer(1, 6))
    story.append(champ('sise', data.get('generateur_adresse')))
    story.append(Spacer(1, 18))

    story.append(Paragraph(
        'Nous certifions que les déchets susmentionnés ont été intégralement détruits '
        'par incinération conformément à la réglementation en vigueur et aux '
        'prescriptions techniques de notre installation.', BODY))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Le présent procès-verbal est établi pour servir et valoir ce que de droit.', BODY))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()

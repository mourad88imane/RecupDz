"""
Génération du PDF Bon de Livraison (BL) — reproduit le formulaire papier du
récupérateur : en-tête avec logo et identité de l'entreprise (agrément,
RC/NIF/NA/NIS), client destinataire, tableau des déchets livrés, puis
chauffeur et signature du gérant.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import io

BLACK = colors.black
GREEN = colors.HexColor('#3B6D11')
COL   = 17 * cm


def _recuperateur_info(data):
    from apps.recuperateurs.models import Recuperateur
    rec_id = data.get('recuperateur') or data.get('recuperateur_id')
    if rec_id:
        try:
            r = Recuperateur.objects.get(pk=rec_id)
            agr = r.agrement_actif
            return {
                'nom':          r.nom_commercial or r.nom_raison_sociale,
                'agrement_num': agr.numero_agrement if agr else '',
                'agrement_date':agr.date_delivrance.strftime('%d/%m/%Y') if agr and agr.date_delivrance else '',
                'adresse':      r.adresse or '',
                'commune':      r.commune or '',
                'code_postal':  r.code_postal or '',
                'rc':           r.registre_commerce or '',
                'nif':          r.nif or '',
                'na':           r.numero_article or '',
                'nis':          r.nis or '',
                'responsable':  r.responsable or '',
                'logo_path':    r.logo.path if r.logo else None,
            }
        except Recuperateur.DoesNotExist:
            pass
    return {'nom': data.get('recuperateur_nom') or '', 'agrement_num': '', 'agrement_date': '',
            'adresse': '', 'commune': '', 'code_postal': '', 'rc': '', 'nif': '', 'na': '', 'nis': '',
            'responsable': '', 'logo_path': None}


def _destinataire_info(data):
    from apps.operateurs.models import Operateur
    dest_id = data.get('destinataire') or data.get('destinataire_id')
    if dest_id:
        try:
            o = Operateur.objects.get(pk=dest_id)
            return {'nom': o.raison_sociale, 'adresse': o.adresse or ''}
        except Operateur.DoesNotExist:
            pass
    return {'nom': data.get('destinataire_nom') or '', 'adresse': data.get('destinataire_adresse') or ''}


def generate_bl_pdf(data: dict) -> bytes:
    buffer = io.BytesIO()

    def ps(name, **kw):
        return ParagraphStyle(name, **kw)

    NOM    = ps('NOM',   fontName='Helvetica-BoldOblique', fontSize=20, alignment=TA_LEFT, leading=24, textColor=GREEN)
    META   = ps('META',  fontName='Helvetica', fontSize=9, alignment=TA_LEFT, leading=13)
    LBL    = ps('LBL',   fontName='Helvetica', fontSize=9.5, leading=15)
    TITRE  = ps('TITRE', fontName='Helvetica-BoldOblique', fontSize=13, alignment=TA_CENTER, leading=16)
    HEAD   = ps('HEAD',  fontName='Helvetica-Bold', fontSize=9, leading=12, alignment=TA_CENTER, textColor=colors.white)
    CELL   = ps('CELL',  fontName='Helvetica', fontSize=9, leading=12, alignment=TA_CENTER)
    SIGN   = ps('SIGN',  fontName='Helvetica', fontSize=10, alignment=TA_RIGHT, leading=14)

    def v(key, default=''):
        val = data.get(key, default)
        return str(val) if val not in (None, '') else default

    rec  = _recuperateur_info(data)
    dest = _destinataire_info(data)

    doc = SimpleDocTemplate(buffer, pagesize=A4,
        topMargin=1.2*cm, bottomMargin=1.2*cm, leftMargin=1.5*cm, rightMargin=1.5*cm)
    story = []

    # ── En-tête : logo + raison sociale ────────────────────────────────────
    logo_cell = ''
    if rec['logo_path']:
        try:
            logo_cell = Image(rec['logo_path'], width=2.2*cm, height=2.2*cm)
        except Exception:
            logo_cell = ''
    entete = Table([[logo_cell, Paragraph(rec['nom'].upper(), NOM)]], colWidths=[2.5*cm, COL-2.5*cm])
    entete.setStyle(TableStyle([('VALIGN', (0,0),(-1,-1), 'MIDDLE')]))
    story.append(entete)
    story.append(Spacer(1, 6))

    if rec['agrement_num']:
        story.append(Paragraph(f"Agrément N° {rec['agrement_num']} du {rec['agrement_date']}", META))
    adresse_ligne = ' '.join(filter(None, [rec['adresse'], rec['code_postal']]))
    if adresse_ligne:
        story.append(Paragraph(adresse_ligne, META))
    id_table = Table([[
        Paragraph(f"RC {rec['rc']}", META), Paragraph(f"NIF {rec['nif']}", META),
    ], [
        Paragraph(f"NA {rec['na']}", META), Paragraph(f"NIS {rec['nis']}", META),
    ]], colWidths=[COL/2, COL/2])
    id_table.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]))
    story.append(id_table)
    story.append(Spacer(1, 14))

    # ── Date / lieu ─────────────────────────────────────────────────────────
    lieu_date = Table([['', Paragraph(f"{rec['commune']} le : {v('date_livraison')}", LBL)]],
        colWidths=[COL-7*cm, 7*cm])
    story.append(lieu_date)
    story.append(Spacer(1, 8))

    # ── Client ──────────────────────────────────────────────────────────────
    story.append(Paragraph(f"Nom de Client : <b>{dest['nom']}</b>", LBL))
    story.append(Paragraph(f"Adresse : <b>{dest['adresse']}</b>", LBL))
    story.append(Spacer(1, 10))

    titre_tbl = Table([[Paragraph('Bon de livraison', TITRE)]], colWidths=[8*cm])
    titre_tbl.setStyle(TableStyle([('BOX', (0,0),(-1,-1), 0.8, BLACK), ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    wrapper = Table([[titre_tbl]], colWidths=[COL])
    wrapper.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER')]))
    story.append(wrapper)
    story.append(Spacer(1, 14))

    # ── Tableau des déchets ─────────────────────────────────────────────────
    lignes = data.get('lignes') or []
    rows = [[Paragraph(h, HEAD) for h in ['N°', 'Description (Nature des déchets)', 'Quantités', 'Unités', 'Stockage']]]
    if not lignes:
        rows.append([Paragraph(str(i), CELL) for i in ['1','','','KG','']])
    else:
        for i, l in enumerate(lignes, start=1):
            rows.append([
                Paragraph(str(i), CELL),
                Paragraph(str(l.get('description','')), CELL),
                Paragraph(str(l.get('quantite','')), CELL),
                Paragraph(str(l.get('unite','KG')), CELL),
                Paragraph(str(l.get('stockage','')), CELL),
            ])
    tbl = Table(rows, colWidths=[1.3*cm, 7.7*cm, 2.5*cm, 2.5*cm, 3*cm])
    tbl.setStyle(TableStyle([
        ('GRID', (0,0),(-1,-1), 0.6, BLACK),
        ('BACKGROUND', (0,0),(-1,0), GREEN),
        ('TOPPADDING', (0,0),(-1,-1), 6), ('BOTTOMPADDING', (0,0),(-1,-1), 6),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 24))

    # ── Chauffeur ───────────────────────────────────────────────────────────
    story.append(Paragraph(f"Nom de chauffeur : {v('chauffeur_nom')}", LBL))
    story.append(Paragraph(f"Immatriculation de camion : {v('camion_immatriculation')}", LBL))
    story.append(Spacer(1, 24))

    # ── Signature ───────────────────────────────────────────────────────────
    story.append(Paragraph('Le Gérant', SIGN))
    if rec['responsable']:
        story.append(Paragraph(rec['responsable'], SIGN))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()

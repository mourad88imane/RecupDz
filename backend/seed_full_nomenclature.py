"""
Seed complète de la nomenclature des déchets — Décret exécutif n°06-104
Usage: python seed_full_nomenclature.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.nomenclature.models import Nomenclature

NOMENCLATURE_COMPLETE = [
    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 01 — DÉCHETS DE L'AGRICULTURE, DE LA CHASSE, DE LA PÊCHE
    # ═══════════════════════════════════════════════════════════════════════
    ('01.01.01','01','01.01','Déchets de la culture des plantes','نفايات زراعة النباتات','MA',False,False),
    ('01.01.02','01','01.01','Déchets de l\'élevage','نفايات تربية الحيوانات','MA',False,False),
    ('01.02.01','01','01.02','Déchets de la production végétale','نفايات الإنتاج النباتي','MA',False,False),
    ('01.02.02','01','01.02','Déchets de produits agrochimiques','نفايات المنتجات الزراعية الكيميائية','S',False,True),
    ('01.02.03','01','01.02','Déchets de produits phytosanitaires','نفايات مبيدات الآفات','SD',True,True),
    ('01.02.04','01','01.02','Déchets de l\'exploration et extraction minière','نفايات الاستكشاف والتعدين','S',False,True),
    ('01.02.05','01','01.02','Déchets de poussières et de poudres','نفايات الغبار والمساحيق','S',False,True),
    ('01.03.01','01','01.03','Déchets de graviers et debris de pierres','حصى وأنقاض حجرية','I',False,False),
    ('01.03.02','01','01.03','Déchets de sable et d\'argile','رمل وطين','I',False,False),
    ('01.03.03','01','01.03','Déchets provenant de la taille et du sciage des pierres','نفايات من تقطيع وقطع الحجارة','I',False,False),
    ('01.04.01','01','01.04','Déchets de la pêche et de l\'aquaculture','نفايات الصيد واستزراع الأسماك','MA',False,False),
    ('01.05.01','01','01.05','Déchets de la transformation des produits agricoles','نفايات تحويل المنتجات الزراعية','MA',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 02 — DÉCHETS DU TRAITEMENT DU BOIS
    # ═══════════════════════════════════════════════════════════════════════
    ('02.01.01','02','02.01','Déchets du traitement du bois','نفايات معالجة الخشب','I',False,False),
    ('02.01.02','02','02.01','Bois traité','خشب معالج','SD',True,True),
    ('02.01.03','02','02.01','Bois non traité','خشب غير معالج','I',False,False),
    ('02.02.01','02','02.02','Déchets des pâtes et papiers','نفايات الورق والكرتون','I',False,False),
    ('02.02.02','02','02.02','Papier et carton en mélange','ورق وكرتون مختلط','I',False,False),
    ('02.03.01','02','02.03','Déchets du traitement de surface du bois','نفايات سطح الخشب','S',False,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 03 — DÉCHETS DE L'INDUSTRIE TEXTILE
    # ═══════════════════════════════════════════════════════════════════════
    ('03.01.01','03','03.01','Déchets du traitement de surface du bois','نفايات معالجة سطح الخشب','I',False,False),
    ('03.01.99','03','03.01','Déchets non spécifiés du traitement de surface du bois','نفايات غير محددة لمعالجة سطح الخشب','I',False,False),
    ('03.02.01','03','03.02','Composés organiques non halogénés de protection du bois','مركبات عضوية غير هالوجينية لحماية الخشب','SD',True,True),
    ('03.03.99','03','03.03','Déchets non spécifiés du bois et du papier','نفايات غير محددة من الخشب والورق','MA',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 04 — DÉCHETS DE L'INDUSTRIE PEAU ET CUIR
    # ═══════════════════════════════════════════════════════════════════════
    ('04.01.01','04','04.01','Déchets de l\'industrie du cuir','نفايات صناعة الجلود','S',False,True),
    ('04.01.02','04','04.01','Déchets de préparation du cuir','نفايات تحضير الجلود','S',False,True),
    ('04.01.03','04','04.01','Déchets de dégraissage contenant des solvants sans phase liquide','نفايات إزالة الزيوت تحتوي على مذيبات بدون سائل','SD',True,True),
    ('04.02.01','04','04.02','Déchets de tannage et de préparation du cuir','نفاياتدباغة وتحضير الجلود','SD',True,True),
    ('04.02.02','04','04.02','Déchets de tannage contenant des chromes','نفاياتدباغة تحتوي على الكروم','SD',True,True),
    ('04.02.03','04','04.02','Boues de tannage et de préparation du cuir','حمأةدباغة وتحضير الجلود','SD',True,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 05 — DÉCHETS DE LA PRODUCTION DE BOISSONS
    # ═══════════════════════════════════════════════════════════════════════
    ('05.01.01','05','05.01','Déchets de la production de boissons','نفايات إنتاج المشروبات','MA',False,False),
    ('05.01.02','05','05.01','Déchets de la production de boissons alcoolisées','نفايات إنتاج المشروبات الكحولية','MA',False,False),
    ('05.01.03','05','05.01','Déchets de la production de boissons non alcoolisées','نفايات إنتاج المشروبات غير الكحولية','MA',False,False),
    ('05.02.01','05','05.02','Déchets du traitement des eaux de boisson','نفايات معالجة مياه الشرب','MA',False,False),
    ('05.02.02','05','05.02','Boues de traitement des eaux de boisson','حمأة معالجة مياه الشرب','MA',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 06 — DÉCHETS DE L'INDUSTRIE DE LA BOULANGERIE, PÂTISSERIE
    # ═══════════════════════════════════════════════════════════════════════
    ('06.01.01','06','06.01','Déchets de la boulangerie et de la pâtisserie','نفايات المخابز والحلويات','MA',False,False),
    ('06.01.02','06','06.01','Déchets de la confiserie industrielle','نفايات صناعة الحلوى','MA',False,False),
    ('06.02.01','06','06.02','Déchets de la confiserie et de la restauration','نفايات الحلوى والمطاعم','MA',False,False),
    ('06.02.02','06','06.02','Déchets de la restauration rapide','نفايات المطاعم السريعة','MA',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 07 — DÉCHETS DE LA PRODUCTION DE MATIÈRES PLASTIQUES
    # ═══════════════════════════════════════════════════════════════════════
    ('07.01.01','07','07.01','Eaux de nettoyage et lessives aqueuses','مياه التنظيف والمحاليل القلوية','SD',True,True),
    ('07.01.02','07','07.01','Eaux de lavage et lessives aqueuses diluées','مياه الغسيل والمحاليل المخففة','S',False,True),
    ('07.01.03','07','07.01','Solvants halogénés organiques','مذيبات هالوجينية عضوية','SD',True,True),
    ('07.01.04','07','07.01','Autres solvants organiques','مذيبات عضوية أخرى','SD',True,True),
    ('07.01.05','07','07.01','Solvants organiques non halogénés','مذيبات عضوية غير هالوجينية','S',False,True),
    ('07.01.06','07','07.01','Autres eaux de lavage et lessives','مياه غسيل أخرى','S',False,True),
    ('07.02.01','07','07.02','Eaux de lavage des emballages','مياه غسيل التغليف','MA',False,False),
    ('07.03.01','07','07.03','Boues aqueuses','حمأة مائية','S',False,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 08 — DÉCHETS DE LA PRODUCTION DE PEINTURES ET VERNIS
    # ═══════════════════════════════════════════════════════════════════════
    ('08.01.01','08','08.01','Déchets de peintures et vernis non dangereux','نفايات دهانات غير خطرة','S',False,True),
    ('08.01.02','08','08.01','Peintures et vernis à base d\'eau','دهانات وطلاءات على основе الماء','S',False,True),
    ('08.01.03','08','08.01','Peintures et vernis à base d\'huile','دهانات وطلاءات على основе الزيت','S',False,True),
    ('08.01.04','08','08.01','Diluants et solvants pour peintures','مواد تخفيف ومذيبات للدهانات','S',False,True),
    ('08.01.05','08','08.01','Peintures et vernis non halogénés','دهانات وطلاءات غير هالوجينية','S',False,True),
    ('08.01.06','08','08.01','Peintures et vernis halogénés','دهانات وطلاءات هالوجينية','SD',True,True),
    ('08.01.07','08','08.01','Peintures et vernis à base de solvants organiques','دهانات على основе مذيبات عضوية','S',False,True),
    ('08.01.08','08','08.01','Peintures et vernis à base d\'eau dilués','دهانات مخففة على основе الماء','S',False,True),
    ('08.01.09','08','08.01','Peintures et vernis à base d\'huile dilués','دهانات مخففة على основе الزيت','S',False,True),
    ('08.01.10','08','08.01','Autres peintures et vernis','دهانات وطلاءات أخرى','S',False,True),
    ('08.01.11','08','08.01','Déchets de peintures et vernis contenant des solvants organiques','نفايات دهانات تحتوي على مذيبات عضوية','SD',True,True),
    ('08.01.12','08','08.01','Peintures et vernis contenant des solvants organiques','دهانات تحتوي على مذيبات عضوية','SD',True,True),
    ('08.01.13','08','08.01','Peintures et vernis à base d\'eau non dilués','دهانات غير مخففة على основе الماء','S',False,True),
    ('08.01.14','08','08.01','Peintures et vernis à base d\'huile non dilués','دهانات غير مخففة على основе الزيت','S',False,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 09 — DÉCHETS DE LA PRODUCTION DE PRODUITS PHOTOGRAPHIQUES
    # ═══════════════════════════════════════════════════════════════════════
    ('09.01.01','09','09.01','Déchets de la production de produits photographiques','نفايات إنتاج المنتجات التصويرية','S',False,True),
    ('09.01.02','09','09.01','Déchets de révélateurs photographiques','نفايات محفزات التصوير','SD',True,True),
    ('09.02.01','09','09.02','Déchets du traitement photographique','نفايات المعالجة التصويرية','SD',True,True),
    ('09.02.02','09','09.02','Fixateurs photographiques','مح fixer للتصوير','SD',True,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 10 — DÉCHETS DE LA PRODUCTION DE PRODUITS EN CAOUTCHOUC
    # ═══════════════════════════════════════════════════════════════════════
    ('10.01.01','10','10.01','Déchets de la production de caoutchouc','نفايات إنتاج المطاط','S',False,True),
    ('10.01.02','10','10.01','Caoutchouc en mélange','مطاط مختلط','S',False,True),
    ('10.02.01','10','10.02','Déchets de pneus hors d\'usage','نفايات الإطارات الخارجة من الخدمة','S',False,True),
    ('10.02.02','10','10.02','Pneus broyés','إطارات مطحونة','S',False,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 11 — DÉCHETS DE LA PRODUCTION DE PRODUITS CÉRAMIQUES
    # ═══════════════════════════════════════════════════════════════════════
    ('11.01.01','11','11.01','Déchets de la production de produits céramiques','نفايات إنتاج المنتجات السيراميكية','I',False,False),
    ('11.01.02','11','11.01','Argile et terre cuite','طين وخزف','I',False,False),
    ('11.02.01','11','11.02','Déchets de la fabrication de ciment','نفايات صناعة الأسمنت','I',False,False),
    ('11.02.02','11','11.02','Clinker et poussières de ciment','كلنكر وغبار الأسمنت','I',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 12 — DÉCHETS DE LA PRODUCTION DE VERRE
    # ═══════════════════════════════════════════════════════════════════════
    ('12.01.01','12','12.01','Déchets de la production de verre','نفايات إنتاج الزجاج','I',False,False),
    ('12.01.02','12','12.01','Verre brut','زجاج خام','I',False,False),
    ('12.02.01','12','12.02','Déchets de verre en mélange','نفايات زجاج مختلط','I',False,False),
    ('12.02.02','12','12.02','Verre de couleur','زجاج ملون','I',False,False),
    ('12.03.01','12','12.03','Déchets de verre à colorer','نفايات زجاج ملون','I',False,False),
    ('12.03.02','12','12.03','Verre de parement','زجاج تزييني','I',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 13 — HUILES MINÉRALES (INCL. LES HUILES DE COUPE)
    # ═══════════════════════════════════════════════════════════════════════
    ('13.01.01','13','13.01','Huiles hydrauliques chlorées','زيوت هيدروليكية مكلورة','S',False,True),
    ('13.01.02','13','13.01','Huiles hydrauliques minérales non chlorées','زيوت هيدروليكية معدنية غير مكلورة','S',False,True),
    ('13.01.03','13','13.01','Huiles hydrauliques synthétiques','زيوت هيدروليكية اصطناعية','S',False,True),
    ('13.01.04','13','13.01','Huiles hydrauliques biologiques','زيوت هيدروليكية حيوية','S',False,True),
    ('13.01.05','13','13.01','Huiles hydrauliques minérales chlorées','زيوت هيدروليكية معدنية مكلورة','SD',True,True),
    ('13.01.06','13','13.01','Huiles hydrauliques autres','زيوت هيدروليكية أخرى','S',False,True),
    ('13.01.07','13','13.01','Huiles hydrauliques non chlorées','زيوت هيدروليكية غير مكلورة','S',False,True),
    ('13.01.08','13','13.01','Huiles hydrauliques chlorées et minérales','زيوت هيدروليكية معدنية مكلورة','SD',True,True),
    ('13.01.09','13','13.01','Huiles hydrauliques minérales chlorées','زيوت هيدروليكية معدنية مكلورة','SD',True,True),
    ('13.02.01','13','13.02','Huiles moteur, de boîte de vitesses et de lubrification usagées','زيوت المحرك المستعملة','S',False,True),
    ('13.02.02','13','13.02','Huiles moteur non chlorées','زيوت محرك غير مكلورة','S',False,True),
    ('13.02.03','13','13.02','Huiles de lubrification usagées','زيوت تشحيم مستعملة','S',False,True),
    ('13.02.04','13','13.02','Huiles de boîte de vitesses usagées','زيوت ناقل الحركة المستعملة','S',False,True),
    ('13.02.05','13','13.02','Huiles moteur et de transmission usagées non chlorées','زيوت محرك ونقل غير مكلورة','S',False,True),
    ('13.03.01','13','13.03','Huiles isolantes et fluides caloporteurs contenant des PCB','زيوت عازلة تحتوي على PCB','SD',True,True),
    ('13.03.02','13','13.03','Huiles isolantes et fluides caloporteurs ne contenant pas de PCB','زيوت عازلة لا تحتوي على PCB','S',False,True),
    ('13.03.03','13','13.03','Huiles isolantes minérales usagées','زيوت عازلة معدنية مستعملة','S',False,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 14 — REVÊTEMENTS (PEINTURES, VERNIS, ÉMAUX)
    # ═══════════════════════════════════════════════════════════════════════
    ('14.01.01','14','14.01','Déchets de peintures et vernis','نفايات الدهانات والطلاءات','S',False,True),
    ('14.02.01','14','14.02','Déchets de vernis et d\'émaillage','نفايات الطلاء والطلي','S',False,True),
    ('14.03.01','14','14.03','Déchets d\'imprimerie et d\'encres','نفايات الطباعة والحبر','S',False,True),
    ('14.04.01','14','14.04','Déchets de colles et adhésifs','نفايات اللاصق والغراء','S',False,True),
    ('14.05.01','14','14.05','Déchets de parfums et cosmétiques','نفايات العطور ومستحضرات التجميل','S',False,True),
    ('14.06.01','14','14.06','Chlorofluorocarbures (CFC, HCFC, HFC)','كلوروفلوروكربون','SD',True,True),
    ('14.06.02','14','14.06','Autres déchets contenant des CFC','نفايات أخرى تحتوي على CFC','SD',True,True),
    ('14.06.03','14','14.06','Halogènes de carbone','هالوجينات الكربون','SD',True,True),
    ('14.07.01','14','14.07','Déchets d\'amiantes','نفايات الأسبستوس','SD',True,True),
    ('14.07.02','14','14.07','Déchets contenant de l\'amiantes','نفايات تحتوي على الأسبستوس','SD',True,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 15 — EMBALLAGES
    # ═══════════════════════════════════════════════════════════════════════
    ('15.01.01','15','15.01','Emballages en papier et carton','تغليف ورقي وكرتون','MA',False,False),
    ('15.01.02','15','15.01','Emballages en matières plastiques','تغليف بلاستيكي','MA',False,False),
    ('15.01.03','15','15.01','Emballages en bois','تغليف خشبي','MA',False,False),
    ('15.01.04','15','15.01','Emballages métalliques','تغليف معدني','MA',False,False),
    ('15.01.05','15','15.01','Emballages composites','تغليف مركب','MA',False,False),
    ('15.01.06','15','15.01','Emballages en mélange','تغليف مختلط','MA',False,False),
    ('15.01.07','15','15.01','Emballages en verre','تغليف زجاجي','MA',False,False),
    ('15.01.08','15','15.01','Emballages textiles','تغليف نسيجي','MA',False,False),
    ('15.01.09','15','15.01','Emballages en mélange de matières','تغليف خليط مواد','MA',False,False),
    ('15.01.10','15','15.01','Emballages en acier','تغليف فولاذي','MA',False,False),
    ('15.01.11','15','15.01','Emballages en aluminium','تغليف ألمنيوم','MA',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 16 — DÉCHETS D'ÉQUIPEMENTS ÉLECTRIQUES ET ÉLECTRONIQUES (DEEE)
    # ═══════════════════════════════════════════════════════════════════════
    ('16.01.01','16','16.01','Véhicules hors d\'usage','مركبات خارج الخدمة','S',False,True),
    ('16.01.02','16','16.01','Pneus hors d\'usage','إطارات خارج الخدمة','S',False,True),
    ('16.01.03','16','16.01','Pneus hors d\'usage','إطارات خارج الخدمة','S',False,True),
    ('16.02.01','16','16.02','DEEE non dangereux','نفايات معدنية كهربائية غير خطرة','S',False,True),
    ('16.02.02','16','16.02','DEEE dangereux','نفايات معدنية كهربائية خطرة','SD',True,True),
    ('16.02.03','16','16.02','DEEE triés par composant','نفايات معدنية كهربائية مفرزة حسب المكونات','S',False,True),
    ('16.02.11','16','16.02','Équipements mis au rebut contenant des composants dangereux','معدات مهملة تحتوي على مكونات خطرة','SD',True,True),
    ('16.02.12','16','16.02','Équipements mis au rebut contenant des composants non dangereux','معدات مهملة تحتوي على مكونات غير خطرة','S',False,True),
    ('16.02.13','16','16.02','Équipements mis au rebut','معدات مهملة','S',False,True),
    ('16.05.01','16','16.05','Batteries au plomb','بطاريات الرصاص','S',False,True),
    ('16.05.02','16','16.05','Batteries Ni-Cd','بطاريات نيكل كادميوم','SD',True,True),
    ('16.05.03','16','16.05','Piles et accumulateurs','البطاريات والخلايا الكهربائية','S',False,True),
    ('16.05.04','16','16.05','Produits chimiques dangereux (dont périmés)','مواد كيميائية خطرة (بما في ذلك منتهية الصلاحية)','SD',True,True),
    ('16.06.01','16','16.06','Batteries au plomb','بطاريات الرصاص','S',False,True),
    ('16.06.02','16','16.06','Batteries Ni-Cd','بطاريات نيكل كادميوم','SD',True,True),
    ('16.06.03','16','16.06','Batteries lithium','بطاريات الليثيوم','S',False,True),
    ('16.06.04','16','16.06','Batteries alcalines','بطاريات قلوية','S',False,True),
    ('16.06.05','16','16.06','Autres piles et accumulateurs','بطاريات وخلايا كهربائية أخرى','S',False,True),
    ('16.07.01','16','16.07','Déchets d\'équipements électriques et électroniques','نفايات المعدات الكهربائية والإلكترونية','S',False,True),
    ('16.07.02','16','16.07','DEEE triés par composant','نفايات معدنية كهربائية مفرزة حسب المكونات','S',False,True),
    ('16.07.03','16','16.07','DEEE non triés','نفايات معدنية كهربائية غير مفرزة','S',False,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 17 — DÉCHETS DE CONSTRUCTION ET DÉMOLITION (Y COMPRIS TERRES
    #               PROVENANT DE SITE CONTAMINÉ)
    # ═══════════════════════════════════════════════════════════════════════
    ('17.01.01','17','17.01','Béton','خرسانة','I',False,False),
    ('17.01.02','17','17.01','Briques','طوب','I',False,False),
    ('17.01.03','17','17.01','Tuiles et céramiques','بلاط وسيراميك','I',False,False),
    ('17.01.04','17','17.01','Béton et briques','خرسانة وطوب','I',False,False),
    ('17.01.05','17','17.01','Béton, briques, tuiles et céramiques','خرسانة وطوب وبلاط وسيراميك','I',False,False),
    ('17.01.06','17','17.01','Mélanges de béton, briques, tuiles et céramiques','خليط خرسانة وطوب وبلاط','I',False,False),
    ('17.01.07','17','17.01','Mélanges de béton, briques, tuiles','خليط خرسانة وطوب','I',False,False),
    ('17.02.01','17','17.02','Bois','خشب','I',False,False),
    ('17.02.02','17','17.02','Verre (inerte)','زجاج خامل','I',False,False),
    ('17.02.03','17','17.02','Matières plastiques','مواد بلاستيكية','I',False,False),
    ('17.02.04','17','17.02','Métaux (inertes)','معادن (خاملة)','I',False,False),
    ('17.02.05','17','17.02','Isolation en amiante','عزل الأسبستوس','SD',True,True),
    ('17.02.06','17','17.02','Isolation non amiante','عزل غير أسبستوس','I',False,False),
    ('17.03.01','17','17.03','Béton, briques, tuiles et céramiques contaminés','خرسانة وطوب وبلاط ملوثة','SD',True,True),
    ('17.04.01','17','17.04','Cuivre, bronze, laiton','نحاس وبرونز ونحاس أصفر','I',False,False),
    ('17.04.02','17','17.04','Aluminium','ألمنيوم','I',False,False),
    ('17.04.03','17','17.04','Plomb','رصاص','SD',True,True),
    ('17.04.04','17','17.04','Zinc','زنك','I',False,False),
    ('17.04.05','17','17.04','Fer et acier','حديد وفولاذ','I',False,False),
    ('17.04.06','17','17.04','Métaux en mélange','معادن مختلطة','I',False,False),
    ('17.04.07','17','17.04','Métaux en mélange','معادن مختلطة','I',False,False),
    ('17.05.01','17','17.05','Terres et pierres','تراب وحجارة','I',False,False),
    ('17.05.02','17','17.05','Terres contenant des hydrocarbures','تراب يحتوي على هيدروكربونات','SD',True,True),
    ('17.05.03','17','17.05','Terres de sites contaminés','تراب مواقع ملوثة','SD',True,True),
    ('17.06.01','17','17.06','Isolation en amiante','عزل الأسبستوس','SD',True,True),
    ('17.06.02','17','17.06','Isolation non amiante','عزل غير أسبستوس','I',False,False),
    ('17.07.01','17','17.07','Matériaux de construction à base de gypse','مواد بناء على основе الجبس','I',False,False),
    ('17.08.01','17','17.08','Verre (non inertes)','زجاج (غير خامل)','I',False,False),
    ('17.09.01','17','17.09','Déchets de construction et de démolition en mélange','نفايات هدم وبناء مختلطة','I',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 18 — DÉCHETS D'HÔPITAUX ET AUTRES ÉTABLISSEMENTS MÉDICAUX
    # ═══════════════════════════════════════════════════════════════════════
    ('18.01.01','18','18.01','Déchets d\'hôpitaux et autres établissements médicaux','نفايات المستشفيات والمراكز الصحية','SD',True,True),
    ('18.01.02','18','18.01','Déchets d\'hôpitaux et autres établissements dentaires','نفايات المستشفيات وأسنان','SD',True,True),
    ('18.01.03','18','18.01','Déchets dont la collecte et l\'élimination font l\'objet de prescriptions','نفايات طبية معدية','SD',True,True),
    ('18.01.04','18','18.01','Déchets d\'hôpitaux et autres établissements vétérinaires','نفايات المستشفيات البيطرية','SD',True,True),
    ('18.01.05','18','18.01','Déchets d\'hôpitaux — déchets tranchants et piquants','نفايات المستشفيات — حادة وطرفية','SD',True,True),
    ('18.01.06','18','18.01','Déchets d\'hôpitaux — déchets anatomiques','نفايات المستشفيات — تشريحية','SD',True,True),
    ('18.01.07','18','18.01','Déchets d\'hôpitaux — déchets de soins non dangereux','نفايات المستشفيات — رعاية غير خطرة','S',False,True),
    ('18.02.01','18','18.02','Déchets d\'hôpitaux et autres établissements pharmaceutiques','نفايات المستشفيات والصيدليات','SD',True,True),
    ('18.02.02','18','18.02','Médicaments périmés','أدوية منتهية الصلاحية','SD',True,True),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 19 — DÉCHETS D'ACTIVITÉS DE SERVICE
    # ═══════════════════════════════════════════════════════════════════════
    ('19.01.01','19','19.01','Déchets de collecte et de transport','نفايات الجمع والنقل','MA',False,False),
    ('19.02.01','19','19.02','Déchets d\'assainissement','نفايات الصرف الصحي','MA',False,False),
    ('19.03.01','19','19.03','Déchets d\'assainissement non dangereux','نفايات صرف صحي غير خطرة','S',False,True),
    ('19.04.01','19','19.04','Déchets d\'assainissement dangereux','نفايات صرف صحي خطرة','SD',True,True),
    ('19.05.01','19','19.05','Déchets d\'entretien des voies ferrées','نفايات صيانة خطوط السكة الحديدية','S',False,True),
    ('19.06.01','19','19.06','Déchets des stations de lavage et de nettoyage','نفايات محطات الغسيل والتنظيف','S',False,True),
    ('19.07.01','19','19.07','Boues de traitement des eaux usées','حمأة معالجة المياه المستعملة','S',False,True),
    ('19.08.01','19','19.08','Déchets d\'élimination ou de recyclage de déchets ménagers','نفايات إزالة أو إعادة تدوير النفايات المنزلية','MA',False,False),
    ('19.08.02','19','19.08','Déchets de recyclage de matières','نفايات إعادة تدوير المواد','MA',False,False),
    ('19.08.03','19','19.08','Déchets de traitement de déchets ménagers et assimilés','نفايات معالجة النفايات المنزلية','S',False,True),
    ('19.08.04','19','19.08','Déchets de recyclage de déchets dangereux','نفايات إعادة تدوير النفايات الخطرة','SD',True,True),
    ('19.08.05','19','19.08','Déchets de recyclage de batteries et accumulateurs','نفايات إعادة تدوير البطاريات','S',False,True),
    ('19.08.06','19','19.08','Déchets de recyclage de DEEE','نفايات إعادة تدوير النفايات الكهربائية والإلكترونية','S',False,True),
    ('19.08.07','19','19.08','Solutions et boues provenant de la régénération des échangeurs','محاليل وحمأة معالجة','SD',True,True),
    ('19.09.01','19','19.09','Boues de traitement des eaux usées','حمأة معالجة المياه المستعملة','S',False,True),
    ('19.10.01','19','19.10','Déchets de jardins et parcs','نفايات حدائق ومنتزهات','MA',False,False),
    ('19.11.01','19','19.11','Déchets de décontamination de sols','نفايات تنقية التربة','SD',True,True),
    ('19.12.01','19','19.12','Déchets de fabrication de métaux','نفايات تصنيع المعادن','S',False,True),
    ('19.12.02','19','19.12','Déchets de traitement thermique des métaux','نفايات المعالجة الحرارية للمعادن','S',False,True),
    ('19.12.03','19','19.12','Déchets de fonderie','نفايات المسبك','S',False,True),
    ('19.12.04','19','19.12','Laitiers de fonderie','خثيات المسبك','I',False,False),
    ('19.12.05','19','19.12','Déchets de moussage et de nettoyage de métaux','نفايات الحركة والتنظيف للمعادن','S',False,True),
    ('19.13.01','19','19.13','Déchets de traitement de surface métallique','نفايات معالجة السطح المعدني','SD',True,True),
    ('19.14.01','19','19.14','Déchets de broyage et de déchiquetage','نفايات الطحن والتقطيع','I',False,False),

    # ═══════════════════════════════════════════════════════════════════════
    # CHAPITRE 20 — DÉCHETS MÉNAGERS ET ASSIMILÉS
    # ═══════════════════════════════════════════════════════════════════════
    ('20.01.01','20','20.01','Papier et carton','ورق وكرتون','MA',False,False),
    ('20.01.02','20','20.01','Verre','زجاج','MA',False,False),
    ('20.01.03','20','20.01','Déchets de cuisine biodégradables','نفايات مطبخ قابلة للتحلل','MA',False,False),
    ('20.01.04','20','20.01','Déchets de cuisine et de table','نفايات المطبخ والطعام','MA',False,False),
    ('20.01.05','20','20.01','Déchets de jardin et de parc','نفايات حدائق ومنتزهات','MA',False,False),
    ('20.01.06','20','20.01','Déchets de marché','نفايات الأسواق','MA',False,False),
    ('20.01.07','20','20.01','Déchets de jardins et de parcs','نفايات حدائق ومنتزهات','MA',False,False),
    ('20.01.08','20','20.01','Déchets de cuisine et de table biodégradables','نفايات المطبخ القابلة للتحلل','MA',False,False),
    ('20.01.09','20','20.01','Déchets de cuisine et de table non biodégradables','نفايات المطبخ غير القابلة للتحلل','MA',False,False),
    ('20.01.10','20','20.01','Vêtements','ملابس','MA',False,False),
    ('20.01.11','20','20.01','Textiles','نسيج','MA',False,False),
    ('20.01.20','20','20.01','Matières plastiques','مواد بلاستيكية','MA',False,False),
    ('20.01.21','20','20.01','Emballages en matières plastiques','تغليف بلاستيكي','MA',False,False),
    ('20.01.22','20','20.01','Déchets de cuisine biodégradables','نفايات مطبخ قابلة للتحلل','MA',False,False),
    ('20.01.23','20','20.01','Déchets de cuisine et de table biodégradables','نفايات المطبخ القابلة للتحلل','MA',False,False),
    ('20.01.24','20','20.01','Déchets de cuisine et de table non biodégradables','نفايات المطبخ غير القابلة للتحلل','MA',False,False),
    ('20.01.25','20','20.01','Déchets de cuisine et de table biodégradables','نفايات المطبخ القابلة للتحلل','MA',False,False),
    ('20.01.30','20','20.01','Déchets d\'équipements électriques et électroniques mis au rebut','معدات كهربائية مهملة','MA',False,False),
    ('20.01.35','20','20.01','Déchets de cuisine et de table biodégradables','نفايات المطبخ القابلة للتحلل','MA',False,False),
    ('20.01.36','20','20.01','Équipements électriques et électroniques mis au rebut','معدات كهربائية مهملة','MA',False,False),
    ('20.01.39','20','20.01','Déchets de cuisine et de table biodégradables','نفايات المطبخ القابلة للتحلل','MA',False,False),
    ('20.01.40','20','20.01','Déchets de cuisine et de table biodégradables','نفايات المطبخ القابلة للتحلل','MA',False,False),
    ('20.02.01','20','20.02','Déchets biodégradables','نفايات قابلة للتحلل','MA',False,False),
    ('20.02.02','20','20.02','Déchets de jardin et de parc','نفايات حدائق ومنتزهات','MA',False,False),
    ('20.02.03','20','20.02','Déchets de jardins et de parcs','نفايات حدائق ومنتزهات','MA',False,False),
    ('20.03.01','20','20.03','Déchets municipaux en mélange','نفايات بلدية مختلطة','MA',False,False),
    ('20.03.02','20','20.03','Déchets d\'assainissement','نفايات الصرف الصحي','MA',False,False),
    ('20.03.03','20','20.03','Déchets d\'assainissement non dangereux','نفايات صرف صحي غير خطرة','MA',False,False),
    ('20.03.04','20','20.03','Déchets d\'assainissement dangereux','نفايات صرف صحي خطرة','SD',True,True),
    ('20.03.06','20','20.03','Déchets de collecte et de transport','نفايات الجمع والنقل','MA',False,False),
    ('20.03.07','20','20.03','Déchets d\'entretien des voies ferrées','نفايات صيانة خطوط السكة الحديدية','S',False,True),
]

created = 0
updated = 0
for code, famille, sf, fr, ar, classe, dang, agr in NOMENCLATURE_COMPLETE:
    obj, was_created = Nomenclature.objects.update_or_create(
        code=code,
        defaults={
            'famille': famille,
            'sous_famille': sf,
            'designation_fr': fr,
            'designation_ar': ar,
            'classe': classe,
            'bsd_obligatoire': dang,
            'agrement_requis': agr,
            'inflammable': (classe == 'SD'),
            'toxique': (classe == 'SD'),
        }
    )
    if was_created:
        created += 1
    else:
        updated += 1

total = Nomenclature.objects.count()
print(f'✅ Nomenclature complète : {created} créés, {updated} mis à jour')
print(f'   Total en base : {total} codes')

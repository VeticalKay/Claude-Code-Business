#!/usr/bin/env python3
"""Vertical Kay Education — Trainingsplan PDF Generator
Dark Luxury Redesign: Schwarz, Didot, fliessende Magenta-Welle.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Fonts registrieren ────────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont('Georgia',
    '/System/Library/Fonts/Supplemental/Georgia.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Bold',
    '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Italic',
    '/System/Library/Fonts/Supplemental/Georgia Italic.ttf'))
try:
    pdfmetrics.registerFont(TTFont('Didot',
        '/System/Library/Fonts/Supplemental/Didot.ttc', subfontIndex=0))
    TITLE_FONT = 'Didot'
except Exception:
    TITLE_FONT = 'Georgia-Italic'

# ── Layout & Farben ──────────────────────────────────────────────────────────
W, H = A4
MAR  = 1.8 * cm
CW   = W - 2 * MAR

# Farben
BLACK    = colors.HexColor('#000000')
NEAR_BLK = colors.HexColor('#0e0e0e')
CARD_BG  = colors.HexColor('#141414')
MAGENTA  = colors.HexColor('#b40087')
LMAGENTA = colors.HexColor('#cd8bbb')
WHITE    = colors.HexColor('#FFFFFF')
CREAM    = colors.HexColor('#F0E6EC')
GREY     = colors.HexColor('#AAAAAA')
LGREY    = colors.HexColor('#666666')

HDR_H = 100
FTR_Y = 22
PAD   = 12

OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'Trainingspläne')
os.makedirs(OUTPUT, exist_ok=True)

# ── Video-Links ──────────────────────────────────────────────────────────────
L = {
    'warm'   : 'https://drive.google.com/file/d/1ta9Gg5Dowem-1kOe41GyaBtkzFZ8nZ3h/view',
    'hgk1'   : 'https://drive.google.com/file/d/1vElPVlbv8_TzNzb0QU_5ZNbOW9TSHMzo/view',
    'hgk2'   : 'https://drive.google.com/file/d/1hJ1HUstJ5z96r5NaVheSNxyDA9w2-onu/view',
    'hgk3'   : 'https://drive.google.com/file/d/1h8g0UWuCsQQ4I0ONETpToaM8M5kWrouY/view',
    'sside'  : 'https://drive.google.com/file/d/1MABwIpo3sPCUONGQUUF0zJCE-e7pb5bO/view',
    'scar'   : 'https://drive.google.com/file/d/18hj1JF4HfNNN7OHWMMrte_ZvEKCvA2fx/view',
    'splank' : 'https://drive.google.com/file/d/1meoM17ZY5NvCZ9qXArZe3CHdX2INafcK/view',
    'dolph'  : 'https://drive.google.com/file/d/1GD_cgou4RiPIFKJFNyzr_ygF1mUpO4Q_/view',
    'wand'   : 'https://drive.google.com/file/d/1mUhr--M1w0Sr6-GQQFVvYe8fGr9FIAUq/view',
    'brust'  : 'https://drive.google.com/file/d/1pqVzEZDd4znL-wqn3B116Oj9F0GoK7U5/view',
    'brust_pl': 'https://drive.google.com/file/d/1dibKGMn_QtGRiTKAPasVRx-qp59ImwbT/view',
    'core2'  : 'https://drive.google.com/file/d/1ZNrsDACRbUNa8dTOh6HJOQaarFUCov9N/view',
    'core3'  : 'https://drive.google.com/file/d/1p0BA0XrOmalERjSZQ4E4e7Two5iPqIGA/view',
    'core5'  : 'https://drive.google.com/file/d/1OHHV9AKCKeeoIhCmjo182TmQdBa4VuTa/view',
    'dbug'   : 'https://drive.google.com/file/d/1ZIkbCtdGqyowVxbid33J6KU98Yxc_y81/view',
    'dbug4'  : 'https://drive.google.com/file/d/1Uol_LrRufGDgrBX7rgzi3TXRaoBGHUia/view',
    'hueft'  : 'https://drive.google.com/file/d/1vH7lWyJuGh5P0AUUgau0-i-MWm2OyHN_/view',
    'cdyn'   : 'https://drive.google.com/file/d/1QwBgHzoEPaxZvXIlyIhPhcUKOX7nGELl/view',
    'sdips'  : 'https://drive.google.com/file/d/15WTJgqQSkdcOXERinRZ99NncP7AfXa2v/view',
    'pu1'    : 'https://drive.google.com/file/d/1aHJsMry-Hgd1nlxxN7pgXwjAGe5w7zHm/view',
    'pu2'    : 'https://drive.google.com/file/d/1JCy1zMdgq7XaTHe6aTYpQ6miY8t6s5B5/view',
    'pu3'    : 'https://drive.google.com/file/d/1WCgO4GcO5BSPG5sLfR3NZ-AxAf9D2Wz-/view',
    'pu4'    : 'https://drive.google.com/file/d/1jOwmPCU0IWI7V_pplfDm2xSLrDXuKzv7/view',
    'strip'  : 'https://drive.google.com/file/d/14ySF8bJBXMR5eG9crtgI4otFg8t4Jewr/view',
}


# ── Dekorations-Funktionen ───────────────────────────────────────────────────

def draw_page_background(c):
    """Schwarzer Seitenhintergrund."""
    c.setFillColor(BLACK)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def draw_magenta_wave(c, y_center, amplitude=18, width_factor=1.0):
    """Fliessende Magenta-Welle als Dekoration."""
    w = W * width_factor
    thick = amplitude

    c.setFillColor(MAGENTA)
    p = c.beginPath()
    # Obere Wellenlinie
    p.moveTo(0, y_center + thick * 0.3)
    p.curveTo(w * 0.20, y_center + thick * 0.9,
              w * 0.40, y_center - thick * 0.2,
              w * 0.55, y_center + thick * 0.5)
    p.curveTo(w * 0.72, y_center + thick * 1.1,
              w * 0.88, y_center + thick * 0.2,
              w,        y_center + thick * 0.6)
    # Untere Wellenlinie (zurück)
    p.lineTo(w, y_center - thick * 0.4)
    p.curveTo(w * 0.88, y_center - thick * 0.8,
              w * 0.72, y_center + thick * 0.1,
              w * 0.55, y_center - thick * 0.5)
    p.curveTo(w * 0.40, y_center - thick * 1.1,
              w * 0.20, y_center - thick * 0.1,
              0,        y_center - thick * 0.7)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # Zweite, hellere Welle dahinter (Tiefeneffekt)
    c.setFillColor(colors.HexColor('#6b0050'))
    p2 = c.beginPath()
    p2.moveTo(0, y_center - thick * 0.7)
    p2.curveTo(w * 0.25, y_center - thick * 1.5,
               w * 0.50, y_center - thick * 0.5,
               w * 0.65, y_center - thick * 1.2)
    p2.curveTo(w * 0.80, y_center - thick * 1.8,
               w,        y_center - thick * 1.1,
               w,        y_center - thick * 1.1)
    p2.lineTo(w, y_center - thick * 2.2)
    p2.lineTo(0, y_center - thick * 2.2)
    p2.close()
    c.drawPath(p2, fill=1, stroke=0)


def draw_logo(c, x, y, dark_bg=True):
    """VK Logo — weiss auf schwarzem Hintergrund."""
    sq = 38
    # Weisses Quadrat
    c.setFillColor(WHITE)
    c.rect(x, y - sq, sq, sq, fill=1, stroke=0)
    # Magenta VK darin
    c.setFillColor(MAGENTA)
    c.setFont('Georgia-Bold', 15)
    c.drawCentredString(x + sq / 2, y - sq + 11, 'VK')
    # VERTICAL KAY daneben
    c.setFillColor(WHITE)
    c.setFont(TITLE_FONT, 15)
    c.drawString(x + sq + 9, y - 13, 'VERTICAL KAY')
    c.setFont('Helvetica', 7)
    c.setFillColor(LMAGENTA)
    c.drawString(x + sq + 11, y - sq + 9, 'E D U C A T I O N')


def draw_header(c, plan_num, plan_name, subtitle):
    """Header mit Logo, Welle und Plan-Titel."""
    draw_page_background(c)

    # Welle am unteren Ende des Headers
    wave_y = H - HDR_H + 22
    draw_magenta_wave(c, wave_y, amplitude=14)

    # Logo oben links
    draw_logo(c, MAR, H - 16)

    # Plan-Nummer klein oben rechts
    c.setFont('Helvetica', 8)
    c.setFillColor(LMAGENTA)
    num_str = f'Plan {plan_num:02d}'
    nw = c.stringWidth(num_str, 'Helvetica', 8)
    c.drawString(W - MAR - nw, H - 12, num_str)

    # Plan-Name gross
    c.setFont(TITLE_FONT, 26)
    c.setFillColor(WHITE)
    tw = c.stringWidth(plan_name, TITLE_FONT, 26)
    c.drawString(W - MAR - tw, H - 34, plan_name)

    # Untertitel
    c.setFont('Georgia-Italic', 9)
    c.setFillColor(GREY)
    sw = c.stringWidth(subtitle, 'Georgia-Italic', 9)
    c.drawString(W - MAR - sw, H - 48, subtitle)

    # Dünne Magenta-Linie ganz unten am Header
    c.setStrokeColor(MAGENTA)
    c.setLineWidth(0.6)
    c.line(MAR, H - HDR_H + 2, W - MAR, H - HDR_H + 2)


def draw_footer(c, page_num):
    """Eleganter Footer auf schwarzem Hintergrund."""
    # Dünne Linie
    c.setStrokeColor(colors.HexColor('#2a2a2a'))
    c.setLineWidth(0.5)
    c.line(MAR, FTR_Y + 14, W - MAR, FTR_Y + 14)
    c.setFillColor(LGREY)
    c.setFont('Helvetica', 7)
    c.drawString(MAR, FTR_Y, 'Vertical Kay Education  ·  verticalkay.com')
    ps = f'{page_num}'
    pw = c.stringWidth(ps, 'Helvetica', 7)
    c.drawString(W - MAR - pw, FTR_Y, ps)


def draw_section_header(c, y, label):
    """Eleganter Sektions-Header: Magenta-Strich + Didot-Text."""
    # Dünne Linie oben
    c.setStrokeColor(colors.HexColor('#222222'))
    c.setLineWidth(0.5)
    c.line(MAR, y, W - MAR, y)

    y -= 6
    # Kleiner Magenta-Punkt als Marker
    c.setFillColor(MAGENTA)
    c.circle(MAR + 4, y - 6, 2.5, fill=1, stroke=0)

    # Section-Label
    c.setFont('Georgia-Italic', 10)
    c.setFillColor(CREAM)
    c.drawString(MAR + 14, y - 10, label)

    return y - 22


def draw_exercise_card(c, y, title, desc_paras, reps, links):
    """Dunkle elegante Übungskarte."""
    all_lines = []
    for para in desc_paras:
        lines = simpleSplit(para, 'Helvetica', 8.5, CW - 2 * PAD - 10)
        all_lines.extend(lines)
        all_lines.append('')
    if all_lines and all_lines[-1] == '':
        all_lines.pop()

    link_rows = [links[i:i+2] for i in range(0, len(links), 2)]
    card_h = (PAD + 15 + 4
              + len(all_lines) * 10.5
              + 8 + 14
              + len(link_rows) * 14
              + PAD)
    card_h = max(card_h, 68)

    # Karten-Hintergrund (kaum sichtbar, leicht heller als schwarz)
    c.setFillColor(CARD_BG)
    c.roundRect(MAR, y - card_h, CW, card_h, 4, fill=1, stroke=0)

    # Linker Magenta-Akzentstreifen
    c.setFillColor(MAGENTA)
    c.rect(MAR, y - card_h, 2.5, card_h, fill=1, stroke=0)

    iy = y - PAD - 3

    # Titel
    c.setFont('Georgia-Bold', 10.5)
    c.setFillColor(WHITE)
    c.drawString(MAR + 12, iy, title)
    iy -= 15

    # Beschreibung
    c.setFont('Helvetica', 8.5)
    c.setFillColor(GREY)
    for line in all_lines:
        if line == '':
            iy -= 3
        else:
            c.drawString(MAR + 12, iy, line)
            iy -= 10.5
    iy -= 6

    # Reps — nur Umriss, nicht gefüllt
    reps_w = c.stringWidth(reps, 'Helvetica', 7.5) + 14
    c.setStrokeColor(MAGENTA)
    c.setLineWidth(0.6)
    c.setFillColor(BLACK)
    c.roundRect(MAR + 12, iy - 11, reps_w, 12, 3, fill=1, stroke=1)
    c.setFillColor(MAGENTA)
    c.setFont('Helvetica', 7.5)
    c.drawString(MAR + 19, iy - 8, reps)
    iy -= 17

    # Video-Links
    for row in link_rows:
        lx = MAR + 12
        for label, url in row:
            txt = f'> {label}'
            c.setFont('Georgia-Italic', 8)
            lw = c.stringWidth(txt, 'Georgia-Italic', 8)
            c.setFillColor(LMAGENTA)
            c.drawString(lx, iy, txt)
            c.setStrokeColor(LMAGENTA)
            c.setLineWidth(0.3)
            c.line(lx, iy - 1.5, lx + lw, iy - 1.5)
            c.linkURL(url, (lx, iy - 3, lx + lw, iy + 9), relative=0)
            lx += lw + 22
        iy -= 14

    return y - card_h - 10


def check_space(c, y, needed, page_num, plan_num, plan_name, subtitle):
    if y - needed < FTR_Y + 35:
        draw_footer(c, page_num)
        c.showPage()
        page_num += 1
        draw_page_background(c)
        # Einfacher Folgeseiten-Header
        c.setFillColor(BLACK)
        c.rect(0, H - 42, W, 42, fill=1, stroke=0)
        draw_logo(c, MAR, H - 8)
        c.setFont(TITLE_FONT, 14)
        c.setFillColor(WHITE)
        c.drawString(MAR + 170, H - 22, plan_name)
        c.setFont('Helvetica', 7)
        c.setFillColor(LMAGENTA)
        c.drawString(MAR + 170, H - 34, f'Plan {plan_num:02d}  ·  {subtitle}')
        c.setStrokeColor(MAGENTA)
        c.setLineWidth(0.5)
        c.line(MAR, H - 42, W - MAR, H - 42)
        y = H - 42 - 16
        draw_footer(c, page_num)
    return page_num, y


def create_plan(filename, plan_num, plan_name, subtitle, tags, exercises):
    c = canvas.Canvas(filename, pagesize=A4)
    page_num = 1

    draw_header(c, plan_num, plan_name, subtitle)
    draw_footer(c, page_num)

    y = H - HDR_H - 14

    # Session-Tags (schmal, elegant)
    tx = MAR
    c.setFont('Helvetica', 7.5)
    for lbl, val in tags:
        tag = f'{lbl}: {val}'
        tw = c.stringWidth(tag, 'Helvetica', 7.5) + 16
        c.setStrokeColor(LMAGENTA)
        c.setLineWidth(0.5)
        c.setFillColor(BLACK)
        c.roundRect(tx, y - 14, tw, 14, 3, fill=1, stroke=1)
        c.setFillColor(LMAGENTA)
        c.drawString(tx + 8, y - 10, tag)
        tx += tw + 6
    y -= 26

    # Warm Up
    page_num, y = check_space(c, y, 85, page_num, plan_num, plan_name, subtitle)
    y = draw_section_header(c, y, 'Warm Up')
    y = draw_exercise_card(
        c, y,
        'Warm Up — Gekürzt · 5 Minuten',
        ['Kurzes Aufwärmen für Gelenke und Muskeln. Führe das Warm Up Video auf halber '
         'Länge aus — ca. 5 Minuten genügen für das Heimtraining.'],
        '5 Min.',
        [('Video ansehen', L['warm'])],
    )

    # Übungen
    for section, exs in exercises:
        page_num, y = check_space(c, y, 65, page_num, plan_num, plan_name, subtitle)
        y = draw_section_header(c, y, section)
        for ex in exs:
            all_l = []
            for p in ex['desc']:
                all_l.extend(simpleSplit(p, 'Helvetica', 8.5, CW - 2 * PAD - 10))
            lr = [ex['links'][i:i+2] for i in range(0, len(ex['links']), 2)]
            ch = PAD + 15 + 4 + len(all_l) * 10.5 + 8 + 14 + len(lr) * 14 + PAD
            ch = max(ch, 68)
            page_num, y = check_space(c, y, ch + 8, page_num, plan_num, plan_name, subtitle)
            y = draw_exercise_card(c, y, ex['title'], ex['desc'],
                                   '3 Sätze  ×  8 Wiederholungen', ex['links'])

    c.save()
    print(f'OK  {os.path.basename(filename)}')


# ── Übungs-Bausteine ─────────────────────────────────────────────────────────

def hgk(key, extra=''):
    names = {
        'hgk1': 'Stärken der Sehnen am Handgelenk',
        'hgk2': 'Handgelenk & Sehnen — Variante 2',
        'hgk3': 'Handgelenk & Sehnen — Variante 3',
    }
    base = ('Gezielte Kräftigung der Handgelenksehnen — essenziell vor Pole und Aerial Hoop. '
            'Schützt vor Überlastung und baut langfristig Stabilität auf.')
    return dict(title=names[key], desc=[base + (' ' + extra if extra else '')],
                links=[('Video ansehen', L[key])])


E = {
    'hgk1': hgk('hgk1'),
    'hgk2': hgk('hgk2', 'Trainiert die Sehnen aus einem anderen Winkel.'),
    'hgk3': hgk('hgk3', 'Dritte Variante für umfassende Prävention.'),

    'sside': dict(
        title='Schulter Side Pushes — Unterarmplank',
        desc=['Laterale Schulterdrücke aus der Unterarmstützposition. Kräftigt die seitliche '
              'Schultermuskulatur und stabilisiert den gesamten Schultergürtel.'],
        links=[('Video ansehen', L['sside'])]),

    'scar': dict(
        title='Scarabeus — Laterale Schulter & Schulterblätter',
        desc=['Kräftigt gezielt die laterale Schultermuskulatur und die Schulterblatt-Stabilisatoren. '
              'Essenziell für Inversionen, Shoulder Mounts und präzise Arm-Haltungen.'],
        links=[('Video ansehen', L['scar'])]),

    'splank': dict(
        title='Schulter & Core — Ober- und Unterarmplank',
        desc=['Kräftigt Schultern und Core gleichzeitig. Der Übergang zwischen beiden '
              'Plankpositionen ist die Trainingsübung — kontrolliert und bewusst ausführen.'],
        links=[('Video ansehen', L['splank'])]),

    'dolph': dict(
        title='Schulterbrust Pushes — Dolphinpose',
        desc=['In der Dolphinpose werden Schultern und Brust durch Drückbewegungen gleichzeitig '
              'trainiert. Stärkt den gesamten Oberkörper und bereitet den Shoulder Mount vor.'],
        links=[('Video ansehen', L['dolph'])]),

    'wand': dict(
        title='Schulter-Brust Push — Wand oder Türrahmen',
        desc=['Drückbewegung gegen Wand oder Türrahmen aktiviert Schultern und Brust gleichzeitig. '
              'Ideal für zu Hause ohne Equipment — Intensität über Körperneigung regulierbar.'],
        links=[('Video ansehen', L['wand'])]),

    'brust': dict(
        title='Mobilisation des Brustbeines',
        desc=['Öffnet und mobilisiert das Brustbein und die Brustwirbelsäule. Fördert die '
              'Beweglichkeit im Oberkörper — essenziell für saubere Figuren am Pole und Hoop.'],
        links=[('Video ansehen', L['brust'])]),

    'brust_pl': dict(
        title='Mobilisation des Brustbeines — im Unterarmplank',
        desc=['Brustbeinmobilisation aus der Unterarmplankposition. Kombiniert Mobilisation mit '
              'Stabilisierungsarbeit — besonders wirksam für Haltung und Körperlinie.'],
        links=[('Video ansehen', L['brust_pl'])]),

    'dbug': dict(
        title='Dead Bug — Variante A',
        desc=['Effektive Übung für die tiefe Bauchmuskulatur. Kräftigt den Rumpf bei gleichzeitiger '
              'Stabilisierung der Wirbelsäule. Lendenwirbelsäule flach am Boden — für alle Levels.'],
        links=[('Video ansehen', L['dbug'])]),

    'dbug4': dict(
        title='Dead Bug — Variante B',
        desc=['Zweite Dead Bug Variante mit erhöhter Herausforderung für Koordination und '
              'tiefe Rumpfstabilisatoren. Langsame, kontrollierte Ausführung.'],
        links=[('Video ansehen', L['dbug4'])]),

    'hueft': dict(
        title='Core & Hüftbeuger — Kräftigung',
        desc=['Kombinationsübung für Bauchmuskulatur und Hüftbeuger. Stärkt die Verbindung '
              'zwischen Core und Hüfte — wichtig für Hebefiguren und Inversionen.'],
        links=[('Video ansehen', L['hueft'])]),

    'cdyn': dict(
        title='Core dynamisch — Unterarmplank',
        desc=['Dynamische Core-Übung aus dem Unterarmstütz. Aktiviert die gesamte Rumpfmuskulatur '
              'durch kontrollierte Bewegungen. Hüften stabil halten — kein Ausweichen.'],
        links=[('Video ansehen', L['cdyn'])]),

    'sdips': dict(
        title='Side Dips — Unterarmplank · Langsam',
        desc=['Seitliche Hüftabsenkungen, bewusst langsam ausgeführt. Trainiert die seitliche '
              'Bauchmuskulatur (Obliques) und verbessert die Körperkontrolle.'],
        links=[('Video ansehen', L['sdips'])]),

    'core2': dict(
        title='Core & Bauchmuskeln — Variante 2',
        desc=['Zweite Variante der Kernkräftigung. Aktiviert die gesamte Bauchmuskulatur mit '
              'neuer Bewegungsqualität. Variiere regelmässig für optimalen Trainingsreiz.'],
        links=[('Video ansehen', L['core2'])]),

    'core3': dict(
        title='Core & Bauchmuskeln — Variante 3',
        desc=['Dritte Variante der Kernkräftigung. Wechsle regelmässig zwischen den Core-Varianten '
              'um die Muskulatur aus unterschiedlichen Winkeln zu trainieren.'],
        links=[('Video ansehen', L['core3'])]),

    'core5': dict(
        title='Core & Bauchmuskeln — Variante 5',
        desc=['Fünfte Variante der Kernkräftigung. Variiere dein Core-Training regelmässig — '
              'alle Fasern der Bauchmuskulatur gleichmässig trainieren.'],
        links=[('Video ansehen', L['core5'])]),

    'pu_beg': dict(
        title='Push Up — Beginner · Wähle deine Variante',
        desc=[
            'Starte mit der Variante, die sich leichter anfühlt — das ist sehr individuell.',
            'Eng (Nr. 1): Hände schulterbreit, Ellbogen nah am Körper.',
            'Weit (Nr. 2): Hände breiter als Schultern — intensiver für die Brust.',
        ],
        links=[('Push Up Eng — Nr. 1', L['pu1']), ('Push Up Weit — Nr. 2', L['pu2'])]),

    'pu3': dict(
        title='Push Up auf Fäusten — Intermediate',
        desc=['Push Up auf geballten Fäusten. Baut Stabilität in Handgelenk und Unterarm auf — '
              'wichtige Vorbereitung für fortgeschrittene Pole-Elemente.'],
        links=[('Video — Nr. 3', L['pu3'])]),

    'pu4': dict(
        title='Push Up Eng · Wechsel auf Fäuste — Nr. 4',
        desc=['Kombination aus engem Push Up und Übergang auf die Fäuste. Trainiert Koordination, '
              'Handgelenksstabilität und Körperkontrolle gleichzeitig.'],
        links=[('Video — Nr. 4', L['pu4'])]),

    'strip': dict(
        title='Stripper Push Up — Fortgeschritten',
        desc=['Fortgeschrittene Push Up Variante mit integrierter Wirbelsäulenmobilisation. '
              'Fördert Flexibilität und stärkt den Oberkörper elegant.'],
        links=[('Video ansehen', L['strip'])]),
}


# ── 8 Pläne (~20 Min. je) ────────────────────────────────────────────────────
# Feste Reihenfolge in allen Plänen:
# 1. Warm Up → 2. Brust & Mobilisation → 3. Handgelenk & Schulter-Vorbereitung
# 4. Schulter — Unterarmplank → 5. Core & Bauch → 6. Hüftbeuger → 7. Push Ups

PLANS = [
    dict(num=1, name='Klassisch', subtitle='Grundlage · alle Levels',
         exercises=[
             ('Brust & Mobilisation',          [E['brust']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk1']]),
             ('Schulter — Unterarmplank',       [E['sside']]),
             ('Core & Bauch',                   [E['dbug']]),
             ('Hüftbeuger',                     [E['hueft']]),
             ('Push Ups',                       [E['pu_beg']]),
         ]),
    dict(num=2, name='Tiefenstabilität', subtitle='Plank-Focus · alle Levels',
         exercises=[
             ('Brust & Mobilisation',          [E['brust_pl']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk2']]),
             ('Schulter — Unterarmplank',       [E['sside']]),
             ('Core & Bauch',                   [E['dbug4']]),
             ('Hüftbeuger',                     [E['hueft']]),
             ('Push Ups',                       [E['pu_beg']]),
         ]),
    dict(num=3, name='Mobilität & Kraft', subtitle='Oberkörper-Focus · alle Levels',
         exercises=[
             ('Brust & Mobilisation',          [E['brust']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk3']]),
             ('Schulter — Unterarmplank',       [E['scar']]),
             ('Core & Bauch',                   [E['core2']]),
             ('Hüftbeuger',                     [E['hueft']]),
             ('Push Ups',                       [E['pu3']]),
         ]),
    dict(num=4, name='Lateralstärke', subtitle='Seitliche Muskulatur · alle Levels',
         exercises=[
             ('Brust & Mobilisation',          [E['brust_pl']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk1']]),
             ('Schulter — Unterarmplank',       [E['sside']]),
             ('Core & Bauch',                   [E['core3']]),
             ('Hüftbeuger',                     [E['sdips']]),
             ('Push Ups',                       [E['pu_beg']]),
         ]),
    dict(num=5, name='Schulter Power', subtitle='Schulter-Schwerpunkt · Intermediate',
         exercises=[
             ('Brust & Mobilisation',          [E['brust']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk2']]),
             ('Schulter — Unterarmplank',       [E['splank']]),
             ('Core & Bauch',                   [E['dbug']]),
             ('Hüftbeuger',                     [E['hueft']]),
             ('Push Ups',                       [E['pu3']]),
         ]),
    dict(num=6, name='Core Intensiv', subtitle='Bauch-Schwerpunkt · alle Levels',
         exercises=[
             ('Brust & Mobilisation',          [E['brust_pl']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk3']]),
             ('Schulter — Unterarmplank',       [E['sside']]),
             ('Core & Bauch',                   [E['core5']]),
             ('Hüftbeuger',                     [E['cdyn']]),
             ('Push Ups',                       [E['pu_beg']]),
         ]),
    dict(num=7, name='Fortgeschritten', subtitle='Progression · Intermediate bis Advanced',
         exercises=[
             ('Brust & Mobilisation',          [E['brust']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk1']]),
             ('Schulter — Unterarmplank',       [E['scar']]),
             ('Core & Bauch',                   [E['dbug4']]),
             ('Hüftbeuger',                     [E['hueft']]),
             ('Push Ups — Progression',         [E['pu4'], E['strip']]),
         ]),
    dict(num=8, name='Voller Mix', subtitle='Alle Bereiche · alle Levels',
         exercises=[
             ('Brust & Mobilisation',          [E['brust']]),
             ('Handgelenk & Schulter-Vorbereitung', [E['hgk2']]),
             ('Schulter — Unterarmplank',       [E['dolph']]),
             ('Core & Bauch',                   [E['core2']]),
             ('Hüftbeuger',                     [E['hueft']]),
             ('Push Ups',                       [E['pu3'], E['pu4']]),
         ]),
]

TAGS = [('Dauer', '~20 Min.'), ('Frequenz', '1–2x / Woche'), ('Sätze', '3 × 8')]

print('Vertical Kay Education — Trainingsplan Generator · Dark Edition')
print('=' * 60)

for plan in PLANS:
    n = plan['num']
    fn = os.path.join(OUTPUT, f'VK_Plan_{n:02d}_{plan["name"]}.pdf')
    create_plan(fn, n, plan['name'], plan['subtitle'], TAGS, plan['exercises'])

print('=' * 60)
print(f'Fertig! 8 PDFs erstellt.')

##https://github.com/mikosavolainen/koulutehtavia
## 22.9.2026


#!/usr/bin/env python3
"""LAB programming intro course week 3, task 2."""

# SATUNNAISIA VAKIOITA
KUNNAT = ['Akaa', 'Alajärvi', 'Alavieska', 'Alavus', 'Asikkala', 'Askola', 'Aura', 'Brändö', 'Eckerö', 'Enonkoski', 'Enontekiö', 'Espoo', 'Eura', 'Eurajoki', 'Evijärvi', 'Finström', 'Forssa', 'Föglö', 'Geta', 'Haapajärvi', 'Haapavesi', 'Hailuoto', 'Halsua', 'Hamina', 'Hammarland', 'Hankasalmi', 'Hanko', 'Harjavalta', 'Hartola', 'Hattula', 'Hausjärvi', 'Heinola', 'Heinävesi', 'Helsinki', 'Hirvensalmi', 'Hollola', 'Huittinen', 'Humppila', 'Hyrynsalmi', 'Hyvinkää', 'Hämeenkyrö', 'Hämeenlinna', 'Ii', 'Iisalmi', 'Iitti', 'Ikaalinen', 'Ilmajoki', 'Ilomantsi', 'Imatra', 'Inari', 'Inkoo', 'Isojoki', 'Isokyrö', 'Janakkala', 'Joensuu', 'Jokioinen', 'Jomala', 'Joroinen', 'Joutsa', 'Juuka', 'Juupajoki', 'Juva', 'Jyväskylä', 'Jämijärvi', 'Jämsä', 'Järvenpää', 'Kaarina', 'Kaavi', 'Kajaani', 'Kalajoki', 'Kangasala', 'Kangasniemi', 'Kankaanpää', 'Kannonkoski', 'Kannus', 'Karijoki', 'Karkkila', 'Karstula', 'Karvia', 'Kaskinen', 'Kauhajoki', 'Kauhava', 'Kauniainen', 'Kaustinen', 'Keitele', 'Kemi', 'Kemijärvi', 'Keminmaa', 'Kemiönsaari', 'Kempele', 'Kerava', 'Keuruu', 'Kihniö', 'Kinnula', 'Kirkkonummi', 'Kitee', 'Kittilä', 'Kiuruvesi', 'Kivijärvi', 'Kokemäki', 'Kokkola', 'Kolari', 'Konnevesi', 'Kontiolahti', 'Korsnäs', 'Koski Tl', 'Kotka', 'Kouvola', 'Kristiinankaupunki', 'Kruunupyy', 'Kuhmo', 'Kuhmoinen', 'Kumlinge', 'Kuopio', 'Kuortane', 'Kurikka', 'Kustavi', 'Kuusamo', 'Kyyjärvi', 'Kärkölä', 'Kärsämäki', 'Kökar', 'Lahti', 'Laihia', 'Laitila', 'Lapinjärvi', 'Lapinlahti', 'Lappajärvi', 'Lappeenranta', 'Lapua', 'Laukaa', 'Lemi', 'Lemland', 'Lempäälä', 'Leppävirta', 'Lestijärvi', 'Lieksa', 'Lieto', 'Liminka', 'Liperi', 'Lohja', 'Loimaa', 'Loppi', 'Loviisa', 'Luhanka', 'Lumijoki', 'Lumparland', 'Luoto', 'Luumäki', 'Maalahti', 'Maarianhamina - Mariehamn', 'Marttila', 'Masku', 'Merijärvi', 'Merikarvia', 'Miehikkälä', 'Mikkeli', 'Muhos', 'Multia', 'Muonio', 'Mustasaari', 'Muurame', 'Mynämäki', 'Myrskylä', 'Mäntsälä', 'Mänttä-Vilppula', 'Mäntyharju', 'Naantali', 'Nakkila', 'Nivala', 'Nokia', 'Nousiainen', 'Nurmes', 'Nurmijärvi', 'Närpiö', 'Orimattila', 'Oripää', 'Orivesi', 'Oulainen', 'Oulu', 'Outokumpu', 'Padasjoki', 'Paimio', 'Paltamo', 'Parainen', 'Parikkala', 'Parkano', 'Pedersören kunta', 'Pelkosenniemi', 'Pello', 'Perho', 'Petäjävesi', 'Pieksämäki', 'Pielavesi', 'Pietarsaari', 'Pihtipudas', 'Pirkkala', 'Polvijärvi', 'Pomarkku', 'Pori', 'Pornainen', 'Porvoo', 'Posio', 'Pudasjärvi', 'Pukkila', 'Punkalaidun', 'Puolanka', 'Puumala', 'Pyhtää', 'Pyhäjoki', 'Pyhäjärvi', 'Pyhäntä', 'Pyhäranta', 'Pälkäne', 'Pöytyä', 'Raahe', 'Raasepori', 'Raisio', 'Rantasalmi', 'Ranua', 'Rauma', 'Rautalampi', 'Rautavaara', 'Rautjärvi', 'Reisjärvi', 'Riihimäki', 'Ristijärvi', 'Rovaniemi', 'Ruokolahti', 'Ruovesi', 'Rusko', 'Rääkkylä', 'Saarijärvi', 'Salla', 'Salo', 'Saltvik', 'Sastamala', 'Sauvo', 'Savitaipale', 'Savonlinna', 'Savukoski', 'Seinäjoki', 'Sievi', 'Siikainen', 'Siikajoki', 'Siikalatva', 'Siilinjärvi', 'Simo', 'Sipoo', 'Siuntio', 'Sodankylä', 'Soini', 'Somero', 'Sonkajärvi', 'Sotkamo', 'Sottunga', 'Sulkava', 'Sund', 'Suomussalmi', 'Suonenjoki', 'Sysmä', 'Säkylä', 'Taipalsaari', 'Taivalkoski', 'Taivassalo', 'Tammela', 'Tampere', 'Tervo', 'Tervola', 'Teuva', 'Tohmajärvi', 'Toholampi', 'Toivakka', 'Tornio', 'Turku', 'Tuusniemi', 'Tuusula', 'Tyrnävä', 'Ulvila', 'Urjala', 'Utajärvi', 'Utsjoki', 'Uurainen', 'Uusikaarlepyy', 'Uusikaupunki', 'Vaala', 'Vaasa', 'Valkeakoski', 'Vantaa', 'Varkaus', 'Vehmaa', 'Vesanto', 'Vesilahti', 'Veteli', 'Vieremä', 'Vihti', 'Viitasaari', 'Vimpeli', 'Virolahti', 'Virrat', 'Vårdö', 'Vöyri', 'Ylitornio', 'Ylivieska', 'Ylöjärvi', 'Ypäjä', 'Ähtäri', 'Äänekoski']
ETUNIMET_MIEHET = ["Juhani", "Olavi", "Tapani", "Johannes", "Antero", "Tapio", "Mikael", "Kalevi", "Pekka", "Matti", "Petteri", "Ilmari", "Matias", "Sakari", "Kristian", "Antti", "Juha", "Heikki", "Timo", "Mikko", "Markus", "Aleksi", "Kari", "Jari", "Oskari", "Jukka", "Petri", "Mika", "Jaakko", "Henrik", "Markku", "Lauri", "Kalervo", "Ville", "Valtteri", "Veikko", "Hannu", "Elias", "Janne", "Marko", "Ari", "Seppo", "Tuomas", "Erkki", "Sami", "Ensio", "Juho", "Onni", "Erik", "Eemeli", "Jani", "Eero", "Samuli", "Oliver", "Eino", "Samuel", "Pentti", "Teemu", "Martti", "Harri", "Viljami", "Emil", "Jorma", "Leo", "Jarmo", "Risto", "Toivo", "Pasi", "Niko", "Veli", "Esa", "Joonas", "Jouni", "Olli", "Arto", "Kalle", "Toni", "Vesa", "Daniel", "Väinö", "Santeri", "Armas", "Alexander", "Pertti", "Johan", "Raimo", "Eetu", "Tomi", "Henri", "Sebastian", "Jouko", "Kimmo", "Esko", "Eemil", "Paavo", "Joni", "Anton", "Tommi", "Otto"]
ETUNIMET_NAISET = ["Maria", "Helena", "Johanna", "Kaarina", "Hannele", "Marjatta", "Kristiina", "Emilia", "Sofia", "Elina", "Liisa", "Maarit", "Susanna", "Tuulikki", "Katariina", "Annikki", "Anna", "Leena", "Marja", "Sinikka"]
ETUNIMET = ETUNIMET_MIEHET + ETUNIMET_NAISET
SUKUNIMET = ["Korhonen", "Virtanen", "Nieminen", "Mäkinen", "Hämäläinen", "Mäkelä", "Laine", "Heikkinen", "Koskinen", "Lehtonen", "Järvinen", "Lehtinen", "Saarinen", "Salminen", "Heinonen", "Heikkilä", "Niemi", "Salonen", "Laitinen", "Turunen", "Kinnunen", "Tuominen", "Savolainen", "Salo", "Rantanen", "Jokinen", "Miettinen", "Mattila", "Karjalainen", "Räsänen", "Ahonen", "Lahtinen", "Pitkänen", "Hiltunen", "Ojala", "Leppänen", "Aaltonen", "Leinonen", "Kallio", "Väisänen", "Anttila", "Mustonen", "Hakala", "Laaksonen", "Manninen", "Koivisto", "Lehto", "Laakso", "Hirvonen", "Toivonen", "Kettunen", "Hartikainen", "Nurmi", "Niskanen", "Aalto", "Partanen", "Peltonen", "Rantala", "Lappalainen", "Pulkkinen", "Niemelä", "Rissanen", "Seppälä", "Saari", "Kauppinen", "Hakkarainen", "Hänninen", "Huttunen", "Seppänen", "Moilanen", "Salmi", "Suominen", "Koskela", "Halonen", "Kemppainen", "Lahti", "Mikkonen", "Peltola", "Parviainen", "Kärkkäinen", "Leskinen", "Ikonen", "Aho", "Ahola", "Koponen", "Pesonen", "Oksanen", "Vainio", "Lindholm", "Heiskanen", "Vuorinen", "Johansson", "Rautiainen", "Mikkola", "Toivanen", "Karppinen", "Nurminen", "Koski", "Immonen", "Honkanen"]

# Tehtävän alustus, kohta tehtävän toteutukseen alempana tiedostossa
import random

luku_1 = random.randint(1, 1000000)
luku_2 = random.randint(1, 1000000)
luku_3 = random.randint(1, 1000000)
luku_4 = random.randint(1, 1000000)
luku_5 = random.random() * random.randint(1, 1000000)
luku_6 = random.random() * random.randint(1, 1000000)
luku_7 = random.random() * random.randint(1, 1000000)
luku_8 = random.random() * random.randint(1, 1000000)
luku_9 = random.random() * random.randint(1, 1000000)

etunimi = random.choice(ETUNIMET)
sukunimi = random.choice(SUKUNIMET)
vuosi = random.randint(1900, 2008)
asuinpaikka = random.choice(KUNNAT)

etunimi_1 = random.choice(ETUNIMET)
sukunimi_1 = random.choice(SUKUNIMET)
vuosi_1 = random.randint(1900, 2008)
asuinpaikka_1 = random.choice(KUNNAT)
etunimi_2 = random.choice(ETUNIMET)
sukunimi_2 = random.choice(SUKUNIMET)
vuosi_2 = random.randint(1900, 2008)
asuinpaikka_2 = random.choice(KUNNAT)
etunimi_3 = random.choice(ETUNIMET)
sukunimi_3 = random.choice(SUKUNIMET)
vuosi_3 = random.randint(1900, 2008)
asuinpaikka_3 = random.choice(KUNNAT)
etunimi_4 = random.choice(ETUNIMET)
sukunimi_4 = random.choice(SUKUNIMET)
vuosi_4 = random.randint(1900, 2008)
asuinpaikka_4 = random.choice(KUNNAT)


# LISÄÄ TEKSTINMUOTOILUT TÄMÄN RIVIN ALLE




muotoiltu_1 = f"{luku_1} + {luku_2} = {luku_1 + luku_2}"

muotoiltu_2 = f"{luku_3} * {luku_4} = {luku_3 * luku_4}"

muotoiltu_3 = f"{luku_5:.2f} / {luku_6:.2f} = {(luku_5 / luku_6):.2f}"

muotoiltu_4 = f"Ensimmäinen luku on {luku_7:e}, toinen luku on {luku_8:e} ja viimeinen {luku_9:e}."

muotoiltu_5 = f"{etunimi:>15s} {sukunimi:>20s} {vuosi:>5d} {asuinpaikka:>20}"

muotoiltu_6 = f"""\
{etunimi_1:>15s} {sukunimi_1:>20s} {vuosi_1:>5d} {asuinpaikka_1:>20}
{etunimi_2:>15s} {sukunimi_2:>20s} {vuosi_2:>5d} {asuinpaikka_2:>20}
{etunimi_3:>15s} {sukunimi_3:>20s} {vuosi_3:>5d} {asuinpaikka_3:>20}
{etunimi_4:>15s} {sukunimi_4:>20s} {vuosi_4:>5d} {asuinpaikka_4:>20}"""




# LISÄÄ TEKSTINMUOTOILUT TÄMÄN RIVIN YLÄPUOLELLE

# TARKISTUSKOODI ALKAA
try:
    print(muotoiltu_1)
    print(muotoiltu_2)
    print(muotoiltu_3)
    print(muotoiltu_4)
    print(muotoiltu_5)
    print(muotoiltu_6)
except Exception:
    print("Osa vaadituista merkkijonoista oli edelleen muotoilematta.")

valmis = True
try:
    if muotoiltu_1 == f"{luku_1} + {luku_2} = {luku_1 + luku_2}":
        print("muotoiltu_1 määritelty ja muotoiltu onnistuneesti.")
    else:
        valmis = False
        print(f"muotoiltu_1 ei ole muotoiltu oikein. Arvo oli: {muotoiltu_1}")
except Exception:
    valmis = False
    print("muotoiltu_1 ei ole vielä määritelty.")
try:
    if muotoiltu_2 == f"{luku_3} * {luku_4} = {luku_3 * luku_4}":
        print("muotoiltu_2 määritelty ja muotoiltu onnistuneesti.")
    else:
        valmis = False
        print(f"muotoiltu_2 ei ole muotoiltu oikein. Arvo oli: {muotoiltu_2}")
except Exception:
    valmis = False
    print("muotoiltu_2 ei ole vielä määritelty.")
try:
    if muotoiltu_3 == f"{luku_5:.2f} / {luku_6:.2f} = {(luku_5 / luku_6):.2f}":
        print("muotoiltu_3 määritelty ja muotoiltu onnistuneesti.")
    else:
        valmis = False
        print(f"muotoiltu_3 ei ole muotoiltu oikein. Arvo oli: {muotoiltu_3}")
except Exception:
    valmis = False
    print("muotoiltu_3 ei ole vielä määritelty.")
try:
    if muotoiltu_4 == f"Ensimmäinen luku on {luku_7:e}, toinen luku on {luku_8:e} ja viimeinen {luku_9:e}.":
        print("muotoiltu_4 määritelty ja muotoiltu onnistuneesti.")
    else:
        valmis = False
        print(f"muotoiltu_4 ei ole muotoiltu oikein. Arvo oli: {muotoiltu_4}")
except Exception:
    valmis = False
    print("muotoiltu_4 ei ole vielä määritelty.")
try:
    if muotoiltu_5 == f"{etunimi:>15s} {sukunimi:>20s} {vuosi:>5d} {asuinpaikka:>20}":
        print("muotoiltu_5 määritelty ja muotoiltu onnistuneesti.")
    else:
        valmis = False
        print(f"muotoiltu_5 ei ole muotoiltu oikein. Arvo oli: {muotoiltu_5}")
except Exception:
    valmis = False
    print("muotoiltu_5 ei ole vielä määritelty.")
try:
    if muotoiltu_6 == f"""\
{etunimi_1:>15s} {sukunimi_1:>20s} {vuosi_1:>5d} {asuinpaikka_1:>20}
{etunimi_2:>15s} {sukunimi_2:>20s} {vuosi_2:>5d} {asuinpaikka_2:>20}
{etunimi_3:>15s} {sukunimi_3:>20s} {vuosi_3:>5d} {asuinpaikka_3:>20}
{etunimi_4:>15s} {sukunimi_4:>20s} {vuosi_4:>5d} {asuinpaikka_4:>20}""":
        print("muotoiltu_6 määritelty ja muotoiltu onnistuneesti.")
    else:
        valmis = False
        print(f"muotoiltu_6 ei ole muotoiltu oikein. Arvo oli: {muotoiltu_6}")
except Exception:
    valmis = False
    print("muotoiltu_6 ei ole vielä määritelty.")

if valmis:
    print("\nKaikki merkkijonot muotoiltu onnistuneesti, tehtävä suoritettu.")
else:
    print("\nJotain puuttuu vielä, tehtävä on kesken.")


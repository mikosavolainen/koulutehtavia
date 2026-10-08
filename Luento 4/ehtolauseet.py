#!/usr/bin/env python3


# Tehtävän alustus (initialization) ja kirjastojen tuonti
import random

# Käytetään pythonin random-kirjastoa lukuarvojen arpomiseen.
# Kyseistä kirjasto on tarkoitettu satunnaislukujen ja -datan luontiin.
vrt_1 = random.randint(0, 100)
vrt_2 = random.randint(0, 100)
vrt_3 = random.randint(0, 11)
vrt_4 = random.randint(0, 11)
vrt_5 = random.randint(0, 100)
vrt_6 = random.randint(0, 100)
vrt_7 = random.randint(0, 21)
vrt_8 = random.randint(0, 21)
vrt_9 = random.randint(-10, 11)
vrt_10 = random.randint(0, 100)
vrt_11 = random.randint(0, 100)
vrt_12 = random.randint(0, 100)
vrt_13 = random.randint(0, 11)


# Vastausmuuttujat alustetaan tyhjällä merkkijonolla, jotta ne ovat olemassa
# myös ne määrittelevän ehtolauseen ulkopuolella
vastaus_1 = ""
vastaus_2 = ""
vastaus_3 = ""
vastaus_4 = ""
vastaus_5 = ""
vastaus_6 = ""
vastaus_7 = ""
vastaus_8 = ""

# ------------------------- ALOITA TEHTÄVÄN TOTEUTUS TÄSTÄ ---------------------------- #

# Osa 1
if vrt_1 < vrt_2:
    vastaus_1 = f"{vrt_1} pienempi kuin {vrt_2}"
else:
    vastaus_1 = f"{vrt_1} suurempi tai yhtäsuuri kuin {vrt_2}"

# Osa 2
if vrt_3 == vrt_4:
    vastaus_2 = f"{vrt_3} ja {vrt_4} yhtäsuuret"
else:
    vastaus_2 = f"{vrt_3} ja {vrt_4} eroavat"

# Osa 3
if vrt_5 > vrt_6:
    vastaus_3 = f"{vrt_5} suurempi kuin {vrt_6}"
else:
    vastaus_3 = f"{vrt_3} pienempi tai yhtäsuuri kuin {vrt_6}"

# Osa 4
if vrt_7 < vrt_8:
    vastaus_4 = f"{vrt_7} pienempi kuin {vrt_8}"
elif vrt_7 == vrt_8:
    vastaus_4 = f"{vrt_7} yhtäsuuri kuin {vrt_8}"
else:
    vastaus_4 = f"{vrt_7} suurempi kuin {vrt_8}"


if vrt_9 < 0:
    vastaus_5 = f"{vrt_9} pienempi kuin 0"
elif vrt_9 == 0:
    vastaus_5 = f"{vrt_9} suurempi kuin 0"
else:
    vastaus_5 = f"{vrt_9} on 0"

# Osa 6
if vrt_10 == 0:
    vastaus_6 = f"{vrt_10} on 0"
elif vrt_10 % 2 == 0:
    vastaus_6 = f"{vrt_10} on parillinen"
else:
    vastaus_6 = f"{vrt_10} on pariton"

# Osa 7
if vrt_11 == 0:
    vastaus_7 = f"{vrt_11} on 0"
elif vrt_11 % 2 == 0 and vrt_11 % 7 == 0:
    vastaus_7 = f"{vrt_11} on jaollinen kahdella ja seitsemällä"
elif vrt_11 % 2 == 0:
    vastaus_7 = f"{vrt_11} on jaollinen kahdella"
elif vrt_11 % 7 == 0:
    vastaus_7 = f"{vrt_11} on jaollinen seitsemällä"
else:
    vastaus_7 = f"{vrt_11} ei ole jaollinen kahdella eikä seitsemällä"

# Osa 8
if vrt_13 == 0:
    vastaus_8 = "Nollalla ei voi jakaa"
elif vrt_12 % vrt_13 == 0:
    vastaus_8 = f"{vrt_12} on jaollinen {vrt_13}:lla"
else:
    vastaus_8 = f"{vrt_12} ei ole jaollinen {vrt_13}:lla"


# ----------------------- TEHTÄVÄN TOTEUTUS ENNEN TÄTÄ RIVIÄ -------------------------- #
# Tarkistetaan osa 1
oikein_1 = ""
if vrt_1 < vrt_2:
    oikein_1 = f"{vrt_1} pienempi kuin {vrt_2}"
else:
    oikein_1 = f"{vrt_1} suurempi tai yhtäsuuri kuin {vrt_2}"
if vastaus_1 == oikein_1:
    print("vastaus_1 on oikein.")
else:
    print(f"""vastaus_1 on väärin.
Haluttu vastaus {oikein_1}
Saatu vastaus {vastaus_1}""")

# Tarkistetaan osa 2
oikein_2 = ""
if vrt_3 == vrt_4:
    oikein_2 = f"{vrt_3} ja {vrt_4} yhtäsuuret"
else:
    oikein_2 = f"{vrt_3} ja {vrt_4} eroavat"
if vastaus_2 == oikein_2:
    print("vastaus_2 on oikein.")
else:
    print(f"""vastaus_2 on väärin.
Haluttu vastaus {oikein_2}
Saatu vastaus {vastaus_2}""")

# Tarkistetaan osa 3
oikein_3 = ""
if vrt_5 > vrt_6:
    oikein_3 = f"{vrt_5} suurempi kuin {vrt_6}"
else:
    oikein_3 = f"{vrt_5} pienempi tai yhtäsuuri kuin {vrt_6}"
if vastaus_3 == oikein_3:
    print("vastaus_3 on oikein.")
else:
    print(f"""vastaus_3 on väärin.
Haluttu vastaus {oikein_3}
Saatu vastaus {vastaus_3}""")

# Tarkistetaan osa 4
oikein_4 = ""
if vrt_7 < vrt_8:
    oikein_4 = f"{vrt_7} pienempi kuin {vrt_8}"
elif vrt_7 == vrt_8:
    oikein_4 = f"{vrt_7} yhtäsuuri kuin {vrt_8}"
else:
    oikein_4 = f"{vrt_7} suurempi kuin {vrt_8}"
if vastaus_4 == oikein_4:
    print("vastaus_4 on oikein.")
else:
    print(f"""vastaus_4 on väärin.
Haluttu vastaus {oikein_4}
Saatu vastaus {vastaus_4}""")

# Tarkistetaan osa 5
oikein_5 = ""
if vrt_9 < 0:
    oikein_5 = f"{vrt_9} pienempi kuin 0"
elif vrt_9 == 0:
    oikein_5 = f"{vrt_9} suurempi kuin 0"
else:
    oikein_5 = f"{vrt_9} on 0"
if vastaus_5 == oikein_5:
    print("vastaus_5 on oikein.")
else:
    print(f"""vastaus_5 on väärin.
Haluttu vastaus {oikein_5}
Saatu vastaus {vastaus_5}""")

# Tarkistetaan osa 6
oikein_6 = ""
if vrt_10 == 0:
    oikein_6 = f"{vrt_10} on 0"
elif vrt_10 % 2 == 0:
    oikein_6 = f"{vrt_10} on parillinen"
else:
    oikein_6 = f"{vrt_10} on pariton"
if vastaus_6 == oikein_6:
    print("vastaus_6 on oikein.")
else:
    print(f"""vastaus_6 on väärin.
Haluttu vastaus {oikein_6}
Saatu vastaus {vastaus_6}""")


# Tarkistetaan osa 7
oikein_7 = ""
if vrt_11 == 0:
    oikein_7 = f"{vrt_11} on 0"
elif vrt_11 % 2 == 0 and vrt_11 % 7 == 0:
    oikein_7 = f"{vrt_11} on jaollinen kahdella ja seitsemällä"
elif vrt_11 % 2 == 0:
    oikein_7 = f"{vrt_11} on jaollinen kahdella"
elif vrt_11 % 7 == 0:
    oikein_7 = f"{vrt_11} on jaollinen seitsemällä"
else:
    oikein_7 = f"{vrt_11} ei ole jaollinen kahdella eikä seitsemällä"
if vastaus_7 == oikein_7:
    print("vastaus_7 on oikein.")
else:
    print(f"""vastaus_7 on väärin.
Haluttu vastaus {oikein_7}
Saatu vastaus {vastaus_7}""")

# Tarkistetaan osa 8
oikein_8 = ""
if vrt_13 == 0:
    oikein_8 = "Nollalla ei voi jakaa"
elif vrt_12 % vrt_13 == 0:
    oikein_8 = f"{vrt_12} on jaollinen {vrt_13}:lla"
else:
    oikein_8 = f"{vrt_12} ei ole jaollinen {vrt_13}:lla"
if vastaus_8 == oikein_8:
    print("vastaus_8 on oikein.")
else:
    print(f"""vastaus_8 on väärin.
Haluttu vastaus {oikein_8}
Saatu vastaus {vastaus_8}""")

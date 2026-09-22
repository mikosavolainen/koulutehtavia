##https://github.com/mikosavolainen/koulutehtavia
## 22.9.2026


#!/usr/bin/env python3
"""LAB programming intro course week 3, task 2."""


# LISÄÄ MÄÄRITTELEMÄSI MUUTTUJAT TÄMÄN RIVIN ALLE



luku_1 = 15
luku_2 = 9122
luku_3 = 51.9244
luku_4 = 912.11222

PI = 3.14159
OSOITE = "https://moodle.lab.fi"

merkkijono_1 = "Tämä on ensimmäinen esimerkki merkkijonosta. "
merkkijono_2 = "Tämä on toinen esimerkki merkkijonosta."

y_1 = luku_2 - luku_1
y_2 = luku_3 + luku_4
y_3 = luku_1 * luku_3

m_1 = merkkijono_1 + merkkijono_2




# LISÄÄ MÄÄRITTELEMÄSI MUUTTUJAT ENNEN TÄTÄ RIVIÄ


# TARKISTUSKOODI ALKAA

valmis = True

try:
    if luku_1 == 15:
        print("luku_1 on määritelty oikein")
    else:
        valmis = False
        print(f"luku_1 on määritelty väärin, määritelty arvo: {luku_1}")
except Exception:
    valmis = False
    print("luku_1 on vielä määrittelemättä")

try:
    if luku_2 == 9122:
        print(f"luku_2 on määritelty oikein")
    else:
        valmis = False
        print(f"luku_2 on määritelty väärin, määritelty arvo: {luku_2}")
except Exception:
    valmis = False
    print("luku_2 on vielä määrittelemättä")

try:
    if luku_3 == 51.9244:
        print("luku_3 on määritelty oikein")
    else:
        valmis = False
        print(f"luku_3 on määritelty väärin, määritelty arvo: {luku_3}")
except Exception:
    valmis = False
    print("luku_3 on vielä määrittelemättä")

try:
    if luku_4 == 912.11222:
        print("luku_4 on määritelty oikein")
    else:
        valmis = False
        print(f"luku_4 on määritelty väärin, määritelty arvo: {luku_4}")
except Exception:
    valmis = False
    print("luku_4 on vielä määrittelemättä")

try:
    if PI == 3.14159:
        print("PI on määritelty oikein")
    else:
        valmis = False
        print(f"PI on määritelty väärin, määritelty arvo: {PI}")
except Exception:
    valmis = False
    print("PI on vielä määrittelemättä")

try:
    if OSOITE == "https://moodle.lab.fi":
        print("OSOITE on määritelty oikein")
    else:
        valmis = False
        print(f"OSOITE on määritelty väärin, määritelty arvo: {OSOITE}")
except Exception:
    valmis = False
    print("OSOITE on vielä määrittelemättä")

try:
    if merkkijono_1 == "Tämä on ensimmäinen esimerkki merkkijonosta. ":
        print("merkkijono_1 on määritelty oikein")
    else:
        valmis = False
        print(f"merkkijono_1 on määritelty väärin, määritelty arvo: {merkkijono_1}")
except Exception:
    valmis = False
    print("merkkijono_1 on vielä määrittelemättä")

try:
    if merkkijono_2 == "Tämä on toinen esimerkki merkkijonosta.":
        print("merkkijono_2 on määritelty oikein")
    else:
        valmis = False
        print(f"merkkijono_2 on määritelty väärin, määritelty arvo: {merkkijono_2}")
except Exception:
    valmis = False
    print("merkkijono_2 on vielä määrittelemättä")

try:
    if y_1 == luku_2 - luku_1:
        print("y_1 on määritelty oikein")
    else:
        valmis = False
        print(f"y_1 on määritelty väärin, määritelty arvo: {y_1}")
except Exception:
    valmis = False
    print("y_1 on vielä määrittelemättä")

try:
    if y_2 == luku_3 + luku_4:
        print("y_2 on määritelty oikein")
    else:
        valmis = False
        print(f"y_2 on määritelty väärin, määritelty arvo: {y_2}")
except Exception:
    valmis = False
    print("y_2 on vielä määrittelemättä")

try:
    if y_3 == luku_1 * luku_3:
        print("y_3 on määritelty oikein")
    else:
        valmis = False
        print(f"y_3 on määritelty väärin, määritelty arvo: {y_3}")
except Exception:
    valmis = False
    print("y_3 on vielä määrittelemättä")

try:
    if m_1 == merkkijono_1 + merkkijono_2:
        print("m_1 on määritelty oikein")
    else:
        valmis = False
        print(f"m_1 on määritelty väärin, määritelty arvo: {m_1}")
except Exception:
    valmis = False
    print("m_1 on vielä määrittelemättä")

if valmis:
    print("\nKaikki muuttujat määritelty onnistuneesti, tehtävä suoritettu.")
else:
    print("\nJotain puuttuu vielä, tehtävä on kesken.")

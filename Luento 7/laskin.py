##https://github.com/mikosavolainen/koulutehtavia
## 28.10.2026


def tulosta_aloitusviesti():
  print("Laskin käynnistyy...")
  print("Ohjelmassa on saatavilla seuraavat toiminnot:")
  print("    +   – laske numeroiden summa")
  print("    -   – laske numeroiden erotus")
  print("    *   – laske numeroiden tulo")
  print("    /   – laske numeroiden osamäärä")
  print("    p   – tulosta operaatioiden historia")
  print("    q   – lopeta ohjelma (myös tyhjä syöte lopettaa ohjelman)")
  print("    ?,h – tulosta tämä viesti")

def paaohjelma():
  historia = []
  tulosta_aloitusviesti()

  while True:
    try:
      syote = input("> ").strip()
    except EOFError:
      break

    if syote == "" or syote.lower() == "q":
      print("Lopetetaan ohjelma...")
      break

    elif syote in ["?", "h"]:
      tulosta_aloitusviesti()

    elif syote == "p":
      for rivi in historia[-10:]:
        print(rivi)

    else:
      operaattori = None
      for op in ["+", "-", "*", "/"]:
        if op in syote:
          operaattori = op
          break

      if operaattori:
        osat = syote.split(operaattori)

        if len(osat) == 2:
          vasen_str = osat[0].strip()
          oikea_str = osat[1].strip()

          try:
            eka = float(vasen_str) if "." in vasen_str else int(vasen_str)
            toka = float(oikea_str) if "." in oikea_str else int(oikea_str)

            if operaattori == "+":
              tulos = eka + toka
            elif operaattori == "-":
              tulos = eka - toka
            elif operaattori == "*":
              tulos = eka * toka
            elif operaattori == "/":
              tulos = eka / toka

            tulos_rivi = f"{vasen_str} {operaattori} {oikea_str} = {tulos}"
            print(tulos_rivi)
            historia.append(tulos_rivi)

          except ValueError:
            print(f"Syötteen muuttaminen numeroiksi epäonnistui. Syötettiin arvot {vasen_str} ja {oikea_str}.")
            print("Syötä vain kokonais- tai desimaalilukuja.")
          except ZeroDivisionError:
            print("Virhe: Nollalla jakaminen ei ole sallittua!")

if __name__ == "__main__":
  paaohjelma()
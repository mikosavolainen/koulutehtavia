def suorita_lasku(valinta, eka, toka):
  """Suorittaa varsinaisen laskutoimituksen valinnan mukaan."""
  if valinta == "1":
    return eka + toka
  elif valinta == "2":
    return eka - toka
  elif valinta == "3":
    return eka * toka
  elif valinta == "4":
    if toka == 0:
      return "Virhe: Nollalla ei voi jakaa!"
    return eka / toka
  else:
    return "Virheellinen toiminto."


def paaohjelma():
  print("Tervetuloa käyttämään komentorivilaskinta!")

  while True:
    print("\nValitse toiminto:")
    print("1. Yhteenlasku (+)")
    print("2. Vähennyslasku (-)")
    print("3. Kertolasku (*)")
    print("4. Jakolasku (/)")
    print("0. Lopeta ohjelma")

    valinta = input("Anna valintasi (0-4): ")

    if valinta == "0":
      print("Lopetetaan ohjelma. Hei hei!")
      break

    if valinta in ["1", "2", "3", "4"]:
      try:

        eka = float(input("Anna ensimmäinen luku: "))
        toka = float(input("Anna toinen luku: "))

        tulos = suorita_lasku(valinta, eka, toka)
        print(f"Tulos: {tulos}")

      except ValueError:
        print("Virhe: Syötthän vain numeroita!")
    else:
      print("Virheellinen valinta. Valitse numero 0-4 väliltä.")


if __name__ == "__main__":
  paaohjelma()
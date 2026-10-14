##https://github.com/mikosavolainen/koulutehtavia
## 14.10.2026

#!/usr/bin/env python3
"""LAB programming course week 6, task 1."""


import random


# ------------------------- ALOITA TEHTÄVÄN TOTEUTUS TÄSTÄ ---------------------------- #
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    if not numbers:
        return 0
    
    sorted_numbers = sorted(numbers)
    index = int(len(sorted_numbers) / 2)
    return sorted_numbers[index]


def most_common(items):
    if not items:
        return []
    
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
        
    max_count = max(counts.values())
    
    common_items = [item for item, count in counts.items() if count == max_count]
    
    return common_items
# ----------------------- TEHTÄVÄN TOTEUTUS ENNEN TÄTÄ RIVIÄ -------------------------- #


# TARKISTUSKOODI ALKAA

def validate_calculate_average():
    """Validate that the calculate_average function works as expected."""
    try:
        # Test calculate_average with 100 randomly generated test cases
        for _ in range(0, 100):
            # Get a list between 0 and 10000 items
            len_list = random.randint(1, 10000)
            values = [random.randint(0, 100000) for _i in range(0, len_list)]
            avg = sum(values) / len_list
            avg_solution = calculate_average(values)
            if avg != avg_solution:
                print("Funktio calculate_average ei ole toteutettu oikein.")
                print(f"Saatiin arvo {avg_solution}, haluttiin arvo {avg}")
                return False

        # Test the case when the list is empty
        try:
            avg_solution = calculate_average([])
            if avg_solution != 0:
                print("Funktio calculate_average ei ole toteutettu oikein.")
                print("Tyhjän listan keskiarvon laskeminen epäonnistuu.")
                return False
        except Exception as e:
            print("Funktio calculate_average ei toimi listan ollessa tyhjä.")
            print(f"Funktio tuotti virheen {e}")
            return False

    except NameError:
        print("Funktiota calculate_average ei ole vielä määritelty.")
        return False

    print("Funktio calculate_average on toteutettu oikein.")
    return True


def validate_calculate_median():
    """Validate that the calculate_median function works as expected."""
    try:
        # Test calculate_median with 100 randomly generated test cases
        for _ in range(0, 100):
            # Get a list between 0 and 10000 items
            len_list = random.randint(1, 10000)
            values = [random.randint(0, 100000) for _i in range(0, len_list)]
            values_sorted = sorted(values)
            median = values_sorted[int(len_list / 2)]
            median_solution = calculate_median(values)
            if median != median_solution:
                print("Funktio calculate_median ei ole toteutettu oikein.")
                print(f"Saatiin arvo {median_solution}, haluttiin arvo {median}")
                return False

        # Test the case when the list is empty
        try:
            median_solution = calculate_median([])
            if median_solution != 0:
                print("Funktio calculate_median ei ole toteutettu oikein.")
                print("Tyhjän listan mediaanin laskeminen epäonnistuu.")
                return False
        except Exception as e:
            print("Funktio calculate_median ei toimi listan ollessa tyhjä.")
            print(f"Funktio tuotti virheen {e}")

    except NameError:
        print("Funktiota calculate_median ei ole vielä määritelty.")
        return False

    print("Funktio calculate_median on toteutettu oikein.")
    return True


def validate_most_common():
    """Validate that the most_common function works as expected."""
    try:
        # Test most_common with 20 randomly generated test cases
        for _ in range(0, 10):
            # Get a list between 0 and 10000 items
            len_list = random.randint(1, 10000)
            values = [random.randint(0, 100) for _i in range(0, len_list)]
            unique_values = set(values)
            most_common_amount = 0
            for value in unique_values:
                count = values.count(value)
                if count > most_common_amount:
                    most_common_amount = count
            most_common_items = list(set([item for item in values if values.count(item) == most_common_amount]))
            most_common_solution = most_common(values)

            if type(most_common_solution) is not list:
                print("Funktio most_common palauttaa väärän tyyppisen muuttujan.")
                print(f"Saatiin tyyppi {type(most_common_solution)}, haluttiin {list}")
                return False

            if sorted(most_common_solution) != sorted(most_common_items): 
                print("Funktio most_common palauttaa väärän arvon.")
                print(f"Saatiin arvo {most_common_solution}, haluttiin {most_common_items}")
                return False

    except NameError:
        print("Funktiota most_common ei ole vielä määritelty.")
        return False

    print("Funktio most_common on toteutettu oikein.")
    return True


def main():
    """Validate all functions."""
    answers = [
        validate_calculate_average(),
        validate_calculate_median(),
        validate_most_common(),
    ]

    if False in answers:
        print("Osa kohdista on vielä väärin, jatka yrittämistä.")
        return False

    print("Kaikki kohdat ovat oikein, onneksi olkoon!")
    return True


if __name__ == "__main__":
    main()

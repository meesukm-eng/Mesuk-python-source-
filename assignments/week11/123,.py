def get_temperatures():
    temps = [31, 31, 32, 29, 33, 31, 27]
    return temps


def analyze_temps(temps):
    highest = temps[0]
    lowest = temps[0]

    for temp in temps:
        if temp > highest:
            highest = temp

        if temp < lowest:
            lowest = temp

    average = sum(temps) / 7

    return (average, highest, lowest)


def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print("Average: %.1f C" % avg)
    print(f"Highest: {high:.1f} C")
    print("Lowest: %.1f C" % low)


temps = get_temperatures()
print(temps)

result = analyze_temps(temps)

display_analysis(result[0], result[1], result[2])
def recite(start_verse, end_verse):
    return [recite(i) for i in range(start_verse, end_verse+1)]

def recite(verse):
    numbers = {1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth'}
    header = f"On the {numbers.get(verse)} day of Christmas my true love gave to me: "
    verses =["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens", "four Calling Birds",
    "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing",
    "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]
    if verse == 1:
        return f"{header}{verses[0]}."
    return f"{header}{', '.join(verses[verse-1:0:-1])}, and {verses[0]}."

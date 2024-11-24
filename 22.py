def convert_to_words(num):
    if num == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    word = ""

    if num >= 100000:
        word += convert_to_words(num // 100000) + " lakh "
        num %= 100000

    
    if num >= 1000:
        word += convert_to_words(num // 1000) + " thousand "
        num %= 1000

   
    if num >= 100:
        word += ones[num // 100] + " hundred "
        num %= 100

    if 10 <= num < 20:
        word += teens[num - 10] + " "
    else:
        
        if num >= 20:
            word += tens[num // 10] + " "
            num %= 10

        
        if num > 0:
            word += ones[num] + " "

    return word.strip()

num = int(input("Enter a number: "))
words = convert_to_words(num)
print(words)

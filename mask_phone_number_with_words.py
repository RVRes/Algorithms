from random import choice


def mask_numbers_with_words(phone_number: str) -> str:
    """
    Mask phone number with replacing some numbers with words.
    """
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    splitters = [', ', ' ', '-']
    result = ''
    for i, num in enumerate(phone_number):
        if not num.isdigit():
            continue
        add_num = choice((num, words[int(num)]))
        if result:
            separator = choice(splitters) if add_num != num else ' ' if result[-1].isalpha() else choice(('', ' '))
            add_num = separator + add_num
        result += add_num
    return result


for _ in range(10):
    print(f"{'(123)3456787':20} {mask_numbers_with_words('(123)3456787')}")

for _ in range(10):
    print(f"{'(452) 345 - 34-56':20} {mask_numbers_with_words('(452) 345 - 34-56')}")

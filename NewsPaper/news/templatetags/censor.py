from django import template
register = template.Library()
bad_words = ['мат', 'хуй', 'блядь', 'сука','суки', 'дурак', 'идиот', 'наркотик', 'алкоголь', 'редиска']
@register.filter
def censor(value):
    if isinstance(value, str):
        for word in bad_words:
            value = value.replace(word, word[0] + '*' * (len(word) - 1))
        return value
    else:
        raise ValueError("Передан неверный тип переменной. Ожидалась строка")


from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
N_words = ['хук', 'пурга', 'домишко']
@register.filter()
def censor(value:str):
    value = value.lower()
    if type(value) != str:
       raise AttributeError # введён неверный тип аргумента
    for N in N_words:
      if N in value:
         value = value.replace(N, N[0] + '*'*len(N[1:]))
    return value


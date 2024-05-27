from django.db.models import Q
from goods.models import Products


def q_search(query):  # Созд. Q объекты, чтоб сделать удобный поиск на сайте
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)  # По опис
        q_objects |= Q(name__icontains=token)  # По назв

    return Products.objects.filter(q_objects)

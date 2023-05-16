from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage

def get_paginator(request, qs):
    try:
        page = int(request.query_params.get("page", 0))
        limit = int(request.query_params.get("limit", 2))

    except ValueError:
        page, limit = 1, 2
    print(page, limit)
    paginator = Paginator(qs, limit)
    print(paginator.page(1))
    
    try:
        page_object = paginator.page(page)
        object_list = page_object.object_list

    except (InvalidPage, PageNotAnInteger, EmptyPage) as e:
        print(e)
        return qs, paginator.count, None
    
    return object_list, paginator.count, page

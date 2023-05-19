from urllib.parse import urlparse

def parse(query: str) -> dict:

    query_parse = urlparse(query)
    useful_query = str(query_parse.query)
    dic = {}
    if '&' in useful_query:
        symbol_id_0 = useful_query.rfind('&')
        if len(useful_query) - 1 == symbol_id_0:
            useful_query = useful_query.rstrip('&')

    if '?' in useful_query:
        symbol_id_1 = useful_query.rfind('?')
        if (len(useful_query) - 1) == symbol_id_1:
            useful_query = useful_query.rstrip('?')

    if '&' in useful_query:
        useful_query = useful_query.split('&')

    if len(useful_query) != 0 and isinstance(useful_query,str):
        useful_query = [useful_query]

    for i in range(len(useful_query)):
        if '=' in useful_query[i]:
            result_list = useful_query[i].split('=')
            if result_list[0] in dic.keys():
                for_renew_value = [dic.get(result_list[0])]
                dic[result_list[0]] = for_renew_value
                dic[(result_list[0])].append(result_list[1])
            else:
                dic[result_list[0]] = result_list[1]

    return dic

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com?name=John&email=john@example.com') == {'name': 'John', 'email': 'john@example.com'}
    assert parse('https://example.com?category=books&sort=asc') == {'category': 'books', 'sort': 'asc'}
    assert parse('https://example.com/search?q=laptop&filter=price&max=1000') == {'q': 'laptop', 'filter': 'price', 'max': '1000'}
    assert parse('https://example.com?lang=en') == {'lang': 'en'}
    assert parse('https://example.com/cart?product=123&quantity=2') == {'product': '123', 'quantity': '2'}
    assert parse('https://example.com/login?redirect=dashboard') == {'redirect': 'dashboard'}
    assert parse('https://example.com?theme=dark') == {'theme': 'dark'}
    assert parse('https://example.com?campaign=summer_sale') == {'campaign': 'summer_sale'}
    assert parse('https://example.com?location=New+York&interests=food&interests=sports') == {'location': 'New+York', 'interests': ['food', 'sports']}
    assert parse('https://example.com/user?id=12345&token=abcdef') == {'id': '12345', 'token': 'abcdef'}
    
def parse_cookie(query: str) -> dict:

    dic_cookies = {}

    if ';' in query:
        symbol_id_1_cookies = query.rfind(';')

        if (len(query) - 1) == symbol_id_1_cookies:
            useful_query = query.rstrip(';')
            result_cokies = useful_query.split(';')
        else:
            result_cokies = query.split(';')

        for i in range(len(result_cokies)):
            if '=' in result_cokies[i]:
                result_list_cokies = result_cokies[i].split('=', 1)
                if result_list_cokies[0] in dic_cookies.keys():
                    for_renew_value_cookies = dic_cookies.get(result_list_cokies[0])
                    if isinstance(for_renew_value_cookies, list):
                        dic_cookies[(result_list_cokies[0])].append(result_list_cokies[1])
                    else:
                        dic_cookies[result_list_cokies[0]] = [for_renew_value_cookies]
                        dic_cookies[(result_list_cokies[0])].append(result_list_cokies[1])
                else:
                    dic_cookies[result_list_cokies[0]] = result_list_cokies[1]

    return dic_cookies

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('food=salat=borsch=cake;') == {'food': 'salat=borsch=cake'}
    assert parse_cookie('chair=red;bed=white') == {'chair': 'red', 'bed': 'white'}
    assert parse_cookie('piano=electric;cable=euro') == {'piano': 'electric', 'cable': 'euro'}
    assert parse_cookie('door=steel;handle=aluminium') == {'door': 'steel', 'handle': 'aluminium'}
    assert parse_cookie('fish=kapr;') == {'fish': 'kapr'}
    assert parse_cookie('mirror=2m;window=5m') == {'mirror': '2m', 'window': '5m'}
    assert parse_cookie('tablets=ip;') == {'tablets': 'ip'}
    assert parse_cookie(';') == {}
    assert parse_cookie('tv program=serial=film;') == {'tv program': 'serial=film'}
    assert parse_cookie('sport=gym;sport=bicycle;sport=walking') == {'sport': ['gym', 'bicycle', 'walking']}



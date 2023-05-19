
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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


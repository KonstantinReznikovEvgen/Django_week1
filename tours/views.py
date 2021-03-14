from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError

# Create your views here.


tours = {
    0: {
        "title": "Hotel title",
        "description": "description",
        "picture": "https://place-hold.it/300x200"
    },
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description": "Отель выглядит уютно. Он был построен из красного соснового дерева и украшен "
                       "синими камнями.  Высокие округлые окна добавляют общий стиль дома и были добавлены "
                       "в дом в довольно симметричном образце.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-1.2.1&ixid=eyJ"
                   "hcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Куба",
        "nights": 6,
        "date": "2 марта",
    },
    2: {
        "title": "Baroque Hotel",
        "description": "Здание отеля имеет форму короткой буквы U. Два расширения "
                       "связаны стеклянными нависающими панелями. Второй этаж такого же размера, "
                       "как и первый, который был построен точно над полом под ним. Этот этаж имеет "
                       "совершенно другой стиль, чем этаж ниже.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?ixlib=rb-"
                   "1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 85000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 8,
        "date": "12 января",
    },
    3: {
        "title": "Voyager Resort",
        "description": "Снаружи отель выглядит красиво и традиционно. Он был построен"
                       " с белыми камнями и имеет еловые деревянные украшения. Высокие, "
                       "большие окна добавляют к общему стилю дома и были добавлены в"
                       " дом в основном симметричным способом.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1569660072562-48a035e65c30?ixlib=rb-1.2.1&ixid=e"
                   "yJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 63000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 11,
        "date": "7 февраля",
    },
    4: {
        "title": "Orbit Hotel",
        "description": "Каждый домик оборудован средней кухней и одной небольшой ванной комнатой, в нем так"
                       "же есть уютная гостиная, две спальни, скромная столовая и большой подвал"
                       ".  Небольшие треугольные окна добавляют к общему стилю дома и были добавлены в дом в "
                       "основном симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid=eyJh"
                   "cHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Индия",
        "nights": 9,
        "date": "22 января",
    },
    5: {
        "title": "Atlantis Cabin Hotel",
        "description": "Этот дом среднего размера имеет футуристический вид и находится в среднем состоянии."
                       " Интерьер выполнен в насыщенных тонах. Двор небольшой и выглядит очень формально. "
                       "Кроме того, странные огни были замечены движущимися в доме ночью.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-1.2.1&ixid=eyJh"
                   "cHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "18 января",
    },
    6: {
        "title": "Light Renaissance Hotel",
        "description": "Этот крошечный дом выглядит довольно современно и находится в ужасном состоянии. "
                       "Интерьер выполнен в цветах, которые напоминают вам о тропическом лесу. Двор небольшо"
                       "й и заросший дикими растениями. Кроме того, это было однажды показано в телесериале,"
                       " демонстрирующем необычно украшенные дома.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&ixid=eyJ"
                   "hcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 53000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 13,
        "date": "15 февраля",
    },
    7: {
        "title": "King's Majesty Hotel",
        "description": "Этот дом средних размеров выглядит немного старомодно и находится в среднем "
                       "состоянии. Интерьер выполнен в цветах, которые напоминают о весеннем цветнике"
                       ". Двор среднего размера и напоминает луг. Кроме того, он был построен над оста"
                       "тками дома, который был разрушен в результате пожара.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1468824357306-a439d58ccb1c?ixlib=rb-1.2.1&ixid=ey"
                   "JhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "5",
        "country": "Мексика",
        "nights": 9,
        "date": "22 января",
    },
    8: {
        "title": "Crown Hotel",
        "description": "Этот огромный дом почти выглядит инопланетянином и находится в среднем состоянии."
                       " Интерьер выполнен в цветах, напоминающих апельсиновое дерево. Двор среднего разм"
                       "ера и напоминает луг. Кроме того, это место печально известного убийства.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1549109786-eb80da56e693?ixlib=rb-1.2.1&ixid=eyJhcHB"
                   "faWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 44000,
        "stars": "4",
        "country": "Тайланд",
        "nights": 7,
        "date": "3 февраля",
    },
    9: {
        "title": "Seascape Resort",
        "description": "Этот большой дом имеет сказочный вид и находится в отличном состоянии. Интерьер "
                       "выполнен в ярких цветах. Двор маленький и аккуратно подстрижен. На заднем дворе "
                       "есть большой участок недавно созданной земли, а дом имеет большой решетчатый заб"
                       "ор через него. На заднем дворе живут различные животные. Многие владельцы приложи"
                       "ли согласованные усилия для поддержания этой собственности.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1570214476695-19bd467e6f7a?ixlib=rb-1.2.1&ixid=eyJh"
                   "cHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 39000,
        "stars": "3",
        "country": "Индия",
        "nights": 10,
        "date": "1 февраля",
    },
    10: {
        "title": "Rose Sanctum Hotel",
        "description": "Снаружи этот дом выглядит старым, но чудесным. Он был построен из желтого сосн"
                       "ового дерева и украшен белым кирпичом. Короткие, широкие окна пропускают много"
                       " света и были добавлены в дом очень симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1560200353-ce0a76b1d438?ixlib=rb-1.2.1&ixid=eyJh"
                   "cHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 52000,
        "stars": "4",
        "country": "Куба",
        "nights": 10,
        "date": "30 января",
    },
    11: {
        "title": "Viridian Obelisk Hotel & Spa",
        "description": "В доме очень хороший двор с большими камнями, похожими на озеро. В задней час"
                       "ти дома окна просторные, с большими окнами, они светлее, чтобы улучшить впечат"
                       "ление. Снаружи есть пять маленьких деревьев. Двор в очень хорошем состоянии и о"
                       "чень живописный. Есть пруд для развлечения",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1477120128765-a0528148fed2?ixlib=rb-1.2.1&ixid=eyJ"
                   "hcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "5",
        "country": "Индия",
        "nights": 9,
        "date": "1 марта",
    },
    12: {
        "title": "Saffron Tundra Hotel & Spa",
        "description": "Дом оборудован огромной кухней и одной современной ванной комнатой, а также имее"
                       "т огромную гостиную, две спальни, небольшую столовую, гостиную и скромную кладов"
                       "ую.  Дом чистый, хорошо построенный и в хорошем состоянии, но, к сожалению, крова"
                       "ти сгорели в мае этого года и, к сожалению, все еще нуждаются в ремонте. Возможно,"
                       " понадобится целая команда, чтобы заменить старую медную топку.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1440151050977-247552660a3b?ixlib=rb-1.2.1&ixid=eyJhc"
                   "HBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "4",
        "country": "Мексика",
        "nights": 12,
        "date": "17 февраля",
    },
    13: {
        "title": "Traveller Resort",
        "description": "Снаружи этот дом выглядит очень элегантно. Он был построен из коричневого кир"
                       "пича и имеет коричневые кирпичные украшения. Высокие, большие окна добавляют к"
                       " общему стилю дома и были добавлены к дому в довольно асимметричном образце. Кр"
                       "ыша высокая и наклонена в одну сторону и покрыта коричневой черепицей. Один бол"
                       "ьшой дымоход высовывает центр крыши. На крыше нет окон. Сам дом окружен великоле"
                       "пным садом с виноградными лозами, пагодой, прудом и множеством разных цветов.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1553653924-39b70295f8da?ixlib=rb-1.2.1&auto=format&f"
                   "it=crop&w=800&q=60",
        "price": 49000,
        "stars": "3",
        "country": "Куба",
        "nights": 8,
        "date": "26 января",
    },
    14: {
        "title": "History Hotel & Spa",
        "description": "Крыша высокая, треугольная, многослойная, покрыта пшеничной соломой. Две боль"
                       "шие трубы находятся по обе стороны от дома. Многие меньшие окна пропускают мно"
                       "го света в комнаты под крышей.Сам дом окружен асфальтированной землей, с место"
                       "м для еды и отдыха на открытом воздухе и различными горшечными растениями.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1509600110300-21b9d5fedeb7?ixlib=rb-1.2.1&ixid=ey"
                   "JhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 91000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 9,
        "date": "3 февраля",
    },
    15: {
        "title": "Riverside Lagoon Hotel & Spa",
        "description": "Здание имеет форму круга. Дом частично окружен деревянными нависающими панел"
                       "ями с двух сторон. Второй этаж меньше первого, что позволило создать нескольк"
                       "о балконов по бокам дома. Этот этаж следует тому же стилю, что и этаж ниже.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 82000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "5 февраля",
    },
    16: {
        "title": "History Hotel & Spa",
        "description": "Крыша высокая, треугольная, многослойная, покрыта пшеничной соломой. Две бол"
                       "ьшие трубы находятся по обе стороны от дома. Многие меньшие окна пропускают м"
                       "ного света в комнаты под крышей.Сам дом окружен асфальтированной землей, с мес"
                       "том для еды и отдыха на открытом воздухе и различными горшечными растениями.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1564056095795-4d63b6463dbf?ixlib=rb-1.2.1&ixid=ey"
                   "JhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 74000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 12,
        "date": "24 января",
    }

}

departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
              "kazan": "Из Казани"}


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы нет.')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


def main_view(request):
    return render(request, "tours/index.html")


def departure_view(request, departure):
    tours_number = 0
    price = []
    nights = []
    tour_id = []
    min_price, max_price, min_nights, max_nights = 0, 0, 0, 0
    for i in range(1, len(tours)):
        if tours[i]['departure'] == departure:
            tours_number += 1
            price.append(tours[i]['price'])
            nights.append(tours[i]['nights'])
            tour_id.append(i)
            min_price = min(price)
            max_price = max(price)
            min_nights = min(nights)
            max_nights = max(nights)
    while len(tour_id) != 6:
        tour_id.append(0)
    context = {'departure': departures[departure],
               'tours_number': tours_number,
               'min_price': min_price,
               'max_price': max_price,
               'min_nights': min_nights,
               'max_nights': max_nights,

               'description1': tours[tour_id[0]]['description'],
               'title1': tours[tour_id[0]]['title'],
               'picture1': tours[tour_id[0]]['picture'],
               'description2': tours[tour_id[1]]['description'],
               'title2': tours[tour_id[1]]['title'],
               'picture2': tours[tour_id[1]]['picture'],
               'description3': tours[tour_id[2]]['description'],
               'title3': tours[tour_id[2]]['title'],
               'picture3': tours[tour_id[2]]['picture'],
               'description4': tours[tour_id[3]]['description'],
               'title4': tours[tour_id[3]]['title'],
               'picture4': tours[tour_id[3]]['picture'],
               'description5': tours[tour_id[4]]['description'],
               'title5': tours[tour_id[4]]['title'],
               'picture5': tours[tour_id[4]]['picture'],
               'description6': tours[tour_id[5]]['description'],
               'title6': tours[tour_id[5]]['title'],
               'picture6': tours[tour_id[5]]['picture'],
               }

    return render(request, 'tours/departure.html', context=context)


def tour_view(request, id):
    context = {'Departure': departures[tours[id]['departure']],
               'Stars': '★' * int(tours[id]['stars'])
               }
    context.update(tours[id])
    return render(request, "tours/tour.html", context=context)

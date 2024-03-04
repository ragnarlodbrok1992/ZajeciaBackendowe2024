STATIC_STRINGS = {'hello_message': "Witaj na stronie aplikacji Holly Movies!",
                  'date_created': "This site was created 3/04/2024."}


def welcome_message(request):
    return STATIC_STRINGS


def autorzy(request):
    autors = ['Antoni Nieprzegoni',
              'Seweryn Kwaśniewski']
    return {'autors': autors}

from plexapi.myplex import MyPlexAccount

from settings import PLEX_USER, PLEX_PASS

account = MyPlexAccount(PLEX_USER, PLEX_PASS)
plex = account.resource('pi').connect()

def currently_watching():
    on_deck = plex.library.onDeck()
    try:
        current = on_deck[0]
    except IndexError:
        current = None
    return current

def unwatched():
    movies = plex.library.section('Movies')
    return movies.search(unwatched=True)[0:3]

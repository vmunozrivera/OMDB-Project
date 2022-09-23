
# Python
import logging
logger = logging.getLogger(__name__)

# Django
from django.core.management.base import BaseCommand

# Models
from movies.models import Movie
from movies.omdb_integration import fill_movie_details


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def add_arguments(self, parser):
        parser.add_argument("imdb_id", nargs=1)

    def handle(self, *args, **options):
        try:
            movie = Movie.objects.get(imdb_id=options["imdb_id"][0])
            print("Hola")
        except Movie.DoesNotExist:
            logger.error("Movie with IMDB ID '%s' was not found", options["imdb_id"][0])
            return

        fill_movie_details(movie)

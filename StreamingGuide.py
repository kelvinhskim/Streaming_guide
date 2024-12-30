# Author: Hyun Seok Kim
# GitHub username: kelvinhskim
# Date: 3/13/2024
# Description: The 'Movie' class represents a movie entity with attributes
# such as title, genre, director, and year of release.
# The 'StreamingService' class represents a streaming service platform with
# a name and a catalog of movies available for streaming.
# The 'StreamingGuide' class represents a guide that contains a list of
# various streaming services.
# These classes work together to manage and organize
# streaming services and their respective movie catalogs, providing users with
# a streamlined way to discover where their desired movies are available for streaming.
#

class Movie:
    """
    A class representing a Movie with title, genre, director, and year.
    """

    def __init__(self, title, genre, director, year):
        """
        Initialize a Movie object with title, genre, director, and year.
        Parameters
            title (str): The title of the movie.
            genre (str): The genre of the movie.
            director (str): The director of the movie.
            year (int): The year the movie was released.
        """
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """
        Get the title of the movie.
        Returns: Title -- The title of the movie.
        """
        return self._title

    def get_genre(self):
        """
        Get the genre of the movie.
        Returns: Genre -- The genre of the movie.
        """
        return self._genre

    def get_director(self):
        """
        Get the director of the movie.
        Returns: Director -- The director of the movie.
        """
        return self._director

    def get_year(self):
        """
        Get the year of the movie was released.
        Returns: Year -- The year of the movie was released.
        """
        return self._year


class StreamingService:
    """
    A class representing a streaming service with a name and a catalog of movies.
    """
    def __init__(self, name):
        """
        Initialize a StreamingService object
        Parameter
            name (str): The name of the streaming service.
        """
        self._name = name
        self._catalog = {}

    def get_name(self):
        """
        Get the name of the streaming service.
        Returns: Name -- The name of the streaming service.
        """
        return self._name

    def get_catalog(self):
        """
        Get the catalog of movies available on the streaming service.
        Returns: Catalog -- The catalog of the movies available on the streaming service.
        """
        return self._catalog

    def add_movie(self, movie):
        """
        Add a movie to the catalog of the streaming service.
        Parameters:
            movie (Movie): The Movie object to be added to the catalog.
        """
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """
        Delete a movie from the catalog of the streaming service.
        Parameter:
            title (str): The title of the movie to be deleted.
        """
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    """
    Represents a streaming guide containing a list of streaming services.
    """

    def __init__(self):
        """
        Initialize a StreamingGuide object with an empty list of streaming services.
        """
        self._streaming_services = []

    def add_streaming_service(self, service):
        """
        Add a streaming service to the streaming guide.
        Parameter:
            service (StreamingService): The StreamingService object to be added.
        """
        self._streaming_services.append(service)

    def delete_streaming_service(self, name):
        """
        Delete a streaming service from the streaming guide.
        Parameter:
            name (str): The name of the streaming service to be deleted.
        """
        for service in self._streaming_services:
            if service.get_name() == name:
                self._streaming_services.remove(service)

    def who_streams_this_movie(self, title):
        """
        Determine which streaming services offer a specific movie.
        Parameter:
            title (str): The title of the movie to search for.
        Returns:
            dict or None: A dictionary containing information about the movie and the streaming services
            offering it, or None if the movie is not available on any streaming service.
        """
        result = {'title': title, 'services': []}
        for service in self._streaming_services:
            catalog = service.get_catalog()
            if title in catalog:
                result['services'].append(service.get_name())
                result['year'] = catalog[title].get_year()
        if result['services']:
            return result
        else:
            return None

# Example usage:
# movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
# movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
# movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
# movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)
#
# stream_serv_1 = StreamingService('Netflick')
# stream_serv_1.add_movie(movie_2)
#
# stream_serv_2 = StreamingService('Hula')
# stream_serv_2.add_movie(movie_1)
# stream_serv_2.add_movie(movie_4)
# stream_serv_2.delete_movie('The Seventh Seal')
# stream_serv_2.add_movie(movie_2)
#
# stream_serv_3 = StreamingService('Dizzy+')
# stream_serv_3.add_movie(movie_4)
# stream_serv_3.add_movie(movie_3)
# stream_serv_3.add_movie(movie_1)
# #stream_serv_3.get_catalog()
# stream_guide = StreamingGuide()
# stream_guide.add_streaming_service(stream_serv_1)
# stream_guide.add_streaming_service(stream_serv_2)
# stream_guide.add_streaming_service(stream_serv_3)
# stream_guide.delete_streaming_service('Hula')
# search_results = stream_guide.who_streams_this_movie('Little Women')
# print(search_results)
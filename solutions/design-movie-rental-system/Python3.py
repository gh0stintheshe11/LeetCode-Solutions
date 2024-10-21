from sortedcontainers import SortedList
from typing import List, Tuple

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented_movies = {}
        self.rented_movies = SortedList()
        self.movie_price_map = {}

        for shop, movie, price in entries:
            if movie not in self.unrented_movies:
                self.unrented_movies[movie] = SortedList()
            self.unrented_movies[movie].add((price, shop))
            self.movie_price_map[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented_movies:
            return []
        return [shop for _, shop in self.unrented_movies[movie][:5]]
    
    def rent(self, shop: int, movie: int) -> None:
        price = self.movie_price_map[(shop, movie)]
        self.unrented_movies[movie].remove((price, shop))
        self.rented_movies.add((price, shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        price = self.movie_price_map[(shop, movie)]
        self.rented_movies.remove((price, shop, movie))
        self.unrented_movies[movie].add((price, shop))
    
    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented_movies[:5]]
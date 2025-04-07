import uuid

from src.config.errors import ResourceNotFound

from src.schemas.movies_schema import MovieCreate, MovieUpdate, Movie
from src.interfaces.repositories.movies_repository_interface import IMoviesRepository
from src.interfaces.usecases.movies_usecase_interface import MoviesUseCaseInterface


class MoviesUseCase(MoviesUseCaseInterface):
    def __init__(self, movie_repo: IMoviesRepository) -> None:
        self._movie_repo = movie_repo

    def get_by_id(self, movie_id: int):
        result = self._movie_repo.get_by_id(movie_id)
        if not result:
            raise ResourceNotFound
        else:
            return result


    def get_all(self):
        return self._movie_repo.get_all()

    def create(self, input_dto: MovieCreate) -> Movie:
        customer = Customer.create(
            input_dto.cpf,
            input_dto.first_name,
            input_dto.last_name,
            input_dto.email,
            input_dto.phone,
        )
        new_customer = self._movie_repo.create(customer)
        return new_customer

    def update(self, customer_id: uuid.UUID, input_dto: MovieUpdate) -> Movie:
        customer = self._movie_repo.get_by_id(customer_id)

        if input_dto.first_name:
            customer.change_first_name(input_dto.first_name)
        if input_dto.last_name:
            customer.change_last_name(input_dto.last_name)
        if input_dto.email:
            customer.change_email(input_dto.email)
        if input_dto.phone:
            customer.change_phone(input_dto.phone)

        updated_customer = self._movie_repo.update(customer_id, customer)
        return updated_customer

    def remove(self, customer_id: uuid.UUID) -> None:
        self._movie_repo.remove(customer_id)

    def anonymize_data(self, customer_id: uuid.UUID) -> Movie:
        customer = self._movie_repo.get_by_id(customer_id)
        customer.anonymize_sensitive_data()

        updated_customer = self._movie_repo.update(customer_id, customer)
        return updated_customer

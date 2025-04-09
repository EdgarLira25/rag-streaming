from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
HASH = TypeVar("HASH")
ID = TypeVar("ID")


class AuthAbstractRepository(ABC, Generic[T, ID, HASH]):
    @abstractmethod
    def get_secret_hash(self, email: ID) -> HASH:
        """Retorna o hash da senha secreta do usuário a partir do email."""

    @abstractmethod
    def get_user_info(self, email: ID) -> T:
        """Retorna informações do usuário (email, nome, tipo, data de criação)."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

HASH = TypeVar("HASH")
NAME = TypeVar("NAME")
ID = TypeVar("ID")


class UserAbstractRepository(ABC, Generic[HASH, NAME, ID]):

    @abstractmethod
    def create_user(self, email: ID, secret_hash: HASH, name: NAME) -> bool:
        """Cria Usuário"""

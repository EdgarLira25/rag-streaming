import base64
from pathlib import Path
from typing import Optional, Self

from src.settings import STORAGE_LOCATION


class NoContainerSelected(Exception): ...


class StorageService:
    def __init__(self, container: Optional[str] = None) -> None:
        self.__base_path = STORAGE_LOCATION
        self.__selected_container = container

    def _delete_empty_dirs(self, dir_path: Path) -> None:
        current_path = dir_path
        while current_path != self._base_path:
            if any(current_path.iterdir()):
                break
            current_path.rmdir()
            current_path = current_path.parent

    @property
    def _base_path(self) -> Path:
        if not self.__selected_container:
            raise NoContainerSelected("Nenhum Container Selecionado")
        return Path(self.__base_path + self.__selected_container)

    def _get_path(self, filename_or_prefix=""):
        return Path(self._base_path.as_posix() + filename_or_prefix)

    def create_container(self, container: str) -> None:
        Path(self.__base_path + container).mkdir(exist_ok=True)

    def get_container(self, container: str) -> Self:
        self.__selected_container = container
        return self

    def create_blob(self, filename: str, file: bytes) -> str:
        path = self._get_path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(file)
        return filename

    def get_blob_base64(self, filename: str) -> str:
        blob = self._get_path(filename)
        if blob.is_file():
            return base64.b64encode(blob.read_bytes()).decode("utf-8")
        return ""

    def get_blob(self, filename: str) -> bytes:
        blob = self._get_path(filename)
        if blob.is_file():
            return blob.read_bytes()
        return bytes()

    def list_blobs(self, prefix="") -> list[str]:
        return [
            path.as_posix().replace(self._base_path.as_posix(), "", 1)
            for path in Path(self._base_path.as_posix() + prefix).rglob("*")
            if path.is_file()
        ]

    def delete_blob(self, filename: str) -> None:
        blob = Path(self._base_path.as_posix() + filename)
        if blob.is_file():
            blob.unlink()
            self._delete_empty_dirs(blob.parent)

    def delete_many_blobs(self, prefix="") -> None:
        for blob in Path(self._base_path.as_posix() + prefix).rglob("*"):
            if blob.is_file():
                blob.unlink()
                self._delete_empty_dirs(blob.parent)

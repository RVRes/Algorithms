from abc import ABC, abstractmethod


class CompressionStrategy(ABC):

    @staticmethod
    def read_unpacked_file(file_path: str) -> bytes:
        with open(file_path, mode='rb') as file:
            unpacked_file = file.read()
        return unpacked_file

    @staticmethod
    def write_unpacked_file(file_path: str, unpacked_file: bytes) -> None:
        with open(file_path, mode='wb') as file:
            file.write(unpacked_file)

    @abstractmethod
    def pack(self, unpacked_file: bytes):
        raise NotImplementedError('Subclasses must implement pack method.')

    @abstractmethod
    def unpack(self, packed_file: bytes):
        raise NotImplementedError('Subclasses must implement unpack method.')

    @abstractmethod
    def read_packed_file(self, file_path: str) -> any:
        raise NotImplementedError(
            'Subclasses must implement read_packed_file method.')

    @abstractmethod
    def write_packed_file(self, file_path: str, packed_file: any) -> None:
        raise NotImplementedError(
            'Subclasses must implement write_packed_file method.')

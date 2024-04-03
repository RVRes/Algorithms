from CompressionStrategy import CompressionStrategy


class CopyCompressionStrategy(CompressionStrategy):
    def pack(self, unpacked_file: bytes):
        return unpacked_file

    def unpack(self, packed_file: bytes):
        return packed_file

    def read_packed_file(self, file_path: str) -> bytes:
        return super().read_unpacked_file(file_path)

    def write_packed_file(self, file_path: str, packed_file: bytes) -> None:
        return super().write_unpacked_file(file_path, packed_file)

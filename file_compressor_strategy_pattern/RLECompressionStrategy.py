from CompressionStrategy import CompressionStrategy


class RLECompressionStrategy(CompressionStrategy):
    def pack(self, unpacked_file: bytes):
        """Compress file using RLE (run-length encoding) algorythm."""
        output_file = bytearray()
        if not unpacked_file:
            return output_file
        repeats = 1
        file_iterator = iter(unpacked_file)
        byte = next(file_iterator)
        for byte_next in file_iterator:
            while byte == byte_next and repeats < 254:
                repeats += 1
                try:
                    byte_next = next(file_iterator)
                except StopIteration:
                    byte_next = None
                    break
            output_file.extend(
                repeats.to_bytes(1, 'big') + byte.to_bytes(1, 'big'))
            byte = byte_next
            repeats = 1
        if byte is not None:
            output_file.extend(
                int(1).to_bytes(1, 'big') + byte.to_bytes(1, 'big'))

        return output_file

    def unpack(self, packed_file: bytes):
        """Decompress file using RLE (run-length encoding) algorythm."""
        file_iterator = iter(packed_file)
        output_file = bytearray()
        for repeats in file_iterator:
            byte = next(file_iterator).to_bytes(1, 'big')
            output_file.extend(byte * repeats)
        return output_file

    def read_packed_file(self, file_path: str) -> bytes:
        return super().read_unpacked_file(file_path)

    def write_packed_file(self, file_path: str, packed_file: bytes) -> None:
        return super().write_unpacked_file(file_path, packed_file)

from CompressionStrategy import CompressionStrategy


class RLE2CompressionStrategy(CompressionStrategy):

    def pack(self, unpacked_file: bytes):
        """Compress file using RLE2 (run-length encoding) algorythm."""
        file_len = len(unpacked_file) - 1
        output_file = bytearray()
        i = 0
        while i <= file_len:
            if i < file_len and unpacked_file[i] != unpacked_file[i + 1]:
                counter = 0
                unique_bytes = bytearray()
                while (((i < file_len
                         and unpacked_file[i] != unpacked_file[i + 1])
                        or i == file_len) and counter < 127):
                    counter += 1
                    unique_bytes.extend(unpacked_file[i].to_bytes(1, 'big'))
                    i += 1
                output_file.extend(counter.to_bytes(1, 'big'))
                output_file.extend(unique_bytes)
            elif i < file_len and unpacked_file[i] == unpacked_file[i + 1]:
                counter = 128
                while (i < file_len and counter < 254
                       and unpacked_file[i] == unpacked_file[i + 1]):
                    counter += 1
                    i += 1
                output_file.extend(counter.to_bytes(1, 'big'))
                output_file.extend(unpacked_file[i - 1].to_bytes(1, 'big'))
                i += 1
            elif i == file_len:
                counter = 1
                output_file.extend(counter.to_bytes(1, 'big'))
                output_file.extend(unpacked_file[i].to_bytes(1, 'big'))
                i += 1
        return output_file

    def unpack(self, packed_file: bytes):
        """Decompress file using RLE2 (run-length encoding) algorythm."""
        file_len = len(packed_file) - 1
        output_file = bytearray()
        i = 0
        while i < file_len:
            counter = packed_file[i]
            i += 1
            if counter < 128:
                for j in range(i, i + counter):
                    output_file.extend(packed_file[j].to_bytes(1, 'big'))
                i = i + counter
            else:
                counter = counter - 127
                byte = packed_file[i].to_bytes(1, 'big')
                output_file.extend(byte * counter)
                i += 1
        return output_file

    def read_packed_file(self, file_path: str) -> bytes:
        return super().read_unpacked_file(file_path)

    def write_packed_file(self, file_path: str, packed_file: bytes) -> None:
        return super().write_unpacked_file(file_path, packed_file)

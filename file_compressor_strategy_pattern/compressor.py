import os
import sys
import time
from enum import Enum, auto
from pathlib import Path
from CopyCompressionStrategy import CopyCompressionStrategy
from RLECompressionStrategy import RLECompressionStrategy
from RLE2CompressionStrategy import RLE2CompressionStrategy

_DEFAULT_FILE_TO_ARCHIVE = r'files/example_with_repeated_letters.txt'
# _DEFAULT_FILE_TO_ARCHIVE = r'files/Orlovskiy_Gay_Yuliy_[Richard_Dlinnyie_Ruki#1]_Richard_Dlinnyie_Ruki.txt'
# _DEFAULT_FILE_TO_ARCHIVE = r'files/Orlovskiy_Gay_Yuliy_[Richard_Dlinnyie_Ruki#1]_Richard_Dlinnyie_Ruki.arc'
_DEFAULT_COMMAND = '-pack'
_DEFAULT_COMPRESSION_METHOD = '-rle'


class Compressor:
    """Compress or decompress one file with selected compression method."""
    _ARCHIVE_FILE_EXTENSION = '.arc'

    class CompressorStrategies(Enum):
        """Returns available compression strategies."""
        COPY = CopyCompressionStrategy()
        RLE = RLECompressionStrategy()
        RLE2 = RLE2CompressionStrategy()

        @classmethod
        def from_key(cls, key: str):
            """Returns compressor strategy enum by command line argument."""
            match key:
                case '-copy':
                    return cls.COPY
                case '-rle':
                    return cls.RLE
                case '-rle2':
                    return cls.RLE2
                case _:
                    raise ValueError('Unsupported compression method.')

    class CompressorCommands(Enum):
        """Returns available compressor commands."""
        PACK = auto()
        UNPACK = auto()

        @classmethod
        def from_key(cls, key: str):
            """Returns compressor command enum by command line argument."""
            match key:
                case '-pack':
                    return cls.PACK
                case '-unpack':
                    return cls.UNPACK
                case _:
                    raise ValueError(
                        'Unsupported compressor command.')

    def __init__(self, command: str, method: str,
                 source_file_path: str) -> None:
        self._command = self.CompressorCommands.from_key(command)
        self._source_file_path = source_file_path
        self._destination_file_path = self._get_destination_file_path(
            self._source_file_path, self._command, self._ARCHIVE_FILE_EXTENSION
        )
        self._compression = self.CompressorStrategies.from_key(method).value
        self._pack = self._compression.pack
        self._unpack = self._compression.unpack
        self._read_packed_file = self._compression.read_packed_file
        self._read_unpacked_file = self._compression.read_unpacked_file
        self._write_packed_file = self._compression.write_packed_file
        self._write_unpacked_file = self._compression.write_unpacked_file

    def _get_destination_file_path(
            self, _source_file_path, _command, _file_extension
    ):
        """Add suffix for packed file. Remove suffix for unpacked."""
        path = Path(_source_file_path)
        match _command:
            case self.CompressorCommands.PACK:
                return str(path.with_suffix(path.suffix + _file_extension))
            case self.CompressorCommands.UNPACK:
                return str(path.with_suffix(''))

    @staticmethod
    def _get_compression_results(source_path, destination_path,
                                 execution_time):
        source_file_size = os.path.getsize(source_path) / 1024 / 1024
        destination_file_size = os.path.getsize(destination_path) / 1024 / 1024
        if destination_file_size:
            ratio = source_file_size / destination_file_size
        else:
            ratio = 0
        return (
            f'input file size: {source_file_size:.4f}Mb, '
            f'output file size: {destination_file_size:.4f}Mb, '
            f'ratio: {ratio:.2f}, '
            f'Execution time: {execution_time:.2f} seconds.')

    def _pack_and_save(self, source_path, destination_path):
        unpacked_file = self._read_unpacked_file(source_path)
        packed_file = self._pack(unpacked_file)
        self._write_packed_file(destination_path, packed_file)

    def _unpack_and_save(self, source_path, destination_path):
        packed_file = self._read_packed_file(source_path)
        unpacked_file = self._unpack(packed_file)
        self._write_unpacked_file(destination_path, unpacked_file)

    def run(self):
        start_time = time.time()
        match self._command:
            case self.CompressorCommands.PACK:
                self._pack_and_save(self._source_file_path,
                                    self._destination_file_path)
            case self.CompressorCommands.UNPACK:
                self._unpack_and_save(self._source_file_path,
                                      self._destination_file_path)
        execution_time = time.time() - start_time
        return self._get_compression_results(self._source_file_path,
                                             self._destination_file_path,
                                             execution_time)


if __name__ == '__main__':
    # python version >= 3.10  required due to:
    # dict implementation changed to work preserves the insertion order in 3.7
    # match operator is introduced in 3.10
    python_version = sys.version_info
    if python_version.major < 3 or python_version.minor < 10:
        raise RuntimeError('Archiver requires Python 3.10 or higher version.')

    arguments = sys.argv[1:]
    if len(arguments) == 3:
        command_key = arguments[0]
        method_key = arguments[1]
        source_file_path_key = arguments[2]
    # TODO delete this
    else:
        command_key = _DEFAULT_COMMAND
        method_key = _DEFAULT_COMPRESSION_METHOD
        source_file_path_key = _DEFAULT_FILE_TO_ARCHIVE

    if not os.path.exists(source_file_path_key):
        raise FileNotFoundError(source_file_path_key)

    compressor = Compressor(command_key, method_key, source_file_path_key)
    result = compressor.run()
    print(result)

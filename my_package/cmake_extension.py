import os
from pathlib import Path
import shutil

import setuptools
import setuptools.command.build_ext


class CMakeExtension(setuptools.Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])


class CMakeBuildExt(setuptools.command.build_ext.build_ext):
    def __init__(self, *args, source_directory, **kwargs):
        super().__init__(*args, **kwargs)
        self.__source_directory = Path(source_directory)

    def run(self):
        self.__build_cmake()

        for ext in self.extensions:
            if isinstance(ext, CMakeExtension):
                self.__copy_ext(ext)

        super().run()

    def __copy_ext(self, ext):
        print(f'Copying extension {ext.name}...')
        target_directory = Path(self.build_lib)
        target_path = Path(self.get_ext_fullpath(ext.name))
        relative_path = target_path.relative_to(target_directory)

        build_directory = Path(self.build_temp).absolute()
        source_path = build_directory / 'output' / relative_path

        print('    relative_path =', relative_path)
        print('    source_path =', source_path)
        print('    target_path =', target_path)

        if not source_path.exists():
            raise Exception(f'Failed to build file: {source_path}')

        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target_path)


    def __build_cmake(self):
        print('Builing CMake project...')
        package_directory = Path().absolute()
        source_directory = package_directory / self.__source_directory
        build_directory = Path(self.build_temp).absolute()
        conan_directory = build_directory / '.conan'

        print('    package_directory =', package_directory)
        print('    source_directory =', source_directory)
        print('    build_directory =', build_directory)

        config = 'Debug' if self.debug else 'Release'

        # TODO: support self.dry_run
    
        print('  Conan install...')
        conan_directory.mkdir(parents=True, exist_ok=True)
        os.chdir(conan_directory)
        self.__spawn('conan', 'install', source_directory)

        print('  CMake configure...')
        build_directory.mkdir(parents=True, exist_ok=True)
        os.chdir(build_directory)
        self.__spawn(
            'cmake',
            source_directory,
            f'-DCMAKE_MODULE_PATH:PATH={str(conan_directory)}',
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY:PATH={str(build_directory)}/output',
        )

        print('  CMake build...')
        self.__spawn('cmake', 
            '--build', build_directory,
            '--config', config,
            '--',
            '-j8',
        )

        os.chdir(package_directory)
        print('  Done.')

    def __spawn(self, *args):
        self.spawn(map(str, args))


def CMakeBuild(source_directory):
    def build_ext(*args, **kwargs):
        return CMakeBuildExt(*args, source_directory=source_directory, **kwargs)
    return build_ext

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import sys
import os
import subprocess
import setuptools


class CMakeExtension(Extension):
    def __init__(self, name, source_dir='base'):  # Point to 'base'
        super().__init__(name, sources=[])
        self.source_dir = os.path.abspath(source_dir)
        
class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)

    def build_cmake(self, ext):
        extdir = self.get_ext_fullpath(ext.name)
        cfg = 'Release'

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={os.path.abspath(os.path.dirname(extdir))}",
            f"-DCMAKE_BUILD_TYPE={cfg}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
        ]

        build_args = ['--config', cfg]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(
            ['cmake', ext.sourcedir] + cmake_args,
            cwd=self.build_temp
        )
        subprocess.check_call(
            ['cmake', '--build', '.'] + build_args,
            cwd=self.build_temp
        )

setup(
    name='backend_module',
    version='0.1.0',
    author='Kumara Krishnappa',
    author_email='you@example.com',
    description='Python bindings and FastAPI service for backend system',
    long_description='Multithreaded backend with C++ producer-consumer and Prometheus integration.',
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'prometheus_client',
    ],
    ext_modules=[CMakeExtension('backend', source_dir='base')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)

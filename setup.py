from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import sys
import os
import subprocess
import setuptools


class CMakeExtension(Extension):
    def __init__(self, name):  # Point to 'base'
        super().__init__(name, sources=[])
        self.source_dir = os.path.abspath(".")
        
class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)

    def build_cmake(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cfg = 'Release'

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DCMAKE_BUILD_TYPE={cfg}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
        ]

        build_args = ['--target', 'backend_module']

        if os.path.exists(os.path.join(self.build_temp, 'CMakeLists.txt')):
            os.remove(os.path.join(self.build_temp, 'CMakeLists.txt'))
            os.makedirs(self.builf_temp, exist_ok=True)

        subprocess.check_call(
            ['cmake', ext.source_dir] + cmake_args,
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
    ext_modules=[CMakeExtension('backend_module')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)

from os import path
from setuptools import setup, find_packages
from setuptools import Extension

try:
    from Cython.Build import cythonize

    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

source_files = (
    ["src/littlefs/lfs.pyx"]
    if USE_CYTHON
    else ["littlefs/lfs.c", "littlefs/lfs_util.c"]
)


# Extension definition
EXTENSIONS = [
    Extension(
        "littlefs.lfs",
        source_files,
        include_dirs=["littlefs"],
        define_macros=[
            ("LFS_NO_DEBUG", "1"),
            ("LFS_NO_WARN", "1"),
            ("LFS_NO_ERROR", "1"),
            # ('LFS_YES_TRACE', '1')
        ],
        extra_compile_args=["-std=c99"],
    )
]

if USE_CYTHON:
    EXTENSIONS = cythonize(
        EXTENSIONS,
        language_level=3,
        annotate=False,
        compiler_directives={"embedsignature": True},
    )

setup_requires = ["setuptools_scm>=3.3.3"]

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.rst"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="littlefs-python",
    url="https://github.com/jrast/littlefs-python",
    author="Jürg Rast",
    author_email="juergr@gmail.com",
    description="A python wrapper for littlefs",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    use_scm_version=True,
    setup_requires=setup_requires,
    packages=find_packages("src"),
    package_data={"*": ["py.typed", "*.pyi"]},
    package_dir={"": "src"},
    zip_safe=False,
    ext_modules=EXTENSIONS,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Filesystems",
    ],
)

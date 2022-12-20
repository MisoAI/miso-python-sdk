from setuptools import setup, find_packages
import pathlib

from miso.version import SDK_VERSION

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="miso-sdk",
    version=SDK_VERSION,
    license='MIT',

    description="Enhance your site with high conversion magic with Miso's power.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/MisoAI/miso-python-sdk",

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={"": "src"},

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(),

    python_requires=">=3.7, <4",
    install_requires=["requests"],
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #     "sample": ["package_data.dat"],
    # },

    project_urls={
        "Miso": "https://askmiso.com/",
        "Miso Document": "https://docs.askmiso.com/",
        "Miso API Document": "https://api.askmiso.com/",
    },
)

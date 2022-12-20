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
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],

    packages=find_packages(),

    python_requires=">=3.7, <4",
    install_requires=["requests"],

    project_urls={
        "Miso": "https://askmiso.com/",
        "Miso Document": "https://docs.askmiso.com/",
        "Miso API Document": "https://api.askmiso.com/",
    },
)

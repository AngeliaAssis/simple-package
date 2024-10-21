from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()


setup(
    name="package_banking_operations",
    version="0.0.1",
    author="Angelia Assis",
    description="Pacote de processamento de operações bancárias básicas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AngeliaAssis/simple-package",
    packages=find_packages(),
    python_requires='>=3.8',
)
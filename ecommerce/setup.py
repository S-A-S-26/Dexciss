from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecommerce/__init__.py
from ecommerce import __version__ as version

setup(
	name="ecommerce",
	version=version,
	description="Ecommerce Jollys",
	author="Dexciss",
	author_email="ssutar@dexciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

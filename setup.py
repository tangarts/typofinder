import setuptools

with open("README.md") as file:
    long_description = file.read()

with open("requirements.txt") as file:
    install_requires = [req.strip() for req in file.readlines()]

setuptools.setup(
    name="typofinder",
    version="0.0.1",
    author="Min ho Kim",
    author_email="minho42@gmail.com",
    description="Find typos from GitHub repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minho42/typofinder",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={"console_scripts": ["tf=typofinder.__main__:main"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Text Processing",
    ],
)


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrape_aruodas",
    version="0.0.1",
    author="valdas-v1",
    description="Collect data from scraping Aruodas.lt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valdas-v1/scrape_aruodas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4', 
        'pandas', 
        'regex', 
        'requests'
    ],
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GetStockTickers",
    version="1.0.3",
    author="Estephe Corlin",
    author_email="estephecorlin@gmail.com",
    description="Scrape Nasdaq's Stock Screener for a daily list of tickers for the NYSE, NASDAQ amd AMEX exchanges.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/estepehcorlin/GetStockTickers",
    packages=['GetStockTickers'],
    install_requires=['pandas', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

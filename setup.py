from setuptools import setup, find_packages

setup(
    name = "pinterest-scraper",
    version = "0.1",
    packages = find_packages(),
    install_requires = [
        "selenium",
        "webdriver-manager",
        "requests"
    ],
    entry_points={
    "console_scripts": [
        "scrape_board=package.main:main",
        ],
    },

)
import setuptools
with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME="Text-Summarizer"
AUTHOR_USERNAME='govardhan-06'
SRC_REPO="Text-Summarizer"
AUTHOR_EMAIL="govardhanar06@gmail.com"

setuptools.setup(
    name="Text-Summarizer",
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Python app for text summarization using NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/govardhan-06/Text-Summarizer',
    project_urls={
        "Bug Tracker": "https://github.com/govardhan-06/Text-Summarizer/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
)
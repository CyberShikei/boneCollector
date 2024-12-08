from setuptools import setup, find_packages

setup(
    name="boneCollector",
    version="1.0.0",
    author="Jaco Ferreira",
    description="A Python package for ETL basic pipeline tasks",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "beautifulsoup4>=4.11.0",
        "pandas>=1.4.0",
        "sqlalchemy>=2.0.0",
        "psycopg2-binary>=2.9.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

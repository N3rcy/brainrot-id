from setuptools import setup, find_packages

setup(
    name="brainrot-id",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'brainrot-id = brainrot_id.cli:main'
        ]
    },
    install_requires=[
        'emoji>=2.0.0',
        'cryptography>=3.4'
    ],
    package_data={
        'brainrot_id': ['data/*.json']
    },
    author="Nercy",
    author_email="nercysvoboda@gmail.com",
    description="Brain-melting ID generator for post-modern applications",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('REQUIREMENTS.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="pi-smart-camper", # Replace with your own username
    version="0.0.1",
    author="Carter Baxter",
    author_email="mail.baxter@gmail.com",
    description="Source code for a 'smart' Raspberry Pi-powered travel trailer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tBaxter/pi-smart-camper",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
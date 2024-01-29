import pathlib
import setuptools

setuptools.setup(
    name="wynn-api",
    version="3.2.1",
    description="A simple Python API Wrapper for the Wynncraft API",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pix3lRift/wynn-api/tree/py-v3#readme",
    author="PixelRift <amogus.my.to>",
    license="Apache-2.0",
    project_urls={
        "Source": "https://github.com/Pix3lRift/wynn-api/tree/py-v3",
        "Wynncraft Developers dc server": "https://discord.gg/CtMKp3hG66",
        "Node.js version": "https://www.npmjs.com/package/wynn-api-node"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    python_requires=">=3.5",
    install_requires=[],
    packages=setuptools.find_packages(),
    include_package_data=True
)
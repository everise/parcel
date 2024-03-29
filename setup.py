import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='parcel',  
    version='0.1',
    scripts=['parcel'] ,
    author="Everise",
    description="A Docker and AWS utility package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/everise/parcel",
    packages=setuptools.find_packages(),
    py_modules=['ecs_helper', 'docker_helper', 'slack_api'],
    install_requires=[
        'requests', 'click', 'configparser'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
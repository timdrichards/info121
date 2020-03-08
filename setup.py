import setuptools
long_description = 'My first pip library'
setuptools.setup(
    name='testpackages',
    url="https://github.com/timdrichards/info121",
    author="Tim Richards",
    author_email="richards@cs.umass.edu",
    packages=["info121"],
    version='0.1',
    license='MIT',
    description="Test Package",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    #packages=setuptools.find_packages(),
 )

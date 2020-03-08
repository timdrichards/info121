import setuptools
long_description = 'My first pip library'
setuptools.setup(
     name='testpackages',  
     version='0.1',
     author="Tim Richards",
     author_email="richards@cs.umass.edu",
     description="Test Package",
     packages=["info121"],
     long_description=long_description,
     # long_description_content_type="text/markdown",
     url="https://github.com/timdrichards/info121",
     packages=setuptools.find_packages(),
 )

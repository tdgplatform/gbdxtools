import sys
from setuptools import setup, find_packages

open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

# with open('README.md', **open_kwds) as f:
#     readme = f.read()

# long_description=readme,
      
setup(name='gbdxtools',
      version='0.1.4',
      description='Parameter enable_acomp of launch_aop_to_s3 set to false by default.',
      classifiers=[],
      keywords='',
      author='Kostas Stamatiou',
      author_email='kostas.stamatiou@digitalglobe.com',
      url='https://github.com/kostasthebarbarian/gbdxtools',
      license='MIT',
      packages=find_packages(exclude=['docs','tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['requests==2.9.1',
                        'boto==2.39.0',
                        'gbdx-auth==0.1.2',
                        'Pillow==3.1.1',
                        'pygeoif==0.6']
      )

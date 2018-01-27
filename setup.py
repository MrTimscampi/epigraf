from distutils.core import setup
import versioneer

setup(
    name='epigraf',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Julien Machiels',
    author_email='iamtimscampi@gmail.com',
    packages=['epigraf'],
    license='LICENSE.txt',
    description='Next-generation file management for data hoarders.',
    long_description=open('README.rst').read(),
    install_requires=[
        'PyQt5',],
)


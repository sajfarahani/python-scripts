from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Sajj Farahani',
    author_email='sajj@email.com',
    packages=find_packages('src'),
    packages_dir={'':'src'},
    install_requires=[]
)
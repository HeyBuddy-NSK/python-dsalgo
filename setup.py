from setuptools import setup, find_packages

# Reading readme file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python_dsalgo',
    version='0.1.0',
    author='Nitin Kendre',
    author_email='kendre.nitin2000@gmail.com',
    description='A Python package for data structures and algorithms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HeyBuddy-NSK/python-dsalgo',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
    
    package_data={
        '': ['README.md', 'LICENSE.md'],  # Include additional files in the package
    },
    
    zip_safe=False,
)

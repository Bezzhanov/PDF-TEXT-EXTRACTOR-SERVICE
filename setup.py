from setuptools import setup, find_packages

setup(
    name='pdf-text-extractor-service',
    version='0.1.1',
    author='Stanislav Bezzhanov',
    author_email='stanislav.bezzhanov@nfp2b.com',
    description='A service to extract text from PDF files',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask',
        'PyPDF2',
        'pdfplumber',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
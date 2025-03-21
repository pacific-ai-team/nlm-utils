from setuptools import setup, find_packages

# Read version from file
try:
    with open("version", "r") as f:
        version = f.read().strip()
except FileNotFoundError:
    version = "0.1.2"  # Default fallback version

setup(
    name='nlm-utils',
    version=version,    
    description='Common utilities used by all nlm-* libraries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nlmatics/nlm-utils',
    author='Ambika Sukla',
    author_email='ambika.sukla@nlmatics.com',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.9.4",
        "dateparser",
        "dnspython==2.1.0",
        "word2number",
        "minio==7.1.0",
        "money==1.3.0",
        "msgpack==1.0.2",
        "nltk==3.9.1",
        "numpy==1.24.4",
        "openai",
        "pymongo==3.11.4",
        "redis==3.5.3",
        "tiktoken",
        "urllib3==1.26.17",
        "xxhash==2.0.2",
        "python-magic==0.4.22",
        "dicttoxml"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only'        
    ],
)
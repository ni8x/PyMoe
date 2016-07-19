from setuptools import setup

setup(
    name='PyMoe',
    version='0.1',
    packages=['Pymoe', 'Pymoe.Hummingbird'],
    url='https://git.vertinext.com/ccubed/PyMoe',
    license='MIT',
    author='Cooper Click',
    author_email='ccubed.techno@gmail.com',
    description="PyMoe is the only lib you'll ever need if you need the animu or mangu on the Python Platform. It supports AniList, VNDB, Hummingbird and AniDB.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'
    ],
    Keywords="Anime Manga LN VN VNDB Anilist Hummingbird AniDB MyAnimeList MAL NovelUpdates Bakatsuki",
    install_requires=['requests', 'bs4', 'lxml']
)
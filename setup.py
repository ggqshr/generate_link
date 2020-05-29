import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

setuptools.setup(
    name="auto_generate_link",
    version="0.0.1",
    author="ggq",
    author_email="ggq18663278150@gmail.com",
    description='一个python脚本，自动在数据盘生成文件夹，然后将其连接到桌面',
    long_description=long_desc,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['generate_link = generate_link.main:main']
    },
    install_requires=[
        'fire',
    ],
)

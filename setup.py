from distutils.core import setup

setup(
    name="X011",
    py_modules=["X011"],
    entry_points={"console_scripts": ["X011=X011:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. X011 rewrite in Python.",
    author="Gokberk Yaltirakli",
    author_email="opensource@gkbrk.com",
    url="https://github.com/Kevinremon/X011",
    keywords=["dos", "http", "X011"],
    license="MIT",
)

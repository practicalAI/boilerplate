from setuptools import setup, find_packages, dist

requirements = [package for package, version in
                [line.split("==") for line in
                 open("requirements.txt").read().split("\n") if line]]

setup(
    name="{{ cookiecutter.package_name }}",
    version="0.0.1",
    description="{{ cookiecutter.project_name }}",
    url="{{ cookiecutter.project_url }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    packages=find_packages(),
    setup_requires=['Flask==1.0.2'],
    install_requires=requirements,
    python_requires=">=3.6",
    test_suite="tests",
)

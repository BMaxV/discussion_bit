import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "disbit",
    version = "0.1",
    author = "Bruno Maximilian Voss",
    author_email = "bruno.m.voss@gmail.com",
    description = ("basic format definition"),
    
    license = "I don't license this. If you have it, delete it.",
    keywords = "discussion",
   
    packages=['discussion_bit'],
)

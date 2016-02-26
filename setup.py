from setuptools import setup

setup(
    name='qualtrics-raven',
    version='0.0.1',
    install_requires=["flask", "freeze", "gunicorn", "pycrypto"],
    url='https://github.com/llewelld/qualtrics-raven',
    license='Artistic 2.0',
    author=['Daniel Chatfield', 'David Llewellyn-Jones'],
    author_email=['chatfielddaniel@gmail.com', 'David.Llewellyn-Jones@cl.cam.ac.uk'],
    description='Raven authentication for access to Qualtrics surveys for the '
                'University of Cambridge',
    packages=['qualtrics-raven'],
    platforms='any'
)


from setuptools import setup, find_packages

setup(name='drf-fcm',
      version='0.1.0',
      description='Firebase Cloud Messaging Server in Django Rest FrameWork',
      packages=find_packages(),
      author='Naveen Subramani',
      author_email='naviensubramani@gmail.com',
      url='https://github.com/naviens/django-fcm',
      keywords=['gcm', 'fcm', 'django-fcm', 'drf-fcm', 'django-gcm'],
      install_requires=[
          'Django>=1.10',
          'djangorestframework>=3.4.7',
      ],
      )

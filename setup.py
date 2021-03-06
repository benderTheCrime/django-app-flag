from distutils.core import setup

setup(name = 'django-app-flag',
      version = '0.9.2',
      author = 'Joe Groseclose',
      author_email = 'joe.groseclose@example.com',
      packages = ['django_app_flag'],
      package_data= {'django_app_flag' : ['templates/*.html']},
      url='http://pypi.python.org/pypi/django_app_flag/',
      license='LICENSE.txt',
      description='Simple flag for your Django webapps',
      long_description=open('README.txt').read(),
      install_requires=["Django >= 1.6.5"],
      )

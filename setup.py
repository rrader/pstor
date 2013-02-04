from distutils.core import setup
 
setup(name = "pstor",
      version = "0.01",
      description = "Encrypted storage manager",
      author = "Roman Rader",
      author_email = "antigluk@gmail.com",
      packages=["pstor","pstor.commands","pstor.helpers","pstor.commands.providers"],
      scripts=['pstor/pstor'],
      install_requires=['sh'],
      )
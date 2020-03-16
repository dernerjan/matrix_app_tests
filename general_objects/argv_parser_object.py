import getopt
import sys


class ArgvParserObject(object):
	""" Reads script parameters and stores it in variables """

	__environment = None
	__web_driver = None

	@classmethod
	def __read_parameters(cls):
		""" Reads script parameters and stores it in variables """
		# Sets default values:
		cls.__environment = 'DEV'
		# cls.__environment = 'PREPROD'
		cls.__web_driver = 'FIREFOX'
		# cls.__web_driver = 'CHROME'

		try:
			# env_val = 'DEV'
			optlist, args = getopt.getopt(sys.argv[1:], '', ['Env=', 'WD='])
		except getopt.GetoptError as err:
			# print help information and exit:
			print(str(err))         # will print something like "option -a not recognized"
			sys.exit(2)
		for o, a in optlist:
			if o == '--Env':
				if a in ('DEV', 'PREPROD'):
					cls.__environment = a
				else:
					print(a - ' envirionment is not supported.')
			elif o == '--WD':
				if a in ('FIREFOX', 'CHROME'):
					cls.__web_driver = a
				else:
					print(a - ' web driver is not supported.')


	@classmethod
	def get_environment(cls):
		""" Returns selected environment (DEV or PREPROD) """

		if cls.__environment is None:
			ArgvParserObject.__read_parameters()

		return cls.__environment

	@classmethod
	def get_webdriver(cls):
		""" Returns selected web driver (FIREFOX, CHROME, etc. ) """

		if cls.__web_driver is None:
			ArgvParserObject.__read_parameters()

		return cls.__web_driver

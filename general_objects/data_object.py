from assets.envdata import DevData, EnvData
from general_objects.argv_parser_object import ArgvParserObject


class DataObject(object):
	__envdata = EnvData

	@classmethod
	def get_envdata(cls):
		""" Returns combined data (general data combined with enviroment data) """
		if cls.__envdata is EnvData:
			cls.__envdata = cls.set_envdata()
		return cls.__envdata

	@staticmethod
	def set_envdata():
		""" Returns GENERAL data from file, combined with ENVIRONMENT data """

		env = ArgvParserObject.get_environment()

		# reads data for selected enviroment
		if env == 'DEV':
			envdata = DevData
		# elif env == 'PREPROD':
		#	envdata = PreprodData
		else:
			raise NameError('Wrong enviroment value. ')

		return envdata

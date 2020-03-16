from assets import testdata
from back_end_tests.objects.parametrized_test_case import ParametrizedTestCase


class FrontEndTest(ParametrizedTestCase):
	""" Tested features:

		-

	"""

	data = testdata


	@classmethod
	def setUpClass(cls):
		super(FrontEndTest, cls).setUpClass()

		cls.clean_db()
		cls.prepare_db()

	@classmethod
	def tearDownClass(cls):
		super(FrontEndTest, cls).tearDownClass()

		cls.clean_db()

	def test_frontend_001(self):
		pass

	@classmethod
	def prepare_db(cls):
		pass

	@classmethod
	def clean_db(cls):
		pass
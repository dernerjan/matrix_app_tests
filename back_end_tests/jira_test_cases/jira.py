from assets import testdata
from back_end_tests.objects.parametrized_test_case import ParametrizedTestCase


class JiraTest(ParametrizedTestCase):
	""" Tested features:

		-

	"""

	data = testdata


	@classmethod
	def setUpClass(cls):
		super(JiraTest, cls).setUpClass()

		cls.clean_db()
		cls.prepare_db()

	@classmethod
	def tearDownClass(cls):
		super(JiraTest, cls).tearDownClass()

		cls.clean_db()

	def test_github(self):
		pass

	@classmethod
	def prepare_db(cls):
		pass

	@classmethod
	def clean_db(cls):
		pass
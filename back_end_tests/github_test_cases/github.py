from assets import testdata
from back_end_tests.objects.parametrized_test_case import ParametrizedTestCase


class GithubTest(ParametrizedTestCase):
	""" Tested features:

		-

	"""

	data = testdata


	@classmethod
	def setUpClass(cls):
		super(GithubTest, cls).setUpClass()

		cls.clean_db()
		cls.prepare_db()

	@classmethod
	def tearDownClass(cls):
		super(GithubTest, cls).tearDownClass()

		cls.clean_db()

	def test_github_001(self):
		pass

	@classmethod
	def prepare_db(cls):
		pass

	@classmethod
	def clean_db(cls):
		pass
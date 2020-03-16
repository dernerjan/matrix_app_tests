import unittest
import time

class ParametrizedTestCase(unittest.TestCase):
	""" TestCase classes that want to be parametrized should
		inherit from this class.
	"""

	assertSleep = 2
	fiftySeconds = 50

	def assertResponseXML(self, method, parameters, xpath, expected_value, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		contains expected value.

	    Keyword arguments:
	    method          -- method which returns response which we want to check
	    parameters      -- parameters of method
	    xpath           -- xpath for retrieving value which we want to check
	    expected_value  -- expected value in response
	    timeout         -- timeout for assertion (default 0)
	    """

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if type(expected_value).__name__ == 'str':
				if len(response) == 0:
					if timeout < (time.time() - start_time):
						raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(response))
					else:
						time.sleep(self.assertSleep)
				elif expected_value == response[0]:
					break
				elif timeout < (time.time() - start_time):
					raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(response[0]))
				else:
					time.sleep(self.assertSleep)

			elif type(expected_value).__name__ == 'int':
				if expected_value == len(response):
					break
				elif timeout < (time.time() - start_time):
					raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(len(response)))
				else:
					time.sleep(self.assertSleep)

			elif type(expected_value).__name__ == 'bool':
				if expected_value == bool(response):
					break
				elif timeout < (time.time() - start_time):
					raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(bool(response)))
				else:
					time.sleep(self.assertSleep)
		return response

	def assertResponseArray(self, method, parameters, expected_value, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		contains expected value.

	    Keyword arguments:
	    method          -- method which returns response which we want to check
	    parameters      -- parameters of method
	    expected_value  -- expected value in response
	    timeout         -- timeout for assertion (default 0)
	    """

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if type(expected_value).__name__ == 'list' or type(expected_value).__name__ == 'str':
				if len(response) == 0:
					if timeout < (time.time() - start_time):
						raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(response))
					else:
						time.sleep(self.assertSleep)
				elif expected_value == response[0]:
					break
				elif timeout < (time.time() - start_time):
					raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(response[0]))
				else:
					time.sleep(self.assertSleep)

			elif type(expected_value).__name__ == 'int':
				if expected_value == len(response):
					break
				elif timeout < (time.time() - start_time):
					raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(len(response)))
				else:
					time.sleep(self.assertSleep)

			else:
				raise AssertionError("Not supported type of expected value")
		return response

	def assertResponseInt(self, method, parameters, expected_value, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		contains expected value.

	    Keyword arguments:
	    method          -- method which returns response which we want to check
	    parameters      -- parameters of method
	    expected_value  -- expected value in response
	    timeout         -- timeout for assertion (default 0)
	    """

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if expected_value == response:
				break
			elif timeout < (time.time() - start_time):
				raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(response))
			else:
				time.sleep(self.assertSleep)
		return response

	def assertResponseString(self, method, parameters, expected_value, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		contains expected value.

	    Keyword arguments:
	    method          -- method which returns response which we want to check
	    parameters      -- parameters of method
	    expected_value  -- expected value in response
	    timeout         -- timeout for assertion (default 0)
	    """

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if expected_value == response:
				break
			elif timeout < (time.time() - start_time):
				raise AssertionError(error_message + ": " + str(expected_value) + " != " + str(response))
			else:
				time.sleep(self.assertSleep)
		return response

	def assertResponseNotString(self, method, parameters, not_expected_value, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		not contains not_expected value.

		Keyword arguments:
		method          -- method which returns response which we want to check
		parameters      -- parameters of method
		non_expected_value  -- non_expected value in response
		timeout         -- timeout for assertion (default 0)
		"""

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if not_expected_value != response:
				break
			elif timeout < (time.time() - start_time):
				raise AssertionError(error_message + ": " + str(not_expected_value) + " != " + str(response))
			else:
				time.sleep(self.assertSleep)
		return response

	def assertResponseNotNull(self, method, parameters, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		is still None.

		Keyword arguments:
		method          -- method which returns response which we want to check
		parameters      -- parameters of method
		timeout         -- timeout for assertion (default 0)
		"""

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if response is not None:
				break
			elif timeout < (time.time() - start_time):
				raise AssertionError(error_message + ": " + str(response) + " != " + "None")
			else:
				time.sleep(self.assertSleep)
		return response

	def assertResponseNull(self, method, parameters, timeout=0, error_message=''):
		""" Additional assert with timeout, which checks whether response from function(parameters)
		is still None.

		Keyword arguments:
		method          -- method which returns response which we want to check
		parameters      -- parameters of method
		timeout         -- timeout for assertion (default 0)
		"""

		start_time = time.time()
		while True:
			if type(parameters).__name__ == 'tuple':
				response = method(*parameters)
			else:
				response = method(parameters)

			if response is None:
				break
			elif timeout < (time.time() - start_time):
				raise AssertionError(error_message + ": " + "None" + " != " + str(response))
			else:
				time.sleep(self.assertSleep)
		return response

	@staticmethod
	def wait_until_true(timeout, lambda_condition):
		start_time = time.time()
		while (time.time() - start_time) <= timeout:
			if lambda_condition():
				return True
		return False
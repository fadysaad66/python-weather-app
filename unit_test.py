import unittest
from unittest.mock import patch
from weather import app, Weather  # Assuming your Flask app is in app.py

class TestWeather(unittest.TestCase):
    @patch('requests.get')  # Mock the 'requests.get' function
    def test_get_data(self, mock_get):
        # Mocked response data
        mock_get.return_value.json.return_value = {
            "main": {
                "temp": 25,
                "temp_max": 30,
                "temp_min": 20
            }
        }

        # Create a Weather object for a test city
        weather = Weather("TestCity", 0, 0)

        # Check if the attributes are correctly assigned
        self.assertEqual(weather.temp, 25)
        self.assertEqual(weather.max_temp, 30)
        self.assertEqual(weather.min_temp, 20)

    def test_print_tem(self):
        city_weather = Weather("TestCity", 0, 0)
        city_weather.temp = 25
        city_weather.max_temp = 30
        city_weather.min_temp = 20

        # Test the output of the print_tem method
        expected_output = "<p>the temp in TestCity is 25 c</p>" \
                          "<p>the max temp in TestCity is 30 c</p>" \
                          "<p>the min temp in TestCity is 20 c</p>"
        self.assertEqual(city_weather.print_tem(), expected_output)

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a test client to simulate requests
        cls.client = app.test_client()
        cls.client.testing = True  # Enables the 'testing' flag to propagate errors

    def test_home(self):
        # Send a GET request to the home route
        response = self.client.get('/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains 'Weather Report' text
        self.assertIn(b'Weather Report', response.data)

if __name__ == '__main__':
    unittest.main()

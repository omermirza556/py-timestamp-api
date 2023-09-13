import os
from unittest import TestCase, mock
import ast

try:
    from app import app
    import unittest
except Exception as e:
    print("Libraries are missing {}".format(e))
    
class FlaskTest(TestCase):
    @mock.patch.dict(os.environ, {"MESSAGE": "Automate all the things!"})
    
    # Check for 200 
    def test_response_code(self):
        
        test = app.test_client(self)
        response = test.get()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    @mock.patch.dict(os.environ, {"MESSAGE": "Automate all the things!"})
    
    # Checks response
    
    def test_response(self):
        test = app.test_client(self)
        response = test.get()
        res = ast.literal_eval(response.data.decode('utf-8'))
        self.assertIn('message', res)
        self.assertIn('timestamp', res)
        
        
if __name__ == "__main__":
    unittest.main()
        
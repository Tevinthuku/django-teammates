"""
Testing the teammates app and endpoints
"""
from rest_framework.test import APITestCase


class TeammatesTestClass(APITestCase):
    """
    Testclass for teamates endpoints
    """

    def test_response_for_getting_all_users(self):
        """
        Ensure we get a 200 response as we get all teammates
        """
        response = self.client.get("/team/all/", format='json')
        self.assertEqual(response.status_code, 200)

    def test_length_of_teammates_list(self):
        """
        Ensure we get a [] as the list of teammates
        since none has been created yet
        """
        response = self.client.get("/team/all/", format='json')
        self.assertEqual(response.data, {'status': 200, 'data': []})

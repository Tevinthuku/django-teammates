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

    def test_posting_a_teammate(self):
        """
            test posting a teammate in the right format
        """
        response = self.client.post(
            '/team/all/', {'name': 'New Name',
                           'email': 'newteammate@gmail.com',
                           'slackhandle': '@NewTeam'},
            format='json')
        self.assertEqual(response.data, {'status': 201,
                                         "data": {'id': 1, 'name': 'New Name',
                                                  'email': 'newteammate@gmail.com',
                                                  'slackhandle': '@NewTeam'}})

    def test_posting_teammate_with_wrong_email_format(self):
        """
            test posting a teammate with the wrong email format
        """
        response = self.client.post(
            '/team/all/', {'name': 'New Name',
                           'email': 'newteammail.com',
                           'slackhandle': '@NewTeam'},
            format='json')
        self.assertEqual(response.data, {
            "email": [
                "Enter a valid email address."
            ]
        })

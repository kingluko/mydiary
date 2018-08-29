from tests.base_test import BaseTestCase
import json

signup_url = '/api/v1/auth/signup'
signin_url = '/api/v1/auth/signin'


class TestSignup(BaseTestCase):
    """This class tests user signup"""

    def test_user_signup(self):
        """This method tests is a user can sign up"""
        rs = self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "You have registered succesfully")

    def test_user_signup_twice(self):
        """This method tests if a user can signup twice"""
        # signs up first time
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        # signs up second time
        rs = self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "User already exists")

    def test_signup_without_details(self):
        """This method tests is a user tries to signup without full details"""
        rs = self.client.post(
                signup_url,
                data=json.dumps(self.signin_data),
                content_type='application/json')
        self.assertEqual(rs.status_code, 400)


class TestSignIn(BaseTestCase):
    """This class tests user signin"""

    def test_user_signin(self):
        """This method tests user sign in"""
        # sign up
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        # sign in
        rs = self.client.post(
                signin_url,
                data=json.dumps(self.signin_data),
                content_type='application/json')
        self.assertEqual(rs.status_code, 201)

    def test_signin_no_details(self):
        """This method test is user can signin with no details"""
        # sign up
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        # signs in with no details
        rs = self.client.post(
                signin_url,
                data=json.dumps({"username": "", "password": ""}),
                content_type='application/json')
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], 'Please enter login details')

    def test_signin_wrong_details(self):
        """This method tests if a user tries to signin with wrong details"""
        # signup
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        rs = self.client.post(
                signin_url,
                data=json.dumps({"username": "hjkashk", "password": "jhsadh"}),
                content_type='application/json')
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], 'User not found')

    def test_signin_wrong_password(self):
        """This method tests if a user signin with the wrong passowrd"""
        # signup
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        # signin
        rs = self.client.post(
                signin_url,
                data=json.dumps({"username": "test123", "password": "jhsade"}),
                content_type='application/json')
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "Invalid password")

    def test_token_generated_on_signin(self):
        """This method tests if token is generated on login"""
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        # signin
        rs = self.client.post(
                signin_url,
                data=json.dumps(self.signin_data),
                content_type='application/json')
        rp = json.loads(rs.data)
        self.assertIn('token', str(rp))
        

class TestProfile(BaseTestCase):
    """This class tests the endpoint functionality"""
    def test_get_profile_details(self):
        # sign up
        self.client.post(
            signup_url,
            data=json.dumps(self.signup_data),
            content_type='application/json')
        # sign in
        rs = self.client.post(
                signin_url,
                data=json.dumps(self.signin_data),
                content_type='application/json')
        rp = json.loads(rs.get_data(as_text=True))
        token = rp.get("token")
        header = {
            "Content-Type": "application/json",
            "x-access-token": token}
        response = self.client.get(
            '/api/v1/profile',
            content_type='application/json',
            headers=header)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Data', str(data))
from tests.base_test import BaseTestCase
import json

signup_url = '/api/v1/auth/signup'
signin_url = '/api/v1/auth/signin'


class TestEntries(BaseTestCase):
    """This class tests entries endpoints"""

    def test_get_entries(self):
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
        # get entry
        response = self.client.get(
            '/api/v1/entries',
            content_type='application/json',
            headers=header)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Entries not found")

    def test_post_entry(self):
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
        # post entry
        response = self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 201)

    def test_get_all_entries(self):
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
        # post entry
        self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps(self.entry))
        response = self.client.get(
            '/api/v1/entries',
            content_type='application/json',
            headers=header)
        self.assertEqual(response.status_code, 200)

    def test_entry_story_validation(self):
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
        # post entry
        response = self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps({"title": " ", " ": " "}))
        data = json.loads(response.data)
        self.assertIn('Enter a valid text', str(data))

    def test_entry_title_validation(self):
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
        # post entry
        response = self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps({" ": " ", "story": "story"}))
        data = json.loads(response.data)
        self.assertIn('Enter a valid title', str(data))

    def test_get_invalid_entry(self):
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
        # post entry
        self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps(self.entry))
        response = self.client.get(
            '/api/v1/entries/5',
            content_type='application/json',
            headers=header)
        self.assertEqual(response.status_code, 404)

    def test_put_entry(self):
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
        response = self.client.put(
            '/api/v1/entries/0',
            content_type='application/json',
            headers=header, data=json.dumps({"title": "haha", "story": "check"}))
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_entry(self):
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
        response = self.client.delete(
            '/api/v1/entries/5',
            content_type='application/json',
            headers=header)
        self.assertEqual(response.status_code, 404)
import unittest

import js_repos_visual as jrv

class JsReposVisualTestCase(unittest.TestCase):
    """Tests for js_repos_visual.py"""
    def setUp(self):
        """Call all the functions here, and test elements separately"""
        self.r = jrv.get_response()
        self.repo_dicts = jrv.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.links, self.stars, self.labels = jrv.get_project_data(self.repo_dicts)

    def test_get_response(self):
        """Test that we get a vailid response"""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """Test that we get correct data"""
        # We should get 30 repositories
        self.assertEqual(len(self.repo_dicts), 30)

        # Repositories should have required keys
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()

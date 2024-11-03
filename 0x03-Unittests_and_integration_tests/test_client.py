#!/usr/bin/env python3
"""testing the client module"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with("https://api.github.com/orgs/{}".format(org))

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 100,
                    "name": "Test",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 200,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/Test",
                    "created_at": "2024-04-19T00:31:37Z",
                    "updated_at": "2024-11-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 17,
                    "default_branch": "master",
                },
                {
                    "id": 300,
                    "name": "Tekken",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 400,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/Tekken",
                    "created_at": "2024-04-19T00:31:37Z",
                    "updated_at": "2024-11-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 18,
                    "default_branch": "master",
                },
            ],
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "Test",
                    "Tekken",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

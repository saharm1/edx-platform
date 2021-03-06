"""
Tests i18n in courseware
"""

import re

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.utils import translation
from nose.plugins.attrib import attr

from openedx.core.djangoapps.dark_lang.models import DarkLangConfig
from openedx.core.djangoapps.lang_pref import LANGUAGE_KEY
from openedx.core.djangoapps.user_api.preferences.api import set_user_preference
from student.tests.factories import UserFactory


class BaseI18nTestCase(TestCase):
    """
    Base utilities for i18n test classes to derive from
    """
    preview_language_url = '/update_lang/'
    url = reverse('dashboard')
    site_lang = settings.LANGUAGE_CODE
    pwd = 'test_password'

    def setUp(self):
        super(BaseI18nTestCase, self).setUp()
        self.addCleanup(translation.deactivate)
        self.client = Client()
        self.create_user()

    def assert_tag_has_attr(self, content, tag, attname, value):
        """Assert that a tag in `content` has a certain value in a certain attribute."""
        regex = r"""<{tag} [^>]*\b{attname}=['"]([\w\d\- ]+)['"][^>]*>""".format(tag=tag, attname=attname)
        match = re.search(regex, content)
        self.assertTrue(match, "Couldn't find desired tag '%s' with attr '%s' in %r" % (tag, attname, content))
        attvalues = match.group(1).split()
        self.assertIn(value, attvalues)

    def release_languages(self, languages):
        """
        Release a set of languages using the dark lang interface.
        languages is a list of comma-separated lang codes, eg, 'ar, es-419'
        """
        user = User()
        user.save()
        DarkLangConfig(
            released_languages=languages,
            changed_by=user,
            enabled=True
        ).save()

    def create_user(self):
        """
        Creates the user log in
        """
        # Create one user and save it to the database
        email = 'test@edx.org'
        self.user = UserFactory.create(username='test', email=email, password=self.pwd)

    def user_login(self):
        """
        Log the user in
        """
        # Get the login url & log in our user
        self.client.login(username=self.user.username, password=self.pwd)

    def tearDown(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='en')


@attr(shard=1)
class I18nTestCase(BaseI18nTestCase):
    """
    Tests for i18n
    """
    def test_default_is_en(self):
        self.release_languages('fr')
        response = self.client.get('/')
        self.assert_tag_has_attr(response.content, "html", "lang", "en")
        self.assertEqual(response['Content-Language'], 'en')
        self.assert_tag_has_attr(response.content, "body", "class", "lang_en")

    def test_esperanto(self):
        self.release_languages('fr, eo')
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='eo')
        self.assert_tag_has_attr(response.content, "html", "lang", "eo")
        self.assertEqual(response['Content-Language'], 'eo')
        self.assert_tag_has_attr(response.content, "body", "class", "lang_eo")

    def test_switching_languages_bidi(self):
        self.release_languages('ar, eo')
        response = self.client.get('/')
        self.assert_tag_has_attr(response.content, "html", "lang", "en")
        self.assertEqual(response['Content-Language'], 'en')
        self.assert_tag_has_attr(response.content, "body", "class", "lang_en")
        self.assert_tag_has_attr(response.content, "body", "class", "ltr")

        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='ar')
        self.assert_tag_has_attr(response.content, "html", "lang", "ar")
        self.assertEqual(response['Content-Language'], 'ar')
        self.assert_tag_has_attr(response.content, "body", "class", "lang_ar")
        self.assert_tag_has_attr(response.content, "body", "class", "rtl")


@attr(shard=1)
class I18nRegressionTests(BaseI18nTestCase):
    """
    Tests for i18n
    """
    def test_es419_acceptance(self):
        # Regression test; LOC-72, and an issue with Django
        self.release_languages('es-419')
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='es-419')
        self.assert_tag_has_attr(response.content, "html", "lang", "es-419")

    def test_unreleased_lang_resolution(self):
        # Regression test; LOC-85
        self.release_languages('fa')
        self.user_login()

        # We've released 'fa', AND we have language files for 'fa-ir' but
        # we want to keep 'fa-ir' as a dark language. Requesting 'fa-ir'
        # in the http request (NOT with the ?preview-lang query param) should
        # receive files for 'fa'
        response = self.client.get(self.url, HTTP_ACCEPT_LANGUAGE='fa-ir')
        self.assert_tag_has_attr(response.content, "html", "lang", "fa")

        # Now try to access with dark lang
        self.client.post(self.preview_language_url, {'preview_lang': 'fa-ir', 'set_language': 'set_language'})
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", "fa-ir")

    def test_preview_lang(self):
        self.user_login()

        # Regression test; LOC-87
        self.release_languages('es-419')
        site_lang = settings.LANGUAGE_CODE
        # Visit the front page; verify we see site default lang
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", site_lang)

        # Verify we can switch language using the preview-lang query param
        # Set the language
        self.client.post(self.preview_language_url, {'preview_lang': 'eo', 'set_language': 'set_language'})

        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", "eo")
        # We should be able to see released languages using preview-lang, too
        self.client.post(self.preview_language_url, {'preview_lang': 'es-419', 'set_language': 'set_language'})
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", "es-419")

        # Clearing the language should go back to site default
        self.client.post(self.preview_language_url, {'reset': 'reset'})
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", site_lang)


@attr(shard=1)
class I18nLangPrefTests(BaseI18nTestCase):
    """
    Regression tests of language presented to the user, when they
    choose a language preference, and when they have a preference
    and use the dark lang preview functionality.
    """
    def setUp(self):
        super(I18nLangPrefTests, self).setUp()
        self.user_login()

    def test_lang_preference(self):
        # Regression test; LOC-87
        self.release_languages('ar, es-419')

        # Visit the front page; verify we see site default lang
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", self.site_lang)

        # Set user language preference
        set_user_preference(self.user, LANGUAGE_KEY, 'ar')
        # and verify we now get an ar response
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", 'ar')

        # Verify that switching language preference gives the right language
        set_user_preference(self.user, LANGUAGE_KEY, 'es-419')
        response = self.client.get(self.url)
        self.assert_tag_has_attr(response.content, "html", "lang", 'es-419')

    def test_preview_precedence(self):
        # Regression test; LOC-87
        self.release_languages('ar, es-419')

        # Set user language preference
        set_user_preference(self.user, LANGUAGE_KEY, 'ar')
        # Verify preview-lang takes precedence
        self.client.post(self.preview_language_url, {'preview_lang': 'eo', 'set_language': 'set_language'})
        response = self.client.get(self.url)

        self.assert_tag_has_attr(response.content, "html", "lang", 'eo')
        # Hitting another page should keep the dark language set.
        response = self.client.get(reverse('courses'))
        self.assert_tag_has_attr(response.content, "html", "lang", "eo")

        # Clearing language must set language back to preference language
        self.client.post(self.preview_language_url, {'reset': 'reset'})
        response = self.client.get(self.url)

        self.assert_tag_has_attr(response.content, "html", "lang", 'ar')

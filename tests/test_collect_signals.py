import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "collect_signals.py"
SPEC = importlib.util.spec_from_file_location("collect_signals", SCRIPT)
collector = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(collector)


class ParseFeedTests(unittest.TestCase):
    def test_parses_rss_items_and_marks_them_unverified(self):
        payload = b"""<?xml version="1.0"?>
        <rss version="2.0"><channel>
          <item>
            <title>Factory automation update</title>
            <link>https://example.com/story/1</link>
            <pubDate>Tue, 27 Oct 2026 12:00:00 GMT</pubDate>
            <description>New industrial automation project.</description>
          </item>
        </channel></rss>"""
        source = {
            "id": "test-rss",
            "name": "Test RSS",
            "type": "rss",
            "url": "https://example.com/feed.xml",
            "region": "global",
            "topic_tags": ["manufacturing"],
            "reliability_tier": "secondary_media",
        }
        records = collector.parse_feed(payload, source)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["title"], "Factory automation update")
        self.assertEqual(records[0]["url"], "https://example.com/story/1")
        self.assertEqual(records[0]["evidence_class"], "lead_unverified")
        self.assertEqual(records[0]["verification_status"], "not_reviewed")
        self.assertEqual(records[0]["topic_tags"], ["manufacturing"])

    def test_parses_atom_entry_and_alternate_link(self):
        payload = b"""<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>https://arxiv.org/abs/2610.12345</id>
            <title>Agent systems in production</title>
            <published>2026-10-27T10:00:00Z</published>
            <summary>Reliability and evaluation methods.</summary>
            <link href="https://arxiv.org/abs/2610.12345" rel="alternate" />
            <author><name>Research Author</name></author>
          </entry>
        </feed>"""
        source = {
            "id": "test-atom",
            "name": "Test Atom",
            "type": "arxiv_api",
            "url": "https://example.com/api",
            "region": "global",
            "topic_tags": ["ai"],
            "reliability_tier": "primary_research",
        }
        records = collector.parse_feed(payload, source)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["url"], "https://arxiv.org/abs/2610.12345")
        self.assertEqual(records[0]["published_at"], "2026-10-27T10:00:00+00:00")

    def test_skips_missing_or_non_http_links(self):
        payload = b"""<rss><channel>
          <item><title>No link</title><description>Skip me</description></item>
          <item><title>Unsafe link</title><link>javascript:alert(1)</link></item>
        </channel></rss>"""
        source = {
            "id": "test-invalid",
            "name": "Test",
            "type": "rss",
            "url": "https://example.com/feed",
        }
        self.assertEqual(collector.parse_feed(payload, source), [])

    def test_stable_id_is_based_on_source_and_url(self):
        payload = b"""<rss><channel><item>
          <title>Same story</title><link>https://example.com/story/2</link>
        </item></channel></rss>"""
        source = {"id": "same-source", "name": "Test", "type": "rss", "url": "https://example.com/feed"}
        first = collector.parse_feed(payload, source)
        second = collector.parse_feed(payload, source)
        self.assertEqual(first[0]["id"], second[0]["id"])


if __name__ == "__main__":
    unittest.main()

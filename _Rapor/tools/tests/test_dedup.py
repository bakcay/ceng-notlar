import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from dedup import file_hash, text_hash, find_duplicates


class TestTextHash(unittest.TestCase):
    def test_whitespace_insensitive(self):
        self.assertEqual(text_hash("a b\nc"), text_hash("  a\t b   c  "))

    def test_case_insensitive(self):
        self.assertEqual(text_hash("Merhaba"), text_hash("MERHABA"))

    def test_different_text_differs(self):
        self.assertNotEqual(text_hash("bir"), text_hash("iki"))

    def test_turkish_preserved_not_asciified(self):
        self.assertNotEqual(text_hash("şık"), text_hash("sik"))


class TestFindDuplicates(unittest.TestCase):
    def test_binary_duplicates_grouped(self):
        entries = [
            {"path": "a", "fhash": "X", "thash": "T1", "words": 10},
            {"path": "b", "fhash": "X", "thash": "T1", "words": 10},
            {"path": "c", "fhash": "Y", "thash": "T2", "words": 5},
        ]
        r = find_duplicates(entries)
        self.assertEqual(len(r["binary"]), 1)
        self.assertEqual(sorted(r["binary"][0]), ["a", "b"])

    def test_text_duplicates_exclude_binary_duplicates(self):
        entries = [
            {"path": "a", "fhash": "X", "thash": "T", "words": 10},
            {"path": "b", "fhash": "X", "thash": "T", "words": 10},
        ]
        r = find_duplicates(entries)
        self.assertEqual(r["text"], [])

    def test_text_duplicate_canonical_is_longest(self):
        entries = [
            {"path": "kisa", "fhash": "X", "thash": "T", "words": 100},
            {"path": "uzun", "fhash": "Y", "thash": "T", "words": 900},
        ]
        r = find_duplicates(entries)
        self.assertEqual(r["text"][0][0], "uzun")

    def test_no_duplicates_returns_empty(self):
        entries = [{"path": "a", "fhash": "X", "thash": "T1", "words": 1}]
        r = find_duplicates(entries)
        self.assertEqual(r["binary"], [])
        self.assertEqual(r["text"], [])


class TestFileHash(unittest.TestCase):
    def test_same_bytes_same_hash(self):
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as f1, \
             tempfile.NamedTemporaryFile(delete=False) as f2:
            f1.write(b"ayni"); f2.write(b"ayni")
            n1, n2 = f1.name, f2.name
        self.assertEqual(file_hash(n1), file_hash(n2))
        os.unlink(n1); os.unlink(n2)


if __name__ == "__main__":
    unittest.main()

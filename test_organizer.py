import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, tempfile
from pathlib import Path
from organizer import organize
class T(unittest.TestCase):
    def test_organizes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/"a.pdf").write_text("x"); (p/"b.txt").write_text("y")
            moved = organize(str(p))
            self.assertEqual(moved, {"a.pdf": "pdf", "b.txt": "txt"})
            self.assertTrue((p/"pdf"/"a.pdf").exists())
if __name__ == "__main__": unittest.main()

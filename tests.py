import unittest
import baseconvert

class TestBaseConverter(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(baseconvert.convert("16xA 10"), "10")
        self.assertEqual(baseconvert.convert("16xA 8"), "12")
        self.assertEqual(baseconvert.convert("16xA 2"), "1010")
        self.assertEqual(baseconvert.convert("10x10 10"), "10")
        self.assertEqual(baseconvert.convert("10x10 16"), "A")
        self.assertEqual(baseconvert.convert("10x10 8"), "12")
        self.assertEqual(baseconvert.convert("10x10 2"), "1010")
        self.assertEqual(baseconvert.convert("8x12 10"), "10")
        self.assertEqual(baseconvert.convert("8x12 16"), "A")
        self.assertEqual(baseconvert.convert("8x12 8"), "12")
        self.assertEqual(baseconvert.convert("8x12 2"), "1010")

    def testInvalidNumberErrors(self):
        with self.assertRaises(Exception):
            baseconvert.convert("10xA")
        with self.assertRaises(Exception):
            baseconvert.convert("2x3")
        with self.assertRaises(Exception):
            baseconvert.convert("3x9")
        with self.assertRaises(Exception):
            baseconvert.convert("0xM")
        with self.assertRaises(Exception):
            baseconvert.convert("0129")
        with self.assertRaises(Exception):
            baseconvert.convert("b1003")
        baseconvert.convert("d120")
        baseconvert.convert("0x120")
        baseconvert.convert("O120")
        baseconvert.convert("b10")

    def testSourcePrefixes(self):
        self.assertEqual(baseconvert.convert("0xA 10"), "10")
        self.assertEqual(baseconvert.convert("07 10"), "7")
        self.assertEqual(baseconvert.convert("d50 10"), "50")
        self.assertEqual(baseconvert.convert("b1011"), "11")

    def testTargetPrefixes(self):
        self.assertEqual(baseconvert.convert("16xA 0x"), "A")
        self.assertEqual(baseconvert.convert("8x7 0x"), "7")
        self.assertEqual(baseconvert.convert("10x50 0x"), "32")
        self.assertEqual(baseconvert.convert("b1011 0x"), "B")
        self.assertEqual(baseconvert.convert("16xA d"), "10")
        self.assertEqual(baseconvert.convert("8x7 d"), "7")
        self.assertEqual(baseconvert.convert("10x50 d"), "50")
        self.assertEqual(baseconvert.convert("2x1011 d"), "11")
        self.assertEqual(baseconvert.convert("16xA b"), "1010")
        self.assertEqual(baseconvert.convert("8x7 b"), "111")
        self.assertEqual(baseconvert.convert("10x50 b"), "110010")
        self.assertEqual(baseconvert.convert("2x1011 b"), "1011")
        self.assertEqual(baseconvert.convert("07 0"), "7")
        self.assertEqual(baseconvert.convert("10x50 0"), "62")

    def testAllPrefixes(self):
        self.assertEqual(baseconvert.convert("0xA 0x"), "A")
        self.assertEqual(baseconvert.convert("O7 0x"), "7")
        self.assertEqual(baseconvert.convert("07 0x"), "7")
        self.assertEqual(baseconvert.convert("d50 0x"), "32")
        self.assertEqual(baseconvert.convert("b1011 0x"), "B")
        self.assertEqual(baseconvert.convert("0xA d"), "10")
        self.assertEqual(baseconvert.convert("O7 d"), "7")
        self.assertEqual(baseconvert.convert("07 d"), "7")
        self.assertEqual(baseconvert.convert("d50 d"), "50")
        self.assertEqual(baseconvert.convert("b1011 d"), "11")
        self.assertEqual(baseconvert.convert("0xA b"), "1010")
        self.assertEqual(baseconvert.convert("8x7 b"), "111")
        self.assertEqual(baseconvert.convert("d50 b"), "110010")
        self.assertEqual(baseconvert.convert("b1011 b"), "1011")
        self.assertEqual(baseconvert.convert("07 0"), "7")
        self.assertEqual(baseconvert.convert("O7 0"), "7")
        self.assertEqual(baseconvert.convert("10x50 0"), "62")
        pass

    def testDefaults(self):
        self.assertEqual(baseconvert.convert("0x50"), "80")
        self.assertEqual(baseconvert.convert("80"), "50")
        self.assertEqual(baseconvert.convert("80 0"), "120")
        self.assertEqual(baseconvert.convert("b10011"), "19")

    def testCaseSensitivity(self):
        self.assertEqual(baseconvert.convert("16XA 0X"), "A")
        self.assertEqual(baseconvert.convert("16xa 0x"), "A")
        self.assertEqual(baseconvert.convert("8X7 0x"), "7")
        self.assertEqual(baseconvert.convert("10x50 0X"), "32")
        self.assertEqual(baseconvert.convert("B1011 0x"), "B")
        self.assertEqual(baseconvert.convert("16xa d"), "10")

if __name__ == '__main__':
    unittest.main()

"""
Unit tests for MathJax SVG to LaTeX Converter.
"""

import unittest
from bs4 import BeautifulSoup
from app.crawler.math_parser import (
    decode_c_hex, parse_mml_ast, decode_mathjax_container, clean_html_with_math
)


class TestMathParser(unittest.TestCase):

    def test_decode_c_hex_basic_digits(self):
        self.assertEqual(decode_c_hex("30"), "0")
        self.assertEqual(decode_c_hex("39"), "9")
        self.assertEqual(decode_c_hex("2B"), "+")
        self.assertEqual(decode_c_hex("3D"), "=")

    def test_decode_c_hex_math_alphanumeric(self):
        # Math italic 'x' -> 0x1D465
        self.assertEqual(decode_c_hex("1D465"), "x")
        # Math italic 'A' -> 0x1D434
        self.assertEqual(decode_c_hex("1D434"), "A")
        # Math italic 'y' -> 0x1D466
        self.assertEqual(decode_c_hex("1D466"), "y")

    def test_decode_c_hex_greek(self):
        # Kappa -> 0x1D705
        self.assertEqual(decode_c_hex("1D705"), r"\kappa")
        # Lambda -> 0x1D706
        self.assertEqual(decode_c_hex("1D706"), r"\lambda")
        # Omega -> 0x03C9 or 0x03A9
        self.assertEqual(decode_c_hex("3A9"), r"\Omega")
        self.assertEqual(decode_c_hex("3C9"), r"\omega")

    def test_decode_c_hex_special_symbols(self):
        # Standard reduction potential circle (⊖)
        self.assertEqual(decode_c_hex("2296"), r"^{\circ}")
        # Minus sign (−)
        self.assertEqual(decode_c_hex("2212"), "-")
        # Times (×)
        self.assertEqual(decode_c_hex("D7"), r" \times ")
        # Right arrow (→)
        self.assertEqual(decode_c_hex("2192"), r" \rightarrow ")

    def test_parse_mml_ast_fraction(self):
        html = '<g data-mml-node="mfrac"><g data-mml-node="mn"><use data-c="31"/></g><g data-mml-node="mn"><use data-c="32"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"\frac{1}{2}")

    def test_parse_mml_ast_power(self):
        html = '<g data-mml-node="msup"><g data-mml-node="mi"><use data-c="1D465"/></g><g data-mml-node="mn"><use data-c="32"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"x^{2}")

    def test_parse_mml_ast_subscript(self):
        html = '<g data-mml-node="msub"><g data-mml-node="mi"><use data-c="1D465"/></g><g data-mml-node="mn"><use data-c="31"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"x_{1}")

    def test_parse_mml_ast_vector(self):
        # \vec{a} -> mover with base 'a' and accent 2192 (→)
        html = '<g data-mml-node="mover"><g data-mml-node="mi"><use data-c="61"/></g><g data-mml-node="mo"><use data-c="2192"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"\vec{a}")

    def test_parse_mml_ast_hat_unit_vector(self):
        # \hat{i} -> mover with base 'i' and accent 2C6 (ˆ)
        html = '<g data-mml-node="mover"><g data-mml-node="mi"><use data-c="69"/></g><g data-mml-node="mo"><use data-c="2C6"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"\hat{i}")

    def test_parse_mml_ast_vector_20d7(self):
        # MathJax ExamSIDE uses 20D7 (combining vector arrow)
        html = '<g data-mml-node="mover"><g data-mml-node="mi"><use data-c="61"/></g><g data-mml-node="mo"><use data-c="20D7"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"\vec{a}")

    def test_parse_mml_ast_sqrt_with_surd_glyph(self):
        # Real MathJax msqrt contains both surd glyph 221A and radicand 33 ('3')
        html = '<g data-mml-node="msqrt"><use data-c="221A"/><g data-mml-node="mn"><use data-c="33"/></g></g>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = parse_mml_ast(soup.find('g'))
        self.assertEqual(tex, r"\sqrt{3}")

    def test_decode_mathjax_container_spacing(self):
        # \omega + t should become \omega t, not \omegat
        html = '<mjx-container><svg><g data-mml-node="math"><use data-c="3C9"/><use data-c="74"/></g></svg></mjx-container>'
        soup = BeautifulSoup(html, 'html.parser')
        tex = decode_mathjax_container(soup.find('mjx-container'))
        self.assertEqual(tex, r"\omega t")

    def test_greek_variants_and_invisible_application(self):
        # 0x1D719 is italic phi
        self.assertEqual(decode_c_hex("1D719"), r"\phi")
        # 0x2061 invisible function application is stripped
        self.assertEqual(decode_c_hex("2061"), "")


if __name__ == '__main__':
    unittest.main()


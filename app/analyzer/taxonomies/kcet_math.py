"""
Dedicated KCET Mathematics Taxonomy.
Tailored specifically to Karnataka CET mathematics curriculum, Karnataka PUC I & II syllabus,
and actual past year KCET questions.
"""

from typing import Dict, List, Any

KCET_MATH_TAXONOMY: Dict[str, List[Dict[str, Any]]] = {
    "kcet-sets-and-relations": [
        {
            "name": "Sets, Power Sets & Operations (De Morgan's Laws)",
            "category": "Set Theory",
            "primary": ["subsets", "power set", "number of elements", "union", "intersection", "complement", "de morgan's laws", "disjoint sets", "symmetric difference", "venn diagram"],
            "formula_cues": [r"n(a \cup b) = n(a) + n(b) - n(a \\cap b)", r"2^n", r"(a \cup b)' = a' \\cap b'", r"p(a)"],
            "secondary": ["set", "cardinality", "elements"],
            "summary": "Set theory principles: Number of subsets of a set with $n$ elements is $2^n$; number of proper subsets is $2^n - 1$. Cardinality formula: $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$. De Morgan's laws: $(A \\cup B)' = A' \\cap B'$ and $(A \\cap B)' = A' \\cup B'$.",
            "standard_formulas": r"n(P(A)) = 2^n, \quad n(A \cup B) = n(A) + n(B) - n(A \\cap B), \quad (A \cup B)' = A' \\cap B'",
            "common_traps": "Power set of an empty set $\\emptyset$ is NOT empty; it contains one element: $P(\\emptyset) = \\{\\emptyset\\}$, so $n(P(\\emptyset)) = 2^0 = 1$!",
            "tips_and_tricks": "Number of subsets with at least one element is $2^n - 1$."
        },
        {
            "name": "Relations: Reflexive, Symmetric, Transitive & Equivalence",
            "category": "Relations",
            "primary": ["relation on set", "reflexive", "symmetric", "transitive", "equivalence relation", "equivalence class", "domain and range", "total number of relations"],
            "formula_cues": [r"(a, a) \in r", r"(a, b) \in r \implies (b, a) \in r", r"(a, b) \in r, (b, c) \in r \implies (a, c) \in r", r"2^{n^2}"],
            "secondary": ["elements", "binary relation", "congruence modulo"],
            "summary": "Types of relations on set $A$ with $n$ elements: Total relations $= 2^{n^2}$. Reflexive: $(a, a) \\in R$ for all $a \\in A$. Symmetric: $(a, b) \\in R \\implies (b, a) \\in R$. Transitive: $(a, b) \\in R$ and $(b, c) \\in R \\implies (a, c) \\in R$. Equivalence relation: satisfies reflexive, symmetric, and transitive simultaneously.",
            "standard_formulas": r"\text{Total Relations on Set } A = 2^{n^2}, \quad \text{Reflexive Relations} = 2^{n^2 - n}, \quad \text{Symmetric Relations} = 2^{\frac{n(n+1)}{2}}",
            "common_traps": "Empty relation on a non-empty set is symmetric and transitive, but NOT reflexive!",
            "tips_and_tricks": "The relation 'is parallel to' among lines is an equivalence relation; 'is perpendicular to' is symmetric but NOT reflexive or transitive."
        }
    ],

    "kcet-functions": [
        {
            "name": "Types of Functions: One-One, Onto & Bijective",
            "category": "Function Classification",
            "primary": ["one-one", "injective", "onto", "surjective", "bijective", "number of onto functions", "number of one-one functions", "domain of function", "range of function"],
            "formula_cues": [r"f(x_1) = f(x_2) \implies x_1 = x_2", r"f: a \to b", r"^n p_m", r"\text{range} = \text{codomain}"],
            "secondary": ["codomain", "function", "mapping", "real values"],
            "summary": "Function mappings from set $A$ ($m$ elements) to set $B$ ($n$ elements): Total functions $= n^m$. Injective (one-one): $f(x_1) = f(x_2) \\implies x_1 = x_2$ (possible only if $m \\le n$; total count $= ^n P_m$). Surjective (onto): $\\text{Range} = \\text{Codomain}$ (possible only if $m \\ge n$). Bijective (one-one and onto): $m = n$, total bijections $= n!$.",
            "standard_formulas": r"\text{Total Mappings } A \to B = n^m, \quad \text{Injections } (m \le n) = ^n P_m, \quad \text{Bijections } (m=n) = n!",
            "common_traps": "A strictly monotonic function ($f'(x) > 0$ or $f'(x) < 0$ throughout its domain) is always one-one (injective).",
            "tips_and_tricks": "Horizontal Line Test: If any horizontal line intersects the graph at most once, the function is one-one."
        },
        {
            "name": "Composition of Functions & Invertibility",
            "category": "Function Operations",
            "primary": ["composite function", "fog", "gof", "inverse function", "invertible", "f^{-1}(x)", "identity function", "binary operation", "associative binary", "identity element"],
            "formula_cues": [r"(g \\circ f)(x) = g(f(x))", r"f^{-1}(f(x)) = x", r"a * b = a + b - ab", r"a * e = a"],
            "secondary": ["inverse", "composition", "commutative"],
            "summary": "Composition $(g \\circ f)(x) = g(f(x))$. A function $f: A \\to B$ is invertible if and only if $f$ is BIJECTIVE (one-one and onto). If $f(x) = y$, then $f^{-1}(y) = x$. Binary operations: Commutative if $a * b = b * a$; Associative if $(a * b) * c = a * (b * c)$; Identity element $e$ satisfies $a * e = e * a = a$.",
            "standard_formulas": r"(f \\circ g)^{-1} = g^{-1} \\circ f^{-1}, \quad f(x) = \frac{ax+b}{cx-a} \implies f^{-1}(x) = f(x)",
            "common_traps": "Composition is NOT commutative in general: $f \\circ g \\ne g \\circ f$!",
            "tips_and_tricks": "If $f(x) = \\frac{ax+b}{cx-a}$ where the diagonal coefficients are equal and opposite ($a$ and $-a$), then $f(f(x)) = x$ and $f^{-1}(x) = f(x)$!"
        }
    ],

    "kcet-trigonometric-ratios-and-identities": [
        {
            "name": "Compound, Multiple & Submultiple Angles",
            "category": "Trigonometric Identities",
            "primary": ["compound angles", "sin(a+b)", "cos(a+b)", "tan(a+b)", "multiple angles", "sin 2theta", "cos 2theta", "tan 2theta", "sin 3theta", "cos 3theta", "half angle formulas"],
            "formula_cues": [r"\\sin 2\\theta = \frac{2\tan\\theta}{1+\tan^2\\theta}", r"\\cos 2\\theta = \frac{1-\tan^2\\theta}{1+\tan^2\\theta}", r"\tan(a+b) = \frac{\tan a + \tan b}{1 - \tan a \tan b}", r"\\sin 15^\\circ = \frac{\sqrt{6}-\sqrt{2}}{4}"],
            "secondary": ["angle", "value", "identities", "simplify"],
            "summary": "Core identities: $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta = \\frac{2\\tan\\theta}{1+\\tan^2\\theta}$, $\\cos 2\\theta = \\cos^2\\theta - \\sin^2\\theta = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta = \\frac{1-\\tan^2\\theta}{1+\\tan^2\\theta}$. Standard angle values: $\\sin 15^\\circ = \\cos 75^\\circ = \\frac{\\sqrt{6}-\\sqrt{2}}{4}$, $\\cos 15^\\circ = \\sin 75^\\circ = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$, $\\sin 18^\\circ = \\frac{\\sqrt{5}-1}{4}$.",
            "standard_formulas": r"\\sin 18^\\circ = \frac{\sqrt{5}-1}{4}, \quad \\cos 36^\\circ = \frac{\sqrt{5}+1}{4}, \quad \tan(A+B+C) = \frac{S_1 - S_3}{1 - S_2}",
            "common_traps": "Watch for signs in different quadrants: ASTC rule (All, Sin, Tan, Cos). In quadrant II, only sine and cosecant are positive.",
            "tips_and_tricks": "If $A + B + C = 180^\\circ$, then $\\tan A + \\tan B + \\tan C = \\tan A \\tan B \\tan C$."
        }
    ],

    "kcet-trigonometric-equations": [
        {
            "name": "General & Principal Solutions of Trigonometric Equations",
            "category": "Trigonometric Equations",
            "primary": ["general solution", "principal solution", "sin x = sin alpha", "cos x = cos alpha", "tan x = tan alpha", "number of solutions", "interval 0 to 2pi"],
            "formula_cues": [r"x = n\pi + (-1)^n \alpha", r"x = 2n\pi \pm \alpha", r"x = n\pi + \alpha", r"a\\cos x + b\\sin x = c"],
            "secondary": ["solutions", "equations", "integer n"],
            "summary": "General solutions: $\\sin\\theta = \\sin\\alpha \\implies \\theta = n\\pi + (-1)^n\\alpha$. $\\cos\\theta = \\cos\\alpha \\implies \\theta = 2n\\pi \\pm \\alpha$. $\\tan\\theta = \\tan\\alpha \\implies \\theta = n\\pi + \\alpha$. For equation $a\\cos x + b\\sin x = c$, real solutions exist if and only if $|c| \\le \\sqrt{a^2 + b^2}$.",
            "standard_formulas": r"\\sin\\theta = 0 \implies \\theta = n\pi, \quad \\cos\\theta = 0 \implies \\theta = (2n+1)\frac{\pi}{2}, \quad -\sqrt{a^2+b^2} \le a\\cos x + b\\sin x \le \sqrt{a^2+b^2}",
            "common_traps": "Squaring both sides of a trigonometric equation introduces extraneous roots; always verify candidate solutions back in the original equation.",
            "tips_and_tricks": "To find the number of solutions in $[0, 2\\pi]$, sketch graphs of LHS and RHS and count intersection points."
        }
    ],

    "kcet-properties-of-triangles": [
        {
            "name": "Sine Rule, Cosine Rule & Triangle Geometry",
            "category": "Triangle Properties",
            "primary": ["sine rule", "cosine rule", "projection formula", "area of triangle", "inradius", "circumradius", "half angle formulas"],
            "formula_cues": [r"\frac{a}{\\sin a} = \frac{b}{\\sin b} = \frac{c}{\\sin c} = 2r", r"\\cos a = \frac{b^2 + c^2 - a^2}{2bc}", r"\\Delta = \frac{abc}{4r} = rs", r"r = (s-a)\tan(a/2)"],
            "secondary": ["angles", "sides", "triangle"],
            "summary": "Sine rule: $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$. Cosine rule: $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}$. Projection formulas: $a = b\\cos C + c\\cos B$. Area $\\Delta = \\frac{1}{2}ab\\sin C = \\sqrt{s(s-a)(s-b)(s-c)} = rs = \\frac{abc}{4R}$.",
            "standard_formulas": r"\frac{a}{\\sin A} = 2R, \quad \\cos A = \frac{b^2+c^2-a^2}{2bc}, \quad \\Delta = rs = \frac{abc}{4R}",
            "common_traps": "In an equilateral triangle: $R = 2r$ (circumradius is twice the inradius).",
            "tips_and_tricks": "In right-angled triangle: Inradius $r = \\frac{a+b-c}{2}$ where $c$ is the hypotenuse."
        }
    ],

    "kcet-complex-numbers": [
        {
            "name": "Modulus, Argument & Polar / Euler Forms",
            "category": "Complex Numbers",
            "primary": ["modulus of complex", "argument", "principal argument", "polar form", "conjugate", "quadrant", "argand plane"],
            "formula_cues": [r"|z| = \sqrt{a^2 + b^2}", r"\arg(z) = \tan^{-1}(b/a)", r"z = r(\\cos\\theta + i\\sin\\theta)", r"z \bar{z} = |z|^2", r"-\pi < \\theta \le \pi"],
            "secondary": ["imaginary", "real part", "complex"],
            "summary": "Modulus $|z| = \\sqrt{a^2+b^2}$. Principal argument $\\theta = \\text{Arg}(z) \\in (-\\pi, \\pi]$. Properties: $|z_1 z_2| = |z_1||z_2|$, $\\arg(z_1 z_2) = \\arg z_1 + \\arg z_2$, $z \\bar{z} = |z|^2$. Square root of $z = a+ib$: $\\pm\\left(\\sqrt{\\frac{|z|+a}{2}} + i\\text{sgn}(b)\\sqrt{\\frac{|z|-a}{2}}\\right)$.",
            "standard_formulas": r"|z_1 + z_2| \le |z_1| + |z_2| \quad (\text{Triangle Inequality}), \quad z = r e^{i\\theta}",
            "common_traps": "Principal argument is strictly defined in the interval $(-\\pi, \\pi]$; do not give values in $[0, 2\\pi]$ if principal argument is requested.",
            "tips_and_tricks": "The triangle inequality $|z_1| - |z_2| \\le |z_1 + z_2| \\le |z_1| + |z_2|$ yields the maximum and minimum distance on Argand diagrams instantly."
        },
        {
            "name": "Cube Roots of Unity & Complex Equations",
            "category": "Roots of Unity",
            "primary": ["cube roots of unity", "omega", "1 + omega + omega^2", "omega^3 = 1", "de moivre's theorem"],
            "formula_cues": [r"\omega = \frac{-1 + i\sqrt{3}}{2}", r"\omega^2 = \frac{-1 - i\sqrt{3}}{2}", r"1 + \omega + \omega^2 = 0", r"\omega^3 = 1", r"\omega^{3n} = 1"],
            "secondary": ["roots", "equation", "power"],
            "summary": "Cube roots of unity are $1, \\omega, \\omega^2$ where $\\omega = \\frac{-1 + i\\sqrt{3}}{2}$ and $\\omega^2 = \\frac{-1 - i\\sqrt{3}}{2}$. Fundamental relations: $1 + \\omega + \\omega^2 = 0$ and $\\omega^3 = 1$. Factors: $a^3 - b^3 = (a-b)(a - b\\omega)(a - b\\omega^2)$; $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a + b\\omega + c\\omega^2)(a + b\\omega^2 + c\\omega)$.",
            "standard_formulas": r"1 + \omega + \omega^2 = 0, \quad \omega^3 = 1, \quad \omega^{3k+1} = \omega, \quad \omega^{3k+2} = \omega^2",
            "common_traps": "When reducing higher powers of $\\omega$, divide the exponent by 3 and keep ONLY the remainder: $\\omega^{100} = \\omega^{3(33)+1} = \\omega^1 = \\omega$.",
            "tips_and_tricks": "The three cube roots of unity form the vertices of an equilateral triangle inscribed in a unit circle centered at the origin on the Argand plane."
        }
    ],

    "kcet-quadratic-equations": [
        {
            "name": "Roots, Coefficients & Nature of Roots (Discriminant)",
            "category": "Quadratic Theory",
            "primary": ["quadratic equation", "roots of equation", "sum of roots", "product of roots", "discriminant", "real and equal roots", "imaginary roots", "rational roots", "common root"],
            "formula_cues": [r"\alpha + \beta = -\frac{b}{a}", r"\alpha \beta = \frac{c}{a}", r"\\Delta = b^2 - 4ac", r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}"],
            "secondary": ["roots", "quadratic", "condition"],
            "summary": "Quadratic equation $ax^2 + bx + c = 0$. Roots $\\alpha, \\beta = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$. Sum $\\alpha + \\beta = -b/a$, Product $\\alpha\\beta = c/a$. Discriminant $\\Delta = b^2 - 4ac$: $\\Delta > 0$ (real & distinct), $\\Delta = 0$ (real & equal), $\\Delta < 0$ (complex conjugate roots). Condition for a common root between two quadratics.",
            "standard_formulas": r"\alpha + \beta = -\frac{b}{a}, \quad \alpha\beta = \frac{c}{a}, \quad x^2 - (\alpha+\beta)x + \alpha\beta = 0",
            "common_traps": "If coefficients $a, b, c$ are rational and $\\Delta$ is not a perfect square, roots occur in conjugate surd pairs ($p + \\sqrt{q}$ and $p - \\sqrt{q}$).",
            "tips_and_tricks": "Difference of roots: $|\\alpha - \\beta| = \\frac{\\sqrt{\\Delta}}{|a|}$."
        }
    ],

    "kcet-permutations-and-combinations": [
        {
            "name": "Permutations, Combinations & Combinatorial Geometry",
            "category": "Combinatorics",
            "primary": ["permutations", "combinations", "npr", "ncr", "number of ways", "circular permutation", "selection", "arrangement", "number of diagonals in polygon", "number of triangles"],
            "formula_cues": [r"^n P_r = \frac{n!}{(n-r)!}", r"^n C_r = \frac{n!}{r!(n-r)!}", r"^n C_r + ^n C_{r-1} = ^{n+1} C_r", r"\text{diagonals} = \frac{n(n-3)}{2}"],
            "secondary": ["chairs", "choose", "people", "digits"],
            "summary": "Permutations (arrangements where order matters) $^n P_r = \\frac{n!}{(n-r)!}$. Combinations (selections where order does not matter) $^n C_r = \\frac{n!}{r!(n-r)!}$. Pascal's identity: $^n C_r + ^n C_{r-1} = ^{n+1} C_r$. Circular permutations of $n$ distinct objects: $(n-1)!$ (for necklaces/garlands where clockwise and anticlockwise are identical: $\\frac{(n-1)!}{2}$). Combinatorial geometry: Number of diagonals in an $n$-sided polygon $= ^n C_2 - n = \\frac{n(n-3)}{2}$.",
            "standard_formulas": r"^n C_r = ^n C_{n-r}, \quad ^n C_r + ^n C_{r-1} = ^{n+1} C_r, \quad \text{Diagonals} = \frac{n(n-3)}{2}, \quad \text{Triangles} = ^n C_3",
            "common_traps": "For necklaces or garlands of $n$ beads, the number of arrangements is $\\frac{(n-1)!}{2}$, NOT $(n-1)!$, because flipping over reverses direction.",
            "tips_and_tricks": "Number of handshakes among $n$ people: $^n C_2 = \\frac{n(n-1)}{2}$."
        }
    ],

    "kcet-binomial-theorem": [
        {
            "name": "General Term, Independent Term & Binomial Coefficients",
            "category": "Binomial Expansion",
            "primary": ["binomial theorem", "general term", "expansion of", "middle term", "term independent of x", "coefficient of x^n", "sum of binomial coefficients"],
            "formula_cues": [r"t_{r+1} = ^n C_r a^{n-r} b^r", r"(x+a)^n = \sum_{r=0}^n ^n C_r x^{n-r} a^r", r"c_0 + c_1 + \dots + c_n = 2^n", r"c_0 + c_2 + c_4 = 2^{n-1}"],
            "secondary": ["expansion", "powers", "terms", "coefficient"],
            "summary": "Binomial expansion: $(a+b)^n = \\sum_{r=0}^n ^n C_r a^{n-r} b^r$. General term $T_{r+1} = ^n C_r a^{n-r} b^r$. Number of terms in expansion of $(a+b)^n$ is $n+1$. Middle term: If $n$ is even, one middle term at $r = n/2$; if $n$ is odd, two middle terms at $r = \\frac{n-1}{2}$ and $r = \\frac{n+1}{2}$. Sum of all coefficients $= 2^n$.",
            "standard_formulas": r"T_{r+1} = ^n C_r x^{n-r} y^r, \quad \sum_{r=0}^n ^n C_r = 2^n, \quad C_0 + C_2 + C_4 + \dots = 2^{n-1}",
            "common_traps": "Remember that $T_{r+1}$ gives the $(r+1)$-th term, so for the 5th term you substitute $r = 4$, not $r = 5$!",
            "tips_and_tricks": "Sum of coefficients of any polynomial expansion $(ax+by)^n$ is obtained immediately by putting $x = 1, y = 1$."
        }
    ],

    "kcet-sequences-and-series": [
        {
            "name": "Arithmetic & Geometric Progressions (AP, GP) & Special Series",
            "category": "Progressions",
            "primary": ["arithmetic progression", "ap", "geometric progression", "gp", "sum of n terms", "infinite gp", "common ratio", "arithmetic mean", "geometric mean", "sum of squares"],
            "formula_cues": [r"t_n = a + (n-1)d", r"s_n = \frac{n}{2}[2a + (n-1)d]", r"t_n = a r^{n-1}", r"s_\infty = \frac{a}{1-r}", r"\sum n^2 = \frac{n(n+1)(2n+1)}{6}"],
            "secondary": ["terms", "ratio", "series", "sum"],
            "summary": "A.P.: $T_n = a + (n-1)d$, $S_n = \\frac{n}{2}[2a + (n-1)d] = \\frac{n}{2}(a + l)$. G.P.: $T_n = a r^{n-1}$, $S_n = \\frac{a(1-r^n)}{1-r}$. Sum of infinite geometric series: $S_\\infty = \\frac{a}{1-r}$ (valid for $|r| < 1$). Sum of first $n$ natural numbers $\\sum n = \\frac{n(n+1)}{2}$; sum of squares $\\sum n^2 = \\frac{n(n+1)(2n+1)}{6}$; sum of cubes $\\sum n^3 = \\left[\\frac{n(n+1)}{2}\\right]^2$.",
            "standard_formulas": r"S_\infty = \frac{a}{1-r} \ (|r| < 1), \quad AM \ge GM \implies \frac{a+b}{2} \ge \sqrt{ab}, \quad \sum n = \frac{n(n+1)}{2}",
            "common_traps": "Infinite GP sum formula $S_\\infty = \\frac{a}{1-r}$ is valid ONLY when common ratio $|r| < 1$.",
            "tips_and_tricks": "For any three positive numbers $a, b, c$: $AM \\ge GM$. Use this inequality to find minimum/maximum values in 10 seconds."
        }
    ],

    "kcet-straight-lines-and-pair-of-straight-lines": [
        {
            "name": "Forms of Straight Line & Distance Formulas",
            "category": "Coordinate Geometry",
            "primary": ["slope of line", "point slope form", "two point form", "intercept form", "normal form", "angle between two lines", "distance of point from line", "distance between parallel lines"],
            "formula_cues": [r"y - y_1 = m(x - x_1)", r"\frac{x}{a} + \frac{y}{b} = 1", r"\tan\\theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|", r"d = \frac{|ax_1 + by_1 + c|}{\sqrt{a^2 + b^2}}", r"d = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}"],
            "secondary": ["lines", "perpendicular", "parallel", "equation"],
            "summary": "Line equations: Slope-intercept $y = mx + c$; Intercept form $\\frac{x}{a} + \\frac{y}{b} = 1$. Angle between lines: $\\tan\\theta = |\\frac{m_1 - m_2}{1 + m_1 m_2}|$. Lines are parallel if $m_1 = m_2$; perpendicular if $m_1 m_2 = -1$. Perpendicular distance from $(x_1, y_1)$ to $ax+by+c=0$: $d = \\frac{|a x_1 + b y_1 + c|}{\\sqrt{a^2 + b^2}}$. Distance between parallel lines: $d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}}$.",
            "standard_formulas": r"m_1 m_2 = -1 \iff L_1 \perp L_2, \quad d = \frac{|ax_1 + by_1 + c|}{\sqrt{a^2+b^2}}, \quad d_{\text{parallel}} = \frac{|c_1 - c_2|}{\sqrt{a^2+b^2}}",
            "common_traps": "Before using the parallel lines distance formula $d = \\frac{|c_1 - c_2|}{\\sqrt{a^2 + b^2}}$, ensure that the coefficients of $x$ and $y$ are made IDENTICAL in both equations!",
            "tips_and_tricks": "Line perpendicular to $ax + by + c = 0$ is simply $bx - ay + k = 0$."
        },
        {
            "name": "Pair of Straight Lines Through Origin",
            "category": "Pair of Lines",
            "primary": ["pair of straight lines", "homogeneous equation", "angle between pair of lines", "perpendicular pair", "coincident lines", "ax^2 + 2hxy + by^2 = 0"],
            "formula_cues": [r"ax^2 + 2hxy + by^2 = 0", r"\tan\\theta = \frac{2\sqrt{h^2 - ab}}{a+b}", r"a + b = 0", r"h^2 = ab"],
            "secondary": ["origin", "lines", "equation"],
            "summary": "Homogeneous equation of second degree $ax^2 + 2hxy + by^2 = 0$ represents two straight lines passing through origin. Angle between them: $\\tan\\theta = \\frac{2\\sqrt{h^2 - ab}}{a+b}$. Lines are perpendicular if $a + b = 0$ (coefficient of $x^2$ + coefficient of $y^2 = 0$). Lines are coincident (parallel) if $h^2 = ab$.",
            "standard_formulas": r"\tan\\theta = \frac{2\sqrt{h^2-ab}}{a+b}, \quad a + b = 0 \iff \text{Lines are perpendicular}, \quad h^2 = ab \iff \text{Lines are coincident}",
            "common_traps": "If $h^2 < ab$, the equation represents imaginary lines intersecting at $(0, 0)$.",
            "tips_and_tricks": "In KCET, if asked whether lines represented by $ax^2 + 2hxy + by^2 = 0$ are perpendicular, just check if $a + b = 0$ in 2 seconds!"
        }
    ],

    "kcet-circle": [
        {
            "name": "Equation of Circle, Center, Radius & Tangents",
            "category": "Conic Sections",
            "primary": ["circle", "center of circle", "radius of circle", "tangent to circle", "intercepts on axes", "length of tangent", "orthogonal circles"],
            "formula_cues": [r"x^2 + y^2 + 2gx + 2fy + c = 0", r"\text{center} = (-g, -f)", r"r = \sqrt{g^2 + f^2 - c}", r"xx_1 + yy_1 = r^2", r"2g_1 g_2 + 2f_1 f_2 = c_1 + c_2"],
            "secondary": ["origin", "radius", "chord"],
            "summary": "General equation of circle: $x^2 + y^2 + 2gx + 2fy + c = 0$. Center is $(-g, -f)$ and radius is $r = \\sqrt{g^2 + f^2 - c}$. Tangent at $(x_1, y_1)$: $x x_1 + y y_1 + g(x+x_1) + f(y+y_1) + c = 0$. Condition for line $y = mx + c$ to be tangent to $x^2+y^2=a^2$: $c^2 = a^2(1+m^2)$. Condition for two circles to cut orthogonally: $2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$.",
            "standard_formulas": r"\text{Center} = (-g, -f), \quad r = \sqrt{g^2+f^2-c}, \quad \text{Condition for Tangency: } c = \pm a\sqrt{1+m^2}",
            "common_traps": "Before calculating center $(-g, -f)$, ensure coefficients of $x^2$ and $y^2$ are reduced to 1!",
            "tips_and_tricks": "Length of tangent from external point $(x_1, y_1)$ to circle $S=0$ is simply $L = \\sqrt{S_1}$."
        }
    ],

    "kcet-parabola": [
        {
            "name": "Parabola: Standard Forms, Focus & Directrix",
            "category": "Conics",
            "primary": ["parabola", "focus of parabola", "directrix", "latus rectum", "vertex", "y^2 = 4ax", "x^2 = 4by", "tangent to parabola"],
            "formula_cues": [r"y^2 = 4ax", r"x^2 = 4by", r"\text{focus} = (a, 0)", r"\text{directrix: } x = -a", r"\text{length of latus rectum} = 4a"],
            "secondary": ["axis", "focal distance", "eccentricity"],
            "summary": "Standard parabola $y^2 = 4ax$: Eccentricity $e = 1$. Vertex $(0, 0)$, Focus $(a, 0)$, Directrix $x = -a$, Axis $y = 0$, Length of latus rectum $= 4a$. Condition for line $y = mx + c$ to be tangent to $y^2 = 4ax$: $c = a/m$.",
            "standard_formulas": r"y^2 = 4ax \implies \text{Focus: } (a, 0), \quad \text{Directrix: } x = -a, \quad \text{Latus Rectum} = 4a, \quad c = \frac{a}{m}",
            "common_traps": "For $x^2 = 4ay$, focus is on the $y$-axis at $(0, a)$ and directrix is horizontal $y = -a$.",
            "tips_and_tricks": "Focal distance of any point $P(x_1, y_1)$ on parabola $y^2 = 4ax$ is simply $x_1 + a$."
        }
    ],

    "kcet-ellipse": [
        {
            "name": "Ellipse: Eccentricity, Foci & Standard Properties",
            "category": "Conics",
            "primary": ["ellipse", "eccentricity of ellipse", "foci of ellipse", "major axis", "minor axis", "directrix of ellipse", "latus rectum of ellipse"],
            "formula_cues": [r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1", r"e = \sqrt{1 - \frac{b^2}{a^2}}", r"\text{foci} = (\pm ae, 0)", r"\text{latus rectum} = \frac{2b^2}{a}"],
            "secondary": ["axes", "coordinates", "distance"],
            "summary": "Standard ellipse $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ ($a > b$): Eccentricity $e = \\sqrt{1 - b^2/a^2} < 1$. Foci $(\\pm ae, 0)$, Directrices $x = \\pm a/e$, Length of major axis $= 2a$, minor axis $= 2b$, Length of latus rectum $= \\frac{2b^2}{a}$. Sum of focal distances of any point is constant: $SP + S'P = 2a$.",
            "standard_formulas": r"e = \sqrt{1 - \frac{b^2}{a^2}}, \quad \text{Foci: } (\pm ae, 0), \quad \text{Latus Rectum} = \frac{2b^2}{a}, \quad SP + S'P = 2a",
            "common_traps": "If $b > a$ (vertical ellipse), major axis is along $y$-axis: $e = \\sqrt{1 - a^2/b^2}$ and foci are $(0, \\pm be)$!",
            "tips_and_tricks": "Distance between foci $= 2ae$; Distance between directrices $= 2a/e$."
        }
    ],

    "kcet-hyperbola": [
        {
            "name": "Hyperbola: Eccentricity, Foci & Rectangular Hyperbola",
            "category": "Conics",
            "primary": ["hyperbola", "eccentricity of hyperbola", "foci of hyperbola", "transverse axis", "conjugate axis", "rectangular hyperbola", "asymptotes"],
            "formula_cues": [r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1", r"e = \sqrt{1 + \frac{b^2}{a^2}}", r"\text{foci} = (\pm ae, 0)", r"\text{latus rectum} = \frac{2b^2}{a}", r"xy = c^2"],
            "secondary": ["curve", "difference of focal distances"],
            "summary": "Standard hyperbola $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$: Eccentricity $e = \\sqrt{1 + b^2/a^2} > 1$. Foci $(\\pm ae, 0)$, Directrices $x = \\pm a/e$, Length of latus rectum $= \\frac{2b^2}{a}$. Rectangular (equilateral) hyperbola $x^2 - y^2 = a^2$ or $xy = c^2$ has eccentricity $e = \\sqrt{2}$ and mutually perpendicular asymptotes.",
            "standard_formulas": r"e = \sqrt{1 + \frac{b^2}{a^2}} > 1, \quad \text{Rectangular Hyperbola: } e = \sqrt{2}, \quad |SP - S'P| = 2a",
            "common_traps": "Eccentricity of a rectangular hyperbola is ALWAYS $\\sqrt{2}$, independent of the value of $a$ or $c$!",
            "tips_and_tricks": "Relation between eccentricities of a hyperbola ($e_1$) and its conjugate hyperbola ($e_2$): $\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1$."
        }
    ],

    "kcet-limits-continuity-and-differentiability": [
        {
            "name": "Limits: L'Hopital's Rule & Standard Trigonometric Limits",
            "category": "Limits",
            "primary": ["limit", "l'hopital", "lhopital", "0/0 form", "infinity/infinity", "standard limit", "sin x / x", "tan x / x", "1 - cos x", "e^x - 1 / x"],
            "formula_cues": [r"\lim_{x \to 0}\frac{\\sin x}{x} = 1", r"\lim_{x \to 0}\frac{\tan x}{x} = 1", r"\lim_{x \to 0}\frac{1-\\cos x}{x^2} = \frac{1}{2}", r"\lim_{x \to a}\frac{x^n - a^n}{x - a} = n a^{n-1}"],
            "secondary": ["evaluating", "approaches", "indeterminate"],
            "summary": "Evaluation of limits in indeterminate forms ($0/0, \\infty/\\infty$) using L'Hôpital's Rule (differentiate numerator and denominator separately). Standard limits: $\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1$, $\\lim_{x \\to 0} \\frac{\\tan x}{x} = 1$, $\\lim_{x \\to 0} \\frac{1-\\cos x}{x^2} = \\frac{1}{2}$, $\\lim_{x \\to 0} (1+x)^{1/x} = e$, $\\lim_{x \\to 0} \\frac{a^x - 1}{x} = \\ln a$.",
            "standard_formulas": r"\lim_{x \to 0}\frac{\\sin x}{x} = 1, \quad \lim_{x \to 0}\frac{1-\\cos x}{x^2} = \frac{1}{2}, \quad \lim_{x \to 0}\frac{e^x - 1}{x} = 1, \quad \lim_{x \to \infty}\left(1 + \frac{1}{x}\right)^x = e",
            "common_traps": "L'Hôpital's Rule applies ONLY to indeterminate forms $0/0$ and $\\infty/\\infty$; check form before differentiating!",
            "tips_and_tricks": "In KCET, for $(1)^\\infty$ forms: $\\lim_{x \\to a} [f(x)]^{g(x)} = e^{\\lim_{x \\to a} g(x)[f(x) - 1]}$."
        },
        {
            "name": "Continuity & Differentiability at a Point",
            "category": "Continuity & Analysis",
            "primary": ["continuous at x =", "discontinuous", "left hand limit", "right hand limit", "find value of k", "differentiable at x =", "modulus function", "greatest integer function"],
            "formula_cues": [r"\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = f(c)", r"f'(c) = \lim_{h \to 0}\frac{f(c+h)-f(c)}{h}", r"|x|", r"[x]"],
            "secondary": ["continuity", "smooth", "sharp corner"],
            "summary": "A function $f(x)$ is continuous at $x=c$ if $\\text{LHL} = \\text{RHL} = f(c)$. Differentiability: $f'(c)$ exists if $\\text{LHD} = \\text{RHD}$. Fundamental theorem: Every differentiable function is continuous, but the converse is NOT true (e.g. $f(x) = |x|$ is continuous at $x=0$ but not differentiable due to sharp corner). Greatest integer function $[x]$ is discontinuous at all integers.",
            "standard_formulas": r"\text{Continuity: } \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = f(c), \quad \text{Differentiability} \implies \text{Continuity}",
            "common_traps": "Finding constant $k$ so $f(x)$ is continuous: simply equate the expressions of the two branches at the junction point and solve for $k$!",
            "tips_and_tricks": "Polynomial, exponential, sine, and cosine functions are continuous and differentiable everywhere on $\\mathbb{R}$."
        }
    ],

    "kcet-application-of-derivatives": [
        {
            "name": "Rate of Change, Tangents & Normals",
            "category": "Derivatives Applications",
            "primary": ["rate of change", "radius increasing at rate", "volume increasing", "slope of tangent", "slope of normal", "equation of tangent", "equation of normal", "orthogonal curves"],
            "formula_cues": [r"\frac{dv}{dt} = 4\pi r^2 \frac{dr}{dt}", r"m = \left(\frac{dy}{dx}\right)_{(x_1, y_1)}", r"m_{\text{normal}} = -\frac{1}{dy/dx}", r"y - y_1 = m(x - x_1)"],
            "secondary": ["seconds", "surface area", "curve", "perpendicular"],
            "summary": "Rate of change $\\frac{dy}{dt} = \\frac{dy}{dx} \\frac{dx}{dt}$. Slope of tangent to $y=f(x)$ at $(x_1, y_1)$ is $m = f'(x_1)$; equation is $y - y_1 = m(x - x_1)$. Slope of normal is $-1/m$; equation is $y - y_1 = -\\frac{1}{m}(x - x_1)$. Two curves cut orthogonally if $m_1 m_2 = -1$.",
            "standard_formulas": r"\text{Slope of Tangent: } m = \frac{dy}{dx}, \quad \text{Slope of Normal: } m_n = -\frac{1}{dy/dx}, \quad m_1 m_2 = -1",
            "common_traps": "When normal is parallel to $x$-axis, its slope is 0, which means $\\frac{dx}{dy} = 0$ or $\\frac{dy}{dx} \\to \\infty$!",
            "tips_and_tricks": "For sphere: $V = \\frac{4}{3}\\pi r^3 \\implies \\frac{dV}{dt} = 4\\pi r^2 \\frac{dr}{dt} = S \\frac{dr}{dt}$."
        },
        {
            "name": "Increasing/Decreasing Functions & Maxima / Minima",
            "category": "Optimization",
            "primary": ["increasing function", "decreasing function", "strictly increasing", "strictly decreasing", "maximum value", "minimum value", "local maxima", "local minima", "first derivative test", "second derivative test"],
            "formula_cues": [r"f'(x) > 0", r"f'(x) < 0", r"f'(x) = 0", r"f''(x) < 0 \ (\text{maxima})", r"f''(x) > 0 \ (\text{minima})"],
            "secondary": ["interval", "critical points", "turning point"],
            "summary": "Monotonicity: $f(x)$ is strictly increasing in $(a, b)$ if $f'(x) > 0$; strictly decreasing if $f'(x) < 0$. Maxima/Minima: Critical points where $f'(x) = 0$. Second derivative test: If $f'(c) = 0$ and $f''(c) < 0$, then $x=c$ is a point of local maximum; if $f''(c) > 0$, it is a local minimum. If $f''(c) = 0$, test fails $\\implies$ use first derivative test.",
            "standard_formulas": r"\text{Increasing: } f'(x) \ge 0, \quad \text{Decreasing: } f'(x) \le 0, \quad \text{Maxima: } f'(c)=0 \land f''(c)<0",
            "common_traps": "Absolute maximum and minimum of a continuous function on a closed interval $[a, b]$ can occur at CRITICAL POINTS or at the ENDPOINTS $a$ and $b$!",
            "tips_and_tricks": "To find intervals of increase/decrease, find roots of $f'(x) = 0$ and apply the wavy curve method on the number line."
        }
    ],

    "kcet-area-under-the-curves": [
        {
            "name": "Area Under Curves & Between Intersecting Parabolas",
            "category": "Integral Applications",
            "primary": ["area of the region", "area bounded by", "parabola and line", "between curves", "y^2 = 4ax", "x^2 = 4by", "area enclosed", "coordinates axes"],
            "formula_cues": [r"\text{area} = \int_a^b y dx", r"\text{area} = \frac{16ab}{3}", r"\text{area} = \frac{8a^2}{3m^3}", r"\text{area} = \pi a b"],
            "secondary": ["quadrant", "limits", "bounded"],
            "summary": "Area bounded by curve $y = f(x)$, $x$-axis and lines $x=a, x=b$: $A = \\int_a^b y dx$. Area enclosed between two parabolas $y^2 = 4ax$ and $x^2 = 4by$ is directly $\\frac{16ab}{3}$. Area between parabola $y^2 = 4ax$ and line $y = mx$ is $\\frac{8a^2}{3m^3}$. Area of ellipse $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ is $\\pi ab$.",
            "standard_formulas": r"\text{Area between } y^2=4ax \text{ and } x^2=4by = \frac{16ab}{3}, \quad \text{Area between } y^2=4ax \text{ and } y=mx = \frac{8a^2}{3m^3}",
            "common_traps": "If the region falls below the $x$-axis ($y < 0$), the integral gives a negative value; area is always positive, so take the absolute value $|\\int y dx|$!",
            "tips_and_tricks": "Memorize the standard KCET shortcuts: (1) Area between $y^2=4ax$ and $x^2=4ay$ is $\\frac{16a^2}{3}$. (2) Area between $y^2=4ax$ and $y=mx$ is $\\frac{8a^2}{3m^3}$. Solves the problem in 5 seconds."
        }
    ],

    "kcet-differential-equations": [
        {
            "name": "Order, Degree & Variable Separable Method",
            "category": "Differential Equations",
            "primary": ["order of differential equation", "degree of differential", "degree is not defined", "variable separable", "general solution", "particular solution", "formation of differential equation"],
            "formula_cues": [r"\frac{dy}{dx} = f(x)g(y)", r"\int \frac{dy}{g(y)} = \int f(x)dx + c", r"\text{order} = 2, \text{degree} = 1"],
            "secondary": ["derivative", "equation", "arbitrary constants"],
            "summary": "Order: highest order derivative occurring in the equation. Degree: power of the highest order derivative when the equation is expressed as a polynomial in derivatives (if $\\sin(dy/dx)$ or $e^{dy/dx}$ is present, degree is NOT defined). Method of Separation of Variables: $\\frac{dy}{dx} = f(x)g(y) \\implies \\int \\frac{dy}{g(y)} = \\int f(x)dx + C$.",
            "standard_formulas": r"\text{Order: Highest derivative order}, \quad \text{Degree: Power of highest derivative when polynomial in derivatives}",
            "common_traps": "For an equation like $\\frac{d^2y}{dx^2} + \\sin\\left(\\frac{dy}{dx}\\right) = 0$, the ORDER is 2, but DEGREE IS NOT DEFINED!",
            "tips_and_tricks": "The number of arbitrary constants in the general solution of an $n$-th order differential equation is $n$. In a PARTICULAR solution, the number of arbitrary constants is always ZERO."
        },
        {
            "name": "Linear Differential Equations & Integrating Factor",
            "category": "Linear Equations",
            "primary": ["linear differential equation", "integrating factor", "if", "dy/dx + py = q", "dx/dy + px = q", "solution of linear"],
            "formula_cues": [r"\frac{dy}{dx} + P y = Q", r"\text{I.F.} = e^{\int P dx}", r"y \cdot \text{I.F.} = \int (Q \cdot \text{I.F.}) dx + C", r"\text{I.F.} = e^{\int P dy}"],
            "secondary": ["differential", "equation", "solution"],
            "summary": "First-order Linear Differential Equation in $y$: $\\frac{dy}{dx} + P(x) y = Q(x)$. Integrating Factor $\\text{I.F.} = e^{\\int P dx}$. General solution: $y \\cdot (\\text{I.F.}) = \\int Q \\cdot (\\text{I.F.}) dx + C$. If linear in $x$: $\\frac{dx}{dy} + P(y) x = Q(y) \\implies \\text{I.F.} = e^{\\int P dy}$, solution $x \\cdot (\\text{I.F.}) = \\int Q \\cdot (\\text{I.F.}) dy + C$.",
            "standard_formulas": r"\text{I.F.} = e^{\int P dx}, \quad y \cdot e^{\int P dx} = \int Q \cdot e^{\int P dx} dx + C, \quad e^{\ln f(x)} = f(x)",
            "common_traps": "Watch for the leading coefficient of $\\frac{dy}{dx}$: If written as $x\\frac{dy}{dx} + y = Q$, divide through by $x$ first to put it in standard form $\\frac{dy}{dx} + \\frac{1}{x}y = \\frac{Q}{x}$!",
            "tips_and_tricks": "Remember the log-exponential simplification: $\\text{I.F.} = e^{\\int \\frac{2}{x}dx} = e^{2\\ln x} = e^{\\ln(x^2)} = x^2$."
        }
    ],

    "kcet-matrices-and-determinants": [
        {
            "name": "Matrix Algebra: Transpose, Symmetric & Skew-Symmetric",
            "category": "Matrices",
            "primary": ["matrix multiplication", "transpose of matrix", "symmetric matrix", "skew symmetric matrix", "orthogonal matrix", "diagonal elements", "a = a^t", "a = -a^t"],
            "formula_cues": [r"a^t = a", r"a^t = -a", r"(a b)^t = b^t a^t", r"a_{ii} = 0"],
            "secondary": ["order", "square matrix", "elements"],
            "summary": "Matrix operations: Matrix multiplication is non-commutative ($AB \\ne BA$). Transpose properties: $(AB)^T = B^T A^T$. Symmetric matrix: $A^T = A$ ($a_{ij} = a_{ji}$). Skew-symmetric matrix: $A^T = -A$ ($a_{ij} = -a_{ji}$). All diagonal elements of a skew-symmetric matrix are strictly ZERO ($a_{ii} = 0$). Any square matrix $A$ can be uniquely decomposed as $A = \\frac{A+A^T}{2} + \\frac{A-A^T}{2}$ (symmetric + skew-symmetric).",
            "standard_formulas": r"(AB)^T = B^T A^T, \quad A = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T), \quad \text{Skew-symmetric: } a_{ii} = 0",
            "common_traps": "The determinant of an odd-order skew-symmetric matrix is ALWAYS zero: $|A| = 0$!",
            "tips_and_tricks": "If $A$ is an idempotent matrix ($A^2 = A$), then $(I+A)^n = I + (2^n - 1)A$."
        },
        {
            "name": "Determinants, Adjoint, Inverse & System of Equations",
            "category": "Determinants & Systems",
            "primary": ["determinant", "properties of determinants", "adjoint of matrix", "adj a", "inverse of matrix", "a^{-1}", "singular matrix", "cramer's rule", "consistent system", "unique solution", "infinite solutions"],
            "formula_cues": [r"|a^t| = |a|", r"|k a| = k^n |a|", r"|\text{adj } a| = |a|^{n-1}", r"a \cdot (\text{adj } a) = |a| i", r"a^{-1} = \frac{\text{adj } a}{|a|}"],
            "secondary": ["rows", "columns", "determinant value"],
            "summary": "Determinant properties: $|k A| = k^n |A|$ for $n \\times n$ matrix. Adjoint properties: $A \\cdot (\\text{adj } A) = |A| I$; $|\\text{adj } A| = |A|^{n-1}$; $|\\text{adj}(\\text{adj } A)| = |A|^{(n-1)^2}$; $\\text{adj}(AB) = \\text{adj}(B) \\cdot \\text{adj}(A)$. Inverse: $A^{-1} = \\frac{\\text{adj } A}{|A|}$ exists if and only if $|A| \\ne 0$ (non-singular). System $AX = B$: Unique solution if $|A| \\ne 0$; no solution (inconsistent) if $|A|=0$ and $(\\text{adj } A)B \\ne 0$.",
            "standard_formulas": r"|kA| = k^n |A|, \quad |\text{adj } A| = |A|^{n-1}, \quad A^{-1} = \frac{\text{adj } A}{|A|}, \quad |\text{adj}(\text{adj } A)| = |A|^{(n-1)^2}",
            "common_traps": "For $3 \\times 3$ matrix ($n=3$): $|2A| = 2^3 |A| = 8|A|$, NOT $2|A|$! And $|\\text{adj } A| = |A|^{3-1} = |A|^2$!",
            "tips_and_tricks": "Shortcut for $2 \\times 2$ matrix inverse: Swap diagonal elements, change signs of off-diagonal elements, divide by $|A|$."
        }
    ],

    "kcet-inverse-trigonometric-functions": [
        {
            "name": "Principal Value Branches, Domains & Standard Identities",
            "category": "Inverse Trigonometry",
            "primary": ["principal value", "domain and range", "sin^{-1}", "cos^{-1}", "tan^{-1}", "cot^{-1}", "sec^{-1}", "cosec^{-1}", "principal branch"],
            "formula_cues": [r"\\sin^{-1}x \in [-\pi/2, \pi/2]", r"\\cos^{-1}x \in [0, \pi]", r"\tan^{-1}x \in (-\pi/2, \pi/2)", r"\\sin^{-1}x + \\cos^{-1}x = \frac{\pi}{2}", r"\tan^{-1}x + \cot^{-1}x = \frac{\pi}{2}"],
            "secondary": ["angles", "radians", "value"],
            "summary": "Principal value branches: $\\sin^{-1}x \\in [-\\pi/2, \\pi/2]$; $\\cos^{-1}x \\in [0, \\pi]$; $\\tan^{-1}x \\in (-\\pi/2, \\pi/2)$. Negative arguments: $\\sin^{-1}(-x) = -\\sin^{-1}x$, $\\cos^{-1}(-x) = \\pi - \\cos^{-1}x$, $\\tan^{-1}(-x) = -\\tan^{-1}x$. Fundamental co-function identities: $\\sin^{-1}x + \\cos^{-1}x = \\pi/2$, $\\tan^{-1}x + \\cot^{-1}x = \\pi/2$, $\\sec^{-1}x + \\text{cosec}^{-1}x = \\pi/2$.",
            "standard_formulas": r"\\sin^{-1}x + \\cos^{-1}x = \frac{\pi}{2}, \quad \\cos^{-1}(-x) = \pi - \\cos^{-1}x, \quad \tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x+y}{1-xy}",
            "common_traps": "$\\cos^{-1}(-1/2) = \\pi - \\pi/3 = 2\\pi/3$, NOT $-\\pi/3$!",
            "tips_and_tricks": "If $\\tan^{-1}x + \\tan^{-1}y + \\tan^{-1}z = \\pi$, then $x + y + z = xyz$."
        }
    ],

    "kcet-three-dimensional-geometry": [
        {
            "name": "Direction Cosines, Direction Ratios & Lines in 3D",
            "category": "3D Geometry",
            "primary": ["direction cosines", "direction ratios", "l^2 + m^2 + n^2 = 1", "equation of line in 3d", "vector equation", "cartesian equation", "angle between lines", "shortest distance between skew lines"],
            "formula_cues": [r"l^2 + m^2 + n^2 = 1", r"\\cos^2\alpha + \\cos^2\beta + \\cos^2\gamma = 1", r"\\sin^2\alpha + \\sin^2\beta + \\sin^2\gamma = 2", r"d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}"],
            "secondary": ["parallel", "perpendicular", "skew lines"],
            "summary": "Direction cosines $(l, m, n)$: $\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$ and $\\sin^2\\alpha + \\sin^2\\beta + \\sin^2\\gamma = 2$. Two lines with direction ratios $(a_1, b_1, c_1)$ and $(a_2, b_2, c_2)$ are perpendicular if $a_1 a_2 + b_1 b_2 + c_1 c_2 = 0$; parallel if $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$. Shortest distance between skew lines $\\vec{r} = \\vec{a}_1 + \\lambda\\vec{b}_1$ and $\\vec{r} = \\vec{a}_2 + \\mu\\vec{b}_2$: $d = \\frac{|(\\vec{a}_2 - \\vec{a}_1) \\cdot (\\vec{b}_1 \\times \\vec{b}_2)|}{|\\vec{b}_1 \\times \\vec{b}_2|}$.",
            "standard_formulas": r"l^2 + m^2 + n^2 = 1, \quad a_1 a_2 + b_1 b_2 + c_1 c_2 = 0 \iff L_1 \perp L_2, \quad d_{\text{skew}} = \frac{|(\vec{a}_2-\vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}",
            "common_traps": "Direction cosines must satisfy $l^2 + m^2 + n^2 = 1$, whereas direction ratios $(a, b, c)$ can be any proportional numbers ($l = \\frac{a}{\\sqrt{a^2+b^2+c^2}}$).",
            "tips_and_tricks": "Lines intersect if and only if the shortest distance between them is zero: $(\\vec{a}_2 - \\vec{a}_1) \\cdot (\\vec{b}_1 \\times \\vec{b}_2) = 0$."
        },
        {
            "name": "Planes in 3D & Line-Plane Intersections",
            "category": "Planes",
            "primary": ["equation of plane", "intercept form of plane", "normal to plane", "angle between planes", "distance of point from plane", "angle between line and plane", "coplanar lines"],
            "formula_cues": [r"ax + by + cz + d = 0", r"\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1", r"d = \frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2 + b^2 + c^2}}", r"\\sin\\theta = \frac{|\vec{b} \cdot \vec{n}|}{|\vec{b}||\vec{n}|}"],
            "secondary": ["plane", "normal", "perpendicular distance"],
            "summary": "General equation of plane: $ax + by + cz + d = 0$ where $(a, b, c)$ are direction ratios of normal to plane. Perpendicular distance of point $(x_1, y_1, z_1)$ from plane: $d = \\frac{|a x_1 + b y_1 + c z_1 + d|}{\\sqrt{a^2+b^2+c^2}}$. Angle $\\theta$ between line with direction $\\vec{b}$ and plane with normal $\\vec{n}$: $\\sin\\theta = \\frac{|\\vec{b} \\cdot \\vec{n}|}{|\\vec{b}||\\vec{n}|}$.",
            "standard_formulas": r"d = \frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2+b^2+c^2}}, \quad \text{Line } \\parallel \text{ Plane} \iff \vec{b} \cdot \vec{n} = 0, \quad \text{Line } \perp \text{ Plane} \iff \vec{b} \parallel \vec{n}",
            "common_traps": "Angle between LINE and PLANE uses SINE ($\\sin\\theta = \\frac{\\vec{b} \\cdot \\vec{n}}{|\\vec{b}||\\vec{n}|}$), NOT cosine, because the angle is measured from the plane surface, not the normal!",
            "tips_and_tricks": "Two parallel planes $ax + by + cz + d_1 = 0$ and $ax + by + cz + d_2 = 0$ have perpendicular distance $d = \\frac{|d_1 - d_2|}{\\sqrt{a^2+b^2+c^2}}$."
        }
    ],

    "kcet-probability": [
        {
            "name": "Conditional Probability, Multiplication Rule & Independence",
            "category": "Conditional Probability",
            "primary": ["conditional probability", "p(a|b)", "multiplication theorem", "independent events", "mutually exclusive", r"p(a \cap b)", r"p(a \cup b)", "cards", "dice"],
            "formula_cues": [r"p(a|b) = \frac{p(a \\cap b)}{p(b)}", r"p(a \\cap b) = p(a) \cdot p(b)", r"p(a \cup b) = p(a) + p(b) - p(a \\cap b)"],
            "secondary": ["events", "probability", "sample space"],
            "summary": "Conditional probability $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ ($P(B) > 0$). Independent events: Occurrence of $A$ does not affect $B$; condition for independence is $P(A \\cap B) = P(A) \\cdot P(B)$. Mutually exclusive events: cannot occur simultaneously $\\implies P(A \\cap B) = 0$.",
            "standard_formulas": r"P(A|B) = \frac{P(A \\cap B)}{P(B)}, \quad \text{Independent: } P(A \\cap B) = P(A) \cdot P(B), \quad P(A' \\cap B') = [1 - P(A)][1 - P(B)]",
            "common_traps": "Mutually exclusive events with non-zero probabilities can NEVER be independent because $P(A \\cap B) = 0 \\ne P(A)P(B)$!",
            "tips_and_tricks": "If $A$ and $B$ are independent, then $A'$ and $B'$ are also independent: $P(A' \\cap B') = P(A') P(B') = (1-P(A))(1-P(B))$."
        },
        {
            "name": "Bayes' Theorem & Binomial Distribution",
            "category": "Distributions & Inference",
            "primary": ["bayes' theorem", "total probability theorem", "reverse probability", "random variable", "probability distribution", "mean of random variable", "variance of random variable", "binomial distribution", "bernoulli trials"],
            "formula_cues": [r"p(e_i|a) = \frac{p(e_i)p(a|e_i)}{\sum p(e_j)p(a|e_j)}", r"p(x=k) = ^n C_k p^k q^{n-k}", r"\mu = n p", r"\sigma^2 = n p q"],
            "secondary": ["trials", "success", "failure", "coin tossed"],
            "summary": r"Bayes' Theorem for posterior probability: $P(E_i|A) = \frac{P(E_i)P(A|E_i)}{\sum P(E_j)P(A|E_j)}$. Binomial distribution $B(n, p)$: $P(X = k) = ^n C_k p^k q^{n-k}$ ($q = 1-p$). Mean $\mu = np$; Variance $\sigma^2 = npq$; Standard deviation $\sigma = \sqrt{npq}$. Since $q < 1$, the variance of a binomial distribution is ALWAYS strictly less than its mean ($\sigma^2 < \mu$).",
            "standard_formulas": r"P(X=k) = ^n C_k p^k q^{n-k}, \quad \text{Mean } = np, \quad \text{Variance } = npq \ (\text{Variance} < \text{Mean})",
            "common_traps": "In binomial distribution, variance can NEVER exceed the mean ($npq < np$ always because $q < 1$). If given a problem where variance > mean, that distribution is impossible!",
            "tips_and_tricks": "Probability of at least one success in $n$ trials: $P(X \\ge 1) = 1 - P(X = 0) = 1 - q^n$."
        }
    ],

    "kcet-statistics": [
        {
            "name": "Mean, Variance, Standard Deviation & Coefficient of Variation",
            "category": "Statistics",
            "primary": ["variance", "standard deviation", "mean", "coefficient of variation", "cv", "sigma^2", "dispersion", "each observation multiplied", "each observation increased"],
            "formula_cues": [r"\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n} = \frac{\sum x_i^2}{n} - (\bar{x})^2", r"\sigma = \sqrt{\text{variance}}", r"\text{c.v.} = \frac{\sigma}{\bar{x}} \times 100"],
            "secondary": ["data", "observations", "scatter"],
            "summary": "Variance $\\sigma^2 = \\frac{\\sum x_i^2}{n} - (\\bar{x})^2$. Standard deviation $\\sigma = \\sqrt{\\text{Variance}}$. Coefficient of variation $\\text{C.V.} = \\frac{\\sigma}{\\bar{x}} \\times 100$ (measures relative variability; series with smaller C.V. is more consistent). Shift of origin: Adding/subtracting a constant $k$ to each observation changes mean by $\\pm k$, but leaves variance and standard deviation completely UNCHANGED. Change of scale: Multiplying each observation by $k$ multiplies mean by $k$, standard deviation by $|k|$, and variance by $k^2$.",
            "standard_formulas": r"\sigma^2 = \frac{\sum x_i^2}{n} - (\bar{x})^2, \quad \text{New Variance after } \times k = k^2 \sigma^2, \quad \text{C.V.} = \frac{\sigma}{\bar{x}} \times 100",
            "common_traps": "Adding or subtracting a number to all observations has ZERO effect on standard deviation and variance!",
            "tips_and_tricks": "Variance of first $n$ natural numbers: $\\sigma^2 = \\frac{n^2 - 1}{12}$. A classic 5-second question in KCET."
        }
    ],

    "kcet-mathematical-reasoning": [
        {
            "name": "Logical Statements, Connectives, Contrapositive & Tautology",
            "category": "Mathematical Logic",
            "primary": ["negation", "contrapositive", "converse", "inverse", "tautology", "contradiction", "truth table", "conditional statement", "p implies q"],
            "formula_cues": [r"\sim p", r"p \land q", r"p \lor q", r"p \implies q", r"\sim q \implies \sim p", r"\sim(p \implies q) \equiv p \land \sim q"],
            "secondary": ["statement", "implication", "logic"],
            "summary": "Logical statements and truth values: Negation ($\\sim p$), Conjunction ($p \\land q$, true only if both true), Disjunction ($p \\lor q$, false only if both false). Conditional $p \\implies q \\equiv \\sim p \\lor q$. Its Contrapositive is $\\sim q \\implies \\sim p$ (logically equivalent to $p \\implies q$). Converse is $q \\implies p$; Inverse is $\\sim p \\implies \\sim q$. Negation of conditional: $\\sim(p \\implies q) \\equiv p \\land \\sim q$. Tautology: always true; Contradiction: always false.",
            "standard_formulas": r"\text{Contrapositive of } (p \implies q) \equiv (\sim q \implies \sim p), \quad \sim(p \implies q) \equiv p \land \sim q, \quad \sim(p \lor q) \equiv \sim p \land \sim q",
            "common_traps": "The contrapositive of 'If $p$, then $q$' is 'If NOT $q$, then NOT $p$'. It is logically equivalent to the original statement, unlike converse or inverse!",
            "tips_and_tricks": "To find contrapositive in English: Swap the 'if' and 'then' clauses and negate both."
        }
    ],

    "kcet-logarithms": [
        {
            "name": "Laws of Logarithms & Exponential Equations",
            "category": "Logarithms",
            "primary": ["logarithm", "base change rule", "log a + log b", "log a - log b", "characteristic and mantissa", "exponential equation", "domain of log"],
            "formula_cues": [r"\log_b a = \frac{\log a}{\log b}", r"\log(xy) = \log x + \log y", r"\log(x/y) = \log x - \log y", r"\log_b(a^k) = k\log_b a", r"a^{\log_a x} = x"],
            "secondary": ["base", "positive real", "power"],
            "summary": "Laws of logarithms: $\\log_b(xy) = \\log_b x + \\log_b y$; $\\log_b(x/y) = \\log_b x - \\log_b y$; $\\log_b(x^k) = k\\log_b x$. Base change rule: $\\log_b a = \\frac{\\log_c a}{\\log_c b} = \\frac{1}{\\log_a b}$. Identity: $a^{\\log_a x} = x$. Domain of $\\log_b x$: $x > 0$, $b > 0$, and $b \\ne 1$.",
            "standard_formulas": r"\log_b a = \frac{\ln a}{\ln b} = \frac{1}{\log_a b}, \quad a^{\log_a x} = x, \quad \log_b(x^k) = k\log_b x",
            "common_traps": "Logarithm is undefined for non-positive numbers ($x \\le 0$) and base cannot be 1 ($b \\ne 1$).",
            "tips_and_tricks": "Product property shortcut: $\\log_b a \\cdot \\log_c b \\cdot \\log_d c = \\log_d a$."
        }
    ],
    # ==========================================
    # SPECIAL KCET SPECIFIC CHAPTERS
    # ==========================================
    "kcet-linear-programming": [   {   'category': 'Core Principle',
        'common_traps': 'If the feasible region is unbounded, the minimum or maximum value of $Z$ may not exist unless '
                        'the open half-plane has no common points with the feasible region.',
        'formula_cues': ['z = ax + by', 'z=px+qy', 'x \\ge 0', 'y \\ge 0', 'x+y \\le'],
        'name': 'Objective Function, Constraints & Feasible Region',
        'primary': [   'feasible region',
                       'constraints',
                       'objective function',
                       'linear inequalities',
                       'non-negative',
                       'unbounded',
                       'bounded region',
                       'infeasible'],
        'secondary': ['region', 'linear', 'inequality', 'statement'],
        'standard_formulas': 'Z = ax + by, \\quad \\text{Feasible Region: Intersection of all half-planes determined '
                             'by constraints}',
        'summary': 'Formulation of LPP: linear objective function $Z = ax + by$, linear constraints, non-negative '
                   'restrictions $x, y \\ge 0$, and identification of bounded vs unbounded feasible regions.',
        'tips_and_tricks': 'In KCET, sketch the constraint boundary lines quickly using intercept form $\\frac{x}{a} + '
                           '\\frac{y}{b} = 1$.'},
    {   'category': 'Optimization Archetypes',
        'common_traps': 'Assuming optimal solution is only at integer points—fractional coordinates of corner points '
                        'are valid.',
        'formula_cues': ['z = 3x+4y', 'max z', 'min z', '(0, 10)', '(15, 15)'],
        'name': 'Corner Point Theorem & Optimal Solutions',
        'primary': [   'corner point',
                       'corner points',
                       'maximum value of z',
                       'minimum value of z',
                       'optimal',
                       'same maximum value',
                       'infinite number of points',
                       'line segment'],
        'secondary': ['vertices', 'evaluate', 'value of z', 'points'],
        'standard_formulas': '\\text{If } Z(A) = Z(B) = Z_{\\max}, \\text{ then } Z \\text{ is maximized at all points '
                             'on segment } AB',
        'summary': 'Corner Point Method: If an optimal value exists, it occurs at a vertex. If the maximum/minimum '
                   'occurs at two distinct corner points, it attains the same optimal value at every point along the '
                   'line segment joining them.',
        'tips_and_tricks': 'When $Z = px + qy$ attains the same maximum at $(x_1, y_1)$ and $(x_2, y_2)$, equate $p '
                           'x_1 + q y_1 = p x_2 + q y_2$ to find $p/q$ directly.'}],

    "kcet-differentiation": [   {   'category': 'Differentiation Techniques',
        'common_traps': 'Check the given interval of $x$ before writing the simplified inverse trigonometric form.',
        'formula_cues': [   '\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)',
                            '\\cos^{-1}(4x^3-3x)',
                            '\\cos^{-1}(2x^2-1)',
                            '\\tan^{-1}\\left(\\frac{3x-x^3}{1-3x^2}\\right)'],
        'name': 'Standard Derivatives & Inverse Trigonometric Substitutions',
        'primary': [   'derivative of',
                       'sin^{-1}',
                       'cos^{-1}',
                       'tan^{-1}',
                       'substitution',
                       'with respect to',
                       "f'(x)",
                       "f'(1/2)",
                       'chain rule'],
        'secondary': ['differentiate', 'function', 'angle'],
        'standard_formulas': '\\frac{d}{dx}[\\sin^{-1}\\frac{2x}{1+x^2}] = \\frac{2}{1+x^2}, \\quad '
                             '\\frac{d}{dx}[\\cos^{-1}(4x^3-3x)] = -\\frac{3}{\\sqrt{1-x^2}}',
        'summary': 'Differentiation of composite functions and inverse trigonometric forms using standard '
                   'substitutions: $x = \\tan\\theta$ for $\\sin^{-1}\\frac{2x}{1+x^2} = 2\\tan^{-1}x$; $x = '
                   '\\cos\\theta$ for $\\cos^{-1}(2x^2-1) = 2\\cos^{-1}x$ and $\\cos^{-1}(4x^3-3x) = 3\\cos^{-1}x$.',
        'tips_and_tricks': 'Derivative of $u(x)$ with respect to $v(x)$ is simply $\\frac{du/dx}{dv/dx}$.'},
    {   'category': 'Advanced Calculus',
        'common_traps': 'For parametric second derivatives, remember the final chain rule step $\\times '
                        '\\frac{dt}{dx}$!',
        'formula_cues': ['\\frac{dy}{dx}', '\\frac{d^2y}{dx^2}', 'x\\frac{dy}{dx} = y', 'y^3 = \\tan x + y', '(x+y)^n'],
        'name': 'Implicit, Logarithmic & Higher Order Derivatives',
        'primary': [   'second order derivative',
                       'd^2y/dx^2',
                       'implicit differentiation',
                       'logarithmic differentiation',
                       'dy/dx',
                       'y =',
                       'x dy/dx - y = 0',
                       'infinite root series'],
        'secondary': ['take log', 'cube both sides', 'with respect to x'],
        'standard_formulas': '\\frac{d}{dx}[u^v] = u^v \\left[\\frac{v}{u}\\frac{du}{dx} + \\ln u '
                             '\\frac{dv}{dx}\\right], \\quad \\frac{d^2y}{dx^2} = \\frac{\\frac{d}{dt}(dy/dx)}{dx/dt}',
        'summary': 'Implicit differentiation: differentiate both sides with respect to $x$. Logarithmic '
                   'differentiation for $y = f(x)^{g(x)}$ or products/quotients. Second order derivatives '
                   '$\\frac{d^2y}{dx^2}$. For parametric equations $x = f(t), y = g(t)$, $\\frac{d^2y}{dx^2} = '
                   '\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right) \\frac{1}{dx/dt}$.',
        'tips_and_tricks': 'For homogeneous implicit equations $x^p y^q = (x+y)^{p+q}$, $\\frac{dy}{dx} = '
                           '\\frac{y}{x}$, and $\\frac{d^2y}{dx^2} = 0$.'}],

    "kcet-indefinite-integration": [   {   'category': 'Integration Methods',
        'common_traps': 'Forgetting the factor $1/a$ in $\\frac{1}{a}\\tan^{-1}\\frac{x}{a}$, or adding $1/a$ to '
                        '$\\sin^{-1}\\frac{x}{a}$.',
        'formula_cues': [   '\\int \\frac{dx}{x^2 + a^2}',
                            '\\int \\frac{dx}{\\sqrt{a^2 - x^2}}',
                            "\\int f'(x)[f(x)]^n dx",
                            "\\int \\frac{f'(x)}{f(x)} dx"],
        'name': 'Integration by Substitution & Standard Integrals',
        'primary': [   'substitute',
                       'indefinite integral',
                       'evaluate',
                       'int',
                       'dx',
                       'standard form',
                       'sec^2',
                       'sin x',
                       'cos x'],
        'secondary': ['function', 'constant of integration', 'c'],
        'standard_formulas': "\\int \\frac{f'(x)}{f(x)}dx = \\ln|f(x)| + C, \\quad \\int \\frac{dx}{x^2+a^2} = "
                             '\\frac{1}{a}\\tan^{-1}\\frac{x}{a} + C',
        'summary': "Method of substitution: $\\int f(g(x))g'(x)dx = \\int f(u)du$. Standard algebraic and "
                   'trigonometric forms: $\\int \\frac{dx}{x^2+a^2} = \\frac{1}{a}\\tan^{-1}\\frac{x}{a}$, $\\int '
                   "\\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a}$, $\\int \\frac{f'(x)}{f(x)}dx = \\ln|f(x)|$.",
        'tips_and_tricks': "For $\\int e^x [f(x) + f'(x)] dx$, the answer is immediately $e^x f(x) + C$."},
    {   'category': 'Advanced Integration',
        'common_traps': 'Applying partial fractions to improper rational functions without dividing numerator by '
                        'denominator first.',
        'formula_cues': ['\\int u v dx', 'u \\int v dx - \\int', '\\frac{a}{x-a} + \\frac{b}{x-b}', "e^x[f(x)+f'(x)]"],
        'name': 'Integration by Parts & Partial Fractions',
        'primary': [   'integration by parts',
                       'partial fractions',
                       'product rule for integration',
                       'ilate',
                       'rational function',
                       'linear factors'],
        'secondary': ['first function', 'second function', 'algebraic'],
        'standard_formulas': '\\int u v dx = u \\int v dx - \\int \\left(\\frac{du}{dx} \\int v dx\\right) dx, \\quad '
                             "\\int e^x[f(x) + f'(x)]dx = e^x f(x) + C",
        'summary': "Integration by parts $\\int u v dx = u \\int v dx - \\int (u' \\int v dx) dx$ guided by the ILATE "
                   'priority rule. Resolution into partial fractions for proper rational functions.',
        'tips_and_tricks': 'In KCET, differentiate the four given options if finding the integral takes more than 1 '
                           'minute.'}],

    "kcet-definite-integration": [   {   'category': 'Definite Integral Properties',
        'common_traps': 'Applying the odd function property $\\int_{-a}^a f(x)dx = 0$ without verifying that the '
                        'limits are exactly symmetric $[-a, a]$.',
        'formula_cues': [   '\\int_0^a f(x)dx = \\int_0^a f(a-x)dx',
                            '\\int_{-a}^a f(x)dx',
                            '\\int_0^{\\pi/2} \\frac{\\sin^n x}{\\sin^n x + \\cos^n x} dx'],
        'name': "Properties of Definite Integrals & King's Rule",
        'primary': [   'definite integral',
                       "king's rule",
                       'f(a+b-x)',
                       'f(a-x)',
                       'odd function',
                       'even function',
                       'properties of definite',
                       'pi/4',
                       'pi/2',
                       '0 to pi/2'],
        'secondary': ['limits', 'upper limit', 'lower limit', 'symmetry'],
        'standard_formulas': '\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx, \\quad \\int_0^{\\pi/2} \\frac{\\sin^n '
                             'x}{\\sin^n x + \\cos^n x} dx = \\frac{\\pi}{4}',
        'summary': "King's property: $\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx$. For symmetric limits: $\\int_{-a}^a "
                   'f(x)dx = 0$ if $f(x)$ is odd, and $2\\int_0^a f(x)dx$ if $f(x)$ is even. Integral of periodic '
                   'functions: $\\int_0^{nT} f(x)dx = n\\int_0^T f(x)dx$.',
        'tips_and_tricks': 'Any integral of the form $\\int_a^b \\frac{f(x)}{f(x) + f(a+b-x)} dx$ is directly equal to '
                           '$\\frac{b-a}{2}$.'}],

}

"""
Curated Concept Taxonomy for all Mathematics Chapters in JEE Main and KCET.
Covers Algebra, Calculus, Coordinate Geometry, Vectors & 3D, Trigonometry, and Probability.
"""

MATH_TAXONOMY = {
    "sets-and-relations": [
        {
            "name": "Equivalence Relations (Reflexive, Symmetric, Transitive)",
            "category": "Relations",
            "primary": ["equivalence relation", "reflexive", "symmetric", "transitive", "relation r on", "equivalence class", "ordered pair"],
            "formula_cues": [r"(a, a) \in R", r"(a, b) \in R \implies (b, a) \in R", r"(a, b), (b, c) \in R \implies (a, c) \in R"],
            "standard_formulas": r"\text{Reflexive: } \forall a \in A, (a,a) \in R, \quad \text{Symmetric: } (a,b) \in R \implies (b,a) \in R, \quad \text{Transitive: } (a,b),(b,c) \in R \implies (a,c) \in R",
            "summary": "Formal definitions of binary relations on sets, properties for equivalence, and total number of reflexive relations $2^{n^2 - n}$.",
            "common_traps": "A relation is vacuously transitive if there are no pairs $(a,b)$ and $(b,c)$ with distinct elements to contradict transitivity.",
            "tips_and_tricks": "Total number of relations on set of $n$ elements is $2^{n^2}$; total number of symmetric relations is $2^{n(n+1)/2}$."
        },
        {
            "name": "Set Operations & Venn Diagram Principle",
            "category": "Set Theory",
            "primary": ["union", "intersection", "complement", "subset", "power set", "demorgan", "venn diagram", "inclusion exclusion"],
            "formula_cues": [r"n(A \cup B) = n(A) + n(B) - n(A \cap B)", r"n(P(A)) = 2^n", r"(A \cup B)' = A' \cap B'"],
            "standard_formulas": r"n(A \cup B) = n(A) + n(B) - n(A \cap B), \quad n(A \cup B \cup C) = \Sigma n(A) - \Sigma n(A \cap B) + n(A \cap B \cap C)",
            "summary": "Inclusion-exclusion principle for cardinality, De Morgan's set identities, and power set cardinality $2^n$.",
            "common_traps": "If set $A$ has $n$ elements, the number of proper subsets is $2^n - 1$ (excluding the set itself).",
            "tips_and_tricks": r"Number of elements belonging to EXACTLY two of three sets: $\Sigma n(A \cap B) - 3n(A \cap B \cap C)$."
        }
    ],

    "functions": [
        {
            "name": "Domain, Range & Composite Functions",
            "category": "Domain & Range",
            "primary": ["domain of function", "range of function", "composite function", "fog", "gof", "square root domain", "fractional part", "greatest integer"],
            "formula_cues": [r"f(g(x))", r"[x]", r"\{x\}", r"\sqrt{f(x)} \ge 0"],
            "standard_formulas": r"\text{For } \sqrt{f(x)} \implies f(x) \ge 0, \quad \text{For } \log_b(f(x)) \implies f(x) > 0, b > 0, b \ne 1, \quad x = [x] + \{x\}",
            "summary": "Determination of real domain and range, floor and fractional part functions, and domain constraints on composite functions.",
            "common_traps": r"Domain of $f(g(x))$ is NOT simply the domain of $g$; it requires $x \in \text{Domain}(g)$ AND $g(x) \in \text{Domain}(f)$!",
            "tips_and_tricks": r"The range of $f(x) = a\sin x + b\cos x + c$ is $[c - \sqrt{a^2 + b^2}, \; c + \sqrt{a^2 + b^2}]$."
        },
        {
            "name": "Injective (One-One), Surjective (Onto) & Inverse",
            "category": "Mappings",
            "primary": ["one-one", "onto", "bijective", "injective", "surjective", "invertible", "horizontal line test", "f'(x) > 0"],
            "formula_cues": [r"f(x_1) = f(x_2) \implies x_1 = x_2", r"f'(x) \ge 0", r"f(f^{-1}(x)) = x"],
            "standard_formulas": r"\text{One-One: } f'(x) > 0 \text{ (strictly monotonic)}, \quad \text{Onto: } \text{Range}(f) = \text{Codomain}(f), \quad \text{Bijective } \iff \text{Invertible}",
            "summary": "Horizontal line test, monotonicity test for injectivity, codomain matching for surjectivity, and finding function inverses.",
            "common_traps": "A function cannot be invertible unless it is BOTH one-one and onto (bijective).",
            "tips_and_tricks": r"If $f(x)$ is continuous and strictly increasing ($f'(x) > 0$) or strictly decreasing on $\mathbb{R}$, it is always one-one."
        }
    ],

    "complex-numbers": [
        {
            "name": "Modulus, Argument & Polar/Euler Form",
            "category": "Complex Basics",
            "primary": ["complex number", "modulus", "argument", "principal argument", "polar form", "euler form", "conjugate", "triangle inequality"],
            "formula_cues": [r"|z| = \sqrt{x^2 + y^2}", r"z = r(\cos\theta + i\sin\theta) = r e^{i\theta}", r"||z_1| - |z_2|| \le |z_1 + z_2| \le |z_1| + |z_2|"],
            "standard_formulas": r"z = x + iy = r e^{i\theta}, \quad |z|^2 = z \bar{z}, \quad \text{Arg}(z_1 z_2) = \text{Arg}(z_1) + \text{Arg}(z_2), \quad ||z_1| - |z_2|| \le |z_1 \pm z_2| \le |z_1| + |z_2|",
            "summary": r"Complex plane geometry, modulus properties, principal argument in $(-\pi, \pi]$, and triangle inequalities.",
            "common_traps": r"Principal argument $\text{Arg}(z)$ must lie strictly in $(-\pi, \pi]$; if $z$ is in the second quadrant, $\text{Arg}(z) = \pi - \tan^{-1}|y/x|$.",
            "tips_and_tricks": "Geometric interpretation: $|z - z_0| = r$ represents a circle centered at $z_0$ with radius $r$."
        },
        {
            "name": "De Moivre's Theorem & Cube Roots of Unity",
            "category": "Roots of Unity",
            "primary": ["cube roots of unity", "omega", "omega squared", "de moivre", "roots of unity", "1 + omega + omega^2", r"1 + \omega + \omega^2 = 0"],
            "formula_cues": [r"\omega = \frac{-1 + i\sqrt{3}}{2}", r"\omega^3 = 1", r"1 + \omega + \omega^2 = 0", r"(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta"],
            "standard_formulas": r"\omega^3 = 1, \quad 1 + \omega + \omega^2 = 0, \quad \omega^2 = \bar{\omega}, \quad (\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta",
            "summary": "Algebraic and geometric properties of cube roots of unity forming an equilateral triangle on the unit circle, and De Moivre powers.",
            "common_traps": r"$1 + \omega^n + \omega^{2n} = 3$ if $n$ is a multiple of 3, and equals $0$ if $n$ is NOT a multiple of 3.",
            "tips_and_tricks": r"Factorization identity: $x^3 - 1 = (x - 1)(x - \omega)(x - \omega^2)$, and $x^2 + x + 1 = (x - \omega)(x - \omega^2)$."
        }
    ],

    "quadratic-equation-and-inequalities": [
        {
            "name": "Roots of Quadratic & Vieta's Relations",
            "category": "Quadratic Roots",
            "primary": ["quadratic equation", "sum of roots", "product of roots", "discriminant", "nature of roots", "equal roots", "imaginary roots", "newton sum"],
            "formula_cues": [r"\alpha + \beta = -\frac{b}{a}", r"\alpha \beta = \frac{c}{a}", r"D = b^2 - 4ac", r"S_n = a\alpha^n + b\beta^n"],
            "standard_formulas": r"\alpha + \beta = -\frac{b}{a}, \quad \alpha\beta = \frac{c}{a}, \quad |\alpha - \beta| = \frac{\sqrt{D}}{|a|}, \quad a S_n + b S_{n-1} + c S_{n-2} = 0 \text{ (Newton)}",
            "summary": "Discriminant analysis for real/complex roots, symmetric root functions, and Newton's power sum theorem.",
            "common_traps": r"If coefficients $a, b, c$ are rational and $D$ is not a perfect square, roots occur in irrational conjugate pairs ($p \pm \sqrt{q}$).",
            "tips_and_tricks": r"Newton's theorem: If $\alpha, \beta$ are roots of $ax^2 + bx + c = 0$ and $S_n = \alpha^n + \beta^n$, then $a S_n + b S_{n-1} + c S_{n-2} = 0$."
        },
        {
            "name": "Location of Roots & Quadratic Inequalities",
            "category": "Location of Roots",
            "primary": ["location of roots", "both roots greater than", "both roots less than", "roots lie between", "sign of quadratic", "wavy curve", "inequality"],
            "formula_cues": [r"D \ge 0", r"-\frac{b}{2a} > k", r"a \cdot f(k) > 0", r"f(k_1) \cdot f(k_2) < 0"],
            "standard_formulas": r"\text{Both roots } > k \iff D \ge 0, \quad -\frac{b}{2a} > k, \quad a \cdot f(k) > 0",
            "summary": "Conditions for roots relative to real numbers $k, k_1, k_2$, and signs of quadratic expression $ax^2 + bx + c$.",
            "common_traps": r"For both roots to be greater than $k$, checking $a \cdot f(k) > 0$ alone is NOT sufficient; you must ALSO check $D \ge 0$ and $-\frac{b}{2a} > k$.",
            "tips_and_tricks": "If $a > 0$, the quadratic $f(x) = ax^2 + bx + c > 0$ for all real $x$ if and only if $D < 0$."
        }
    ],

    "matrices-and-determinants": [
        {
            "name": "Properties of Determinants & System of Linear Equations",
            "category": "Determinants & Linear Systems",
            "primary": ["determinant", "cramer's rule", "system of linear equations", "consistent", "inconsistent", "infinitely many solutions", "no solution", "unique solution", "trivial solution"],
            "formula_cues": [r"\Delta = 0", r"\Delta_x = \Delta_y = \Delta_z = 0", r"\det(A) = 0", r"\det(kA) = k^n \det(A)"],
            "standard_formulas": r"\det(kA) = k^n\det(A), \quad \text{Unique: } \Delta \ne 0, \quad \text{Infinite: } \Delta = \Delta_x = \Delta_y = \Delta_z = 0, \quad \text{No sol: } \Delta = 0 \text{ & at least one } \Delta_i \ne 0",
            "summary": "Evaluation of determinants, Cramer's rule, and consistency conditions for non-homogeneous and homogeneous linear systems.",
            "common_traps": r"For an $n \times n$ matrix $A$, $\det(kA) = k^n\det(A)$, NOT $k\det(A)$!",
            "tips_and_tricks": r"A homogeneous system $AX = 0$ has non-trivial (infinite) solutions if and only if $\det(A) = 0$."
        },
        {
            "name": "Matrix Inversion, Adjoint & Powers",
            "category": "Matrix Algebra",
            "primary": ["adjoint", "inverse of matrix", "symmetric matrix", "skew-symmetric", "orthogonal matrix", "nilpotent", "idempotent", "cayley hamilton"],
            "formula_cues": [r"A^{-1} = \frac{\text{adj}(A)}{\det(A)}", r"\det(\text{adj}(A)) = (\det A)^{n-1}", r"A \cdot \text{adj}(A) = (\det A) I", r"A^T = -A"],
            "standard_formulas": r"A \cdot \text{adj}(A) = (\det A) I_n, \quad \det(\text{adj}(A)) = (\det A)^{n-1}, \quad \text{adj}(\text{adj}(A)) = (\det A)^{n-2} A",
            "summary": "Properties of adjoint and inverse matrices, matrix multiplication transpose $(AB)^T = B^T A^T$, and symmetric/skew-symmetric decomposition.",
            "common_traps": r"A skew-symmetric matrix of ODD order has determinant equal to ZERO ($\det(A) = 0$).",
            "tips_and_tricks": r"For a $3 \times 3$ matrix: $\det(\text{adj}(A)) = (\det A)^2$, and $\det(\text{adj}(\text{adj}(A))) = (\det A)^4$."
        }
    ],

    "permutations-and-combinations": [
        {
            "name": "Fundamental Principles & Permutations (Distinct & Identical)",
            "category": "Arrangements",
            "primary": ["permutation", "arrangement", "factorial", "identical objects", "dictionary order", "rank of word", "circular permutation"],
            "formula_cues": [r"^n P_r = \frac{n!}{(n-r)!}", r"\frac{n!}{p! q! r!}", r"(n-1)!"],
            "standard_formulas": r"^n P_r = \frac{n!}{(n-r)!}, \quad \text{Arrangements with duplicates: } \frac{n!}{p! q! r!}, \quad \text{Circular: } (n-1)!",
            "summary": "Multiplication and addition principles, linear permutations with repetitions, rank of words in dictionary, and circular arrangements.",
            "common_traps": r"For circular permutations of necklaces/garlands where clockwise and anticlockwise arrangements are indistinguishable, divide by 2: $\frac{(n-1)!}{2}$.",
            "tips_and_tricks": "Gap method: Place items that cannot be adjacent into the gaps created by the remaining unrestricted items."
        },
        {
            "name": "Combinations, Selection & Multinomial Partitioning",
            "category": "Selections & Distribution",
            "primary": ["combination", "selection", "beggar's method", "distribution of identical", "derangement", "number of divisors", "handshakes"],
            "formula_cues": [r"^n C_r = \frac{n!}{r!(n-r)!}", r"^{n+r-1} C_{r-1}", r"D_n = n!(1 - \frac{1}{1!} + \frac{1}{2!} - \dots)"],
            "standard_formulas": r"^n C_r = \frac{n!}{r!(n-r)!}, \quad \text{Non-negative solutions: } ^{n+r-1}C_{r-1}, \quad \text{Derangements: } D_n = n!\Sigma_{k=0}^n \frac{(-1)^k}{k!}",
            "summary": "Combinatorial selection, Pascal identity $^n C_r + ^n C_{r-1} = ^{n+1} C_r$, distribution of identical items into distinct bins, and derangements.",
            "common_traps": r"Number of positive integral solutions ($x_i \ge 1$) to $x_1 + x_2 + \dots + x_r = n$ is $^{n-1} C_{r-1}$, whereas non-negative ($x_i \ge 0$) is $^{n+r-1} C_{r-1}$.",
            "tips_and_tricks": "Number of derangements of 4 items is $D_4 = 9$; for 5 items is $D_5 = 44$."
        }
    ],

    "binomial-theorem": [
        {
            "name": "General Term, Middle Term & Greatest Term",
            "category": "Expansion Terms",
            "primary": ["binomial theorem", "general term", "middle term", "term independent of x", "coefficient of", "numerically greatest term"],
            "formula_cues": [r"T_{r+1} = ^n C_r a^{n-r} b^r", r"\text{Middle term}", r"r = \frac{n\alpha}{\alpha + \beta}"],
            "standard_formulas": r"(a + b)^n = \Sigma_{r=0}^n {^n C_r} a^{n-r} b^r, \quad T_{r+1} = {^n C_r} a^{n-r} b^r, \quad \text{Middle: } T_{\frac{n}{2} + 1} \text{ (if } n \text{ is even)}",
            "summary": r"Expansion of $(x + a)^n$, formula for general $(r+1)^{\text{th}}$ term, finding term independent of $x$, and middle term determination.",
            "common_traps": r"In $(a + b)^n$, total number of terms is $n + 1$. If $n$ is odd, there are TWO middle terms: $\frac{n+1}{2}^{\text{th}}$ and $\frac{n+3}{2}^{\text{th}}$.",
            "tips_and_tricks": r"In expansion of $(ax^p + bx^{-q})^n$, the term independent of $x$ occurs at index $r = \frac{n p}{p + q}$ (provided $r$ is an integer)."
        },
        {
            "name": "Properties & Series Sum of Binomial Coefficients",
            "category": "Coefficient Identities",
            "primary": ["binomial coefficients", "sum of coefficients", "c_0 + c_1 + c_2", "c_0 - c_1 + c_2", "differentiation of binomial", "integration of binomial"],
            "formula_cues": [r"C_0 + C_1 + \dots + C_n = 2^n", r"\Sigma r C_r = n 2^{n-1}", r"\Sigma \frac{C_r}{r+1} = \frac{2^{n+1}-1}{n+1}"],
            "standard_formulas": r"\Sigma_{r=0}^n {^n C_r} = 2^n, \quad C_0 - C_1 + C_2 - \dots = 0, \quad \Sigma_{r=1}^n r {^n C_r} = n 2^{n-1}, \quad \Sigma_{r=0}^n ({^n C_r})^2 = {^{2n} C_n}",
            "summary": "Combinatorial identities, summing coefficient series via differentiation and integration of $(1+x)^n$.",
            "common_traps": "To find the sum of all coefficients of a polynomial expansion $P(x)$, simply substitute $x = 1$.",
            "tips_and_tricks": r"Useful ratio identity: $\frac{^n C_r}{^n C_{r-1}} = \frac{n - r + 1}{r}$."
        }
    ],

    "sequences-and-series": [
        {
            "name": "Arithmetic & Geometric Progressions (AP, GP, AGP)",
            "category": "Progressions",
            "primary": ["arithmetic progression", "geometric progression", "common difference", "common ratio", "sum of ap", "sum of gp", "infinite gp", "arithmetico-geometric"],
            "formula_cues": [r"S_n = \frac{n}{2}(2a + (n-1)d)", r"S_\infty = \frac{a}{1 - r}", r"T_n = a r^{n-1}"],
            "standard_formulas": r"S_n = \frac{n}{2}[2a + (n-1)d], \quad S_n = \frac{a(1 - r^n)}{1 - r}, \quad S_\infty = \frac{a}{1 - r} \; (|r| < 1), \quad T_n = S_n - S_{n-1}",
            "summary": "nth term and sum formulas for AP and GP, infinite geometric series convergence, and Arithmetico-Geometric series summation.",
            "common_traps": r"The formula $S_\infty = \frac{a}{1 - r}$ is valid ONLY when $|r| < 1$. If $|r| \ge 1$, the infinite series diverges.",
            "tips_and_tricks": "To choose 3 terms in AP: $a - d, a, a + d$ (sum eliminates $d$). In GP: $a/r, a, ar$ (product eliminates $r$)."
        },
        {
            "name": "AM-GM-HM Inequality & Telescoping Series",
            "category": "Inequalities & Sigma",
            "primary": ["am-gm", "arithmetic mean greater than geometric mean", "minimum value using am gm", "telescoping series", "sigma n", "sigma n^2", "sigma n^3"],
            "formula_cues": [r"\text{AM} \ge \text{GM} \ge \text{HM}", r"\Sigma n = \frac{n(n+1)}{2}", r"\Sigma n^2 = \frac{n(n+1)(2n+1)}{6}", r"\Sigma n^3 = (\frac{n(n+1)}{2})^2"],
            "standard_formulas": r"\frac{a + b}{2} \ge \sqrt{ab} \ge \frac{2ab}{a+b}, \quad \Sigma n^2 = \frac{n(n+1)(2n+1)}{6}, \quad \Sigma n^3 = [\Sigma n]^2, \quad \frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}",
            "summary": "Arithmetic, geometric, and harmonic mean inequalities for positive numbers, sum of first $n$ natural powers, and partial fraction telescoping.",
            "common_traps": r"AM $\ge$ GM equality holds IF AND ONLY IF all participating positive numbers are equal ($a_1 = a_2 = \dots = a_n$).",
            "tips_and_tricks": r"Whenever asked for the minimum value of a sum of positive terms whose product is constant (e.g. $x + \frac{1}{x}$), use $\text{AM} \ge \text{GM}$."
        }
    ],

    "limits-continuity-and-differentiability": [
        {
            "name": "Evaluation of Limits & L'Hopital's Rule",
            "category": "Limits",
            "primary": ["limit", "indeterminate form", "l'hopital", "standard limits", "expansion", "taylor", "1^infinity", "0/0", "infinity/infinity"],
            "formula_cues": [r"\lim_{x \to 0}\frac{\sin x}{x} = 1", r"\lim_{x \to 0}\frac{e^x - 1}{x} = 1", r"\lim_{x \to 0}(1 + x)^{1/x} = e", r"e^{\lim (f(x) - 1)g(x)}"],
            "standard_formulas": r"\lim_{x \to 0}\frac{\sin x}{x} = 1, \quad \lim_{x \to 0}\frac{\ln(1+x)}{x} = 1, \quad \lim_{x \to a} f(x)^{g(x)} = e^{\lim_{x \to a} (f(x) - 1)g(x)} \text{ (for } 1^\infty)",
            "summary": r"Resolution of indeterminate forms ($0/0, \infty/\infty, 1^\infty$), standard trigonometric and exponential limits, and Series expansion.",
            "common_traps": r"Before applying L'Hopital's rule, ALWAYS check that the limit is in an indeterminate form ($0/0$ or $\infty/\infty$). Differentiating a determinate form produces an incorrect answer.",
            "tips_and_tricks": r"Maclaurin expansions are often faster than repeated L'Hopital: $\sin x = x - \frac{x^3}{6}$, $\cos x = 1 - \frac{x^2}{2}$, $e^x = 1 + x + \frac{x^2}{2}$."
        },
        {
            "name": "Continuity & Differentiability at a Point",
            "category": "Continuity & Differentiability",
            "primary": ["continuous", "discontinuous", "differentiable", "non-differentiable", "left hand limit", "right hand limit", "sharp corner", "cusp", "greatest integer continuity"],
            "formula_cues": [r"\text{LHL} = \text{RHL} = f(a)", r"f'(a^-) = f'(a^+)", r"\lim_{h \to 0}\frac{f(a+h) - f(a)}{h}"],
            "standard_formulas": r"\text{Continuous at } a \iff \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = f(a), \quad \text{Differentiability } \implies \text{Continuity}",
            "summary": "Epsilon-delta and limit criteria for continuity, left/right hand derivatives, and graphical identification of non-differentiable sharp points.",
            "common_traps": "Differentiability implies continuity, but continuity DOES NOT imply differentiability (e.g. $f(x) = |x|$ is continuous at $x=0$ but not differentiable).",
            "tips_and_tricks": r"The greatest integer function $[x]$ is discontinuous at all integer points $x \in \mathbb{Z}$."
        }
    ],

    "application-of-derivatives": [
        {
            "name": "Tangents, Normals & Rate of Change",
            "category": "Tangents & Rates",
            "primary": ["tangent", "normal", "slope of tangent", "point of contact", "orthogonal curves", "rate of change", "leaking", "balloon"],
            "formula_cues": [r"m = \frac{dy}{dx}", r"y - y_1 = m(x - x_1)", r"m_{\text{normal}} = -\frac{1}{dy/dx}", r"m_1 m_2 = -1"],
            "standard_formulas": r"m = \left(\frac{dy}{dx}\right)_{(x_1, y_1)}, \quad \text{Tangent: } y - y_1 = m(x - x_1), \quad \text{Normal: } y - y_1 = -\frac{1}{m}(x - x_1)",
            "summary": "Equations of tangent and normal lines, angle of intersection between two curves, and time derivatives as physical rates.",
            "common_traps": "Two curves cut orthogonally if and only if the product of their tangent slopes at the intersection point is $-1$ ($m_1 m_2 = -1$).",
            "tips_and_tricks": r"Length of sub-tangent $= \left|\frac{y}{dy/dx}\right|$; length of sub-normal $= |y \cdot \frac{dy}{dx}|$."
        },
        {
            "name": "Monotonicity, Maxima & Minima",
            "category": "Optimization",
            "primary": ["increasing function", "decreasing function", "strictly increasing", "local maxima", "local minima", "critical point", "first derivative test", "second derivative test", "inflection point"],
            "formula_cues": [r"f'(x) \ge 0", r"f'(x) \le 0", r"f'(c) = 0", r"f''(c) < 0 \implies \text{max}", r"f''(c) > 0 \implies \text{min}"],
            "standard_formulas": r"f'(x) > 0 \implies \text{Strictly Increasing}, \quad f'(c) = 0 \text{ & } f''(c) < 0 \implies \text{Local Max}, \quad f''(c) > 0 \implies \text{Local Min}",
            "summary": "First and second derivative tests for optimization, global extreme values on closed intervals, and Rolle's/Lagrange's Mean Value Theorems.",
            "common_traps": "A critical point occurs where $f'(x) = 0$ OR where $f'(x)$ DOES NOT EXIST (e.g. at $x=0$ for $|x|$).",
            "tips_and_tricks": r"LMVT statement: If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then $\exists c \in (a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$."
        }
    ],

    "indefinite-integrals": [
        {
            "name": "Standard Integrals, Substitution & By Parts",
            "category": "Integration Techniques",
            "primary": ["indefinite integral", "integration by substitution", "integration by parts", "ilate", "partial fractions", "antiderivative"],
            "formula_cues": [r"\int u v dx = u \int v dx - \int (u' \int v dx) dx", r"\int e^x (f(x) + f'(x)) dx = e^x f(x)", r"\int \frac{dx}{x^2 + a^2} = \frac{1}{a}\tan^{-1}\frac{x}{a}"],
            "standard_formulas": r"\int e^x [f(x) + f'(x)]\,dx = e^x f(x) + C, \quad \int \frac{dx}{x^2 - a^2} = \frac{1}{2a}\ln\left|\frac{x - a}{x + a}\right| + C, \quad \int \frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}\left(\frac{x}{a}\right) + C",
            "summary": "Fundamental integrals, substitution methods, ILATE integration by parts, and linear/quadratic partial fractions.",
            "common_traps": "In integration by parts, follow the ILATE priority strictly for choosing the first function $u$ (Inverse, Logarithmic, Algebraic, Trigonometric, Exponential).",
            "tips_and_tricks": r"The pattern $\int e^x [f(x) + f'(x)]\,dx = e^x f(x) + C$ appears with high frequency in both JEE Main and KCET."
        },
        {
            "name": "Partial Fractions & Special Algebraic Integrals",
            "category": "Algebraic Integrals",
            "primary": ["partial fraction", "rational function", "quadratic in denominator", "completing square", "linear by quadratic", "dx/(x^2 - a^2)"],
            "formula_cues": [r"\int \frac{dx}{ax^2 + bx + c}", r"\int \frac{px + q}{ax^2 + bx + c}dx", r"\frac{1}{2a}\ln|\frac{x-a}{x+a}|"],
            "standard_formulas": r"\int \frac{dx}{x^2 + a^2} = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + C, \quad \int \frac{dx}{\sqrt{x^2 \pm a^2}} = \ln|x + \sqrt{x^2 \pm a^2}| + C",
            "summary": "Integration using partial fraction decompositions, linear over quadratic forms, and standard quadratic root substitutions.",
            "common_traps": r"Check if degree of numerator $\ge$ degree of denominator; if so, polynomial long division MUST be performed first.",
            "tips_and_tricks": r"For integrals of type $\int \frac{dx}{a + b\cos^2 x}$, divide numerator and denominator by $\cos^2 x$ and substitute $\tan x = t$."
        }
    ],

    "definite-integration": [
        {
            "name": "King's Property & Definite Integral Properties",
            "category": "Integral Properties",
            "primary": ["definite integral", "king's property", "f(a+b-x)", "even function integral", "odd function integral", "periodic integral", "leibnitz rule"],
            "formula_cues": [r"\int_a^b f(x)dx = \int_a^b f(a + b - x)dx", r"\int_0^a f(x)dx = \int_0^a f(a - x)dx", r"\int_{-a}^a f(x)dx = 0", r"\frac{d}{dx}\int_{u(x)}^{v(x)} f(t)dt"],
            "standard_formulas": r"\int_a^b f(x)\,dx = \int_a^b f(a+b-x)\,dx, \quad \int_{-a}^a f(x)\,dx = 0 \text{ (if odd)}, \quad \frac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,dt = f(v(x))v'(x) - f(u(x))u'(x)",
            "summary": "King's property $f(a+b-x)$, reflection symmetry, integrals of even/odd functions, periodic functions, and Leibnitz integral differentiation.",
            "common_traps": r"King's property added to the original integral often yields $2I = \int_a^b 1\,dx = b - a \implies I = \frac{b - a}{2}$.",
            "tips_and_tricks": r"Integral of odd function over symmetric limits $[-a, a]$ is always ZERO: $\int_{-a}^a f(x)\,dx = 0$."
        },
        {
            "name": "Limit of a Sum & Area Under Curves",
            "category": "Summation & Area",
            "primary": ["limit of sum", "area under curve", "area bounded by", "area between curves", "riemann sum", "parabola and line area"],
            "formula_cues": [r"\lim_{n \to \infty} \frac{1}{n} \Sigma f(\frac{r}{n}) = \int_0^1 f(x)dx", r"\text{Area} = \int (y_1 - y_2)dx", r"\text{Area} = \frac{8}{3}\frac{a^2}{m^3}"],
            "standard_formulas": r"\lim_{n \to \infty} \frac{1}{n}\Sigma_{r=1}^n f\left(\frac{r}{n}\right) = \int_0^1 f(x)\,dx, \quad \text{Area between } y^2 = 4ax \text{ and } y = mx \implies \frac{8a^2}{3m^3}",
            "summary": "Definite integrals as limits of Riemann sums ($r/n \to x, 1/n \to dx$), and enclosed area calculations between curves.",
            "common_traps": r"Area is always a positive geometric quantity; if the curve dips below the x-axis, take absolute value $|\int y\,dx|$.",
            "tips_and_tricks": "Area bounded by $y^2 = 4ax$ and $x^2 = 4by$ is given directly by $\frac{16ab}{3}$."
        }
    ],

    "differential-equations": [
        {
            "name": "Variable Separable & Homogeneous DE",
            "category": "Separable DE",
            "primary": ["differential equation", "order and degree", "variable separable", "homogeneous differential equation", "substitution y = vx"],
            "formula_cues": [r"\frac{dy}{dx} = f(x)g(y)", r"\frac{dy}{dx} = F(\frac{y}{x})", r"y = vx \implies \frac{dy}{dx} = v + x\frac{dv}{dx}"],
            "standard_formulas": r"\int \frac{dy}{g(y)} = \int f(x)\,dx + C, \quad \text{For homogeneous: substitute } y = vx \implies \frac{dy}{dx} = v + x\frac{dv}{dx}",
            "summary": "Classification of order and degree, separation of variables, and reduction of homogeneous equations via $y = vx$.",
            "common_traps": r"Degree of a differential equation is defined ONLY when the equation is a polynomial in its derivatives (no fractional powers or $\sin(dy/dx)$).",
            "tips_and_tricks": "Equations of the form $\frac{dy}{dx} = f(ax + by + c)$ can be solved by substituting $z = ax + by + c$."
        },
        {
            "name": "Linear Differential Equations & Integrating Factor",
            "category": "Linear DE",
            "primary": ["linear differential equation", "integrating factor", "if = e^{int p dx}", "dy/dx + py = q", "dx/dy + px = q"],
            "formula_cues": [r"\text{IF} = e^{\int P dx}", r"y \cdot \text{IF} = \int (Q \cdot \text{IF}) dx + C", r"\frac{dy}{dx} + P y = Q"],
            "standard_formulas": r"\frac{dy}{dx} + P(x)y = Q(x) \implies \text{I.F.} = e^{\int P(x)\,dx}, \quad y \cdot (\text{I.F.}) = \int Q(x) \cdot (\text{I.F.})\,dx + C",
            "summary": "Standard first-order linear differential equations and integrating factor technique for $y(x)$ and $x(y)$.",
            "common_traps": "If the equation has $x \frac{dy}{dx}$, remember to divide by $x$ throughout first so the coefficient of $\frac{dy}{dx}$ is $1$!",
            "tips_and_tricks": r"If the equation is non-linear in $y$, check if it is linear in $x$: $\frac{dx}{dy} + P(y)x = Q(y) \implies \text{I.F.} = e^{\int P(y)\,dy}$."
        }
    ],

    "straight-lines-and-pair-of-straight-lines": [
        {
            "name": "Distance, Slopes & Forms of Straight Line",
            "category": "Straight Lines",
            "primary": ["straight line", "slope of line", "intercept form", "perpendicular distance", "distance between parallel lines", "foot of perpendicular", "image of a point"],
            "formula_cues": [r"d = \frac{|a x_1 + b y_1 + c|}{\sqrt{a^2 + b^2}}", r"d = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}", r"\frac{x - x_1}{a} = \frac{y - y_1}{b} = -\frac{a x_1 + b y_1 + c}{a^2 + b^2}"],
            "standard_formulas": r"d = \frac{|a x_1 + b y_1 + c|}{\sqrt{a^2 + b^2}}, \quad d_{\text{parallel}} = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}, \quad \text{Foot: } \frac{x - x_1}{a} = \frac{y - y_1}{b} = -\frac{ax_1 + by_1 + c}{a^2 + b^2}",
            "summary": r"Linear equations, distance formulas, family of lines $L_1 + \lambda L_2 = 0$, and coordinates of reflections (images) in lines.",
            "common_traps": "For distance between parallel lines, ensure coefficients of $x$ and $y$ are MADE IDENTICAL before subtracting $c_1 - c_2$.",
            "tips_and_tricks": r"Image of point $(x_1, y_1)$ in line $ax + by + c = 0$ is given by $\frac{x - x_1}{a} = \frac{y - y_1}{b} = -2\frac{ax_1 + by_1 + c}{a^2 + b^2}$."
        },
        {
            "name": "Pair of Straight Lines & Angle Bisectors",
            "category": "Homogeneous Lines",
            "primary": ["pair of straight lines", "homogeneous equation", "angle between lines", "coincident lines", "perpendicular lines", "bisectors of angles", "h^2 = ab", "a + b = 0"],
            "formula_cues": [r"ax^2 + 2hxy + by^2 = 0", r"\tan\theta = \frac{2\sqrt{h^2 - ab}}{a + b}", r"a + b = 0", r"\frac{x^2 - y^2}{a - b} = \frac{xy}{h}"],
            "standard_formulas": r"\tan\theta = \left|\frac{2\sqrt{h^2 - ab}}{a + b}\right|, \quad \text{Perpendicular } \iff a + b = 0, \quad \text{Coincident } \iff h^2 = ab, \quad \frac{x^2 - y^2}{a - b} = \frac{xy}{h}",
            "summary": "Joint equations of lines through origin, condition of perpendicularity ($a + b = 0$), and joint equation of angle bisectors.",
            "common_traps": r"If $a + b = 0$, the lines represented by $ax^2 + 2hxy + by^2 = 0$ are mutually perpendicular regardless of value of $h$.",
            "tips_and_tricks": r"General second degree equation represents pair of lines if $\Delta = abc + 2fgh - af^2 - bg^2 - ch^2 = 0$."
        }
    ],

    "circle": [
        {
            "name": "Circle Equation, Tangents & Chord of Contact",
            "category": "Circles",
            "primary": ["circle", "radius of circle", "center of circle", "tangent to circle", "chord of contact", "condition of tangency", "director circle", "orthogonal circles"],
            "formula_cues": [r"x^2 + y^2 + 2gx + 2fy + c = 0", r"r = \sqrt{g^2 + f^2 - c}", r"c^2 = a^2(1 + m^2)", r"T = 0", r"2g_1 g_2 + 2f_1 f_2 = c_1 + c_2"],
            "standard_formulas": r"r = \sqrt{g^2 + f^2 - c}, \quad \text{Tangent: } y = mx \pm a\sqrt{1 + m^2}, \quad \text{Chord of contact: } T = 0, \quad \text{Orthogonal: } 2g_1 g_2 + 2f_1 f_2 = c_1 + c_2",
            "summary": "Standard and general equations of circles, condition for line $y = mx + c$ to be tangent, and director circle $x^2 + y^2 = 2a^2$.",
            "common_traps": "The center of $x^2 + y^2 + 2gx + 2fy + c = 0$ is $(-g, -f)$, NOT $(+g, +f)$.",
            "tips_and_tricks": r"The locus of the point of intersection of two perpendicular tangents to a circle is its director circle (radius $\sqrt{2}a$)."
        },
        {
            "name": "Tangents, Normals & Orthogonal Circles",
            "category": "Tangents & Circles",
            "primary": ["tangent to circle", "normal to circle", "length of tangent", "power of point", "director circle", "orthogonal circles", "common chord"],
            "formula_cues": [r"y = mx \pm a\sqrt{1 + m^2}", r"T = 0", r"L = \sqrt{S_1}", r"2g_1 g_2 + 2f_1 f_2 = c_1 + c_2"],
            "standard_formulas": r"\text{Tangent: } y = mx \pm a\sqrt{1 + m^2}, \quad \text{Length of tangent: } L = \sqrt{S_1}, \quad \text{Orthogonal: } 2g_1 g_2 + 2f_1 f_2 = c_1 + c_2",
            "summary": "Point and slope forms of circle tangents, director circle $x^2 + y^2 = 2a^2$, and orthogonality condition.",
            "common_traps": "The normal to a circle at any point ALWAYS passes through the center of the circle $(-g, -f)$.",
            "tips_and_tricks": "Common chord of two intersecting circles $S_1 = 0$ and $S_2 = 0$ is given directly by the linear equation $S_1 - S_2 = 0$."
        }
    ],

    "parabola": [
        {
            "name": "Standard Parabola, Focus, Directrix & Tangents",
            "category": "Parabola",
            "primary": ["parabola", "focus", "directrix", "latus rectum", "tangent to parabola", "parametric coordinates", "condition of tangency"],
            "formula_cues": [r"y^2 = 4ax", r"\text{Focus } (a, 0)", r"x = -a", r"y = mx + \frac{a}{m}", r"(at^2, 2at)"],
            "standard_formulas": r"y^2 = 4ax \implies \text{Focus}(a, 0), \text{ Directrix: } x = -a, \text{ LR } = 4a, \quad \text{Tangent: } y = mx + \frac{a}{m}, \quad \text{Parametric: } (at^2, 2at)",
            "summary": "Focal properties of $y^2 = 4ax$, slope form of tangent $y = mx + a/m$, and parametric chords.",
            "common_traps": "For $x^2 = 4ay$, the tangent in slope form is $y = mx - am^2$, NOT $y = mx + a/m$!",
            "tips_and_tricks": r"The tangents at the extremities of any focal chord intersect at right angles ($90^\circ$) strictly on the DIRECTRIX."
        },
        {
            "name": "Normals to Parabola & Co-Normal Points",
            "category": "Normals",
            "primary": ["normal to parabola", "slope form of normal", "co-normal", "three normals", "feet of normals", "centroid of co-normal"],
            "formula_cues": [r"y = mx - 2am - am^3", r"y + tx = 2at + at^3", r"m_1 + m_2 + m_3 = 0"],
            "standard_formulas": r"\text{Normal: } y = mx - 2am - am^3, \quad \text{Parametric: } y + tx = 2at + at^3, \quad \Sigma m_i = 0",
            "summary": "Cubic normal equation $am^3 + (2a - x)m + y = 0$, maximum of three normals from external point, and co-normal properties.",
            "common_traps": "From an external point $(h, k)$, three normals can be drawn to $y^2 = 4ax$ if and only if $h > 2a$.",
            "tips_and_tricks": "The algebraic sum of the slopes of three co-normal points is always ZERO: $m_1 + m_2 + m_3 = 0$."
        }
    ],

    "ellipse": [
        {
            "name": "Eccentricity, Foci & Tangents of Ellipse",
            "category": "Ellipse",
            "primary": ["ellipse", "eccentricity", "foci", "major axis", "minor axis", "tangent to ellipse", "auxiliary circle", "director circle"],
            "formula_cues": [r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1", r"e = \sqrt{1 - \frac{b^2}{a^2}}", r"y = mx \pm \sqrt{a^2 m^2 + b^2}", r"x^2 + y^2 = a^2 + b^2"],
            "standard_formulas": r"e = \sqrt{1 - \frac{b^2}{a^2}}, \quad \text{Foci: } (\pm ae, 0), \quad \text{LR} = \frac{2b^2}{a}, \quad \text{Tangent: } y = mx \pm \sqrt{a^2 m^2 + b^2}, \quad \text{Director: } x^2 + y^2 = a^2 + b^2",
            "summary": "Standard ellipse equation, focal distance sum property $SP + S'P = 2a$, eccentricity $e < 1$, and director circle.",
            "common_traps": r"If $b > a$ (vertical ellipse), major axis is along y-axis and $e = \sqrt{1 - a^2/b^2}$ with foci at $(0, \pm be)$.",
            "tips_and_tricks": "Product of perpendiculars from the two foci onto any tangent to the ellipse is always constant and equal to $b^2$."
        },
        {
            "name": "Focal Properties & Auxiliary Circle",
            "category": "Focal Geometry",
            "primary": ["focal distance", "sum of focal distances", "auxiliary circle", "eccentric angle", "sp + s'p = 2a", "latus rectum of ellipse"],
            "formula_cues": [r"SP + S'P = 2a", r"x^2 + y^2 = a^2", r"(a\cos\theta, b\sin\theta)", r"\frac{2b^2}{a}"],
            "standard_formulas": r"SP + S'P = 2a = \text{Major Axis}, \quad \text{Auxiliary Circle: } x^2 + y^2 = a^2, \quad \text{Parametric: } (a\cos\theta, b\sin\theta)",
            "summary": "Focal radius property $SP + S'P = 2a$, auxiliary circle projections, and parametric coordinate representation.",
            "common_traps": "In an ellipse, the eccentric angle $\theta$ is measured on the auxiliary circle, NOT from the center to the point on the ellipse.",
            "tips_and_tricks": "Maximum area of a rectangle inscribed in an ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ is $2ab$."
        }
    ],

    "hyperbola": [
        {
            "name": "Asymptotes, Rectangular Hyperbola & Conjugate",
            "category": "Hyperbola",
            "primary": ["hyperbola", "rectangular hyperbola", "eccentricity of hyperbola", "asymptotes", "conjugate hyperbola", "foci of hyperbola"],
            "formula_cues": [r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1", r"e = \sqrt{1 + \frac{b^2}{a^2}}", r"y = mx \pm \sqrt{a^2 m^2 - b^2}", r"xy = c^2", r"e = \sqrt{2}"],
            "standard_formulas": r"e = \sqrt{1 + \frac{b^2}{a^2}}, \quad \text{LR} = \frac{2b^2}{a}, \quad \text{Tangent: } y = mx \pm \sqrt{a^2 m^2 - b^2}, \quad \text{Rectangular: } xy = c^2 \implies e = \sqrt{2}",
            "summary": r"Focal distance difference property $|SP - S'P| = 2a$, eccentricity $e > 1$, asymptotes $y = \pm \frac{b}{a}x$, and rectangular hyperbola.",
            "common_traps": r"For the conjugate hyperbola $-\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, eccentricity is $e' = \sqrt{1 + a^2/b^2}$, and $\frac{1}{e^2} + \frac{1}{e'^2} = 1$.",
            "tips_and_tricks": r"The eccentricity of ANY rectangular hyperbola ($a = b$ or $xy = c^2$) is always uniquely equal to $\sqrt{2}$."
        },
        {
            "name": "Rectangular Hyperbola & Asymptotes",
            "category": "Asymptotes & Geometry",
            "primary": ["rectangular hyperbola", "asymptotes of hyperbola", "xy = c^2", "eccentricity root 2", "angle between asymptotes", "conjugate hyperbola"],
            "formula_cues": [r"xy = c^2", r"e = \sqrt{2}", r"y = \pm \frac{b}{a}x", r"\theta = 2\tan^{-1}(b/a)"],
            "standard_formulas": r"\text{Asymptotes: } \frac{x^2}{a^2} - \frac{y^2}{b^2} = 0 \implies y = \pm \frac{b}{a}x, \quad \text{Rectangular: } a = b \iff e = \sqrt{2}, \quad xy = c^2 \implies (ct, c/t)",
            "summary": "Equations and properties of asymptotes, angle between asymptotes $2\tan^{-1}(b/a)$, and parametric properties of $xy = c^2$.",
            "common_traps": "The asymptotes of a hyperbola pass through its CENTER and are parallel to the conjugate hyperbola's asymptotes.",
            "tips_and_tricks": "Tangent to rectangular hyperbola $xy = c^2$ at $(ct, c/t)$ is $\frac{x}{t} + yt = 2c$."
        }
    ],

    "vector-algebra": [
        {
            "name": "Dot Product & Projection of Vectors",
            "category": "Scalar Product",
            "primary": ["dot product", "scalar product", "projection of vector", "angle between vectors", "perpendicular vectors", "collinear"],
            "formula_cues": [r"\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta", r"\text{proj} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}", r"\vec{a} \cdot \vec{b} = 0"],
            "standard_formulas": r"\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3, \quad \cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}, \quad \text{Projection of } \vec{a} \text{ on } \vec{b} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}",
            "summary": r"Algebraic definition of scalar product, projection length along a direction, and orthogonality condition ($\vec{a} \cdot \vec{b} = 0$).",
            "common_traps": r"Projection vector of $\vec{a}$ on $\vec{b}$ is a VECTOR: $\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|^2}\right)\vec{b}$. Scalar projection is just the length $\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$.",
            "tips_and_tricks": "Magnitude identity: $|\vec{a} + \vec{b}|^2 + |\vec{a} - \vec{b}|^2 = 2(|\vec{a}|^2 + |\vec{b}|^2)$."
        },
        {
            "name": "Cross Product & Scalar Triple Product (Box Product)",
            "category": "Vector Products",
            "primary": ["cross product", "vector product", "scalar triple product", "box product", "coplanar vectors", "area of triangle", "area of parallelogram", "volume of parallelepiped"],
            "formula_cues": [r"\vec{a} \times \vec{b}", r"[\vec{a} \;\; \vec{b} \;\; \vec{c}]", r"[\vec{a} \;\; \vec{b} \;\; \vec{c}] = 0", r"V = |\vec{a} \cdot (\vec{b} \times \vec{c})|"],
            "standard_formulas": r"\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}, \quad \text{Area} = \frac{1}{2}|\vec{a} \times \vec{b}|, \quad [\vec{a}\,\vec{b}\,\vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c})",
            "summary": r"Non-commutative cross product $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$, area of triangles, and coplanarity condition $[\vec{a}\,\vec{b}\,\vec{c}] = 0$.",
            "common_traps": r"Three vectors $\vec{a}, \vec{b}, \vec{c}$ are COPLANAR if and only if their scalar triple product is ZERO: $[\vec{a} \;\; \vec{b} \;\; \vec{c}] = 0$.",
            "tips_and_tricks": r"Lagrange's identity: $|\vec{a} \times \vec{b}|^2 = |\vec{a}|^2|\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2$."
        }
    ],

    "3d-geometry": [
        {
            "name": "Direction Cosines & Equations of Lines in 3D",
            "category": "3D Lines",
            "primary": ["direction cosines", "direction ratios", "shortest distance between skew lines", "symmetric form", "coplanar lines", "angle between lines"],
            "formula_cues": [r"l^2 + m^2 + n^2 = 1", r"\frac{x - x_1}{a} = \frac{y - y_1}{b} = \frac{z - z_1}{c}", r"d = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}"],
            "standard_formulas": r"l^2 + m^2 + n^2 = 1, \quad \frac{x - x_1}{a} = \frac{y - y_1}{b} = \frac{z - z_1}{c}, \quad d_{\text{skew}} = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}",
            "summary": "Direction cosines $(l, m, n)$, line passing through two points, and shortest distance formula between skew lines.",
            "common_traps": "Direction ratios $(a, b, c)$ can be any proportional numbers, but direction cosines $(l, m, n)$ MUST satisfy $l^2 + m^2 + n^2 = 1$.",
            "tips_and_tricks": r"Two lines in 3D intersect (are coplanar) if and only if the shortest distance between them is ZERO: $(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2) = 0$."
        },
        {
            "name": "Planes & Line-Plane Intersections in 3D",
            "category": "3D Planes",
            "primary": ["equation of plane", "normal to plane", "intercept form of plane", "distance of point from plane", "plane through three points", "angle between line and plane"],
            "formula_cues": [r"ax + by + cz + d = 0", r"d = \frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2 + b^2 + c^2}}", r"\sin\theta = \frac{|\vec{b} \cdot \vec{n}|}{|\vec{b}||\vec{n}|}"],
            "standard_formulas": r"a(x - x_1) + b(y - y_1) + c(z - z_1) = 0, \quad d = \frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2 + b^2 + c^2}}, \quad \sin\theta = \frac{|\vec{b} \cdot \vec{n}|}{|\vec{b}||\vec{n}|}",
            "summary": r"Normal vector to a plane, perpendicular distance from point to plane, and angle between a line and plane (uses $\sin\theta$).",
            "common_traps": r"Angle between a LINE (vector $\vec{b}$) and a PLANE (normal $\vec{n}$) is computed with SINE ($\sin\theta = \frac{|\vec{b} \cdot \vec{n}|}{|\vec{b}||\vec{n}|}$), NOT cosine!",
            "tips_and_tricks": r"A line is parallel to a plane if and only if it is perpendicular to the plane's normal: $\vec{b} \cdot \vec{n} = 0$."
        }
    ],

    "probability": [
        {
            "name": "Conditional Probability & Bayes' Theorem",
            "category": "Conditional & Bayes",
            "primary": ["conditional probability", "bayes theorem", "independent events", "total probability theorem", "partition of sample space", "urn", "bag contains"],
            "formula_cues": [r"P(A|B) = \frac{P(A \cap B)}{P(B)}", r"P(A \cap B) = P(A)P(B)", r"P(E_i|A) = \frac{P(E_i)P(A|E_i)}{\Sigma P(E_k)P(A|E_k)}"],
            "standard_formulas": r"P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(A \cap B) = P(A) \cdot P(B) \text{ (independent)}, \quad P(E_i|A) = \frac{P(E_i)P(A|E_i)}{\Sigma P(E_j)P(A|E_j)}",
            "summary": "Multiplication rule of probability, test for statistical independence, law of total probability, and inverse probability via Bayes' theorem.",
            "common_traps": r"Mutually exclusive events ($A \cap B = \emptyset \implies P(A \cap B) = 0$) CANNOT be independent if both have non-zero probabilities!",
            "tips_and_tricks": r"For independent events: $P(A \cup B) = 1 - P(A')P(B')$."
        },
        {
            "name": "Probability Distribution & Binomial Distribution",
            "category": "Random Variables",
            "primary": ["random variable", "probability distribution", "mean of distribution", "variance", "standard deviation", "binomial distribution", "bernoulli trials", "tossing coin"],
            "formula_cues": [r"\Sigma P_i = 1", r"\mu = \Sigma x_i P_i", r"\sigma^2 = \Sigma x_i^2 P_i - \mu^2", r"P(X=r) = ^n C_r p^r q^{n-r}"],
            "standard_formulas": r"\text{Mean } \mu = \Sigma x_i p_i, \quad \text{Var } \sigma^2 = \Sigma x_i^2 p_i - \mu^2, \quad \text{Binomial: } P(X = r) = {^n C_r} p^r q^{n-r}, \; \text{Mean} = np, \; \text{Var} = npq",
            "summary": "Discrete probability distributions, expected value $E(X)$, variance, and Binomial Bernoulli trials ($q = 1 - p$).",
            "common_traps": "In a Binomial distribution, the variance ($npq$) is ALWAYS strictly less than the mean ($np$) because $q < 1$.",
            "tips_and_tricks": r"Variance formula shortcut: $\text{Var}(X) = E(X^2) - [E(X)]^2$."
        }
    ],

    "statistics": [
        {
            "name": "Mean, Variance & Standard Deviation",
            "category": "Dispersion",
            "primary": ["mean", "variance", "standard deviation", "coefficient of variation", "change of origin and scale", "grouped data"],
            "formula_cues": [r"\bar{x} = \frac{\Sigma x_i}{n}", r"\sigma^2 = \frac{\Sigma x_i^2}{n} - \bar{x}^2", r"\text{CV} = \frac{\sigma}{\bar{x}} \times 100"],
            "standard_formulas": r"\bar{x} = \frac{\Sigma x_i}{n}, \quad \sigma^2 = \frac{\Sigma x_i^2}{n} - (\bar{x})^2, \quad \sigma = \sqrt{\text{Variance}}, \quad \text{CV} = \frac{\sigma}{\bar{x}} \times 100",
            "summary": "Measures of central tendency, variance calculation using mean of squares minus square of mean, and dispersion scaling.",
            "common_traps": r"Adding a constant $c$ to every observation changes the mean ($\bar{x}' = \bar{x} + c$), but leaves the VARIANCE completely UNCHANGED ($\sigma'^2 = \sigma^2$).",
            "tips_and_tricks": r"If every observation is multiplied by $k$: new mean $= k\bar{x}$, new standard deviation $= |k|\sigma$, and new variance $= k^2\sigma^2$."
        },
        {
            "name": "Measures of Central Tendency & Median",
            "category": "Central Tendency",
            "primary": ["median", "mode", "mean median mode relation", "grouped data median", "cumulative frequency", "quartile"],
            "formula_cues": [r"\text{Mode} = 3\text{Median} - 2\text{Mean}", r"\text{Median} = l + \frac{n/2 - cf}{f}h"],
            "standard_formulas": r"\text{Empirical: } \text{Mode} \approx 3\text{Median} - 2\text{Mean}, \quad \text{Median} = l + \left(\frac{N/2 - CF}{f}\right)h",
            "summary": "Computation of median and mode for discrete and continuous distributions, and Pearson empirical relationship.",
            "common_traps": r"Sum of absolute deviations is minimum when taken about the MEDIAN ($\Sigma |x_i - M| = \text{min}$), whereas sum of squared deviations is minimum about the MEAN ($\Sigma (x_i - \bar{x})^2 = \text{min}$).",
            "tips_and_tricks": "Mean is heavily sensitive to extreme outlier values, while Median is robust against outliers."
        }
    ]
}

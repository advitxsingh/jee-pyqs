"""
Curated Concept Taxonomy for all Physics Chapters in JEE Main and KCET.
Covers 30 canonical syllabus chapters with standard formulas, common traps, and key tips.
"""

PHYSICS_TAXONOMY = {
    "units-and-measurements": [
        {
            "name": "Dimensional Analysis & Principle of Homogeneity",
            "category": "Dimensions",
            "primary": ["dimension", "dimensional", "homogeneity", "mlt", "m^", "l^", "t^", "planck constant", "gravitational constant", "permittivity"],
            "formula_cues": [r"[m", r"[l", r"[t", r"\text{dimension}"],
            "standard_formulas": r"[G] = M^{-1}L^3T^{-2}, \quad [h] = ML^2T^{-1}, \quad [\mu_0] = MLT^{-2}A^{-2}",
            "summary": "Application of dimensions to check equation consistency and derive relations between physical quantities.",
            "common_traps": "Trigonometric, logarithmic, and exponential arguments must strictly be dimensionless.",
            "tips_and_tricks": "Equate powers of M, L, T on both sides to find unknown exponents."
        },
        {
            "name": "Error Analysis & Significant Figures",
            "category": "Errors",
            "primary": ["percentage error", "fractional error", "relative error", "vernier", "screw gauge", "least count", "zero error", "measured value", "significant figures"],
            "formula_cues": [r"\frac{\Delta x}{x}", r"\Delta", r"\pm", r"\%"],
            "standard_formulas": r"\frac{\Delta Z}{Z} = a\frac{\Delta A}{A} + b\frac{\Delta B}{B} + c\frac{\Delta C}{C} \quad \text{for } Z = \frac{A^a B^b}{C^c}",
            "summary": "Maximum fractional and percentage errors in combination of quantities and screw gauge / vernier calipers reading.",
            "common_traps": "Errors always ADD up in worst-case analysis; never subtract fractional errors.",
            "tips_and_tricks": "Least count = Pitch / (Number of circular divisions). Total reading = MSR + (CSR × LC) - (Zero Error)."
        }
    ],

    "motion-in-a-straight-line": [
        {
            "name": "Kinematic Equations & Free Fall",
            "category": "Kinematics",
            "primary": ["kinematic", "free fall", "dropped from", "thrown upward", "acceleration due to gravity", "maximum height", "time of flight", "equations of motion", "stopping distance"],
            "formula_cues": [r"v = u + at", r"v^2 = u^2", r"s = ut", r"h = \frac{u^2}{2g}"],
            "standard_formulas": r"v = u + at, \quad s = ut + \frac{1}{2}at^2, \quad v^2 = u^2 + 2as, \quad s_n = u + \frac{a}{2}(2n - 1)",
            "summary": "Uniformly accelerated rectilinear motion, vertical motion under gravity, and displacement in the nth second.",
            "common_traps": "Assign a consistent sign convention (e.g. upward positive, downward negative) at the beginning of problem solving.",
            "tips_and_tricks": r"Stopping distance $d \propto u^2$. For an object dropped from rest, distance ratio in successive seconds is $1 : 3 : 5 : 7$ (Galileo's odd numbers)."
        },
        {
            "name": "Velocity-Time & Position-Time Graphs",
            "category": "Graphical Analysis",
            "primary": ["graph", "v-t graph", "x-t graph", "slope", "area under", "acceleration-time", "velocity-displacement"],
            "formula_cues": [r"\frac{dx}{dt}", r"\frac{dv}{dt}", r"\int v dt", r"v \frac{dv}{dx}"],
            "standard_formulas": r"v = \frac{dx}{dt}, \quad a = \frac{dv}{dt} = v\frac{dv}{dx}, \quad \text{Displacement} = \int v\,dt",
            "summary": "Interpretation of motion curves: slope of x-t is velocity, slope of v-t is acceleration, area under v-t is displacement.",
            "common_traps": "Area under speed-time curve gives distance (always positive), while area under velocity-time curve gives displacement.",
            "tips_and_tricks": r"When $a$ is given as a function of $x$, use $a = v\frac{dv}{dx}$ rather than $\frac{dv}{dt}$."
        }
    ],

    "motion-in-a-plane": [
        {
            "name": "Projectile Motion & Trajectory",
            "category": "Projectiles",
            "primary": ["projectile", "trajectory", "angle of projection", "horizontal range", "maximum height", "time of flight", "elevation angle"],
            "formula_cues": [r"u \cos\theta", r"u \sin\theta", r"\frac{u^2 \sin 2\theta}{g}", r"\frac{u^2 \sin^2\theta}{2g}"],
            "standard_formulas": r"T = \frac{2u\sin\theta}{g}, \quad H = \frac{u^2\sin^2\theta}{2g}, \quad R = \frac{u^2\sin 2\theta}{g}, \quad y = x\tan\theta\left(1 - \frac{x}{R}\right)",
            "summary": "2D motion under constant gravity with independent horizontal and vertical components.",
            "common_traps": r"Range is identical for complementary angles $(\theta \text{ and } 90^\circ - \theta)$, but flight time and maximum height differ.",
            "tips_and_tricks": r"Equation of trajectory form $y = x\tan\theta(1 - x/R)$ allows fast calculation of range when trajectory coordinates are given."
        },
        {
            "name": "Relative Velocity in 2D (Rain-Man & River-Swimmer)",
            "category": "Relative Motion",
            "primary": ["relative velocity", "rain", "umbrella", "swimmer", "river", "shortest path", "shortest time", "drift", "crossing"],
            "formula_cues": [r"\vec{v}_{AB}", r"\vec{v}_r - \vec{v}_m", r"\frac{d}{v \cos\theta}"],
            "standard_formulas": r"\vec{v}_{A/B} = \vec{v}_A - \vec{v}_B, \quad t_{\text{min}} = \frac{d}{v_{\text{br}}}, \quad \text{Drift} = (v_r - v_{\text{br}}\sin\theta)t",
            "summary": "Relative vector addition in planar motion, umbrella holding angle for rain, and river crossing optimization.",
            "common_traps": r"To cross a river in shortest time, head perpendicular to the river flow ($\theta = 90^\circ$ relative to bank).",
            "tips_and_tricks": r"To cross with zero drift (shortest path), swim upstream such that $\sin\theta = \frac{v_{\text{river}}}{v_{\text{swimmer}}}$ (requires $v_{\text{swimmer}} > v_{\text{river}}$)."
        }
    ],

    "laws-of-motion": [
        {
            "name": "Newton's Laws & Free Body Diagrams",
            "category": "Dynamics",
            "primary": ["newton", "free body", "tension", "pulley", "normal force", "pseudo force", "elevator", "lift", "contact force", "acceleration of system"],
            "formula_cues": [r"\Sigma F = ma", r"T - mg", r"m(g + a)", r"m(g - a)"],
            "standard_formulas": r"\Sigma \vec{F} = m\vec{a}, \quad T = \frac{2m_1 m_2}{m_1 + m_2}g, \quad a = \frac{m_2 - m_1}{m_1 + m_2}g",
            "summary": "Equations of motion for connected bodies, string-pulley constraints, and apparent weight in non-inertial frames.",
            "common_traps": "In an accelerating elevator with upward acceleration $a$, apparent weight is $N = m(g + a)$, NOT $m(g - a)$.",
            "tips_and_tricks": r"Use string constraint $\Sigma T_i \cdot x_i = 0 \implies \Sigma T_i \cdot a_i = 0$ to relate accelerations in complex pulley systems."
        },
        {
            "name": "Friction (Static, Limiting & Kinetic)",
            "category": "Friction",
            "primary": ["friction", "coefficient of friction", "limiting friction", "kinetic friction", "rough", "incline", "angle of repose", "block on block"],
            "formula_cues": [r"\mu N", r"\mu_s", r"\mu_k", r"f_s \le \mu_s N", r"\tan\theta = \mu"],
            "standard_formulas": r"f_{\text{max}} = \mu_s N, \quad f_k = \mu_k N, \quad \theta_{\text{repose}} = \tan^{-1}\mu_s, \quad a = g(\sin\theta - \mu_k\cos\theta)",
            "summary": r"Static self-adjusting friction up to limiting value $\mu_s N$ and constant kinetic friction $\mu_k N$ on rough surfaces.",
            "common_traps": r"Static friction is self-adjusting: $f_s = F_{\text{applied}}$ as long as $F_{\text{applied}} \le \mu_s N$. It does NOT automatically equal $\mu_s N$.",
            "tips_and_tricks": "In two-block systems, find the maximum common acceleration allowed by friction before determining if slipping occurs."
        }
    ],

    "work-energy-and-power": [
        {
            "name": "Work-Energy Theorem & Conservative Forces",
            "category": "Work & Energy",
            "primary": ["work energy theorem", "work done", "conservative force", "potential energy", "kinetic energy", "spring force", "spring potential"],
            "formula_cues": [r"W_{\text{net}} = \Delta K", r"\frac{1}{2}kx^2", r"F = -\frac{dU}{dx}", r"\int \vec{F} \cdot d\vec{r}"],
            "standard_formulas": r"W_{\text{net}} = \Delta K, \quad W_{\text{ext}} = \Delta K + \Delta U, \quad F = -\frac{dU}{dx}, \quad U_{\text{spring}} = \frac{1}{2}kx^2",
            "summary": "Work-energy theorem relating net work to change in kinetic energy, and potential energy gradients for conservative forces.",
            "common_traps": "Work done by static friction on a pure-rolling body is strictly ZERO because the point of contact is instantaneously at rest.",
            "tips_and_tricks": r"Stable equilibrium occurs where $\frac{dU}{dx} = 0$ and $\frac{d^2U}{dx^2} > 0$ (local potential minimum)."
        },
        {
            "name": "Power & Collisions (Elastic & Inelastic)",
            "category": "Collisions & Power",
            "primary": ["power", "collision", "elastic collision", "inelastic", "coefficient of restitution", "head-on", "loss of kinetic energy"],
            "formula_cues": [r"P = \vec{F} \cdot \vec{v}", r"e = \frac{v_2 - v_1}{u_1 - u_2}", r"\Delta K = \frac{1}{2}\frac{m_1 m_2}{m_1 + m_2}(u_1 - u_2)^2"],
            "standard_formulas": r"P = \vec{F} \cdot \vec{v} = \frac{dW}{dt}, \quad e = \frac{v_2 - v_1}{u_1 - u_2}, \quad \Delta K_{\text{loss}} = \frac{m_1 m_2}{2(m_1 + m_2)}(1 - e^2)(u_1 - u_2)^2",
            "summary": "Instantaneous power delivery, linear momentum conservation, and coefficient of restitution in 1D and 2D impacts.",
            "common_traps": "In perfectly inelastic collisions ($e = 0$), momentum is conserved, but kinetic energy is NOT conserved.",
            "tips_and_tricks": "For two equal masses undergoing head-on elastic collision ($e = 1$), they completely exchange velocities."
        }
    ],

    "center-of-mass": [
        {
            "name": "Center of Mass Calculation & Cut-out Sections",
            "category": "Center of Mass",
            "primary": ["center of mass", "centre of mass", "cut out", "cavity", "removed", "circular disc", "hemisphere", "uniform rod"],
            "formula_cues": [r"X_{\text{cm}} = \frac{\Sigma m_i x_i}{\Sigma m_i}", r"\frac{\int x dm}{M}", r"\frac{4R}{3\pi}", r"\frac{3R}{8}"],
            "standard_formulas": r"\vec{r}_{\text{cm}} = \frac{\Sigma m_i \vec{r}_i}{\Sigma m_i}, \quad \vec{r}_{\text{remaining}} = \frac{M\vec{r}_0 - m\vec{r}_{\text{removed}}}{M - m}",
            "summary": "Discrete and continuous center of mass coordinates, and negative mass method for cavity problems.",
            "common_traps": "Hemisphere CM is at $3R/8$ from center, whereas hemispherical shell CM is at $R/2$.",
            "tips_and_tricks": r"Treat a removed cavity as negative mass at the cavity's geometric center: $X_{\text{new}} = \frac{A_1 x_1 - A_2 x_2}{A_1 - A_2}$."
        },
        {
            "name": "Conservation of Linear Momentum & Explosion",
            "category": "Momentum",
            "primary": ["conservation of momentum", "explosion", "explodes", "bullet", "recoil", "external force", "f_ext = 0"],
            "formula_cues": [r"\vec{P} = \text{const}", r"m_1 v_1 + m_2 v_2", r"\vec{v}_{\text{cm}} = \frac{\Sigma m_i \vec{v}_i}{M}"],
            "standard_formulas": r"\vec{F}_{\text{ext}} = M\vec{a}_{\text{cm}}, \quad \text{If } \vec{F}_{\text{ext}} = 0 \implies \vec{v}_{\text{cm}} = \text{const}, \quad \Sigma m_i \vec{v}_i = \text{const}",
            "summary": "Motion of center of mass under zero net external force and explosive fragmentation trajectories.",
            "common_traps": "Internal forces (like explosion or spring expansion) cannot change the trajectory of the center of mass.",
            "tips_and_tricks": "If a projectile explodes mid-air, the center of mass continues along the original parabolic trajectory until fragments hit the ground."
        }
    ],

    "rotational-motion": [
        {
            "name": "Moment of Inertia & Parallel/Perpendicular Axes Theorems",
            "category": "Inertia",
            "primary": ["moment of inertia", "parallel axis", "perpendicular axis", "radius of gyration", "disc", "ring", "cylinder", "sphere", "rod"],
            "formula_cues": [r"I = \Sigma m r^2", r"I = I_{\text{cm}} + Md^2", r"I_z = I_x + I_y", r"I = Mk^2"],
            "standard_formulas": r"I = \int r^2 dm, \quad I = I_{\text{cm}} + Md^2, \quad I_z = I_x + I_y \quad (\text{laminar planar bodies})",
            "summary": r"Calculation of rotational inertia, radius of gyration $k = \sqrt{I/M}$, and axes shift theorems.",
            "common_traps": "Perpendicular axis theorem $I_z = I_x + I_y$ is strictly valid ONLY for 2D laminar (flat) objects lying in the xy-plane.",
            "tips_and_tricks": r"Solid sphere $I_{\text{cm}} = \frac{2}{5}MR^2$; hollow spherical shell $I_{\text{cm}} = \frac{2}{3}MR^2$; circular disc $I_{\text{cm}} = \frac{1}{2}MR^2$."
        },
        {
            "name": "Torque, Angular Momentum & Pure Rolling",
            "category": "Dynamics & Rolling",
            "primary": ["torque", "angular momentum", "pure rolling", "rolling without slipping", "conservation of angular momentum", "incline rolling"],
            "formula_cues": [r"\vec{\tau} = \vec{r} \times \vec{F}", r"\tau = I\alpha", r"L = I\omega", r"v_{\text{cm}} = R\omega", r"a_{\text{cm}} = \frac{g\sin\theta}{1 + I/MR^2}"],
            "standard_formulas": r"\vec{\tau} = I\vec{\alpha} = \frac{d\vec{L}}{dt}, \quad K_{\text{roll}} = \frac{1}{2}Mv_{\text{cm}}^2\left(1 + \frac{k^2}{R^2}\right), \quad a = \frac{g\sin\theta}{1 + k^2/R^2}",
            "summary": "Rotational analogue of Newton's second law, conservation of angular momentum, and rolling down an incline.",
            "common_traps": "On an incline, the body with the smallest $k^2/R^2$ reaches the bottom first (Solid Sphere > Solid Cylinder > Hollow Sphere > Ring).",
            "tips_and_tricks": r"In pure rolling on a flat surface, the instantaneous axis of rotation passes through the contact point ($v_{\text{contact}} = 0$)."
        }
    ],

    "gravitation": [
        {
            "name": "Gravitational Field & Potential",
            "category": "Field & Potential",
            "primary": ["gravitational field", "gravitational potential", "acceleration due to gravity", "variation of g", "depth", "altitude", "height h", "rotation of earth"],
            "formula_cues": [r"g = \frac{GM}{R^2}", r"g_h = g(1 - \frac{2h}{R})", r"g_d = g(1 - \frac{d}{R})", r"V = -\frac{GM}{r}"],
            "standard_formulas": r"g_h \approx g\left(1 - \frac{2h}{R}\right) \; (h \ll R), \quad g_d = g\left(1 - \frac{d}{R}\right), \quad V(r) = -\frac{GM}{r}",
            "summary": r"Newton's law of gravitation, variation of $g$ with height, depth, and latitude $\lambda$ ($g' = g - \omega^2 R \cos^2\lambda$).",
            "common_traps": r"At $h = R$ above Earth, $g_h = \frac{g}{(1 + 1)^2} = \frac{g}{4}$. The approximation $(1 - 2h/R)$ fails when $h$ is comparable to $R$!",
            "tips_and_tricks": r"Decrease in $g$ at height $h$ is double the decrease at depth $d$ for $h = d \ll R$."
        },
        {
            "name": "Orbital Velocity, Escape Velocity & Kepler's Laws",
            "category": "Satellites & Orbits",
            "primary": ["orbital velocity", "escape velocity", "satellite", "time period", "kepler", "areal velocity", "geostationary", "binding energy"],
            "formula_cues": [r"v_e = \sqrt{2gR}", r"v_o = \sqrt{\frac{GM}{r}}", r"T^2 \propto r^3", r"\frac{dA}{dt} = \frac{L}{2m}"],
            "standard_formulas": r"v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR} \approx 11.2\text{ km/s}, \quad v_o = \sqrt{\frac{GM}{r}}, \quad v_e = \sqrt{2}v_o, \quad T^2 = \frac{4\pi^2}{GM}r^3",
            "summary": "Orbital mechanics of satellites, escape speed from planetary surfaces, and Kepler's three laws of planetary motion.",
            "common_traps": r"Total energy of a bound satellite is negative: $E = -K = \frac{1}{2}U = -\frac{GMm}{2r}$.",
            "tips_and_tricks": r"Geostationary satellite period is 24 hours, orbits at height $\approx 36,000\text{ km}$ strictly in the equatorial plane from West to East."
        }
    ],

    "properties-of-matter": [
        {
            "name": "Elasticity & Hooke's Law",
            "category": "Solids",
            "primary": ["young's modulus", "bulk modulus", "modulus of rigidity", "poisson ratio", "stress", "strain", "hooke", "elongation", "elastic potential energy"],
            "formula_cues": [r"Y = \frac{FL}{A\Delta L}", r"B = -V\frac{\Delta P}{\Delta V}", r"U = \frac{1}{2} \text{stress} \times \text{strain}"],
            "standard_formulas": r"Y = \frac{F/A}{\Delta L/L}, \quad \Delta L = \frac{FL}{AY}, \quad u = \frac{1}{2}\sigma \epsilon = \frac{\sigma^2}{2Y}, \quad U = \frac{1}{2}F\Delta L",
            "summary": "Stress-strain relationships, Young's modulus, shear modulus, bulk modulus, and energy stored in stretched wires.",
            "common_traps": r"Elongation due to self-weight is $\Delta L = \frac{\rho g L^2}{2Y} = \frac{MgL}{2AY}$ (half of an equivalent end load $Mg$).",
            "tips_and_tricks": r"When two wires are in series, equivalent $Y$ is obtained by adding extensions: $\Delta L = \Delta L_1 + \Delta L_2$."
        },
        {
            "name": "Fluid Statics & Dynamics (Bernoulli & Torricelli)",
            "category": "Fluids",
            "primary": ["bernoulli", "pascal", "archimedes", "buoyant", "continuity equation", "efflux", "torricelli", "venturimeter", "gauge pressure"],
            "formula_cues": [r"P + \frac{1}{2}\rho v^2 + \rho gh", r"A_1 v_1 = A_2 v_2", r"v = \sqrt{2gh}", r"P = P_0 + \rho gh"],
            "standard_formulas": r"A_1 v_1 = A_2 v_2, \quad P + \frac{1}{2}\rho v^2 + \rho gh = \text{const}, \quad v_{\text{efflux}} = \sqrt{2gh}, \quad R = 2\sqrt{h(H - h)}",
            "summary": "Continuity equation, Bernoulli's energy conservation principle, Torricelli's efflux theorem, and hydraulic lift.",
            "common_traps": r"Speed of efflux is $\sqrt{2gh}$ where $h$ is depth from the free liquid surface, NOT height from the ground!",
            "tips_and_tricks": r"Maximum horizontal range of water jet occurs when hole is at mid-depth $h = H/2$, with $R_{\text{max}} = H$."
        },
        {
            "name": "Surface Tension & Viscosity (Stokes' Law)",
            "category": "Surface & Flow",
            "primary": ["surface tension", "capillary", "excess pressure", "soap bubble", "liquid drop", "viscosity", "terminal velocity", "stokes", "poiseuille", "reynolds"],
            "formula_cues": [r"\Delta P = \frac{2T}{R}", r"\Delta P = \frac{4T}{R}", r"h = \frac{2T\cos\theta}{\rho g r}", r"v_t = \frac{2}{9}\frac{r^2(\rho - \sigma)g}{\eta}"],
            "standard_formulas": r"\Delta P_{\text{drop}} = \frac{2T}{R}, \quad \Delta P_{\text{bubble}} = \frac{4T}{R}, \quad h = \frac{2T\cos\theta}{\rho g r}, \quad v_t = \frac{2r^2(\rho - \sigma)g}{9\eta}",
            "summary": "Surface energy, excess pressure in drops and bubbles, capillary rise formula, and terminal velocity of falling spheres.",
            "common_traps": r"A soap bubble in air has TWO liquid-air interfaces, so excess pressure is $\Delta P = \frac{4T}{R}$, while a liquid drop has ONE ($\Delta P = \frac{2T}{R}$).",
            "tips_and_tricks": r"Terminal velocity $v_t \propto r^2$. When $n$ identical droplets coalesce: $R = n^{1/3}r$, and surface energy is released: $\Delta U = 4\pi T r^2(n - n^{2/3})$."
        }
    ],

    "heat-and-thermodynamics": [
        {
            "name": "First Law & Thermodynamic Processes",
            "category": "First Law",
            "primary": ["first law", "isothermal", "adiabatic", "isochoric", "isobaric", "work done by gas", "internal energy", "p-v diagram", "heat supplied"],
            "formula_cues": [r"\Delta Q = \Delta U + W", r"\Delta U = nC_v\Delta T", r"W = nRT \ln", r"PV^\gamma = \text{const}"],
            "standard_formulas": r"\Delta Q = \Delta U + W, \quad \Delta U = n C_v \Delta T, \quad W_{\text{iso}} = nRT\ln\left(\frac{V_2}{V_1}\right), \quad W_{\text{adi}} = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1}",
            "summary": "First law of thermodynamics, molar heat capacities ($C_p - C_v = R$), and work done in cyclic/open processes.",
            "common_traps": r"Internal energy $\Delta U = nC_v\Delta T$ depends ONLY on temperature change $\Delta T$, regardless of whether the path is isobaric, isothermal, or adiabatic.",
            "tips_and_tricks": "In cyclic processes on a P-V diagram: clockwise cycles give positive net work (heat engine); counter-clockwise cycles give negative work (refrigerator)."
        },
        {
            "name": "Carnot Engine & Second Law Efficiency",
            "category": "Heat Engines",
            "primary": ["carnot", "efficiency", "heat engine", "refrigerator", "coefficient of performance", "source", "sink", "entropy"],
            "formula_cues": [r"\eta = 1 - \frac{T_2}{T_1}", r"\beta = \frac{T_2}{T_1 - T_2}", r"\frac{Q_2}{Q_1} = \frac{T_2}{T_1}"],
            "standard_formulas": r"\eta = 1 - \frac{Q_2}{Q_1} = 1 - \frac{T_2}{T_1}, \quad \text{COP } \beta = \frac{Q_2}{W} = \frac{T_2}{T_1 - T_2}, \quad \beta = \frac{1 - \eta}{\eta}",
            "summary": "Carnot cycle efficiency limit, reversible refrigerators, and Clausius/Kelvin-Planck statements.",
            "common_traps": r"Temperatures $T_1$ (source) and $T_2$ (sink) MUST strictly be substituted in Kelvin ($K$), never in Celsius ($^\circ\text{C}$).",
            "tips_and_tricks": r"To maximize Carnot efficiency, lowering sink temperature $T_2$ by $\Delta T$ is more effective than raising source temperature $T_1$ by the same $\Delta T$."
        },
        {
            "name": "Kinetic Theory of Gases & Thermal Radiation",
            "category": "KTG & Radiation",
            "primary": ["rms velocity", "degrees of freedom", "equipartition", "mean free path", "stefan", "wien", "newton law of cooling", "black body"],
            "formula_cues": [r"v_{\text{rms}} = \sqrt{\frac{3RT}{M}}", r"E = \sigma T^4", r"\lambda_m T = b", r"-\frac{dT}{dt} = k(T - T_0)"],
            "standard_formulas": r"v_{\text{rms}} = \sqrt{\frac{3RT}{M}}, \quad v_{\text{avg}} = \sqrt{\frac{8RT}{\pi M}}, \quad \lambda_m T = b, \quad E = e\sigma A T^4, \quad \frac{T_1 - T_2}{t} = K\left(\frac{T_1 + T_2}{2} - T_0\right)",
            "summary": r"Molecular speeds, energy equipartition $E = \frac{f}{2}nRT$, Stefan-Boltzmann law, Wien's displacement law, and Newton's law of cooling.",
            "common_traps": r"Degrees of freedom: Monatomic $f = 3$ ($\gamma = 5/3$); Diatomic at room temp $f = 5$ ($\gamma = 7/5$); Polyatomic non-linear $f = 6$ ($\gamma = 4/3$).",
            "tips_and_tricks": r"Net heat radiated by a body at temperature $T$ in surroundings $T_0$ is $P_{\text{net}} = e\sigma A(T^4 - T_0^4)$."
        }
    ],

    "simple-harmonic-motion": [
        {
            "name": "Kinematics & Dynamics of SHM",
            "category": "SHM Basics",
            "primary": ["shm", "simple harmonic", "amplitude", "angular frequency", "phase", "phase constant", "time period of shm", "velocity in shm", "acceleration in shm"],
            "formula_cues": [r"x = A\sin(\omega t", r"v = \omega\sqrt{A^2 - x^2}", r"a = -\omega^2 x", r"\omega = \sqrt{\frac{k}{m}}"],
            "standard_formulas": r"x(t) = A\sin(\omega t + \phi), \quad v = \omega\sqrt{A^2 - x^2}, \quad a = -\omega^2 x, \quad T = 2\pi\sqrt{\frac{m}{k}}",
            "summary": r"Differential equation of SHM $\frac{d^2x}{dt^2} + \omega^2 x = 0$, displacement, velocity, acceleration, and phase relations.",
            "common_traps": r"Velocity leads displacement by $\pi/2$; acceleration leads displacement by $\pi$ rad (opposite phase).",
            "tips_and_tricks": r"At mean position ($x = 0$): $v_{\text{max}} = A\omega$, $a = 0$. At extreme ($x = \pm A$): $v = 0$, $a_{\text{max}} = \omega^2 A$."
        },
        {
            "name": "Energy in SHM & Spring-Pendulum Systems",
            "category": "Energy & Systems",
            "primary": ["kinetic energy in shm", "potential energy in shm", "total energy", "spring constant", "spring combination", "simple pendulum", "effective length"],
            "formula_cues": [r"E = \frac{1}{2}m\omega^2 A^2", r"K = \frac{1}{2}m\omega^2(A^2 - x^2)", r"U = \frac{1}{2}m\omega^2 x^2", r"T = 2\pi\sqrt{\frac{l}{g}}"],
            "standard_formulas": r"E_{\text{total}} = \frac{1}{2}m\omega^2 A^2 = \frac{1}{2}kA^2 = \text{const}, \quad T_{\text{spring}} = 2\pi\sqrt{\frac{m}{k}}, \quad T_{\text{pendulum}} = 2\pi\sqrt{\frac{l}{g}}",
            "summary": "Energy oscillation in SHM (frequency of $K$ and $U$ is $2f$), springs in series/parallel, and simple pendulum period.",
            "common_traps": r"Kinetic energy and potential energy oscillate at TWICE the frequency ($2\omega$) of displacement.",
            "tips_and_tricks": r"When a spring of constant $k$ is cut into ratio $1 : n$, the parts have constants $k_1 = k(n+1)$ and $k_2 = k\frac{n+1}{n}$."
        }
    ],

    "waves": [
        {
            "name": "Wave Equation & Velocity of Sound",
            "category": "Wave Motion",
            "primary": ["wave equation", "wave speed", "transverse wave", "longitudinal wave", "speed of sound", "string tension", "newton laplace", "wavelength"],
            "formula_cues": [r"y = A\sin(kx - \omega t)", r"v = \sqrt{\frac{T}{\mu}}", r"v = \sqrt{\frac{\gamma P}{\rho}}", r"k = \frac{2\pi}{\lambda}"],
            "standard_formulas": r"y(x,t) = A\sin(kx \mp \omega t + \phi), \quad v = \frac{\omega}{k} = f\lambda, \quad v_{\text{string}} = \sqrt{\frac{T}{\mu}}, \quad v_{\text{gas}} = \sqrt{\frac{\gamma RT}{M}}",
            "summary": r"Progressive traveling harmonic waves, wave vector $k = 2\pi/\lambda$, and Laplace-corrected speed of sound in gases.",
            "common_traps": r"Maximum particle velocity $v_{\text{particle, max}} = A\omega$ is completely different from wave propagation velocity $v = f\lambda$.",
            "tips_and_tricks": r"Wave travels in positive x-direction if signs of $kx$ and $\omega t$ are OPPOSITE: $\sin(kx - \omega t)$."
        },
        {
            "name": "Standing Waves, Resonance & Doppler Effect",
            "category": "Interference & Acoustics",
            "primary": ["standing wave", "organ pipe", "open pipe", "closed pipe", "harmonics", "overtones", "resonance", "end correction", "beats", "doppler"],
            "formula_cues": [r"f = \frac{nv}{2L}", r"f = \frac{(2n-1)v}{4L}", r"f_{\text{beat}} = |f_1 - f_2|", r"f' = f\left(\frac{v \pm v_o}{v \mp v_s}\right)"],
            "standard_formulas": r"f_{\text{open}} = \frac{n v}{2L} \; (n=1,2,3), \quad f_{\text{closed}} = \frac{(2n-1)v}{4L} \; (n=1,2,3), \quad f' = f\left(\frac{v \pm v_0}{v \mp v_s}\right), \quad f_{\text{beat}} = |f_1 - f_2|",
            "summary": "Stationary waves in strings and organ pipes, beat frequency, and Doppler frequency shift for moving sources and observers.",
            "common_traps": r"A closed organ pipe produces ONLY odd harmonics ($1, 3, 5\dots$). The first overtone is the 3rd harmonic ($3v/4L$).",
            "tips_and_tricks": "Doppler rule: When distance decreases, apparent frequency INCREASES; when distance increases, apparent frequency DECREASES."
        }
    ],

    "electrostatics": [
        {
            "name": "Coulomb's Law, Electric Field & Dipole",
            "category": "Forces & Fields",
            "primary": ["coulomb", "electric field", "point charge", "electric dipole", "dipole moment", "axial point", "equatorial", "torque on dipole", "potential energy of dipole"],
            "formula_cues": [r"F = \frac{1}{4\pi\epsilon_0}\frac{q_1 q_2}{r^2}", r"\vec{p} = q(2\vec{a})", r"E_{\text{axial}} = \frac{2kp}{r^3}", r"\tau = \vec{p} \times \vec{E}"],
            "standard_formulas": r"F = \frac{q_1 q_2}{4\pi\epsilon_0 r^2}, \quad E_{\text{axial}} = \frac{2kp}{r^3}, \quad E_{\text{equatorial}} = \frac{kp}{r^3}, \quad \vec{\tau} = \vec{p} \times \vec{E}, \quad U = -\vec{p} \cdot \vec{E}",
            "summary": "Electrostatic forces, electric field intensity due to point charges and dipoles, and dipole torque/energy in uniform fields.",
            "common_traps": r"$E_{\text{axial}} = 2E_{\text{equatorial}}$ for a short dipole. $\vec{E}_{\text{equatorial}}$ points opposite to dipole moment $\vec{p}$.",
            "tips_and_tricks": r"Work done in rotating dipole from $\theta_1$ to $\theta_2$: $W = pE(\cos\theta_1 - \cos\theta_2)$."
        },
        {
            "name": "Gauss's Law & Electrostatic Potential",
            "category": "Flux & Potential",
            "primary": ["gauss", "electric flux", "gaussian surface", "conducting sphere", "non-conducting sphere", "infinite sheet", "cylindrical shell", "potential difference", "equipotential"],
            "formula_cues": [r"\oint \vec{E} \cdot d\vec{A} = \frac{q_{\text{encl}}}{\epsilon_0}", r"V = \frac{kq}{r}", r"E = -\frac{dV}{dr}", r"\sigma/\epsilon_0"],
            "standard_formulas": r"\Phi_E = \oint \vec{E} \cdot d\vec{A} = \frac{q_{\text{in}}}{\epsilon_0}, \quad E = \frac{\sigma}{2\epsilon_0} \text{ (sheet)}, \quad E = \frac{\lambda}{2\pi\epsilon_0 r} \text{ (wire)}, \quad \vec{E} = -\vec{\nabla}V",
            "summary": r"Gauss's flux theorem, symmetry applications (infinite sheet, cylinder, sphere), and electric potential gradient $\vec{E} = -\vec{\nabla}V$.",
            "common_traps": r"Inside a charged hollow conducting sphere, electric field is ZERO, but potential is NON-ZERO and constant: $V_{\text{inside}} = \frac{kq}{R}$.",
            "tips_and_tricks": "Electric field lines are always perpendicular to equipotential surfaces and point in the direction of steepest potential decrease."
        }
    ],

    "capacitor": [
        {
            "name": "Capacitance & Dielectric Insertion",
            "category": "Capacitance",
            "primary": ["capacitor", "capacitance", "parallel plate", "dielectric", "dielectric constant", "slab", "inserted", "charge on capacitor", "induced surface charge"],
            "formula_cues": [r"C = \frac{\epsilon_0 A}{d}", r"C = \frac{K\epsilon_0 A}{d}", r"C = \frac{\epsilon_0 A}{d - t + t/K}", r"Q = CV"],
            "standard_formulas": r"C_0 = \frac{\epsilon_0 A}{d}, \quad C = \frac{K\epsilon_0 A}{d}, \quad C_{\text{slab}} = \frac{\epsilon_0 A}{d - t(1 - 1/K)}, \quad q_p = q\left(1 - \frac{1}{K}\right)",
            "summary": "Parallel plate capacitance, dielectric polarization, and partial dielectric slab insertion.",
            "common_traps": r"If battery remains CONNECTED: $V = \text{const}$, $C$ increases by $K \implies Q$ increases by $K$. If battery is DISCONNECTED: $Q = \text{const} \implies V$ decreases by $1/K$.",
            "tips_and_tricks": r"Energy stored $U = \frac{1}{2}CV^2 = \frac{Q^2}{2C}$. When dielectric is inserted with disconnected battery, $U$ decreases because electrostatic attraction does work."
        },
        {
            "name": "Capacitor Networks & Energy Redistribution",
            "category": "Circuits & Energy",
            "primary": ["series combination", "parallel combination", "equivalent capacitance", "common potential", "loss of energy", "heat produced", "sharing of charge"],
            "formula_cues": [r"\frac{1}{C_s} = \frac{1}{C_1} + \frac{1}{C_2}", r"C_p = C_1 + C_2", r"V_c = \frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}", r"\Delta U = \frac{1}{2}\frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2"],
            "standard_formulas": r"C_{\text{parallel}} = \Sigma C_i, \quad \frac{1}{C_{\text{series}}} = \Sigma \frac{1}{C_i}, \quad V_{\text{common}} = \frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}, \quad \Delta U_{\text{loss}} = \frac{C_1 C_2}{2(C_1 + C_2)}(V_1 - V_2)^2",
            "summary": "Equivalent capacitance reduction, charge sharing between interconnected capacitors, and Joule heating loss.",
            "common_traps": "When connecting with opposite polarity, use numerator $(C_1 V_1 - C_2 V_2)$ for common potential.",
            "tips_and_tricks": r"Energy loss during charge sharing $\Delta U_{\text{loss}}$ is completely independent of wire resistance; it always turns into heat and EM radiation."
        }
    ],

    "current-electricity": [
        {
            "name": "Ohm's Law, Drift Velocity & Resistance Temperature",
            "category": "Conduction",
            "primary": ["drift velocity", "mobility", "current density", "relaxation time", "temperature coefficient of resistance", "color code", "internal resistance"],
            "formula_cues": [r"I = n e A v_d", r"v_d = \frac{e E \tau}{m}", r"R_t = R_0(1 + \alpha \Delta T)", r"j = \sigma E"],
            "standard_formulas": r"I = n e A v_d, \quad v_d = \frac{e E \tau}{m}, \quad \rho = \frac{m}{n e^2 \tau}, \quad R(T) = R_0(1 + \alpha \Delta T), \quad \vec{J} = \sigma \vec{E}",
            "summary": r"Microscopic model of electrical conduction, electron mobility $\mu = v_d/E$, and thermal variation of resistivity.",
            "common_traps": r"For conductors, $\alpha > 0$ (resistance increases with temperature). For semiconductors, $\alpha < 0$ (resistance decreases with temperature).",
            "tips_and_tricks": "When a wire is stretched to $n$ times its initial length while preserving volume, its resistance becomes $n^2 R$."
        },
        {
            "name": "Kirchhoff's Laws, Wheatstone Bridge & Potentiometer",
            "category": "DC Instruments",
            "primary": ["kirchhoff", "wheatstone", "potentiometer", "meter bridge", "galvanometer", "shunt", "voltmeter", "ammeter", "null deflection", "balancing length"],
            "formula_cues": [r"\frac{P}{Q} = \frac{R}{S}", r"\frac{E_1}{E_2} = \frac{l_1}{l_2}", r"r = R(\frac{l_1}{l_2} - 1)", r"S = \frac{I_g G}{I - I_g}"],
            "standard_formulas": r"\frac{P}{Q} = \frac{R}{S} \text{ (Wheatstone)}, \quad \frac{E_1}{E_2} = \frac{l_1}{l_2}, \quad r = R\left(\frac{l_1}{l_2} - 1\right), \quad S = \frac{I_g G}{I - I_g}, \quad R_{\text{series}} = \frac{V}{I_g} - G",
            "summary": "Kirchhoff's junction and loop rules, balanced bridges, potentiometer EMF comparison, and galvanometer conversion.",
            "common_traps": "A potentiometer measures EMF with zero drawn current, making it infinitely superior to a real voltmeter which always draws finite current.",
            "tips_and_tricks": "To convert galvanometer to ammeter: connect small shunt $S$ in parallel. To voltmeter: connect high resistance $R$ in series."
        }
    ],

    "moving-charges-and-magnetism": [
        {
            "name": "Biot-Savart Law & Ampere's Circuital Law",
            "category": "Magnetic Field",
            "primary": ["biot savart", "ampere circuital", "magnetic field at center", "circular coil", "solenoid", "toroid", "straight conductor", "axis of coil"],
            "formula_cues": [r"B = \frac{\mu_0 I}{2\pi r}", r"B = \frac{\mu_0 N I}{2R}", r"B = \frac{\mu_0 N I R^2}{2(R^2 + x^2)^{3/2}}", r"B = \mu_0 n I"],
            "standard_formulas": r"dB = \frac{\mu_0 I dl \sin\theta}{4\pi r^2}, \quad B_{\text{wire}} = \frac{\mu_0 I}{2\pi d}, \quad B_{\text{center}} = \frac{\mu_0 N I}{2R}, \quad B_{\text{solenoid}} = \mu_0 n I",
            "summary": "Calculation of magnetic fields generated by steady currents in wires, loops, and solenoids.",
            "common_traps": r"In solenoid formula $B = \mu_0 n I$, $n$ is number of turns per UNIT LENGTH ($n = N/L$), not total turns $N$.",
            "tips_and_tricks": "Right-hand thumb rule: thumb points along current, curled fingers give direction of circular magnetic field lines."
        },
        {
            "name": "Lorentz Force, Cyclotron & Magnetic Force on Wires",
            "category": "Magnetic Forces",
            "primary": ["lorentz force", "cyclotron", "helical path", "magnetic force", "radius of circular path", "pitch", "parallel conductors", "force per unit length"],
            "formula_cues": [r"\vec{F} = q(\vec{v} \times \vec{B})", r"r = \frac{mv}{qB}", r"T = \frac{2\pi m}{qB}", r"F/L = \frac{\mu_0 I_1 I_2}{2\pi d}"],
            "standard_formulas": r"\vec{F} = q(\vec{E} + \vec{v} \times \vec{B}), \quad r = \frac{mv}{qB} = \frac{\sqrt{2mK}}{qB}, \quad T = \frac{2\pi m}{qB}, \quad \frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}",
            "summary": r"Trajectory of charged particles in magnetic fields, velocity selector ($\vec{E} \perp \vec{B}$), and force between parallel currents.",
            "common_traps": r"Magnetic force $\vec{F} = q(\vec{v} \times \vec{B})$ does ZERO work because $\vec{F} \perp \vec{v}$. It changes direction of velocity, never kinetic energy!",
            "tips_and_tricks": "Parallel currents in the SAME direction ATTRACT; anti-parallel currents REPEL."
        }
    ],

    "magnetic-properties-of-matter": [
        {
            "name": "Magnetic Dipole Moment & Earth's Magnetism",
            "category": "Dipoles & Terrestrial",
            "primary": ["magnetic dipole", "magnetic moment", "bohr magneton", "dipole in magnetic field", "earth magnetism", "angle of dip", "declination", "horizontal component"],
            "formula_cues": [r"M = I A", r"\mu_B = \frac{eh}{4\pi m}", r"B_H = B \cos\delta", r"B_V = B \sin\delta", r"\tan\delta = \frac{B_V}{B_H}"],
            "standard_formulas": r"\vec{M} = I\vec{A} = N I A, \quad \mu_B = \frac{e\hbar}{2m} \approx 9.27 \times 10^{-24}\text{ A m}^2, \quad B_H = B\cos\delta, \quad \tan\delta = \frac{B_V}{B_H}",
            "summary": "Current loops as magnetic dipoles, orbital electron magnetic moment, and elements of Earth's magnetic field.",
            "common_traps": r"At the magnetic equator, dip angle $\delta = 0^\circ$ ($B_V = 0$). At magnetic poles, dip angle $\delta = 90^\circ$ ($B_H = 0$).",
            "tips_and_tricks": r"Apparent dip $\delta_1, \delta_2$ in two mutually perpendicular vertical planes: $\cot^2\delta = \cot^2\delta_1 + \cot^2\delta_2$."
        },
        {
            "name": "Magnetic Materials (Dia, Para, Ferro) & Hysteresis",
            "category": "Materials",
            "primary": ["diamagnetic", "paramagnetic", "ferromagnetic", "susceptibility", "permeability", "curie law", "hysteresis", "retentivity", "coercivity"],
            "formula_cues": [r"\chi = \frac{M}{H}", r"\mu_r = 1 + \chi", r"\chi \propto \frac{1}{T}", r"\chi = \frac{C}{T - T_c}"],
            "standard_formulas": r"\vec{B} = \mu_0(\vec{H} + \vec{M}), \quad \mu_r = 1 + \chi, \quad \chi_{\text{para}} = \frac{C}{T}, \quad \chi_{\text{ferro}} = \frac{C}{T - T_c}",
            "summary": "Classification of magnetic materials, Curie-Weiss law, and hysteresis loop area (energy dissipation).",
            "common_traps": r"Diamagnetic materials have small negative susceptibility $\chi < 0$ that is strictly independent of temperature.",
            "tips_and_tricks": "Permanent magnets require high retentivity and high coercivity (e.g. Alnico). Transformer cores require high permeability and low hysteresis loss (soft iron)."
        }
    ],

    "electromagnetic-induction": [
        {
            "name": "Faraday'S Law & Lenz's Law",
            "category": "Core Principle",
            "primary": ["magnetic flux", "faraday", "lenz", "induced emf", "dphi/dt", "flux change"],
            "formula_cues": [r"\mathcal{E} = -\frac{d\Phi}{dt}", r"\Phi = BA\cos\theta"],
            "standard_formulas": r"\mathcal{E} = -\frac{d\Phi}{dt}, \quad \Phi = \vec{B} \cdot \vec{A}, \quad q = \frac{\Delta\Phi}{R}",
            "summary": "Electromagnetic induction, Lenz's conservation of energy rule, and induced charge flow independent of time.",
            "common_traps": r"Total induced charge flown $\Delta q = \Delta\Phi/R$ does NOT depend on the time interval over which flux changed.",
            "tips_and_tricks": r"Peak induced EMF in rotating coil: $\mathcal{E}_0 = N B A \omega$."
        },
        {
            "name": "Motional EMF & Inductance",
            "category": "Motional & Inductance",
            "primary": ["motional emf", "bvl", "self inductance", "mutual inductance", "solenoid", "eddy current"],
            "formula_cues": [r"Bvl", r"\frac{1}{2}B\omega L^2", r"L = \mu_0 n^2 A l", r"M = k\sqrt{L_1 L_2}"],
            "standard_formulas": r"\mathcal{E} = Bvl, \quad \mathcal{E}_{\text{rot}} = \frac{1}{2}B\omega L^2, \quad \mathcal{E} = -L\frac{di}{dt}, \quad U = \frac{1}{2}LI^2",
            "summary": "Motional EMF in moving/rotating conductors, self-inductance of solenoids, and magnetic energy storage.",
            "common_traps": r"At $t = 0^+$ an inductor acts as an open circuit; at $t \to \infty$ it behaves as a short wire.",
            "tips_and_tricks": "Mutual inductance reciprocity holds: $M_{12} = M_{21}$ regardless of turn difference."
        }
    ],

    "alternating-current": [
        {
            "name": "LCR Series Resonance & Impedance",
            "category": "LCR Circuits",
            "primary": ["lcr", "impedance", "resonance", "resonant frequency", "power factor", "quality factor", "q-factor", "reactance"],
            "formula_cues": [r"Z = \sqrt{R^2 + (X_L - X_C)^2}", r"\omega_0 = \frac{1}{\sqrt{LC}}", r"\cos\phi = \frac{R}{Z}", r"Q = \frac{\omega_0 L}{R}"],
            "standard_formulas": r"Z = \sqrt{R^2 + (X_L - X_C)^2}, \quad \omega_0 = \frac{1}{\sqrt{LC}}, \quad \cos\phi = \frac{R}{Z}, \quad Q = \frac{1}{R}\sqrt{\frac{L}{C}}",
            "summary": r"Impedance of RLC circuits, series resonance where $X_L = X_C \implies Z_{\text{min}} = R$, and sharpness $Q$.",
            "common_traps": r"At resonance, the voltages across inductor and capacitor are equal and opposite in phase ($\Delta\phi = \pi$), cancelling out!",
            "tips_and_tricks": r"Average power dissipated in AC circuit: $P_{\text{avg}} = V_{\text{rms}} I_{\text{rms}} \cos\phi$. For pure L or C, $P_{\text{avg}} = 0$ (wattless current)."
        },
        {
            "name": "Transformers & AC Power",
            "category": "Transformers",
            "primary": ["transformer", "step up", "step down", "turns ratio", "efficiency of transformer", "eddy current losses", "hysteresis loss"],
            "formula_cues": [r"\frac{V_s}{V_p} = \frac{N_s}{N_p}", r"\frac{I_p}{I_s}", r"\eta = \frac{V_s I_s}{V_p I_p}"],
            "standard_formulas": r"\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}, \quad \eta = \frac{P_{\text{out}}}{P_{\text{in}}} = \frac{V_s I_s \cos\phi_s}{V_p I_p \cos\phi_p}",
            "summary": "Step-up and step-down transformers, voltage-to-current inverse transformation, and core loss mechanisms.",
            "common_traps": "Transformers work STRICTLY with AC; applying steady DC produces zero EMF in the secondary and burns the primary winding.",
            "tips_and_tricks": "Core lamination reduces eddy current heating by interrupting conductive loops."
        }
    ],

    "electromagnetic-waves": [
        {
            "name": "Displacement Current & Maxwell's Equations",
            "category": "Maxwell",
            "primary": ["displacement current", "maxwell", "ampere maxwell", "conduction current", "capacitor charging"],
            "formula_cues": [r"I_d = \epsilon_0 \frac{d\Phi_E}{dt}", r"\oint \vec{B} \cdot d\vec{l} = \mu_0(I_c + I_d)"],
            "standard_formulas": r"I_d = \epsilon_0 \frac{d\Phi_E}{dt}, \quad \oint \vec{B} \cdot d\vec{l} = \mu_0\left(I_c + \epsilon_0\frac{d\Phi_E}{dt}\right)",
            "summary": "Maxwell's correction to Ampere's law, displacement current inside charging capacitor dielectric space.",
            "common_traps": "Inside the charging capacitor plates, conduction current is 0 and displacement current equals $I_c$; in the wire, displacement current is 0.",
            "tips_and_tricks": r"Continuity of current holds everywhere: $I_{\text{conduction}} = I_{\text{displacement}}$."
        },
        {
            "name": "EM Wave Characteristics & Spectrum",
            "category": "EM Spectrum",
            "primary": ["electromagnetic spectrum", "speed of light", "pointing vector", "energy density", "radiation pressure", "radio waves", "microwaves", "infrared", "ultraviolet", "x-rays", "gamma rays"],
            "formula_cues": [r"c = \frac{1}{\sqrt{\mu_0\epsilon_0}}", r"E_0 = c B_0", r"u = \frac{1}{2}\epsilon_0 E^2 + \frac{B^2}{2\mu_0}", r"S = \frac{1}{\mu_0}(\vec{E} \times \vec{B})"],
            "standard_formulas": r"c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = \frac{E_0}{B_0}, \quad u_{\text{avg}} = \epsilon_0 E_{\text{rms}}^2 = \frac{B_{\text{rms}}^2}{\mu_0}, \quad I = u_{\text{avg}} c = \frac{E_0 B_0}{2\mu_0}",
            "summary": r"Transverse nature of EM waves ($\vec{E} \perp \vec{B} \perp \vec{k}$), Poynting vector, energy density, and frequency bands of spectrum.",
            "common_traps": "In an EM wave, the energy is distributed EQUALLY between electric and magnetic fields: $u_E = u_B$.",
            "tips_and_tricks": "Radiation pressure on perfect absorbing surface: $P = I/c$; on perfect reflecting surface: $P = 2I/c$."
        }
    ],

    "ray-optics": [
        {
            "name": "Reflection at Spherical Mirrors & Mirror Formula",
            "category": "Mirrors",
            "primary": ["mirror formula", "concave mirror", "convex mirror", "focal length", "magnification", "real image", "virtual image"],
            "formula_cues": [r"\frac{1}{v} + \frac{1}{u} = \frac{1}{f}", r"m = -\frac{v}{u}", r"f = \frac{R}{2}"],
            "standard_formulas": r"\frac{1}{v} + \frac{1}{u} = \frac{1}{f}, \quad m = -\frac{v}{u} = \frac{f}{f - u}, \quad f = \frac{R}{2}",
            "summary": "Image formation by concave and convex mirrors, Cartesian sign convention, and linear/longitudinal magnification.",
            "common_traps": "Concave mirror has negative focal length ($f < 0$); convex mirror has positive focal length ($f > 0$).",
            "tips_and_tricks": "Virtual image in a concave mirror is ALWAYS magnified ($|m| > 1$), while in a convex mirror it is ALWAYS diminished ($|m| < 1$)."
        },
        {
            "name": "Refraction at Interfaces, Snell's Law & TIR",
            "category": "Refraction",
            "primary": ["snell", "refractive index", "total internal reflection", "critical angle", "apparent depth", "normal shift", "optical fiber"],
            "formula_cues": [r"n_1 \sin\theta_1 = n_2 \sin\theta_2", r"\sin C = \frac{1}{\mu}", r"d_{\text{apparent}} = \frac{d}{\mu}", r"\Delta t = t(1 - \frac{1}{\mu})"],
            "standard_formulas": r"n_1 \sin i = n_2 \sin r, \quad \sin\theta_c = \frac{n_2}{n_1} \; (n_1 > n_2), \quad d' = \frac{d}{\mu}, \quad \text{Shift} = t\left(1 - \frac{1}{\mu}\right)",
            "summary": r"Snell's law, apparent depth shift in transparent media, and total internal reflection condition ($i \ge \theta_c$ from denser to rarer).",
            "common_traps": "Total internal reflection can ONLY occur when light travels from an optically DENSER medium to a RARER medium.",
            "tips_and_tricks": r"Area of circle through which light emerges from fish/source at depth $h$: $A = \frac{\pi h^2}{\mu^2 - 1}$."
        },
        {
            "name": "Prism Dispersion & Minimum Deviation",
            "category": "Prisms",
            "primary": ["prism", "angle of deviation", "minimum deviation", "dispersive power", "dispersion without deviation", "deviation without dispersion"],
            "formula_cues": [r"\delta = i + e - A", r"\mu = \frac{\sin(\frac{A + \delta_m}{2})}{\sin(A/2)}", r"\delta = (\mu - 1)A", r"\omega = \frac{\mu_v - \mu_r}{\mu_y - 1}"],
            "standard_formulas": r"\delta = i + e - A, \quad \mu = \frac{\sin\left(\frac{A + \delta_m}{2}\right)}{\sin(A/2)}, \quad \delta \approx (\mu - 1)A \; (\text{thin prism})",
            "summary": "Ray refraction through triangular prisms, condition for minimum deviation ($i = e, r_1 = r_2 = A/2$), and angular dispersion.",
            "common_traps": "At minimum deviation, the refracted ray inside an equilateral prism passes strictly PARALLEL to the base.",
            "tips_and_tricks": r"Condition for no emergent ray (always TIR on second face): $A > 2\theta_c$."
        },
        {
            "name": "Lens Maker's Formula & Optical Instruments",
            "category": "Lenses & Instruments",
            "primary": ["lens maker", "convex lens", "concave lens", "combination of lenses", "power of lens", "compound microscope", "astronomical telescope", "magnifying power"],
            "formula_cues": [r"\frac{1}{f} = (\mu - 1)(\frac{1}{R_1} - \frac{1}{R_2})", r"P = \frac{1}{f}", r"m = -\frac{v_0}{u_0}(1 + \frac{D}{f_e})", r"M = \frac{f_o}{f_e}"],
            "standard_formulas": r"\frac{1}{f} = (\mu - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right), \quad P = \frac{1}{f}, \quad M_{\text{telescope}} = \frac{f_o}{f_e}, \quad M_{\text{microscope}} = \frac{L}{f_o}\frac{D}{f_e}",
            "summary": "Thin lens refraction, Lens Maker's equation, lens power in Dioptres ($P = 1/f$), and magnifying power of optical devices.",
            "common_traps": r"When a lens is immersed in a liquid of refractive index $\mu_l > \mu_{\text{glass}}$, its converging/diverging nature REVERSES (convex acts concave).",
            "tips_and_tricks": "When a lens is cut vertically in half, each half retains the SAME focal length $f$. When cut horizontally, focal length remains $f$, but image brightness is halved."
        }
    ],

    "wave-optics": [
        {
            "name": "Huygens' Principle & Interference (YDSE)",
            "category": "Interference",
            "primary": ["young double slit", "ydse", "fringe width", "maxima", "minima", "path difference", "phase difference", "coherent sources", "slit width ratio"],
            "formula_cues": [r"\beta = \frac{\lambda D}{d}", r"\Delta x = \frac{yd}{D}", r"I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\phi", r"\Delta x = n\lambda"],
            "standard_formulas": r"\Delta x = \frac{y d}{D}, \quad \beta = \frac{\lambda D}{d}, \quad I_{\text{max}} = (\sqrt{I_1} + \sqrt{I_2})^2, \quad \text{Shift due to slab} = \frac{(\mu - 1)t D}{d}",
            "summary": r"Wavefront geometry, Young's double slit interference, fringe width $\beta = \lambda D/d$, and fringe shift on introducing thin mica sheet.",
            "common_traps": r"Fringe width $\beta$ depends on wavelength ($\beta \propto \lambda$). If YDSE is immersed in water ($\mu = 4/3$), fringe width decreases by factor of $4/3$.",
            "tips_and_tricks": r"Number of fringes shifted when a transparent slab of thickness $t$ is placed: $N = \frac{(\mu - 1)t}{\lambda}$."
        },
        {
            "name": "Diffraction & Polarization (Brewster's & Malus' Law)",
            "category": "Diffraction & Polarization",
            "primary": ["single slit diffraction", "central maximum", "angular width", "airy disc", "resolving power", "polarization", "brewster", "malus", "polaroid"],
            "formula_cues": [r"a \sin\theta = n\lambda", r"\beta_0 = \frac{2\lambda D}{a}", r"I = I_0 \cos^2\theta", r"\tan i_p = \mu"],
            "standard_formulas": r"a\sin\theta = n\lambda \text{ (minima)}, \quad \beta_0 = \frac{2\lambda D}{a} \text{ (central max)}, \quad I = I_0 \cos^2\theta \text{ (Malus)}, \quad \tan i_p = \mu \text{ (Brewster)}",
            "summary": "Fraunhofer single-slit diffraction, width of central bright maximum, Brewster's angle, and Malus' intensity law for polarized light.",
            "common_traps": r"In single slit diffraction, minima occur at $a\sin\theta = n\lambda$, whereas in YDSE interference, maxima occur at $d\sin\theta = n\lambda$!",
            "tips_and_tricks": r"At Brewster's angle of incidence $i_p$, the reflected ray and refracted ray are mutually PERPENDICULAR ($i_p + r = 90^\circ$)."
        }
    ],

    "dual-nature-of-radiation": [
        {
            "name": "Photoelectric Effect & Einstein's Equation",
            "category": "Photoelectric",
            "primary": ["photoelectric", "work function", "threshold frequency", "stopping potential", "einstein photoelectric", "kinetic energy of photoelectron", "cut-off wavelength"],
            "formula_cues": [r"h\nu = \phi + K_{\text{max}}", r"eV_0 = K_{\text{max}}", r"K_{\text{max}} = h(\nu - \nu_0)", r"\phi = h\nu_0 = \frac{hc}{\lambda_0}"],
            "standard_formulas": r"E = h\nu = \phi_0 + K_{\text{max}}, \quad K_{\text{max}} = e V_s = h(\nu - \nu_0) = hc\left(\frac{1}{\lambda} - \frac{1}{\lambda_0}\right)",
            "summary": r"Quantum nature of light, work function $\phi_0$, threshold frequency $\nu_0$, and stopping potential $V_s$ dependence on frequency.",
            "common_traps": "Stopping potential depends solely on FREQUENCY and work function; it is completely independent of intensity of incident light!",
            "tips_and_tricks": r"Slope of stopping potential vs frequency curve is always universal: $\text{Slope} = h/e$."
        },
        {
            "name": "De Broglie Hypothesis & Matter Waves",
            "category": "Matter Waves",
            "primary": ["de broglie", "matter wave", "wavelength of electron", "accelerated through potential", "davisson germer", "thermal neutron"],
            "formula_cues": [r"\lambda = \frac{h}{p}", r"\lambda = \frac{h}{\sqrt{2mK}}", r"\lambda = \frac{h}{\sqrt{2mqV}}", r"\lambda_e = \frac{12.27}{\sqrt{V}}"],
            "standard_formulas": r"\lambda = \frac{h}{p} = \frac{h}{\sqrt{2mE}} = \frac{h}{\sqrt{2mqV}}, \quad \lambda_{\text{electron}} \approx \frac{1.227}{\sqrt{V}}\text{ nm} = \frac{12.27}{\sqrt{V}}\text{ \AA}",
            "summary": "Dual wave-particle nature of moving particles, de Broglie wavelength under electrostatic acceleration $V$, and thermal gas particles.",
            "common_traps": r"For neutral particles (neutrons), de Broglie wavelength is $\lambda = \frac{h}{\sqrt{3mkT}}$, where $k$ is Boltzmann constant.",
            "tips_and_tricks": r"For proton vs alpha particle accelerated through same voltage $V$: $\frac{\lambda_p}{\lambda_\alpha} = \sqrt{\frac{m_\alpha q_\alpha}{m_p q_p}} = \sqrt{4 \times 2} = 2\sqrt{2}$."
        }
    ],

    "atoms-and-nuclei": [
        {
            "name": "Bohr's Hydrogen Model & Spectral Series",
            "category": "Atomic Models",
            "primary": ["bohr model", "radius of bohr orbit", "velocity in orbit", "energy of hydrogen", "rydberg", "lyman", "balmer", "paschen", "bracket", "pfund", "ionization energy"],
            "formula_cues": [r"r_n = 0.529 \frac{n^2}{Z}", r"E_n = -13.6 \frac{Z^2}{n^2}", r"\frac{1}{\lambda} = R Z^2(\frac{1}{n_1^2} - \frac{1}{n_2^2})"],
            "standard_formulas": r"r_n = 0.529\frac{n^2}{Z}\text{ \AA}, \quad v_n = 2.18 \times 10^6 \frac{Z}{n}\text{ m/s}, \quad E_n = -13.6\frac{Z^2}{n^2}\text{ eV}, \quad \frac{1}{\lambda} = R Z^2\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)",
            "summary": r"Quantization of angular momentum $L = n\hbar$, orbital radii, energy levels of hydrogenic species ($Z$), and emission lines.",
            "common_traps": "Balmer series lines fall in the VISIBLE spectrum ($n_1 = 2$). Lyman series lines fall in the ULTRAVIOLET ($n_1 = 1$).",
            "tips_and_tricks": r"Total number of spectral lines emitted when electron de-excites from state $n$ to ground state is $N = \frac{n(n-1)}{2}$."
        },
        {
            "name": "Nuclear Physics, Binding Energy & Radioactivity",
            "category": "Nuclear Physics",
            "primary": ["mass defect", "binding energy", "binding energy per nucleon", "nuclear density", "half life", "decay constant", "activity", "radioactive", "becquerel", "curie", "fission", "fusion"],
            "formula_cues": [r"\Delta E = \Delta m c^2", r"N(t) = N_0 e^{-\lambda t}", r"T_{1/2} = \frac{\ln 2}{\lambda}", r"A = \lambda N", r"R = R_0 A^{1/3}"],
            "standard_formulas": r"R = R_0 A^{1/3}, \quad \Delta E_b = [Z m_p + (A - Z)m_n - M_{\text{nuc}}]c^2, \quad N(t) = N_0 e^{-\lambda t}, \quad T_{1/2} = \frac{0.693}{\lambda} \approx 0.693\tau",
            "summary": r"Nuclear radius scaling $R \propto A^{1/3}$, constant nuclear density, mass defect conversion ($1\text{ amu} \approx 931.5\text{ MeV}$), and radioactive decay law.",
            "common_traps": r"Nuclear density is CONSTANT ($\approx 2.3 \times 10^{17}\text{ kg/m}^3$) and completely independent of the mass number $A$!",
            "tips_and_tricks": r"Amount remaining after $n$ half-lives: $N = \frac{N_0}{2^n}$, where $n = t / T_{1/2}$."
        }
    ],

    "electronic-devices": [
        {
            "name": "p-n Junction Diode & Zener Diode Regulation",
            "category": "Semiconductor Diodes",
            "primary": ["p-n junction", "forward bias", "reverse bias", "depletion layer", "barrier potential", "rectifier", "half wave", "full wave", "zener diode", "voltage regulator", "breakdown"],
            "formula_cues": [r"i = i_0(e^{ev/\eta kt} - 1)", r"v_z = \text{const}", r"r_d = \frac{\Delta v}{\Delta i}", r"\eta = \frac{P_{\text{dc}}}{P_{\text{ac}}}"],
            "standard_formulas": r"\text{Efficiency}_{\text{half-wave}} = 40.6\%, \quad \text{Efficiency}_{\text{full-wave}} = 81.2\%, \quad V_L = V_Z = \text{const}, \quad I_S = I_Z + I_L",
            "summary": "Forward and reverse characteristics of p-n junctions, rectifiers, ripple frequency, and Zener diode shunt voltage stabilization.",
            "common_traps": r"In full-wave rectifiers, output ripple frequency is TWICE the AC input frequency ($2f_{\text{in}}$), whereas for half-wave it is $f_{\text{in}}$.",
            "tips_and_tricks": r"In reverse breakdown, Zener diode maintains constant voltage $V_Z$ across its terminals as long as $I_Z \ge I_{Z,\text{min}}$."
        },
        {
            "name": "Logic Gates & Truth Tables",
            "category": "Digital Electronics",
            "primary": ["logic gate", "truth table", "boolean", "and gate", "or gate", "not gate", "nand gate", "nor gate", "xor", "de morgan"],
            "formula_cues": [r"y = a \cdot b", r"y = a + b", r"\overline{a \cdot b} = \overline{a} + \overline{b}", r"\overline{a + b} = \overline{a} \cdot \overline{b}"],
            "standard_formulas": r"\text{NAND: } Y = \overline{A \cdot B}, \quad \text{NOR: } Y = \overline{A + B}, \quad \overline{A \cdot B} = \overline{A} + \overline{B}, \quad \overline{A + B} = \overline{A} \cdot \overline{B}",
            "summary": "Universal logic gates (NAND and NOR), De Morgan's theorems, and Boolean circuit reduction.",
            "common_traps": "NAND and NOR gates are UNIVERSAL gates: any Boolean function can be constructed using only NAND or only NOR gates.",
            "tips_and_tricks": r"Connect inputs of a NAND or NOR gate together to obtain a NOT gate: $\overline{A \cdot A} = \overline{A}$."
        }
    ],

    "communication-systems": [
        {
            "name": "Amplitude Modulation & Sideband Analysis",
            "category": "Modulation",
            "primary": ["modulation", "modulation index", "amplitude modulation", "carrier wave", "sideband", "bandwidth", "am wave", "demodulation", "am signal"],
            "formula_cues": [r"\mu = \frac{A_m}{A_c}", r"\text{bandwidth} = 2f_m", r"P_t = P_c(1 + \frac{\mu^2}{2})", r"A_{\text{max}}"],
            "standard_formulas": r"\mu = \frac{A_m}{A_c} = \frac{A_{\text{max}} - A_{\text{min}}}{A_{\text{max}} + A_{\text{min}}}, \quad \text{Bandwidth} = 2f_m, \quad P_t = P_c\left(1 + \frac{\mu^2}{2}\right)",
            "summary": r"Principles of amplitude modulation, carrier and sideband components $(f_c \pm f_m)$, modulation index, and power relationships.",
            "common_traps": r"Modulation index $\mu$ must satisfy $\mu \le 1$ ($100\%$) to prevent envelope distortion.",
            "tips_and_tricks": r"Carrier power does not depend on modulation index $\mu$, only sideband power increases as $\mu$ increases."
        },
        {
            "name": "EM Wave Propagation & Space Communication",
            "category": "Wave Propagation",
            "primary": ["sky wave", "ground wave", "space wave", "line of sight", "antenna height", "coverage distance", "critical frequency", "skip distance", "maximum usable frequency", "muf", "ionosphere"],
            "formula_cues": [r"d = \sqrt{2Rh_t} + \sqrt{2Rh_r}", r"f_c = 9\sqrt{N_{\text{max}}}", r"f_{\text{muf}} = \frac{f_c}{\cos\theta}", r"d_{\text{max}}"],
            "standard_formulas": r"d_{\text{max}} = \sqrt{2Rh_T} + \sqrt{2Rh_R}, \quad f_c = 9\sqrt{N_{\text{max}}}, \quad f_{\text{MUF}} = f_c \sec\theta_i, \quad \text{Antenna length } \ge \frac{\lambda}{4}",
            "summary": r"Propagation modes of electromagnetic waves (ground, sky, and space waves), critical frequency, MUF, and antenna LOS range calculations.",
            "common_traps": r"Ensure earth radius $R \approx 6400\,\text{km}$ and heights $h_T, h_R$ are converted into the exact same units before square rooting.",
            "tips_and_tricks": r"For an antenna of height $h$, maximum range is $d = \sqrt{2Rh}$, and population covered is $\pi d^2 \times \rho$."
        }
    ]
}

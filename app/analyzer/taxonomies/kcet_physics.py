"""
Dedicated KCET Physics Taxonomy.
Tailored specifically to the Karnataka CET exam pattern, NCERT/PUC syllabus,
and authentic past year questions.
"""

from typing import Dict, List, Any

KCET_PHYSICS_TAXONOMY: Dict[str, List[Dict[str, Any]]] = {
    "kcet-units-and-measurement-and-dimensions": [
        {
            "name": "Dimensional Analysis & Physical Constants",
            "category": "Dimensions & Units",
            "primary": ["dimensions of", "dimensional formula", "permeability", "permittivity", "planck's constant", "gravitational constant", "stefan", "boltzmann", "dimensionless"],
            "formula_cues": [r"m^1 l^1 t^{-2}", r"m l^2 t^{-1}", r"\mu_0 \varepsilon_0", r"m l^2 t^{-2}"],
            "secondary": ["fundamental", "derived", "quantity", "formula"],
            "summary": "Dimensional analysis of physical constants and equations. Determining dimensions of $\\varepsilon_0, \\mu_0, h, G$ and testing homogeneity of physical equations.",
            "standard_formulas": r"[h] = [ML^2T^{-1}], \quad [G] = [M^{-1}L^3T^{-2}], \quad \left[\frac{1}{\sqrt{\mu_0\varepsilon_0}}\right] = [LT^{-1}]",
            "common_traps": "Confusing angular momentum $[ML^2T^{-1}]$ with linear momentum $[MLT^{-1}]$, or torque with work (same dimensions $[ML^2T^{-2}]$ but different physical natures).",
            "tips_and_tricks": "In KCET, use the speed of light relation $c = 1/\\sqrt{\\mu_0\\varepsilon_0}$ to find dimensions of $(\\mu_0\\varepsilon_0)^{-1/2}$ in 2 seconds without computing $\\mu_0$ or $\\varepsilon_0$ separately."
        },
        {
            "name": "Errors in Measurement & Vernier / Screw Gauge",
            "category": "Experimental Physics",
            "primary": ["vernier", "screw gauge", "pitch", "least count", "percentage error", "relative error", "fractional error", "main scale", "circular scale"],
            "formula_cues": [r"\frac{\\Delta z}{z}", r"\text{least count}", r"\frac{\text{pitch}}{\text{divisions}}"],
            "secondary": ["divisions", "measurement", "reading"],
            "summary": "Calculation of least count for Vernier calipers ($1\\text{ MSD} - 1\\text{ VSD}$) and Screw Gauge ($\\text{Pitch} / \\text{Total divisions}$). Error propagation in products and powers: $\\frac{\\Delta Z}{Z} = a\\frac{\\Delta A}{A} + b\\frac{\\Delta B}{B}$.",
            "standard_formulas": r"\text{LC} = 1\text{ MSD} - 1\text{ VSD}, \quad Z = A^a B^b \implies \frac{\\Delta Z}{Z} = a\frac{\\Delta A}{A} + b\frac{\\Delta B}{B}",
            "common_traps": "When calculating percentage error, remember that powers multiply the fractional error: if $Z = A^3$, the error in $A$ is multiplied by 3!",
            "tips_and_tricks": "Always check zero error: Positive zero error must be subtracted from the observed reading; negative zero error must be added."
        }
    ],

    "kcet-motion-in-a-straight-line": [
        {
            "name": "Uniformly Accelerated Rectilinear Motion & Stopping Distance",
            "category": "1D Kinematics",
            "primary": ["uniform acceleration", "stopping distance", "retardation", "distance travelled", "initial velocity", "final velocity", "reaction time", "brakes applied", "ratio of distances"],
            "formula_cues": [r"v = u + at", r"s = ut + \frac{1}{2}at^2", r"v^2 - u^2 = 2as", r"s_n = u + \frac{a}{2}(2n-1)"],
            "secondary": ["speed", "time", "car", "meters"],
            "summary": "Equations of motion for constant acceleration. Distance covered in $n$-th second $S_n = u + \\frac{a}{2}(2n-1)$. Stopping distance $d_s = \\frac{u^2}{2a} \\propto u^2$.",
            "standard_formulas": r"v^2 = u^2 + 2as, \quad S_n = u + \frac{a}{2}(2n-1), \quad d_{\text{stop}} = \frac{u^2}{2a}",
            "common_traps": "Stopping distance is proportional to $u^2$, NOT $u$. Doubling the vehicle speed quadruples the stopping distance!",
            "tips_and_tricks": "For a body starting from rest with uniform acceleration, distances travelled in successive equal time intervals are in the ratio $1 : 3 : 5 : 7 : \\dots$ (Galileo's odd number ratio)."
        },
        {
            "name": "Motion Under Gravity & Kinematic Graphs",
            "category": "Gravity & Graphs",
            "primary": ["freely falling", "dropped from height", "projected vertically upwards", "maximum height", "time of ascent", "v-t graph", "x-t graph", "area under v-t graph", "slope"],
            "formula_cues": [r"h = \frac{u^2}{2g}", r"t = \frac{u}{g}", r"\sqrt{2gh}", r"t_{\text{flight}} = \frac{2u}{g}"],
            "secondary": ["ball", "tower", "ground", "velocity"],
            "summary": "Vertical motion under gravity: Maximum height $H = \\frac{u^2}{2g}$, time of flight $T = \\frac{2u}{g}$, striking speed $v = \\sqrt{2gh}$. Slope of $x-t$ curve gives velocity; slope of $v-t$ curve gives acceleration; area under $v-t$ curve gives displacement.",
            "standard_formulas": r"H_{\max} = \frac{u^2}{2g}, \quad T_{\text{total}} = \frac{2u}{g}, \quad \text{Area under } v-t = \text{Displacement}",
            "common_traps": "At maximum height, vertical velocity is momentarily zero, but acceleration is still $g = 9.8\\text{ m/s}^2$ downwards!",
            "tips_and_tricks": "If a ball is dropped from height $h$ and another is projected vertically downwards with speed $u$, the difference in their velocities remains constant."
        }
    ],

    "kcet-motion-in-a-plane": [
        {
            "name": "Projectile Motion: Range, Maximum Height & Flight Time",
            "category": "2D Kinematics",
            "primary": ["projectile", "angle of projection", "horizontal range", "maximum height", "time of flight", "trajectory", "complementary angles", "speed at highest point"],
            "formula_cues": [r"r = \frac{u^2 \\sin 2\\theta}{g}", r"h = \frac{u^2 \\sin^2\\theta}{2g}", r"t = \frac{2u\\sin\\theta}{g}", r"y = x\tan\\theta - \frac{gx^2}{2u^2\\cos^2\\theta}"],
            "secondary": ["horizontal", "vertical", "elevation", "velocity"],
            "summary": "2D parabolic projectile motion under uniform downward gravity. Horizontal range $R = \\frac{u^2\\sin 2\\theta}{g}$, maximum height $H = \\frac{u^2\\sin^2\\theta}{2g}$, flight time $T = \\frac{2u\\sin\\theta}{g}$. Horizontal velocity $u\\cos\\theta$ remains invariant throughout.",
            "standard_formulas": r"R = \frac{u^2 \\sin 2\\theta}{g}, \quad H = \frac{u^2 \\sin^2\\theta}{2g}, \quad R_{\max} = \frac{u^2}{g} \ (\text{at } \\theta=45^\\circ)",
            "common_traps": "Horizontal range is identical for complementary angles $\\theta$ and $(90^\\circ - \\theta)$, but maximum heights and flight times are different!",
            "tips_and_tricks": "Relation between Range and Max Height: $R = 4H\\cot\\theta$. At $\\theta = 45^\\circ$, $R = 4H$."
        },
        {
            "name": "Relative Velocity in 2D (Rain-Man & River-Boat)",
            "category": "Relative Motion",
            "primary": ["relative velocity", "river", "boat", "swimmer", "rain falling", "umbrella", "shortest path", "shortest time", "drift", "crossing the river"],
            "formula_cues": [r"\vec{v}_{ab} = \vec{v}_a - \vec{v}_b", r"t = \frac{d}{v_b \\cos\\theta}", r"\\sin\\theta = \frac{v_r}{v_b}"],
            "secondary": ["downstream", "upstream", "stream", "speed"],
            "summary": "Relative velocity $\\vec{v}_{AB} = \\vec{v}_A - \\vec{v}_B$. Crossing a river in shortest time requires heading directly perpendicular to the bank ($t_{\\min} = d/v_b$). Crossing along the shortest path (zero drift) requires swimming upstream at $\\sin\\theta = v_r/v_b$.",
            "standard_formulas": r"t_{\min} = \frac{d}{v_b}, \quad \text{Shortest Path: } \\sin\\theta = \frac{v_{\text{river}}}{v_{\text{boat}}}, \quad \vec{v}_{\text{rain, man}} = \vec{v}_r - \vec{v}_m",
            "common_traps": "To protect from vertically falling rain when walking forward, hold the umbrella tilted FORWARD in the direction of motion at $\\tan\\theta = v_m/v_r$.",
            "tips_and_tricks": "Shortest path across a river is only possible if swimmer speed $v_b > v_r$. If $v_b < v_r$, zero drift is impossible."
        }
    ],

    "kcet-circular-motion": [
        {
            "name": "Kinematics of Circular Motion: Angular Velocity & Acceleration",
            "category": "Kinematics",
            "primary": ["uniform circular motion", "angular velocity", "angular acceleration", "complete revolution", "trajectory", "centripetal acceleration", "radial acceleration", "displacement of the athlete", "speed along circular"],
            "formula_cues": [r"\omega = \frac{v}{r}", r"a_c = \frac{v^2}{r}", r"\omega^2 r", r"(x-2)^2 + y^2 = 25"],
            "secondary": ["radius", "revolution", "circle", "track"],
            "summary": "Circular motion kinematics: $v = \\omega r$, centripetal acceleration $a_c = \\frac{v^2}{r} = \\omega^2 r$. In uniform circular motion (UCM), speed and kinetic energy are constant, but velocity and acceleration vectors continuously change direction.",
            "standard_formulas": r"v = r\omega, \quad a_c = \frac{v^2}{r} = \omega^2 r = 4\pi^2 f^2 r, \quad a_{\text{net}} = \sqrt{a_c^2 + a_t^2}",
            "common_traps": "After one complete revolution in UCM, total distance is $2\\pi r$, but net displacement is zero!",
            "tips_and_tricks": "In UCM, work done by the centripetal force is always identically zero ($W = 0$) because $\\vec{F}_c \\perp \\vec{v}$."
        },
        {
            "name": "Dynamics: Centripetal Force, Banking & Turntable Slipping",
            "category": "Dynamics & Problem Archetypes",
            "primary": ["centripetal force", "turntable", "coin placed on a rotating", "slips", "banking of roads", "angle of banking", "car is moving in a circular", "bob is suspended", "maximum safe speed"],
            "formula_cues": [r"\frac{mv^2}{r}", r"v = \sqrt{\mu r g}", r"\tan\\theta = \frac{v^2}{rg}", r"m \omega^2 r"],
            "secondary": ["friction", "string", "horizontal", "track"],
            "summary": "Centripetal force $F_c = \\frac{m v^2}{r} = m \\omega^2 r$. Slipping on a rotating turntable: $\\mu m g = m \\omega^2 r \\implies \\omega^2 r = \\text{const}$. Angle of banking for frictionless turning: $\\tan\\theta = \\frac{v^2}{r g}$.",
            "standard_formulas": r"F_c = \frac{m v^2}{r} = m \omega^2 r, \quad r_1 \omega_1^2 = r_2 \omega_2^2, \quad \tan\\theta = \frac{v^2}{r g}, \quad v_{\max} = \sqrt{\mu r g}",
            "common_traps": "For turntable coin problems, distance $r$ is inversely proportional to $\\omega^2$ ($r \\propto 1/\\omega^2$). If $\\omega$ is doubled, coin must be placed at $1/4$ the original distance to avoid slipping.",
            "tips_and_tricks": "For a suspended pendulum bob inside a car rounding a curve of radius $r$ at speed $v$, the string deflects by angle $\\tan\\theta = \\frac{v^2}{r g}$ from the vertical."
        }
    ],

    "kcet-laws-of-motion": [
        {
            "name": "Newton's Laws of Motion & Connected Systems (Pulleys)",
            "category": "Classical Dynamics",
            "primary": ["newton's second law", "impulse", "momentum", "pulley", "tension in string", "acceleration of blocks", "lift accelerating", "apparent weight in lift", "connected bodies"],
            "formula_cues": [r"f = ma", r"t = \frac{2m_1 m_2 g}{m_1 + m_2}", r"a = \frac{(m_1 - m_2)g}{m_1 + m_2}", r"w = m(g \pm a)"],
            "secondary": ["mass", "force", "string", "acceleration"],
            "summary": "Newton's laws: $\\vec{F} = \\frac{d\\vec{p}}{dt} = m\\vec{a}$, impulse $\\vec{J} = \\Delta\\vec{p} = \\vec{F}\\Delta t$. Connected systems on Atwood machine: $a = \\frac{(m_1-m_2)g}{m_1+m_2}$, tension $T = \\frac{2m_1m_2g}{m_1+m_2}$. Apparent weight in an elevator accelerating upward is $m(g+a)$; accelerating downward is $m(g-a)$.",
            "standard_formulas": r"a = \frac{F_{\text{net}}}{M_{\text{total}}}, \quad T_{\text{Atwood}} = \frac{2m_1m_2g}{m_1+m_2}, \quad W_{\text{app}} = m(g \pm a)",
            "common_traps": "In a free-falling lift ($a = g$), apparent weight is zero (weightlessness) and normal reaction $N = 0$.",
            "tips_and_tricks": "For pulley problems, treat the entire string assembly as one 1D system: $a = \\frac{\\text{Net Unbalanced Pulling Force}}{\\text{Total Inertial Mass}}$."
        },
        {
            "name": "Friction: Static, Kinetic & Inclined Plane Dynamics",
            "category": "Friction",
            "primary": ["friction", "coefficient of friction", "static friction", "limiting friction", "kinetic friction", "angle of repose", "inclined plane", "block sliding down", "minimum force to move"],
            "formula_cues": [r"f_s \le \mu_s n", r"f_k = \mu_k n", r"a = g(\\sin\\theta - \mu\\cos\\theta)", r"\tan\\theta = \mu"],
            "secondary": ["normal reaction", "slope", "rough surface"],
            "summary": "Static friction is self-adjusting up to limiting friction $f_L = \\mu_s N$. Kinetic friction $f_k = \\mu_k N$ (with $\\mu_k < \\mu_s$). Acceleration down a rough inclined plane: $a = g(\\sin\\theta - \\mu_k\\cos\\theta)$. Angle of repose $\\tan\\theta = \\mu_s$.",
            "standard_formulas": r"f_{\max} = \mu_s mg\\cos\\theta, \quad a = g(\\sin\\theta - \mu\\cos\\theta), \quad \tan\phi = \mu_s",
            "common_traps": "Static friction is NOT always equal to $\\mu_s N$; it equals the applied force up to the threshold $\\mu_s N$!",
            "tips_and_tricks": "Time taken to slide down a rough incline compared to smooth incline of same length: $t_{\\text{rough}} = n \\times t_{\\text{smooth}} \\implies \\mu = \\tan\\theta \\left(1 - \\frac{1}{n^2}\\right)$."
        }
    ],

    "kcet-work-energy-and-power": [
        {
            "name": "Work-Energy Theorem & Conservative Forces",
            "category": "Work & Energy",
            "primary": ["work done", "work-energy theorem", "kinetic energy", "potential energy", "conservative force", "spring force", "elongation of spring", "force-displacement graph"],
            "formula_cues": [r"w = \vec{f} \cdot \vec{d}", r"w_{\text{net}} = \\Delta k", r"u = \frac{1}{2} k x^2", r"p = \vec{f} \cdot \vec{v}"],
            "secondary": ["joules", "force", "displacement", "velocity"],
            "summary": "Work-Energy Theorem: $W_{\\text{net}} = \\Delta K = K_f - K_i$. Work done by variable force is area under $F-x$ curve. Potential energy of spring $U = \\frac{1}{2}kx^2$. Mechanical energy $E = K + U$ is conserved under conservative forces.",
            "standard_formulas": r"W = \int F dx = \\Delta K, \quad U_{\text{spring}} = \frac{1}{2} k x^2, \quad P = \vec{F} \cdot \vec{v} = \frac{dW}{dt}",
            "common_traps": "Work done by a perpendicular force (like centripetal force or magnetic Lorentz force) is strictly ZERO ($W=0$).",
            "tips_and_tricks": "Relation between kinetic energy $K$ and momentum $p$: $K = \\frac{p^2}{2m}$. If momentum increases by $100\\%$, kinetic energy increases by $300\\%$!"
        },
        {
            "name": "Power & Collisions (Elastic and Inelastic)",
            "category": "Collisions & Power",
            "primary": ["power", "engine", "collision", "coefficient of restitution", "elastic collision", "perfectly inelastic", "loss of kinetic energy", "head-on collision"],
            "formula_cues": [r"e = \frac{v_2 - v_1}{u_1 - u_2}", r"v_1 = \frac{m_1-m_2}{m_1+m_2}u_1", r"p = f v", r"\\Delta k = \frac{1}{2}\frac{m_1 m_2}{m_1+m_2}(u_1-u_2)^2"],
            "secondary": ["masses", "speeds", "velocity", "rebound"],
            "summary": "Instantaneous power $P = \\vec{F} \\cdot \\vec{v}$. Coefficient of restitution $e = \\frac{\\text{velocity of separation}}{\\text{velocity of approach}}$. In 1D elastic collision ($e=1$) between equal masses ($m_1=m_2$), velocities are completely exchanged! In perfectly inelastic collision ($e=0$), bodies stick together with common speed $v = \\frac{m_1 u_1 + m_2 u_2}{m_1 + m_2}$.",
            "standard_formulas": r"e = \frac{v_2 - v_1}{u_1 - u_2}, \quad v_{\text{common}} = \frac{m_1 u_1 + m_2 u_2}{m_1 + m_2}, \quad \\Delta K = \frac{m_1 m_2 (1-e^2)}{2(m_1+m_2)}(u_1 - u_2)^2",
            "common_traps": "Momentum is conserved in ALL collisions (elastic or inelastic); kinetic energy is conserved ONLY in perfectly elastic collisions.",
            "tips_and_tricks": "When a moving body hits an identical stationary body elastically ($m_1=m_2, u_2=0$), the incident body stops dead ($v_1=0$) and the target moves off with speed $v_2 = u_1$."
        }
    ],

    "kcet-center-of-mass": [
        {
            "name": "Center of Mass of Two-Particle & Continuous Systems",
            "category": "Center of Mass",
            "primary": ["center of mass", "centre of mass", "position vector", "two particles", "distance from origin", "shift in center of mass", "cut out", "disc", "system of particles"],
            "formula_cues": [r"r_{cm} = \frac{m_1 r_1 + m_2 r_2}{m_1 + m_2}", r"\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}", r"m_1 r_1 = m_2 r_2"],
            "secondary": ["mass", "coordinates", "distance", "origin"],
            "summary": "Position of center of mass $R_{cm} = \\frac{\\sum m_i r_i}{\\sum m_i}$. For a two-particle system, the center of mass divides the line joining them inversely as their masses ($m_1 r_1 = m_2 r_2$).",
            "standard_formulas": r"X_{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}, \quad r_1 = \frac{m_2}{m_1+m_2} d, \quad r_2 = \frac{m_1}{m_1+m_2} d",
            "common_traps": "Center of mass is closer to the heavier mass, not the geometric center.",
            "tips_and_tricks": "If no external horizontal force acts on a system ($F_{\\text{ext}} = 0$), the position of the center of mass remains completely unchanged even if internal parts move!"
        }
    ],

    "kcet-rotational-motion": [
        {
            "name": "Moment of Inertia & Theorems of Parallel / Perpendicular Axes",
            "category": "Rotational Inertia",
            "primary": ["moment of inertia", "radius of gyration", "parallel axis theorem", "perpendicular axis theorem", "circular ring", "circular disc", "solid sphere", "hollow sphere", "rod about center"],
            "formula_cues": [r"i = m k^2", r"i = i_{cm} + m d^2", r"i_z = i_x + i_y", r"\frac{1}{2} m r^2", r"\frac{2}{5} m r^2", r"\frac{1}{12} m l^2"],
            "secondary": ["axis", "diameter", "tangent", "mass"],
            "summary": "Moment of inertia $I = \\sum m_i r_i^2 = M k^2$. Parallel axis theorem: $I = I_{cm} + M d^2$. Perpendicular axis theorem for laminar bodies: $I_z = I_x + I_y$. Standard values: Ring about axis $M R^2$; Disc $\\frac{1}{2}M R^2$; Solid Sphere $\\frac{2}{5}M R^2$; Thin Rod $\\frac{1}{12}M L^2$.",
            "standard_formulas": r"I_{\text{disc}} = \frac{1}{2}MR^2, \quad I_{\text{solid sphere}} = \frac{2}{5}MR^2, \quad I_{\text{tangent}} = I_{cm} + Md^2",
            "common_traps": "Perpendicular axis theorem applies ONLY to flat planar (2D) lamina, NEVER to 3D objects like solid spheres or cylinders!",
            "tips_and_tricks": "For rolling bodies down an incline, acceleration is $a = \\frac{g\\sin\\theta}{1 + k^2/r^2}$. Smaller $k^2/r^2$ reaches bottom first: Solid Sphere ($0.4$) > Disc ($0.5$) > Ring ($1.0$)."
        },
        {
            "name": "Torque, Angular Momentum & Rotational Kinetic Energy",
            "category": "Rotational Dynamics",
            "primary": ["torque", "angular momentum", "conservation of angular momentum", "rotational kinetic energy", "angular acceleration", "wheel is rotating", "stopped by applying torque"],
            "formula_cues": [r"\tau = i \alpha", r"l = i \omega", r"k_{\text{rot}} = \frac{1}{2} i \omega^2", r"i_1 \omega_1 = i_2 \omega_2"],
            "secondary": ["omega", "rad/s", "revolutions", "torque"],
            "summary": "Rotational dynamics: Torque $\\tau = I\\alpha = \\frac{dL}{dt}$. Angular momentum $L = I\\omega = \\vec{r} \\times \\vec{p}$. If external torque is zero ($\\tau_{\\text{ext}} = 0$), angular momentum is conserved ($I_1\\omega_1 = I_2\\omega_2$). Rotational kinetic energy $K_{\\text{rot}} = \\frac{1}{2}I\\omega^2$.",
            "standard_formulas": r"\tau = I\alpha, \quad L = I\omega, \quad K_{\text{rot}} = \frac{1}{2}I\omega^2, \quad I_1\omega_1 = I_2\omega_2",
            "common_traps": "When a ballet dancer pulls in her arms, $I$ decreases, $\\omega$ increases, but rotational kinetic energy INCREASES due to internal muscular work done!",
            "tips_and_tricks": "Convert rpm to rad/s: $\\omega = \\frac{2\\pi N}{60}$. A common 1-step calculation in KCET rotational problems."
        }
    ],

    "kcet-gravitation": [
        {
            "name": "Newton's Law of Gravitation & Acceleration Due to Gravity (g)",
            "category": "Gravitational Field",
            "primary": ["gravitational force", "acceleration due to gravity", "value of g", "height above earth", "depth below surface", "latitude", "rotation of earth", "at the center of earth"],
            "formula_cues": [r"g = \frac{gm}{r^2}", r"g' = g\left(1 - \frac{2h}{r}\right)", r"g' = g\left(1 - \frac{d}{r}\right)", r"g' = g - \omega^2 r \\cos^2\lambda"],
            "secondary": ["earth", "radius", "surface", "weight"],
            "summary": "Gravitational acceleration at surface: $g = \\frac{GM}{R^2}$. Variation with height: $g_h = g(1 - 2h/R)$ (for $h \\ll R$) or $g_h = g\\frac{R^2}{(R+h)^2}$. Variation with depth: $g_d = g(1 - d/R)$ (strictly linear). At center of earth ($d=R$), $g=0$. Effect of rotation: $g' = g - \\omega^2 R \\cos^2\\lambda$.",
            "standard_formulas": r"g = \frac{GM}{R^2}, \quad g_h \approx g\left(1 - \frac{2h}{R}\right), \quad g_d = g\left(1 - \frac{d}{R}\right), \quad g_{\text{pole}} - g_{\text{equator}} = \omega^2 R",
            "common_traps": "Height variation decreases $g$ twice as fast as depth: at depth $d = 2h$, the decrease in $g$ matches the decrease at height $h$.",
            "tips_and_tricks": "Weight is maximum at the poles and minimum at the equator due to centrifugal relief from Earth's axial rotation."
        },
        {
            "name": "Orbital Velocity, Escape Speed & Kepler's Laws",
            "category": "Orbits & Satellites",
            "primary": ["escape speed", "escape velocity", "orbital speed", "orbital velocity", "time period of satellite", "kepler's third law", "geostationary satellite", "height of geostationary"],
            "formula_cues": [r"v_e = \sqrt{2gr}", r"v_o = \sqrt{gr}", r"v_e = \sqrt{2} v_o", r"t^2 \propto r^3", r"v_e = 11.2\text{ km/s}"],
            "secondary": ["satellite", "planet", "orbit", "radius"],
            "summary": "Escape velocity from surface $v_e = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR} \\approx 11.2\\text{ km/s}$. Orbital velocity for close orbit $v_o = \\sqrt{gR} \\approx 7.9\\text{ km/s}$. Key ratio: $v_e = \\sqrt{2} v_o$. Kepler's third law: $T^2 \\propto r^3$. Geostationary satellite: period $24\\text{ hours}$, height $\\approx 36,000\\text{ km}$, orbits west to east.",
            "standard_formulas": r"v_e = \sqrt{2gR} = \sqrt{2} v_o, \quad \left(\frac{T_1}{T_2}\right)^2 = \left(\frac{r_1}{r_2}\right)^3, \quad E_{\text{total}} = -K = \frac{U}{2} = -\frac{GMm}{2r}",
            "common_traps": "Escape velocity is completely INDEPENDENT of the mass of the projectile and the angle of projection!",
            "tips_and_tricks": "Total energy of an orbiting satellite is negative: $E = -K = U/2$. If orbital speed is increased by $41.4\\%$ (factor of $\\sqrt{2}$), the satellite escapes Earth's gravity."
        }
    ],

    "kcet-heat-and-thermodynamics": [
        {
            "name": "First Law of Thermodynamics & PV Thermodynamic Processes",
            "category": "Thermodynamic Laws",
            "primary": ["first law of thermodynamics", "internal energy", "work done by gas", "isothermal process", "adiabatic process", "isochoric", "isobaric", "gamma", "ratio of specific heats", "p-v diagram"],
            "formula_cues": [r"\\Delta q = \\Delta u + \\Delta w", r"p v^\gamma = \text{const}", r"w = nrt \ln\frac{v_2}{v_1}", r"w = \frac{p_1 v_1 - p_2 v_2}{\gamma - 1}", r"\\Delta u = n c_v \\Delta t"],
            "secondary": ["gas", "heat", "temperature", "pressure", "work"],
            "summary": "First Law: $\\Delta Q = \\Delta U + \\Delta W$. In isothermal process ($\\Delta T = 0$), $\\Delta U = 0 \\implies Q = W = nRT\\ln(V_2/V_1)$. In adiabatic process ($Q = 0$), $PV^\\gamma = \\text{const}$ and $W = -\\Delta U = \\frac{nR(T_1-T_2)}{\\gamma - 1}$. In isochoric process ($\\Delta V = 0$), $W = 0$. In isobaric process, $W = P\\Delta V$.",
            "standard_formulas": r"\\Delta Q = \\Delta U + \\Delta W, \quad PV^\gamma = \text{const}, \quad W_{\text{iso}} = nRT\ln\frac{V_2}{V_1}, \quad \\Delta U = n C_v \\Delta T",
            "common_traps": "Slope of an adiabatic curve on a $P-V$ diagram is $\\gamma$ times steeper than the isothermal curve: $(\\frac{dP}{dV})_{\\text{adia}} = \\gamma (\\frac{dP}{dV})_{\\text{iso}}$.",
            "tips_and_tricks": "Work done in a cyclic process equals the enclosed area of the loop on the $P-V$ diagram. Clockwise cycle $\\implies W > 0$ (Heat engine); Counter-clockwise $\\implies W < 0$ (Refrigerator)."
        },
        {
            "name": "Carnot Heat Engine Efficiency & Refrigerator COP",
            "category": "Heat Engines",
            "primary": ["carnot engine", "efficiency of carnot", "source temperature", "sink temperature", "refrigerator", "coefficient of performance", "heat absorbed", "heat rejected", "second law"],
            "formula_cues": [r"\eta = 1 - \frac{t_2}{t_1}", r"\eta = \frac{w}{q_1}", r"\beta = \frac{t_2}{t_1 - t_2}", r"\beta = \frac{1-\eta}{\eta}"],
            "secondary": ["kelvin", "temperatures", "engine", "sink"],
            "summary": "Carnot engine efficiency $\\eta = 1 - \\frac{T_2}{T_1} = \\frac{W}{Q_1}$ (temperatures strictly in Kelvin). Coefficient of performance (COP) of Carnot refrigerator $\\beta = \\frac{Q_2}{W} = \\frac{T_2}{T_1 - T_2}$. Relation between $\\beta$ and $\\eta$: $\\beta = \\frac{1-\\eta}{\\eta}$.",
            "standard_formulas": r"\eta = 1 - \frac{T_2}{T_1} = \frac{Q_1 - Q_2}{Q_1}, \quad \beta = \frac{T_2}{T_1 - T_2}, \quad T(\text{K}) = T(^\\circ\text{C}) + 273",
            "common_traps": "Substituting Celsius instead of Kelvin temperatures into $\\eta = 1 - T_2/T_1$. ALWAYS convert to Kelvin first!",
            "tips_and_tricks": "To double the efficiency of a Carnot engine, it is always more effective to lower the sink temperature $T_2$ than to raise the source temperature $T_1$ by the same amount."
        }
    ],

    "kcet-simple-harmonic-motion": [
        {
            "name": "SHM Kinematics & Energy Relations",
            "category": "Oscillations",
            "primary": ["simple harmonic motion", "displacement in shm", "velocity in shm", "acceleration in shm", "kinetic energy of shm", "potential energy in shm", "at mean position", "at extreme position", "amplitude"],
            "formula_cues": [r"x = a\\sin(\omega t + \phi)", r"v = \omega \sqrt{a^2 - x^2}", r"a = -\omega^2 x", r"k = \frac{1}{2}m\omega^2(a^2-x^2)", r"u = \frac{1}{2}m\omega^2 x^2"],
            "secondary": ["frequency", "maximum", "total energy", "particle"],
            "summary": "Kinematics of SHM: $x = A\\sin\\omega t$, $v = \\omega\\sqrt{A^2-x^2}$, $a = -\\omega^2 x$. At mean position ($x=0$): $v = v_{\\max} = A\\omega$, $a = 0$, $K$ is maximum. At extremes ($x=\\pm A$): $v = 0$, $a = a_{\\max} = \\omega^2 A$, $U$ is maximum. Total energy $E = \\frac{1}{2}m\\omega^2 A^2$ is constant at all positions.",
            "standard_formulas": r"v = \omega\sqrt{A^2 - x^2}, \quad a = -\omega^2 x, \quad E_{\text{total}} = \frac{1}{2}m\omega^2 A^2 = 2\pi^2 m f^2 A^2",
            "common_traps": "Kinetic and potential energy oscillate with frequency $2f$ (twice the frequency of displacement $x$)!",
            "tips_and_tricks": "At what displacement is $K = U$? When $x = \\frac{A}{\\sqrt{2}}$. At what displacement is $K = 3U$? When $x = \\frac{A}{2}$."
        },
        {
            "name": "Time Period of Simple Pendulum & Spring-Mass Systems",
            "category": "Oscillation Systems",
            "primary": ["time period of simple pendulum", "length of pendulum", "seconds pendulum", "spring mass system", "spring constant", "cutting of spring", "combination of springs"],
            "formula_cues": [r"t = 2\pi\sqrt{\frac{l}{g}}", r"t = 2\pi\sqrt{\frac{m}{k}}", r"k' = n k", r"t \propto \sqrt{l}"],
            "secondary": ["seconds", "vibration", "frequency", "pendulum"],
            "summary": "Time period of simple pendulum: $T = 2\\pi\\sqrt{\\frac{L}{g}}$. A seconds pendulum has period $T = 2\\text{ s}$ and length $L \\approx 1\\text{ m}$. Spring-mass system: $T = 2\\pi\\sqrt{\\frac{m}{k}}$. If a spring of constant $k$ is cut into $n$ equal parts, each part has stiffness $k' = n k$.",
            "standard_formulas": r"T_{\text{pendulum}} = 2\pi\sqrt{\frac{L}{g}}, \quad T_{\text{spring}} = 2\pi\sqrt{\frac{m}{k}}, \quad k \times L = \text{constant}",
            "common_traps": "Time period of a spring-mass system is independent of gravity $g$; taking a spring-mass oscillator to the Moon does not change its frequency!",
            "tips_and_tricks": "If the length of a pendulum increases by $2\\%$, its time period increases by $1\\%$ ($T \\propto L^{1/2}$). It loses $432\\text{ seconds}$ per day."
        }
    ],

    "kcet-waves": [
        {
            "name": "Wave Velocity, Standing Waves & Organ Pipes",
            "category": "Acoustics & Waves",
            "primary": ["speed of sound", "closed pipe", "open pipe", "organ pipe", "fundamental frequency", "first overtone", "harmonics", "nodes and antinodes", "end correction"],
            "formula_cues": [r"v = \nu \lambda", r"v = \sqrt{\frac{\gamma p}{\rho}}", r"f_c = \frac{v}{4l}", r"f_o = \frac{v}{2l}", r"1:3:5", r"1:2:3:4"],
            "secondary": ["frequency", "wavelength", "resonance", "air column"],
            "summary": "Newton-Laplace formula: $v = \\sqrt{\\frac{\\gamma P}{\\rho}}$. Closed organ pipe produces only ODD harmonics: $f_n = (2n-1)\\frac{v}{4L}$ (ratio $1:3:5$). Open organ pipe produces ALL harmonics: $f_n = n\\frac{v}{2L}$ (ratio $1:2:3:4$). Fundamental frequency of open pipe is twice that of closed pipe of same length.",
            "standard_formulas": r"f_{\text{closed}} = \frac{v}{4L}, \frac{3v}{4L}, \frac{5v}{4L}; \quad f_{\text{open}} = \frac{v}{2L}, \frac{2v}{2L}, \frac{3v}{2L}; \quad v_{\text{string}} = \sqrt{\frac{T}{\mu}}",
            "common_traps": "In organ pipes, remember: Third harmonic = First overtone in a closed pipe, but Second harmonic = First overtone in an open pipe!",
            "tips_and_tricks": "Speed of sound in a gas is INDEPENDENT of pressure changes at constant temperature because $\\frac{P}{\\rho}$ remains constant."
        },
        {
            "name": "Beats & Doppler Effect for Sound",
            "category": "Wave Phenomena",
            "primary": ["beat frequency", "number of beats", "tuning fork", "wax is loaded", "filed", "doppler effect", "apparent frequency", "source moving", "observer moving", "train approaching"],
            "formula_cues": [r"f_b = |f_1 - f_2|", r"f' = f\left(\frac{v \pm v_o}{v \mp v_s}\right)", r"f' > f"],
            "secondary": ["hertz", "sound", "speed", "frequency"],
            "summary": "Beat frequency $f_b = |f_1 - f_2|$ produced by superposition of two waves of slightly different frequencies. Loading a tuning fork with wax decreases its frequency; filing a fork increases its frequency. Doppler effect: $f' = f\\left(\\frac{v \\pm v_o}{v \\mp v_s}\\right)$.",
            "standard_formulas": r"f_b = |f_1 - f_2|, \quad f' = f\left(\frac{v - v_o}{v - v_s}\right) \ (\text{towards each other: } f' > f)",
            "common_traps": "When source moves TOWARDS stationary observer, use minus sign in denominator: $f' = f\\frac{v}{v - v_s} > f$.",
            "tips_and_tricks": "If a tuning fork $A$ (frequency $f_A$) gives 4 beats/s with $B$, $f_B = f_A \\pm 4$. If loading $A$ with wax decreases beat count, $f_A > f_B$."
        }
    ],

    "kcet-electrostatics": [
        {
            "name": "Coulomb's Law, Electric Field & Dipoles",
            "category": "Electrostatic Forces",
            "primary": ["coulomb's law", "electric field", "electric dipole", "dipole moment", "axial line", "equatorial line", "torque on dipole", "potential energy of dipole", "neutral point"],
            "formula_cues": [r"f = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2}", r"e_{\text{axial}} = \frac{2kp}{r^3}", r"e_{\text{eq}} = \frac{kp}{r^3}", r"\vec{\tau} = \vec{p} \times \vec{e}", r"u = -\vec{p} \cdot \vec{e}"],
            "secondary": ["charge", "distance", "coulombs", "newtons"],
            "summary": "Coulomb's Law: $F = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1 q_2}{r^2}$. Electric dipole $\\vec{p} = q(2\\vec{a})$. Field at axial point $E_{\\text{axial}} = \\frac{2kp}{r^3}$; field at equatorial point $E_{\\text{eq}} = \\frac{kp}{r^3} = \\frac{1}{2}E_{\\text{axial}}$. Torque on dipole $\\vec{\\tau} = \\vec{p} \\times \\vec{E}$; potential energy $U = -\\vec{p} \\cdot \\vec{E} = -pE\\cos\\theta$.",
            "standard_formulas": r"E_{\text{axial}} = \frac{1}{4\pi\varepsilon_0}\frac{2p}{r^3}, \quad E_{\text{eq}} = \frac{1}{4\pi\varepsilon_0}\frac{p}{r^3}, \quad \tau = pE\\sin\\theta, \quad W = pE(\\cos\\theta_1 - \\cos\\theta_2)",
            "common_traps": "Field of a short dipole falls off as $1/r^3$, NOT $1/r^2$ like a point charge!",
            "tips_and_tricks": "Work done to rotate a dipole from stable equilibrium ($\\theta = 0^\\circ$) to unstable equilibrium ($\\theta = 180^\\circ$) is $W = 2pE$."
        },
        {
            "name": "Gauss's Law & Electric Potential",
            "category": "Flux & Potential",
            "primary": ["gauss's law", "electric flux", "gaussian surface", "infinitely long wire", "infinite plane sheet", "electric potential", "potential of conducting sphere", "equipotential surface"],
            "formula_cues": [r"\phi = \oint \vec{e} \cdot d\vec{a} = \frac{q_{\text{encl}}}{\varepsilon_0}", r"e = \frac{\lambda}{2\pi\varepsilon_0 r}", r"e = \frac{\sigma}{2\varepsilon_0}", r"v = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}"],
            "secondary": ["surface", "sphere", "inside", "outside"],
            "summary": "Gauss's law $\\Phi = \\frac{q_{\\text{encl}}}{\\varepsilon_0}$. Applications: Line charge $E = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}$, infinite non-conducting sheet $E = \\frac{\\sigma}{2\\varepsilon_0}$ (independent of distance). Conducting sphere: $E_{\\text{in}} = 0$, $V_{\\text{in}} = V_{\\text{surface}} = \\frac{kq}{R}$. Equipotential surfaces are always perpendicular to electric field lines; work done moving a charge on an equipotential surface is zero.",
            "standard_formulas": r"\Phi = \frac{q_{\text{in}}}{\varepsilon_0}, \quad E_{\text{sheet}} = \frac{\sigma}{2\varepsilon_0}, \quad E = -\frac{dV}{dr}, \quad V_{\text{inside sphere}} = \frac{q}{4\pi\varepsilon_0 R}",
            "common_traps": "Electric potential inside a charged conducting hollow sphere is constant and non-zero ($V = \\frac{kq}{R}$), while electric field inside is zero!",
            "tips_and_tricks": "If $n$ identical mercury droplets each of potential $V$ coalesce to form one big drop, the new potential is $V' = n^{2/3} V$."
        }
    ],

    "kcet-current-electricity": [
        {
            "name": "Ohm's Law, Drift Velocity & Resistance Scaling",
            "category": "Conduction & Resistance",
            "primary": ["drift velocity", "relaxation time", "mobility", "temperature coefficient of resistance", "wire stretched", "radius halved", "stretched to double length", "color code of resistor", "internal resistance"],
            "formula_cues": [r"v_d = \frac{e e \tau}{m}", r"i = n e a v_d", r"r = \rho \frac{l}{a}", r"r_t = r_0(1 + \alpha \\Delta t)", r"r' = n^2 r"],
            "secondary": ["current", "ohms", "resistance", "length"],
            "summary": "Drift velocity $v_d = \\frac{e E \\tau}{m}$, current $I = n e A v_d$. Resistance $R = \\rho \\frac{L}{A} = \\rho \\frac{L}{\\pi r^2}$. Temperature dependence $R_t = R_0(1 + \\alpha\\Delta T)$ ($\\alpha > 0$ for metals, $\\alpha < 0$ for semiconductors). When a wire of resistance $R$ is stretched to $n$ times its length at constant volume, its new resistance is $R' = n^2 R$.",
            "standard_formulas": r"I = n e A v_d, \quad R = \rho \frac{L}{A}, \quad R_{\text{stretched}} \propto L^2 \propto \frac{1}{r^4}, \quad R' = n^2 R",
            "common_traps": "If length is stretched by $x\\%$ ($x \\le 5\\%$), resistance increases by $2x\\%$! If radius is decreased by $x\\%$, resistance increases by $4x\\%$.",
            "tips_and_tricks": "Resistor color code mnemonic: 'BB ROY of Great Britain has a Very Good Wife' (Black 0, Brown 1, Red 2, Orange 3, Yellow 4, Green 5, Blue 6, Violet 7, Grey 8, White 9; Gold 5%, Silver 10%)."
        },
        {
            "name": "Kirchhoff's Laws, Bridges & Measuring Instruments",
            "category": "Circuits & Instruments",
            "primary": ["wheatstone bridge", "meter bridge", "potentiometer", "null deflection", "balancing length", "kirchhoff's current law", "kirchhoff's voltage law", "cells in parallel", "cells in series"],
            "formula_cues": [r"\frac{p}{q} = \frac{r}{s}", r"\frac{r}{s} = \frac{l}{100-l}", r"\frac{e_1}{e_2} = \frac{l_1}{l_2}", r"r = r\left(\frac{l_1}{l_2}-1\right)", r"e_{\text{eq}} = \frac{e_1/r_1 + e_2/r_2}{1/r_1 + 1/r_2}"],
            "secondary": ["galvanometer", "battery", "emf", "jockey"],
            "summary": "Kirchhoff's Current Law (junction rule: charge conservation) & Voltage Law (loop rule: energy conservation). Balanced Wheatstone bridge $\\frac{P}{Q} = \\frac{R}{S}$. Meter bridge: unknown resistance $R = S\\left(\\frac{l}{100-l}\\right)$. Potentiometer draws no current at null point: $\\frac{E_1}{E_2} = \\frac{l_1}{l_2}$; internal resistance $r = R\\left(\\frac{l_1}{l_2}-1\\right)$.",
            "standard_formulas": r"\text{Meter Bridge: } R = S\frac{l}{100-l}, \quad \text{Potentiometer: } \frac{E_1}{E_2} = \frac{l_1}{l_2}, \quad r = R\left(\frac{l_1}{l_2}-1\right)",
            "common_traps": "In a balanced Wheatstone bridge, the galvanometer resistance has ZERO effect on the circuit and can be removed completely.",
            "tips_and_tricks": "Potentiometer is preferred over a voltmeter for measuring EMF because it measures open-circuit potential without drawing any current (infinite effective resistance)."
        }
    ],

    "kcet-moving-charges-and-magnetism": [
        {
            "name": "Biot-Savart Law & Magnetic Field Calculations",
            "category": "Magnetic Fields",
            "primary": ["biot-savart", "magnetic field at center of circular", "axis of circular coil", "straight wire", "solenoid", "toroid", "ampere's circuital law", "mu_0"],
            "formula_cues": [r"b = \frac{\mu_0 i}{2\pi r}", r"b = \frac{\mu_0 n i}{2 r}", r"b = \frac{\mu_0 n i r^2}{2(r^2+x^2)^{3/2}}", r"b = \mu_0 n i"],
            "secondary": ["current", "turns", "radius", "tesla"],
            "summary": "Biot-Savart law: $d\\vec{B} = \\frac{\\mu_0}{4\\pi}\\frac{I d\\vec{l} \\times \\hat{r}}{r^2}$. Magnetic field at center of circular loop $B = \\frac{\\mu_0 N I}{2R}$. On the axis of circular coil: $B = \\frac{\\mu_0 N I R^2}{2(R^2+x^2)^{3/2}}$. Infinitely long straight wire: $B = \\frac{\\mu_0 I}{2\\pi d}$. Inside a long solenoid: $B = \\mu_0 n I$.",
            "standard_formulas": r"B_{\text{center}} = \frac{\mu_0 N I}{2 R}, \quad B_{\text{wire}} = \frac{\mu_0 I}{2\pi d}, \quad B_{\text{solenoid}} = \mu_0 n I \ (n = N/L)",
            "common_traps": "At the ends of a semi-infinite solenoid, magnetic field drops to exactly HALF: $B_{\\text{end}} = \\frac{1}{2}\\mu_0 n I$.",
            "tips_and_tricks": "If a circular wire of radius $R$ is bent into $n$ turns of radius $R/n$, the magnetic field at the center increases by $n^2$ times!"
        },
        {
            "name": "Lorentz Force, Galvanometer & Conversion to Ammeter / Voltmeter",
            "category": "Magnetic Forces & Devices",
            "primary": ["lorentz force", "cyclotron", "helical path", "pitch of helix", "force between two parallel currents", "moving coil galvanometer", "shunt resistance", "conversion into ammeter", "conversion into voltmeter"],
            "formula_cues": [r"\vec{f} = q(\vec{e} + \vec{v} \times \vec{b})", r"r = \frac{m v}{q b}", r"t = \frac{2\pi m}{q b}", r"s = \frac{i_g g}{i - i_g}", r"r = \frac{v}{i_g} - g"],
            "secondary": ["deflection", "current sensitivity", "voltage sensitivity", "ampere"],
            "summary": "Lorentz force $\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B})$. Circular radius $r = \\frac{mv}{qB}$, period $T = \\frac{2\\pi m}{qB}$ (independent of speed $v$). Force between parallel wires: $\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi d}$ (parallel currents attract). Galvanometer conversion: Ammeter $\\implies$ small shunt $S = \\frac{I_g G}{I - I_g}$ in parallel; Voltmeter $\\implies$ high resistance $R = \\frac{V}{I_g} - G$ in series.",
            "standard_formulas": r"r = \frac{mv}{qB}, \quad \text{Shunt: } S = \frac{I_g G}{I - I_g}, \quad \text{Multiplier: } R = \frac{V}{I_g} - G",
            "common_traps": "Ammeter is connected in SERIES and must have very low resistance (ideal = 0). Voltmeter is connected in PARALLEL and must have very high resistance (ideal = $\\infty$).",
            "tips_and_tricks": "To increase the range of an ammeter by $n$ times ($I = n I_g$), the required shunt is simply $S = \\frac{G}{n - 1}$."
        }
    ],

    "kcet-magnetism-and-matter": [
        {
            "name": "Bar Magnet, Earth's Magnetism & Magnetic Materials",
            "category": "Magnetism Properties",
            "primary": ["magnetic dipole moment", "bar magnet", "earth's magnetic field", "angle of dip", "magnetic declination", "horizontal component", "diamagnetic", "paramagnetic", "ferromagnetic", "curie's law", "susceptibility"],
            "formula_cues": [r"m = m \times 2l", r"b_h = b\\cos\\theta", r"b_v = b\\sin\\theta", r"\tan\\theta = \frac{b_v}{b_h}", r"\chi_m = \frac{c}{t}"],
            "secondary": ["magnetic", "field", "poles", "dip"],
            "summary": "Earth's magnetic elements: Declination, Dip angle $\\theta$ where $\\tan\\theta = \\frac{B_v}{B_h}$, and Horizontal component $B_h = B\\cos\\theta$. At the magnetic poles: $\\theta = 90^\\circ, B_h = 0$. At the magnetic equator: $\\theta = 0^\\circ, B_v = 0$. Material classification: Diamagnetic ($\\chi < 0$, independent of $T$), Paramagnetic ($\\chi > 0$, $\\chi \\propto 1/T$ Curie's law), Ferromagnetic ($\\chi \\gg 1$, loses ferromagnetism above Curie temperature $T_c$).",
            "standard_formulas": r"\tan\\theta = \frac{B_v}{B_h}, \quad B = \sqrt{B_h^2 + B_v^2}, \quad \mu_r = 1 + \chi_m, \quad \text{Curie: } \chi = \frac{C}{T}",
            "common_traps": "Superconductors exhibit perfect diamagnetism with $\\chi = -1$ and $\\mu_r = 0$ (Meissner effect).",
            "tips_and_tricks": "If a bar magnet of moment $M$ is cut into two equal halves along its length, each half has moment $M/2$. If cut perpendicular to its length, each half also has moment $M/2$."
        }
    ],

    "kcet-electromagnetic-induction": [
        {
            "name": "Faraday-Lenz Law, Induced EMF & Motional Induction",
            "category": "Electromagnetic Induction",
            "primary": ["magnetic flux", "faraday's law", "lenz's law", "induced emf", "motional emf", "rod rotating", "sliding on rails", "change in flux", "charge flown"],
            "formula_cues": [r"\phi = \vec{b} \cdot \vec{a}", r"\mathcal{e} = -\frac{d\phi}{dt}", r"\mathcal{e} = bvl", r"\mathcal{e} = \frac{1}{2}b\omega l^2", r"q = \frac{\\Delta \phi}{r}"],
            "secondary": ["coil", "turns", "magnetic field", "loop"],
            "summary": "Faraday's Law: $\\mathcal{E} = -N\\frac{d\\Phi}{dt}$. Lenz's Law dictates that induced effects oppose the cause (energy conservation). Motional EMF for translating rod $\\mathcal{E} = B v L$; for rotating rod pivoted at one end $\\mathcal{E} = \\frac{1}{2}B\\omega L^2$. Induced charge $\\Delta q = \\frac{\\Delta\\Phi}{R}$ depends only on total flux change, NOT on the rate of change.",
            "standard_formulas": r"\mathcal{E} = -N\frac{d\Phi}{dt}, \quad \mathcal{E}_{\text{trans}} = B v L, \quad \mathcal{E}_{\text{rot}} = \frac{1}{2}B\omega L^2, \quad \\Delta q = \frac{\\Delta\Phi}{R}",
            "common_traps": "Charge flown $\\Delta q = \\Delta\\Phi / R$ is INDEPENDENT of time taken! Whether the flux changes in 1 millisecond or 1 hour, the same charge flows.",
            "tips_and_tricks": "For an aircraft flying horizontally in the northern hemisphere, vertical component of Earth's magnetic field $B_v$ induces an EMF across the wings: $\\mathcal{E} = B_v v L$."
        },
        {
            "name": "Self & Mutual Inductance & Energy Stored",
            "category": "Inductance",
            "primary": ["self inductance", "mutual inductance", "coefficient of coupling", "solenoid", "henry", "energy stored in inductor", "eddy currents"],
            "formula_cues": [r"\mathcal{e} = -l\frac{di}{dt}", r"l = \mu_0 n^2 a l", r"u = \frac{1}{2} l i^2", r"m = k\sqrt{l_1 l_2}"],
            "secondary": ["coil", "current", "induction", "magnetic"],
            "summary": "Self inductance $\\mathcal{E} = -L\\frac{dI}{dt}$, where $L = \\mu_0 n^2 A l$ for a solenoid ($L \\propto N^2$). Mutual inductance $\\mathcal{E}_2 = -M\\frac{dI_1}{dt}$, with coupling factor $M = k\\sqrt{L_1 L_2}$ ($0 \\le k \\le 1$). Magnetic energy stored in inductor $U = \\frac{1}{2}L I^2$.",
            "standard_formulas": r"L = \frac{N\Phi}{I} = \mu_0 n^2 A l, \quad U = \frac{1}{2} L I^2, \quad M = k\sqrt{L_1 L_2}",
            "common_traps": "Self inductance of a solenoid is proportional to $N^2$ (square of turns), not $N$! If turns are doubled, inductance quadruples.",
            "tips_and_tricks": "Eddy currents are minimized by using laminated magnetic cores with insulating varnish (used in transformers and chokes)."
        }
    ],

    "kcet-alternating-current": [
        {
            "name": "Peak, RMS Values & AC Through R, L, C",
            "category": "AC Fundamentals",
            "primary": ["rms current", "rms voltage", "peak value", "mean value", "inductive reactance", "capacitive reactance", "phase difference", "pure inductor", "pure capacitor"],
            "formula_cues": [r"i_{\text{rms}} = \frac{i_0}{\sqrt{2}}", r"v_{\text{rms}} = \frac{v_0}{\sqrt{2}}", r"x_l = \omega l", r"x_c = \frac{1}{\omega c}"],
            "secondary": ["hertz", "frequency", "cycle", "current"],
            "summary": "AC relations: $I_{\\text{rms}} = \\frac{I_0}{\\sqrt{2}} \\approx 0.707 I_0$, $V_{\\text{rms}} = \\frac{V_0}{\\sqrt{2}}$. Inductive reactance $X_L = \\omega L = 2\\pi f L$ (current lags voltage by $90^\\circ$). Capacitive reactance $X_C = \\frac{1}{\\omega C} = \\frac{1}{2\\pi f C}$ (current leads voltage by $90^\\circ$). For pure L or C, average power consumed over a cycle is strictly ZERO.",
            "standard_formulas": r"I_{\text{rms}} = \frac{I_0}{\sqrt{2}}, \quad X_L = 2\pi f L, \quad X_C = \frac{1}{2\pi f C}, \quad P_{\text{avg, pure L/C}} = 0",
            "common_traps": "Household AC supply specification $220\\text{ V}$ is the RMS voltage; peak voltage is $V_0 = 220\\sqrt{2} \\approx 311\\text{ V}$!",
            "tips_and_tricks": "In a DC circuit ($f = 0$): $X_L = 0$ (inductor acts as short circuit / straight wire) and $X_C = \\infty$ (capacitor acts as open circuit / blocks DC)."
        },
        {
            "name": "Series LCR Resonance, Power Factor & Transformers",
            "category": "Resonance & Transformers",
            "primary": ["series lcr", "resonance", "resonant frequency", "impedance", "quality factor", "power factor", "transformer", "step up", "step down", "turns ratio"],
            "formula_cues": [r"z = \sqrt{r^2 + (x_l - x_c)^2}", r"\omega_0 = \frac{1}{\sqrt{lc}}", r"\\cos\phi = \frac{r}{z}", r"\frac{v_s}{v_p} = \frac{n_s}{n_p} = \frac{i_p}{i_s}"],
            "secondary": ["voltage", "current", "primary", "secondary"],
            "summary": "Series LCR impedance $Z = \\sqrt{R^2 + (X_L - X_C)^2}$. At resonance ($X_L = X_C$): $Z = R$ (minimum), current is maximum, resonant frequency $\\omega_0 = \\frac{1}{\\sqrt{LC}}$, and power factor $\\cos\\phi = 1$. Power dissipated: $P = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi$. Ideal transformer: $\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s}$.",
            "standard_formulas": r"f_0 = \frac{1}{2\pi\sqrt{LC}}, \quad Z = \sqrt{R^2 + (X_L-X_C)^2}, \quad \\cos\phi = \frac{R}{Z}, \quad \frac{V_s}{V_p} = \frac{N_s}{N_p}",
            "common_traps": "Voltages across L and C in a resonant circuit can individually exceed the applied source voltage because $V_L$ and $V_C$ are $180^\\circ$ out of phase and cancel out!",
            "tips_and_tricks": "Step-up transformer increases voltage but decreases current ($I_s < I_p$) in accordance with energy conservation ($V_p I_p = V_s I_s$)."
        }
    ],

    "kcet-electromagnetic-waves": [
        {
            "name": "Displacement Current, EM Spectrum & Wave Properties",
            "category": "EM Waves",
            "primary": ["displacement current", "maxwell", "electromagnetic spectrum", "gamma rays", "x-rays", "ultraviolet", "infrared", "microwaves", "radio waves", "speed of light", "radiation pressure"],
            "formula_cues": [r"i_d = \varepsilon_0 \frac{d\phi_e}{dt}", r"c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}", r"c = \frac{e_0}{b_0}", r"i = \frac{1}{2}\varepsilon_0 c e_0^2"],
            "secondary": ["wavelength", "frequency", "electric", "magnetic"],
            "summary": "Displacement current $I_d = \\varepsilon_0 \\frac{d\\Phi_E}{dt}$. EM waves are transverse with mutually perpendicular $\\vec{E}$ and $\\vec{B}$ vectors: $\\vec{E} \\perp \\vec{B} \\perp \\vec{c}$. Speed of propagation $c = \\frac{1}{\\sqrt{\\mu_0\\varepsilon_0}} = \\frac{E_0}{B_0} \\approx 3 \\times 10^8\\text{ m/s}$. EM spectrum in order of increasing wavelength: $\\gamma\\text{-rays} < \\text{X-rays} < \\text{UV} < \\text{Visible} < \\text{IR} < \\text{Microwaves} < \\text{Radio}$.",
            "standard_formulas": r"c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = \frac{E_0}{B_0}, \quad I_d = \varepsilon_0 \frac{d\Phi_E}{dt}, \quad \text{Energy Density: } u = \frac{1}{2}\varepsilon_0 E^2 + \frac{B^2}{2\mu_0}",
            "common_traps": "In an EM wave, the average electric energy density equals the average magnetic energy density: $u_E = u_B$!",
            "tips_and_tricks": "Mnemonic for decreasing frequency: 'Grandma's eX-box Uses Video In Most Rooms' (Gamma, X-ray, UV, Visible, IR, Micro, Radio)."
        }
    ],

    "kcet-ray-optics": [
        {
            "name": "Refraction, Snell's Law & Total Internal Reflection (TIR)",
            "category": "Geometric Optics",
            "primary": ["snell's law", "refraction", "refractive index", "total internal reflection", "critical angle", "optical fiber", "apparent depth", "normal shift"],
            "formula_cues": [r"n_1 \\sin i = n_2 \\sin r", r"\\sin c = \frac{1}{n}", r"\text{apparent depth} = \frac{d}{n}", r"\\Delta t = d\left(1 - \frac{1}{n}\right)"],
            "secondary": ["denser", "rarer", "angle of incidence", "light"],
            "summary": "Snell's Law: $n_1\\sin i = n_2\\sin r$. Total Internal Reflection (TIR) occurs when light travels from a denser to a rarer medium at an angle of incidence exceeding the critical angle $C$: $\\sin C = \\frac{n_{\\text{rarer}}}{n_{\\text{denser}}}$. Applications: optical fibers, mirage, diamond brilliance. Apparent depth of a submerged object: $d' = d/n$.",
            "standard_formulas": r"\\sin C = \frac{1}{n}, \quad d_{\text{apparent}} = \frac{d_{\text{real}}}{n}, \quad \text{Shift} = d\left(1 - \frac{1}{n}\right)",
            "common_traps": "TIR can ONLY occur when light travels from an optically DENSER medium to an optically RARER medium, never vice versa!",
            "tips_and_tricks": "Critical angle for glass ($n=1.5$) is $C \\approx 42^\\circ$; for water ($n=4/3$) is $C \\approx 49^\\circ$; for diamond ($n=2.42$) is $C \\approx 24^\\circ$."
        },
        {
            "name": "Prism Dispersion & Angle of Minimum Deviation",
            "category": "Prisms",
            "primary": ["prism", "angle of deviation", "minimum deviation", "angle of prism", "equilateral glass prism", "angle of incidence is equal to angle of emergence", "refractive index of prism"],
            "formula_cues": [r"n = \frac{\\sin\left(\frac{a + d_m}{2}\right)}{\\sin\left(\frac{a}{2}\right)}", r"d = (n-1)a", r"i + e = a + d", r"r_1 + r_2 = a"],
            "secondary": ["deviation", "speed of light inside", "spectrum"],
            "summary": "Prism formulas: $A = r_1 + r_2$ and $i + e = A + D$. At minimum deviation $D = D_m$: $i = e$ and $r_1 = r_2 = A/2$. Refractive index $n = \\frac{\\sin((A+D_m)/2)}{\\sin(A/2)}$. For a thin prism: $D = (n-1)A$.",
            "standard_formulas": r"n = \frac{\\sin\left(\frac{A + D_m}{2}\right)}{\\sin\left(\frac{A}{2}\right)}, \quad i = e = \frac{A + D_m}{2}, \quad r = \frac{A}{2}",
            "common_traps": "At minimum deviation in an equilateral prism ($A = 60^\\circ$), the refracted ray inside the prism travels PARALLEL to the base.",
            "tips_and_tricks": "If $D_m = A$ for an equilateral prism, $n = \\frac{\\sin A}{\\sin(A/2)} = 2\\cos(A/2) = 2\\cos 30^\\circ = \\sqrt{3} \\approx 1.732$."
        },
        {
            "name": "Thin Lenses, Lens Maker's Formula & Optical Instruments",
            "category": "Lenses & Instruments",
            "primary": ["lens maker's formula", "thin lens", "focal length", "power of lens", "combination of lenses", "microscope", "telescope", "magnifying power", "convex lens", "concave lens"],
            "formula_cues": [r"\frac{1}{f} = (n-1)\left(\frac{1}{r_1} - \frac{1}{r_2}\right)", r"\frac{1}{f} = \frac{1}{v} - \frac{1}{u}", r"p = \frac{1}{f}", r"p = p_1 + p_2", r"m = \frac{f_o}{f_e}"],
            "secondary": ["dioptres", "magnification", "image", "object"],
            "summary": "Lens Maker's formula: $\\frac{1}{f} = (n-1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$. Power $P = \\frac{1}{f(\\text{m})}$ in Dioptres. Combination of lenses in contact: $P = P_1 + P_2 \\implies \\frac{1}{F} = \\frac{1}{f_1} + \\frac{1}{f_2}$. Telescope magnifying power in normal adjustment: $m = -\\frac{f_o}{f_e}$, tube length $L = f_o + f_e$. Compound microscope: $m = -\\frac{v_o}{u_o}\\left(1 + \\frac{D}{f_e}\\right)$.",
            "standard_formulas": r"\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right), \quad P = P_1 + P_2, \quad m_{\text{telescope}} = \frac{f_o}{f_e}, \quad L = f_o + f_e",
            "common_traps": "When a glass lens ($n=1.5$) is immersed in water ($n=4/3$), its focal length increases by 4 times ($f_{\\text{water}} = 4 f_{\\text{air}}$) and its power decreases to $1/4$!",
            "tips_and_tricks": "If an equiconvex lens of focal length $f$ is cut vertically in half, each plano-convex half has focal length $2f$. If cut horizontally in half, each piece retains focal length $f$."
        }
    ],

    "kcet-wave-optics": [
        {
            "name": "Interference of Light & Young's Double Slit Experiment",
            "category": "Interference",
            "primary": ["young's double slit", "ydse", "fringe width", "coherent sources", "constructive interference", "destructive interference", "path difference", "dark fringe", "bright fringe", "slits separation"],
            "formula_cues": [r"\beta = \frac{\lambda D}{d}", r"\\Delta x = n\lambda", r"\\Delta x = (2n-1)\frac{\lambda}{2}", r"i_{\max} = (\sqrt{i_1} + \sqrt{i_2})^2", r"\frac{i_{\max}}{i_{\min}}"],
            "secondary": ["screen", "intensity", "wavelength", "fringes"],
            "summary": "Conditions for interference: coherent sources (constant phase difference). Constructive interference: path difference $\\Delta x = n\\lambda$, intensity $I_{\\max} = (\\sqrt{I_1} + \\sqrt{I_2})^2$. Destructive interference: $\\Delta x = (2n-1)\\frac{\\lambda}{2}$, $I_{\\min} = (\\sqrt{I_1} - \\sqrt{I_2})^2$. Fringe width $\\beta = \\frac{\\lambda D}{d}$.",
            "standard_formulas": r"\beta = \frac{\lambda D}{d}, \quad \frac{I_{\max}}{I_{\min}} = \left(\frac{a_1 + a_2}{a_1 - a_2}\right)^2, \quad \beta \propto \lambda",
            "common_traps": "If YDSE apparatus is immersed in water of refractive index $n$, fringe width decreases to $\\beta' = \\beta/n$ because $\\lambda' = \\lambda/n$.",
            "tips_and_tricks": "If one slit of YDSE is covered with a transparent sheet of thickness $t$ and refractive index $\\mu$, the entire fringe pattern shifts by $y = \\frac{D}{d}(\\mu - 1)t$ without changing fringe width."
        },
        {
            "name": "Diffraction, Polarization & Brewster's Law",
            "category": "Diffraction & Polarization",
            "primary": ["diffraction", "single slit", "central maximum", "width of central maximum", "polarization", "brewster's law", "brewster angle", "polarizing angle", "malus' law"],
            "formula_cues": [r"w = \frac{2\lambda D}{a}", r"a \\sin\\theta = n\lambda", r"n = \tan i_p", r"i = i_0 \\cos^2\\theta", r"i_p + r_p = 90^\\circ"],
            "secondary": ["polarizer", "analyzer", "light", "intensity"],
            "summary": "Single slit Fraunhofer diffraction: Minima condition $a\\sin\\theta = n\\lambda$. Width of central maximum $\\beta_0 = \\frac{2\\lambda D}{a}$ (twice the width of secondary maxima). Brewster's Law for polarization by reflection: $n = \\tan i_p$. At the Brewster angle, the reflected and refracted rays are mutually perpendicular ($i_p + r = 90^\\circ$). Malus' Law: $I = I_0\\cos^2\\theta$.",
            "standard_formulas": r"\text{Central Max Width: } \beta_0 = \frac{2\lambda D}{a}, \quad n = \tan i_p, \quad I = I_0 \\cos^2\\theta",
            "common_traps": "Diffraction occurs with sound and light, but POLARIZATION is unique to transverse waves (sound waves cannot be polarized!).",
            "tips_and_tricks": "When unpolarized light of intensity $I_0$ passes through an ideal Polaroid, the transmitted intensity is ALWAYS exactly $I_0/2$, regardless of orientation."
        }
    ],

    "kcet-dual-nature-of-radiation": [
        {
            "name": "Photoelectric Effect & Einstein's Equation",
            "category": "Quantum Nature",
            "primary": ["photoelectric effect", "work function", "threshold frequency", "threshold wavelength", "stopping potential", "einstein's photoelectric", "maximum kinetic energy", "cutoff potential"],
            "formula_cues": [r"e V_0 = h\nu - \phi", r"k_{\max} = h\nu - h\nu_0", r"\phi = h\nu_0 = \frac{hc}{\lambda_0}", r"k_{\max} = e V_0"],
            "secondary": ["frequency", "intensity", "electrons", "incident light"],
            "summary": "Einstein's photoelectric equation: $K_{\\max} = e V_0 = h\\nu - \\phi = h(\\nu - \\nu_0)$. Work function $\\phi = h\\nu_0 = \\frac{hc}{\\lambda_0}$. Photoelectric current is directly proportional to light intensity. Maximum kinetic energy $K_{\\max}$ and stopping potential $V_0$ depend strictly on frequency $\\nu$, completely independent of light intensity.",
            "standard_formulas": r"e V_0 = h\nu - \phi, \quad K_{\max} = \frac{hc}{\lambda} - \phi, \quad \text{Slope of } V_0 \text{ vs } \nu = \frac{h}{e}",
            "common_traps": "Increasing light intensity increases the number of emitted photoelectrons (current), but does NOT change their maximum kinetic energy or stopping potential!",
            "tips_and_tricks": "The slope of the graph of stopping potential $V_0$ versus frequency $\\nu$ is a universal constant $\\frac{h}{e}$, identical for all metals."
        },
        {
            "name": "de Broglie Wavelength of Matter Waves",
            "category": "Matter Waves",
            "primary": ["de broglie wavelength", "matter waves", "electron accelerated through potential", "proton and alpha particle", "thermal neutron", "wavelength ratio"],
            "formula_cues": [r"\lambda = \frac{h}{p}", r"\lambda = \frac{h}{\sqrt{2mE}}", r"\lambda = \frac{h}{\sqrt{2mqV}}", r"\lambda_e = \frac{1.227}{\sqrt{V}}\text{ nm}", r"\lambda = \frac{12.27}{\sqrt{V}}"],
            "secondary": ["potential difference", "momentum", "mass", "particle"],
            "summary": "de Broglie hypothesis: $\\lambda = \\frac{h}{p} = \\frac{h}{mv} = \\frac{h}{\\sqrt{2mE}}$. For an electron accelerated through potential difference $V$: $\\lambda = \\frac{h}{\\sqrt{2meV}} = \\frac{1.227}{\\sqrt{V}}\\text{ nm} = \\frac{12.27}{\\sqrt{V}}\\text{ \\AA}$. For a gas molecule at temperature $T$: $\\lambda = \\frac{h}{\\sqrt{3mkT}}$.",
            "standard_formulas": r"\lambda = \frac{h}{\sqrt{2mqV}}, \quad \lambda_e = \frac{1.227}{\sqrt{V}}\text{ nm}, \quad \lambda_p : \lambda_\alpha = \frac{\sqrt{m_\alpha q_\alpha}}{\sqrt{m_p q_p}}",
            "common_traps": "For proton ($m, q$) vs $\\alpha$-particle ($4m, 2q$) accelerated through same potential $V$: $\\frac{\\lambda_p}{\\lambda_\\alpha} = \\sqrt{\\frac{m_\\alpha q_\\alpha}{m_p q_p}} = \\sqrt{4 \\times 2} = \\sqrt{8} = 2\\sqrt{2}$.",
            "tips_and_tricks": "Remember the quick electron formula: Accelerated through $100\\text{ V}$, $\\lambda = \\frac{1.227}{\\sqrt{100}} = 0.1227\\text{ nm} = 1.227\\text{ \\AA}$."
        }
    ],

    "kcet-atoms-and-nuclei": [
        {
            "name": "Bohr Atom Model & Hydrogen Spectral Series",
            "category": "Atomic Physics",
            "primary": ["bohr model", "radius of orbit", "energy of electron", "ground state", "hydrogen spectrum", "lyman series", "balmer series", "paschen series", "longest wavelength", "shortest wavelength", "rydberg constant"],
            "formula_cues": [r"r_n = 0.529 \frac{n^2}{z}\text{ \AA}", r"e_n = -13.6 \frac{z^2}{n^2}\text{ eV}", r"\frac{1}{\lambda} = r\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)", r"m v r = \frac{n h}{2\pi}"],
            "secondary": ["transition", "orbit", "photon", "ultraviolet"],
            "summary": "Bohr's postulates: $mvr = \\frac{nh}{2\\pi}$. Orbital radius $r_n \\propto n^2/Z$. Energy levels $E_n = -\\frac{13.6 Z^2}{n^2}\\text{ eV}$. Spectral series: Lyman ($n_1=1$, UV region), Balmer ($n_1=2$, Visible region), Paschen ($n_1=3$, Infrared). Longest wavelength corresponds to transition from $n_2 = n_1+1$; shortest wavelength corresponds to $n_2 = \\infty$ (series limit).",
            "standard_formulas": r"r_n \propto n^2, \quad E_n = -\frac{13.6}{n^2}\text{ eV}, \quad \frac{1}{\lambda} = R\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \quad \lambda_{\text{limit}} = \frac{n_1^2}{R}",
            "common_traps": "Only the Balmer series falls in the VISIBLE spectrum; Lyman is strictly ultraviolet, and Paschen/Brackett/Pfund are infrared.",
            "tips_and_tricks": "Ratio of maximum to minimum wavelength in Lyman series: $\\frac{\\lambda_{\\max}}{\\lambda_{\\min}} = \\frac{1/(1 - 1/4)}{1/(1 - 0)} = \\frac{4}{3}$."
        },
        {
            "name": "Nuclear Binding Energy & Law of Radioactive Decay",
            "category": "Nuclear Physics",
            "primary": ["mass defect", "binding energy", "binding energy per nucleon", "nuclear density", "radioactive decay", "half life", "mean life", "decay constant", "activity", "curie", "becquerel"],
            "formula_cues": [r"\\Delta m = [z m_p + (a-z)m_n] - m_n", r"\text{be} = \\Delta m \times 931.5\text{ MeV}", r"n = n_0 e^{-\lambda t}", r"t_{1/2} = \frac{0.693}{\lambda}", r"r = r_0 a^{1/3}"],
            "secondary": ["nucleus", "disintegration", "fraction", "sample"],
            "summary": "Nuclear radius $R = R_0 A^{1/3} \\implies$ nuclear density is constant and independent of mass number $A$. Mass defect $\\Delta m$, Binding energy $BE = \\Delta m \\times 931.5\\text{ MeV}$. Maximum $BE/A \\approx 8.8\\text{ MeV}$ around Iron ($^{56}\\text{Fe}$). Radioactive decay law: $N = N_0 e^{-\\lambda t} = N_0 (1/2)^{t/T_{1/2}}$. Half-life $T_{1/2} = \\frac{0.693}{\\lambda}$, Mean life $\\tau = 1/\\lambda = 1.44 T_{1/2}$.",
            "standard_formulas": r"N(t) = N_0\left(\frac{1}{2}\right)^{t / T_{1/2}}, \quad T_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}, \quad R = R_0 A^{1/3}",
            "common_traps": "Nuclear density is of the order of $10^{17}\\text{ kg/m}^3$ and is IDENTICAL for all nuclei, from hydrogen to uranium!",
            "tips_and_tricks": "Fraction remaining after $n$ half-lives is $(1/2)^n$. After 3 half-lives, $1/8$ remains ($87.5\\%$ has decayed)."
        }
    ],

    "kcet-communication-systems": [
        {
            "name": "Modulation & Space Wave Propagation Range",
            "category": "Communication",
            "primary": ["amplitude modulation", "modulation index", "carrier wave", "sidebands", "bandwidth", "range of antenna", "transmitting antenna", "receiving antenna", "line of sight"],
            "formula_cues": [r"\mu = \frac{a_m}{a_c}", r"d = \sqrt{2 r h_t}", r"d_{\max} = \sqrt{2rh_t} + \sqrt{2rh_r}", r"\text{bandwidth} = 2f_m"],
            "secondary": ["height", "earth", "tower", "radius"],
            "summary": "Modulation index in AM: $\\mu = \\frac{A_m}{A_c} = \\frac{A_{\\max} - A_{\\min}}{A_{\\max} + A_{\\min}}$ ($0 \\le \\mu \\le 1$ to prevent distortion). Bandwidth of AM wave is $2f_m$. Maximum line-of-sight range for a transmitting antenna of height $h_t$: $d = \\sqrt{2 R h_t}$. Between transmitter and receiver: $d_{\\max} = \\sqrt{2Rh_t} + \\sqrt{2Rh_r}$.",
            "standard_formulas": r"\mu = \frac{A_{\max} - A_{\min}}{A_{\max} + A_{\min}}, \quad d = \sqrt{2 R h}, \quad \text{Population Covered} = \rho \pi d^2 = \rho \pi (2Rh)",
            "common_traps": "Antenna range $d$ depends on $\\sqrt{h}$ (square root of height). To double the transmission range, the tower height must be quadrupled ($4\\times$)!",
            "tips_and_tricks": "Using Earth radius $R = 6.4 \\times 10^6\\text{ m}$: $d \\approx \\sqrt{2 \\times 6400000 \\times h} = \\sqrt{1.28 \\times 10^7 h} \\approx 3578\\sqrt{h}$ meters."
        }
    ],

    "kcet-vector-algebra": [
        {
            "name": "Vector Operations: Dot Product & Cross Product",
            "category": "Vector Operations",
            "primary": ["dot product", "cross product", "scalar product", "vector product", "projection of vector", "angle between vectors", "unit vector", "area of parallelogram", "area of triangle"],
            "formula_cues": [r"\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\\cos\\theta", r"|\vec{a} \times \vec{b}| = |\vec{a}||\vec{b}|\\sin\\theta", r"\text{proj} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}", r"\hat{a} = \frac{\vec{a}}{|\vec{a}|}"],
            "secondary": ["perpendicular", "parallel", "coplanar", "magnitude"],
            "summary": "Dot product $\\vec{a} \\cdot \\vec{b} = a_x b_x + a_y b_y + a_z b_z$. Two non-zero vectors are perpendicular if and only if $\\vec{a} \\cdot \\vec{b} = 0$. Projection of $\\vec{a}$ on $\\vec{b}$: $\\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|}$. Cross product $\\vec{a} \\times \\vec{b}$ gives a vector perpendicular to both $\\vec{a}$ and $\\vec{b}$; two vectors are parallel if $\\vec{a} \\times \\vec{b} = \\vec{0}$. Area of triangle = $\\frac{1}{2}|\\vec{a} \\times \\vec{b}|$; area of parallelogram = $|\\vec{a} \\times \\vec{b}|$.",
            "standard_formulas": r"\vec{a} \cdot \vec{b} = 0 \iff \vec{a} \perp \vec{b}, \quad \text{Projection of } \vec{a} \text{ on } \vec{b} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}, \quad \text{Area} = \frac{1}{2}|\vec{a} \times \vec{b}|",
            "common_traps": "Projection of $\\vec{a}$ on $\\vec{b}$ has $|\\vec{b}|$ in denominator, NOT $|\\vec{a}|$!",
            "tips_and_tricks": "Lagrange's Identity: $|\\vec{a} \\times \\vec{b}|^2 + (\\vec{a} \\cdot \\vec{b})^2 = |\\vec{a}|^2 |\\vec{b}|^2$. Useful for instant evaluation in KCET."
        }
    ],
    # ==========================================
    # SPECIAL KCET SPECIFIC CHAPTERS
    # ==========================================
    "kcet-elasticity": [   {   'category': 'Elastic Moduli',
        'common_traps': 'Ratio problems with diameter: remember $A \\propto d^2$, so $\\Delta L \\propto '
                        '\\frac{L}{d^2}$. If diameter is doubled, elongation becomes 1/4!',
        'formula_cues': ['\\frac{fl}{a \\delta l}', '\\frac{f l}{a \\delta l}', '\\pi r^2', '2 \\times 10^{11}'],
        'name': "Hooke's Law & Young's Modulus of Wires",
        'primary': [   "young's modulus",
                       'youngs modulus',
                       'wire',
                       'elongation',
                       'stretch',
                       'diameter',
                       'ratio of lengths',
                       'ratio of diameters',
                       'extension',
                       'breaking stress'],
        'secondary': ['stress', 'strain', 'tension', 'length', 'radius'],
        'standard_formulas': 'Y = \\frac{F L}{A \\Delta L} = \\frac{M g L}{\\pi r^2 \\Delta L}, \\quad \\Delta L '
                             '\\propto \\frac{L}{r^2} \\propto \\frac{L}{d^2}',
        'summary': "Hooke's law in 1D: Longitudinal stress $\\sigma = \\frac{F}{A}$ and strain $\\epsilon = "
                   "\\frac{\\Delta L}{L}$. Young's modulus $Y = \\frac{F L}{A \\Delta L} = \\frac{F L}{\\pi r^2 "
                   '\\Delta L}$.',
        'tips_and_tricks': 'For two wires under equal tension: $\\frac{\\Delta L_1}{\\Delta L_2} = '
                           '\\left(\\frac{L_1}{L_2}\\right) \\left(\\frac{d_2}{d_1}\\right)^2 '
                           '\\left(\\frac{Y_2}{Y_1}\\right)$.'},
    {   'category': 'Energy & Special Cases',
        'common_traps': 'Elongation due to own weight has factor 1/2 in denominator because effective center of '
                        'gravity acts at L/2!',
        'formula_cues': [   '\\frac{1}{2} f \\delta l',
                            '\\frac{\\rho g l^2}{2y}',
                            '\\sigma = \\frac{\\text{lateral}}{\\text{longitudinal}}',
                            '\\sigma = 0.25'],
        'name': 'Elastic Potential Energy & Wire Elongation Due to Weight',
        'primary': [   'own weight',
                       'density rho',
                       'potential energy',
                       'work done in stretching',
                       'energy stored',
                       'energy density',
                       "poisson's ratio",
                       'poissons ratio',
                       'lateral strain'],
        'secondary': ['volume', 'half', 'work', 'stored'],
        'standard_formulas': 'U = \\frac{1}{2} F \\Delta L, \\quad u = \\frac{1}{2} \\text{Stress} \\times '
                             '\\text{Strain}, \\quad \\Delta L_{\\text{self}} = \\frac{\\rho g L^2}{2 Y}, \\quad '
                             '\\sigma = \\frac{\\Delta d / d}{\\Delta L / L}',
        'summary': 'Work done in stretching a wire $W = U = \\frac{1}{2} F \\Delta L = \\frac{1}{2} Y '
                   '(\\text{strain})^2 \\times \\text{Volume}$. Elongation of a hanging wire under its own weight '
                   "$\\Delta L = \\frac{\\rho g L^2}{2 Y}$. Poisson's ratio $\\sigma = -\\frac{\\Delta r / r}{\\Delta "
                   'L / L}$.',
        'tips_and_tricks': "Poisson's ratio theoretical limits: $-1 \\le \\sigma \\le 0.5$. For practical materials, "
                           '$0 \\le \\sigma \\le 0.5$.'}],

    "kcet-fluid-mechanics": [   {   'category': 'Fluid Statics',
        'common_traps': 'Total absolute pressure is $P = P_0 + \\rho g h$; gauge pressure is only $\\rho g h$. Watch '
                        'whether the question asks for gauge or absolute pressure.',
        'formula_cues': ['p = \\rho g h', '\\rho g h', 'f_1 / a_1 = f_2 / a_2', 'w_{\\text{app}} = w - \\rho v g'],
        'name': "Hydrostatics, Pascal's Principle & Archimedes' Buoyancy",
        'primary': [   'hydrostatic',
                       'pascal',
                       'hydraulic lift',
                       'gauge pressure',
                       'atmospheric pressure',
                       'buoyant force',
                       'upthrust',
                       'apparent weight',
                       'floating',
                       'density of liquid'],
        'secondary': ['manometer', 'depth', 'density', 'liquid'],
        'standard_formulas': 'P = P_0 + \\rho g h, \\quad \\frac{F_1}{A_1} = \\frac{F_2}{A_2}, \\quad F_B = \\rho_L '
                             'V_{\\text{sub}} g',
        'summary': "Fluid pressure variation with depth $P = P_0 + \\rho g h$. Pascal's law of pressure transmission "
                   "in hydraulic machines: $\\frac{F_1}{A_1} = \\frac{F_2}{A_2}$. Archimedes' principle: buoyant "
                   'upthrust $F_B = \\rho_{\\text{fluid}} V_{\\text{displaced}} g$.',
        'tips_and_tricks': 'Fraction of volume submerged for a floating body: '
                           '$\\frac{V_{\\text{sub}}}{V_{\\text{total}}} = '
                           '\\frac{\\rho_{\\text{body}}}{\\rho_{\\text{liquid}}}$.'},
    {   'category': 'Fluid Dynamics',
        'common_traps': 'Where fluid velocity is highest (narrow section), static pressure is lowest, NOT highest!',
        'formula_cues': ['a_1 v_1 = a_2 v_2', 'p + \\frac{1}{2}\\rho v^2', '\\sqrt{2gh}', 'v = \\sqrt{2gh}'],
        'name': "Continuity Equation & Bernoulli's Principle",
        'primary': [   'streamline',
                       'equation of continuity',
                       'cross-sectional area',
                       'bernoulli',
                       'horizontal pipe',
                       'speed of flow',
                       'venturi',
                       'carburetor',
                       'torricelli',
                       'velocity of efflux'],
        'secondary': ['velocity', 'pipe', 'pressure', 'narrow'],
        'standard_formulas': 'A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 = P_2 + \\frac{1}{2}\\rho v_2^2, '
                             '\\quad v_{\\text{efflux}} = \\sqrt{2gh}',
        'summary': "Conservation of mass for incompressible fluid: $A_1 v_1 = A_2 v_2$. Bernoulli's equation $P + "
                   "\\frac{1}{2}\\rho v^2 + \\rho g h = \\text{constant}$. Torricelli's speed of efflux $v = "
                   "\\sqrt{2gh}$. Carburetor / atomizer suction operates on Bernoulli's principle.",
        'tips_and_tricks': 'In horizontal pipes, $\\Delta P = \\frac{1}{2}\\rho (v_2^2 - v_1^2)$. If radius is halved, '
                           'area is 1/4, velocity is 4x.'},
    {   'category': 'Surface & Transport Phenomena',
        'common_traps': '1. Terminal velocity depends on $r^2$, NOT $r$! If radius is doubled, $v_t$ quadruples. 2. A '
                        'bubble inside a liquid has only 1 surface ($2T/R$), while a soap bubble in air has 2 surfaces '
                        '($4T/R$).',
        'formula_cues': [   '6\\pi \\eta r v',
                            'v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta}',
                            'h = \\frac{2t\\cos\\theta}{\\rho g r}',
                            '\\frac{2t}{r}',
                            '\\frac{4t}{r}'],
        'name': "Viscosity, Stokes' Law & Surface Tension",
        'primary': [   'coefficient of viscosity',
                       'stokes',
                       'terminal velocity',
                       'spherical steel ball',
                       'viscous force',
                       'surface tension',
                       'capillary tube',
                       'capillarity',
                       'rise in capillary',
                       'excess pressure',
                       'soap bubble'],
        'secondary': ['liquid', 'radius', 'water', 'droplet'],
        'standard_formulas': 'v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta}, \\quad \\Delta P_{\\text{drop}} = '
                             '\\frac{2T}{R}, \\quad \\Delta P_{\\text{bubble}} = \\frac{4T}{R}, \\quad h = '
                             '\\frac{2T\\cos\\theta}{\\rho g r}',
        'summary': "Stokes' drag $F = 6\\pi \\eta r v$. Terminal velocity $v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 "
                   '\\eta} \\propto r^2$. Excess pressure $\\Delta P = \\frac{2T}{R}$ (liquid drop), $\\Delta P = '
                   '\\frac{4T}{R}$ (soap bubble). Capillary rise $h = \\frac{2T\\cos\\theta}{\\rho g r}$.',
        'tips_and_tricks': 'In an artificial satellite or free-fall weightlessness ($g=0$), capillary water rises to '
                           'the very top of the tube, no matter how long the tube is ($h \\to L$).'}],

    "kcet-capacitor": [   {   'category': 'Core Principle',
        'common_traps': 'Distinguish whether the battery is kept connected ($V = \\text{const}$) or disconnected ($Q = '
                        '\\text{const}$) before inserting the dielectric slab.',
        'formula_cues': ['c = \\frac{\\epsilon_0 a}{d}', "c' = k c", 'q = c v', '\\epsilon_0'],
        'name': 'Parallel Plate Capacitance & Dielectric Slabs',
        'primary': [   'parallel plate capacitor',
                       'capacitance',
                       'dielectric slab',
                       'dielectric constant',
                       'dielectric in between',
                       'distance between the plates',
                       'battery remains connected',
                       'battery disconnected'],
        'secondary': ['electric field', 'charge', 'plates', 'potential difference'],
        'standard_formulas': 'C = \\frac{K \\varepsilon_0 A}{d}, \\quad E = \\frac{V}{d} = '
                             '\\frac{\\sigma}{\\varepsilon_0}, \\quad Q = C V',
        'summary': 'Capacitance of parallel plate capacitor $C_0 = \\frac{\\varepsilon_0 A}{d}$. With dielectric slab '
                   'of constant $K$, $C = K C_0$. If battery disconnected: charge $Q$ is constant, potential $V = '
                   'V_0/K$, electric field $E = E_0/K$. If battery connected: $V$ is constant, $Q = K Q_0$.',
        'tips_and_tricks': 'KCET Rule of Thumb: Disconnected battery $\\implies Q$ stays constant. Connected battery '
                           '$\\implies V$ stays constant.'},
    {   'category': 'Circuits & Energy',
        'common_traps': 'In series capacitors, voltage divides inversely to capacitance: $V_1 = V '
                        '\\left(\\frac{C_2}{C_1 + C_2}\\right)$. Smaller capacitor takes larger voltage!',
        'formula_cues': [   '\\frac{1}{c_s} = \\sum \\frac{1}{c_i}',
                            'c_p = \\sum c_i',
                            '\\frac{1}{2} c v^2',
                            '\\frac{q^2}{2c}',
                            '\\Delta u = \\frac{c_1 c_2}{2(c_1+c_2)}(v_1-v_2)^2'],
        'name': 'Capacitor Combinations, Energy Stored & Charge Sharing',
        'primary': [   'equivalent capacitance',
                       'series',
                       'parallel',
                       'energy stored',
                       'potential difference across',
                       'sharing of charge',
                       'common potential',
                       'loss of energy',
                       'bridge',
                       'microfarad'],
        'secondary': ['battery', 'circuit', 'voltage', 'joules'],
        'standard_formulas': 'C_p = \\sum C_i, \\quad \\frac{1}{C_s} = \\sum \\frac{1}{C_i}, \\quad U = \\frac{1}{2} C '
                             'V^2, \\quad \\Delta U_{\\text{loss}} = \\frac{C_1 C_2}{2(C_1+C_2)}(V_1 - V_2)^2',
        'summary': 'Series combination $\\frac{1}{C_s} = \\frac{1}{C_1} + \\frac{1}{C_2}$ (charge $Q$ is same). '
                   'Parallel combination $C_p = C_1 + C_2$ ($V$ is same). Energy stored $U = \\frac{1}{2} C V^2 = '
                   '\\frac{Q^2}{2C}$. Common potential on connecting two capacitors: $V_{\\text{common}} = \\frac{C_1 '
                   'V_1 + C_2 V_2}{C_1 + C_2}$.',
        'tips_and_tricks': 'For $n$ identical capacitors of capacitance $C$: $C_{\\text{parallel}} / '
                           'C_{\\text{series}} = n^2$.'}],

    "kcet-semiconductor-devices-and-logic-gates": [   {   'category': 'Device Physics',
        'common_traps': 'In the depletion region of an unbiased p-n junction, there are NO free electrons or '
                        'holes—only immobile positive and negative donor/acceptor ions!',
        'formula_cues': ['n_e n_h = n_i^2', '\\text{group 13}', '\\text{group 15}', 'd_1 \\text{ and } d_2'],
        'name': 'Semiconductor Physics: Doping, p-n Junction & Rectifiers',
        'primary': [   'p-type',
                       'n-type',
                       'doping',
                       'arsenic',
                       'indium',
                       'germanium',
                       'silicon',
                       'majority carriers',
                       'depletion region',
                       'barrier potential',
                       'reverse biased',
                       'forward biased',
                       'half-wave rectifier',
                       'full-wave rectifier'],
        'secondary': ['diode', 'electrons', 'holes', 'current', 'conduction'],
        'standard_formulas': 'n_e n_h = n_i^2, \\quad f_{\\text{ripple, half}} = f_{\\text{in}}, \\quad '
                             'f_{\\text{ripple, full}} = 2 f_{\\text{in}}',
        'summary': 'Doping with pentavalent impurities (As, P, Sb) creates n-type (electrons majority). Doping with '
                   'trivalent impurities (In, B, Al) creates p-type (holes majority). Mass action law $n_e n_h = '
                   'n_i^2$. Depletion layer contains immobile uncompensated ions. Forward bias reduces barrier; '
                   'reverse bias widens barrier. Ideal diode acts as closed switch in forward bias, open switch in '
                   'reverse bias.',
        'tips_and_tricks': 'In reverse biased circuits with ideal diodes, replace the reverse-biased diode with an '
                           'open circuit (break the wire) to simplify the circuit instantly.'},
    {   'category': 'Digital Electronics',
        'common_traps': 'NAND with all inputs tied together acts as a NOT gate. NOR with all inputs tied together also '
                        'acts as a NOT gate.',
        'formula_cues': [   'y = \\overline{a \\cdot b}',
                            'y = \\overline{a + b}',
                            '\\overline{a+b} = \\overline{a} \\cdot \\overline{b}',
                            '\\overline{a \\cdot b} = \\overline{a} + \\overline{b}'],
        'name': "Logic Gates, Truth Tables & De Morgan's Laws",
        'primary': [   'logic gate',
                       'truth table',
                       'nand gate',
                       'nor gate',
                       'universal gate',
                       'and gate',
                       'or gate',
                       'not gate',
                       'boolean expression',
                       'de morgan',
                       'output y',
                       'inputs a and b'],
        'secondary': ['binary', 'low', 'high', 'output'],
        'standard_formulas': '\\text{NAND: } Y = \\overline{A \\cdot B}, \\quad \\text{NOR: } Y = \\overline{A + B}, '
                             '\\quad \\overline{A + B} = \\bar{A} \\cdot \\bar{B}, \\quad \\overline{A \\cdot B} = '
                             '\\bar{A} + \\bar{B}',
        'summary': 'Basic gates: AND ($Y = A \\cdot B$), OR ($Y = A + B$), NOT ($Y = \\bar{A}$). Universal gates: NAND '
                   "($Y = \\overline{A \\cdot B}$) and NOR ($Y = \\overline{A + B}$). De Morgan's laws: $\\overline{A "
                   '+ B} = \\bar{A} \\cdot \\bar{B}$ and $\\overline{A \\cdot B} = \\bar{A} + \\bar{B}$.',
        'tips_and_tricks': 'KCET Speed Trick: To identify mystery gate circuits, test inputs $(A=0, B=0)$ and $(A=1, '
                           'B=1)$ first. This eliminates 2 out of 4 options in under 10 seconds.'}],

}

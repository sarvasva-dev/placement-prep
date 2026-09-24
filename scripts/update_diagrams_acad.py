import re

fpath = r'D:\Projects\Placement_Master_Handbook_Web\js\diagrams_acad.js'
with open(fpath, 'r', encoding='utf-8') as f:
    code = f.read()

# Dispatch additions
dispatch_marker = "  // 15. Gauss Elimination & Matrix Upper Triangular (Day 15)"
dispatch_additions = """  // 15a. Gauss-Jordan Method (Diagonal Reduction)
  if (t.includes('jordan')) {
    return createGaussJordanSvg();
  }

  // 15b. Gauss-Seidel Method (Iterative)
  if (t.includes('seidel')) {
    return createGaussSeidelSvg();
  }

  // 15c. Gauss-Jacobi Method (Simultaneous Iteration)
  if (t.includes('jacobi')) {
    return createGaussJacobiSvg();
  }

  // 15d. Numerical Integration: Simpson's 1/3 & 3/8 Rules
  if (t.includes('simpson')) {
    return createSimpsonRulesSvg();
  }

  // 15e. Numerical Integration: Trapezoidal Rule
  if (t.includes('trapezoidal')) {
    return createTrapezoidalSvg();
  }

  // 15f. ODE: Runge-Kutta 4th Order (RK4)
  if (t.includes('runge') || t.includes('rk4') || t.includes('kutta')) {
    return createRk4Svg();
  }

  // 15g. ODE: Euler & Modified Euler Methods
  if (t.includes('euler') || t.includes('heun')) {
    return createEulerMethodsSvg();
  }

  // 15h. Interpolation Workflow
  if (t.includes('interpolation') || t.includes('divided difference') || t.includes('lagrange')) {
    return createInterpolationWorkflowSvg();
  }

  // 15. Gauss Elimination & Matrix Upper Triangular (Day 15)"""

code = code.replace(dispatch_marker, dispatch_additions)

svg_definitions = """
function createGaussJordanSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Gauss-Jordan Method: Complete Diagonal Reduction to Identity [I | X*]</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(50, 40)">
        <rect width="260" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="130" y="30" text-anchor="middle" fill="#38bdf8" font-weight="700">Augmented [A | b]</text>
        <text x="130" y="58" text-anchor="middle" fill="#fff" font-family="monospace">[ a11 a12 a13 | b1 ]</text>
        <text x="130" y="80" text-anchor="middle" fill="#fff" font-family="monospace">[ a21 a22 a23 | b2 ]</text>
        <text x="130" y="102" text-anchor="middle" fill="#fff" font-family="monospace">[ a31 a32 a33 | b3 ]</text>
      </g>
      <line x1="330" y1="95" x2="490" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <text x="410" y="85" text-anchor="middle" fill="#38bdf8" font-size="11">Normalize & Eliminate Above/Below</text>
      <g transform="translate(510, 40)">
        <rect width="280" height="110" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="140" y="30" text-anchor="middle" fill="#a7f3d0" font-weight="700">Reduced Echelon [ I | x* ]</text>
        <text x="140" y="58" text-anchor="middle" fill="#34d399" font-family="monospace">[  1   0   0  | x1* ]</text>
        <text x="140" y="80" text-anchor="middle" fill="#34d399" font-family="monospace">[  0   1   0  | x2* ]</text>
        <text x="140" y="102" text-anchor="middle" fill="#34d399" font-family="monospace">[  0   0   1  | x3* ]</text>
      </g>
      <text x="430" y="180" text-anchor="middle" fill="#cbd5e1" font-size="11">Direct Readout: No back-substitution required; operations = n^3 / 2 flops</text>
    </svg>
  </div>
  `;
}

function createGaussSeidelSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Gauss-Seidel Iterative Method: Immediate In-Place Updating</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(60, 30)">
        <rect width="740" height="120" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <text x="370" y="25" text-anchor="middle" fill="#c084fc" font-weight="800">SUCCESSIVE ITERATIVE UPDATING EQUATIONS</text>
        <text x="370" y="52" text-anchor="middle" fill="#e9d5ff" font-family="monospace">x^(k+1) = [b1 - a12*y^(k) - a13*z^(k)] / a11</text>
        <text x="370" y="77" text-anchor="middle" fill="#34d399" font-family="monospace">y^(k+1) = [b2 - a21*x^(k+1) - a23*z^(k)] / a22  &lt;-- Uses newly computed x^(k+1)!</text>
        <text x="370" y="102" text-anchor="middle" fill="#38bdf8" font-family="monospace">z^(k+1) = [b3 - a31*x^(k+1) - a32*y^(k+1)] / a33 &lt;-- Uses both newly updated values!</text>
      </g>
      <rect x="60" y="165" width="740" height="32" rx="6" fill="#0f172a" stroke="#34d399"/>
      <text x="430" y="186" text-anchor="middle" fill="#a7f3d0" font-size="11">Convergence: Guaranteed if strictly diagonally dominant (|a_ii| > ∑|a_ij|) OR symmetric positive-definite (Ostrowski-Reich)</text>
    </svg>
  </div>
  `;
}

function createGaussJacobiSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Gauss-Jacobi Method: Simultaneous Vector Updating</span>
    </div>
    <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(60, 30)">
        <rect width="320" height="110" rx="8" fill="#1e293b" stroke="#38bdf8"/>
        <text x="160" y="30" text-anchor="middle" fill="#38bdf8" font-weight="700">Iteration k Vector</text>
        <text x="160" y="60" text-anchor="middle" fill="#fff" font-family="monospace">x^(k) , y^(k) , z^(k)</text>
        <text x="160" y="85" text-anchor="middle" fill="#94a3b8" font-size="11">All values held fixed during step</text>
      </g>
      <line x1="400" y1="85" x2="470" y2="85" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#acadArrow)"/>
      <g transform="translate(490, 30)">
        <rect width="320" height="110" rx="8" fill="#0369a1" stroke="#38bdf8"/>
        <text x="160" y="30" text-anchor="middle" fill="#e0f2fe" font-weight="700">Iteration k+1 Vector</text>
        <text x="160" y="60" text-anchor="middle" fill="#fff" font-family="monospace">x^(k+1) , y^(k+1) , z^(k+1)</text>
        <text x="160" y="85" text-anchor="middle" fill="#bae6fd" font-size="11">Simultaneously updated in parallel</text>
      </g>
      <text x="430" y="175" text-anchor="middle" fill="#cbd5e1" font-size="11">Comparison: Jacobi requires 2 full storage vectors; converges roughly 50% slower than Gauss-Seidel</text>
    </svg>
  </div>
  `;
}

function createSimpsonRulesSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Numerical Quadrature: Simpson's 1/3 and 3/8 Parabolic Integration Rules</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 30)">
        <rect width="370" height="110" rx="8" fill="#065f46" stroke="#34d399" stroke-width="2"/>
        <text x="185" y="28" text-anchor="middle" fill="#34d399" font-weight="800">SIMPSON'S 1/3 RULE (2nd Degree Parabolas)</text>
        <text x="185" y="52" text-anchor="middle" fill="#fff" font-family="monospace">I = (h/3) [ (y0 + yn) + 4∑y_odd + 2∑y_even ]</text>
        <text x="185" y="78" text-anchor="middle" fill="#a7f3d0" font-weight="700">Constraint: n MUST BE EVEN (Multiple of 2)</text>
        <text x="185" y="98" text-anchor="middle" fill="#cbd5e1" font-size="10">Truncation error: O(h^4) • Integrates cubics exactly</text>
      </g>
      <g transform="translate(450, 30)">
        <rect width="370" height="110" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="185" y="28" text-anchor="middle" fill="#c7d2fe" font-weight="800">SIMPSON'S 3/8 RULE (3rd Degree Cubics)</text>
        <text x="185" y="52" text-anchor="middle" fill="#fff" font-family="monospace">I = (3h/8) [ (y0 + yn) + 3∑y_non3 + 2∑y_mult3 ]</text>
        <text x="185" y="78" text-anchor="middle" fill="#ddd6fe" font-weight="700">Constraint: n MUST BE A MULTIPLE OF 3</text>
        <text x="185" y="98" text-anchor="middle" fill="#cbd5e1" font-size="10">Truncation error: O(h^4) • Fits cubics through 4 points</text>
      </g>
      <text x="430" y="175" text-anchor="middle" fill="#94a3b8" font-size="11">Parity validation rule: Verify n % 2 == 0 for 1/3 rule and n % 3 == 0 for 3/8 rule before calculating</text>
    </svg>
  </div>
  `;
}

function createTrapezoidalSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Trapezoidal Rule: Linear Segment Numerical Quadrature</span>
    </div>
    <svg viewBox="0 0 860 190" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(60, 25)">
        <rect width="740" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="370" y="28" text-anchor="middle" fill="#38bdf8" font-weight="800">COMPOSITE TRAPEZOIDAL QUADRATURE FORMULA</text>
        <text x="370" y="58" text-anchor="middle" fill="#fff" font-family="monospace">I = (h/2) [ (y0 + yn) + 2 * (y1 + y2 + y3 + ... + y_{n-1}) ]</text>
        <text x="370" y="85" text-anchor="middle" fill="#94a3b8" font-size="11">Applies straight chord trapezoids across strips • Works for ANY number of subintervals n >= 1</text>
      </g>
      <text x="430" y="165" text-anchor="middle" fill="#cbd5e1" font-size="11">Truncation Error: E_T = -[(b - a) h^2 / 12] f''(\u03be) • Order of Accuracy: O(h^2)</text>
    </svg>
  </div>
  `;
}

function createRk4Svg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Runge-Kutta 4th Order (RK4): 4-Slope Simpson Weighted Average</span>
    </div>
    <svg viewBox="0 0 860 210" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 25)">
        <rect width="180" height="90" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="90" y="25" text-anchor="middle" fill="#38bdf8" font-weight="700">k1 (Initial Slope)</text>
        <text x="90" y="55" text-anchor="middle" fill="#fff" font-family="monospace" font-size="10">h * f(x_n, y_n)</text>
      </g>
      <g transform="translate(240, 25)">
        <rect width="180" height="90" rx="6" fill="#0369a1" stroke="#38bdf8"/>
        <text x="90" y="25" text-anchor="middle" fill="#e0f2fe" font-weight="700">k2 (Midpoint Slope 1)</text>
        <text x="90" y="55" text-anchor="middle" fill="#fff" font-family="monospace" font-size="10">h*f(x_n+h/2, y_n+k1/2)</text>
      </g>
      <g transform="translate(440, 25)">
        <rect width="180" height="90" rx="6" fill="#6d28d9" stroke="#c084fc"/>
        <text x="90" y="25" text-anchor="middle" fill="#ddd6fe" font-weight="700">k3 (Midpoint Slope 2)</text>
        <text x="90" y="55" text-anchor="middle" fill="#fff" font-family="monospace" font-size="10">h*f(x_n+h/2, y_n+k2/2)</text>
      </g>
      <g transform="translate(640, 25)">
        <rect width="180" height="90" rx="6" fill="#065f46" stroke="#34d399"/>
        <text x="90" y="25" text-anchor="middle" fill="#a7f3d0" font-weight="700">k4 (Endpoint Slope)</text>
        <text x="90" y="55" text-anchor="middle" fill="#fff" font-family="monospace" font-size="10">h * f(x_n+h, y_n+k3)</text>
      </g>
      <rect x="40" y="135" width="780" height="45" rx="6" fill="#0f172a" stroke="#facc15" stroke-width="2"/>
      <text x="430" y="162" text-anchor="middle" fill="#fde68a" font-weight="800" font-family="monospace">y_(n+1) = y_n + (1/6) * [ k1 + 2*k2 + 2*k3 + k4 ] | Global Error O(h^4)</text>
    </svg>
  </div>
  `;
}

function createEulerMethodsSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Euler's Explicit vs Modified Euler (Heun Predictor-Corrector)</span>
    </div>
    <svg viewBox="0 0 860 190" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 25)">
        <rect width="370" height="110" rx="8" fill="#1e293b" stroke="#38bdf8"/>
        <text x="185" y="28" text-anchor="middle" fill="#38bdf8" font-weight="700">STANDARD EULER (Order 1)</text>
        <text x="185" y="55" text-anchor="middle" fill="#fff" font-family="monospace">y_(n+1) = y_n + h * f(x_n, y_n)</text>
        <text x="185" y="85" text-anchor="middle" fill="#94a3b8" font-size="11">Tangent projection • Global Truncation Error O(h)</text>
      </g>
      <g transform="translate(450, 25)">
        <rect width="370" height="110" rx="8" fill="#1e1b4b" stroke="#a855f7"/>
        <text x="185" y="28" text-anchor="middle" fill="#c084fc" font-weight="700">MODIFIED EULER / HEUN (Order 2)</text>
        <text x="185" y="55" text-anchor="middle" fill="#e9d5ff" font-family="monospace">y* = y_n + h*f(x_n, y_n) (Predictor)</text>
        <text x="185" y="78" text-anchor="middle" fill="#34d399" font-family="monospace">y_(n+1) = y_n + (h/2)[f_n + f(x+h, y*)] (Corrector)</text>
        <text x="185" y="100" text-anchor="middle" fill="#a7f3d0" font-size="11">Global Truncation Error O(h^2)</text>
      </g>
    </svg>
  </div>
  `;
}

function createInterpolationWorkflowSvg() {
  return `
  <div class="svg-diagram-wrapper">
    <div class="svg-diagram-header">
      <span class="svg-tag">CSJMU BCA-5004</span>
      <span class="svg-title">Interpolation Algorithm Selection Workflow Decision Tree</span>
    </div>
    <svg viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg" class="interactive-study-svg">
      <g transform="translate(40, 20)">
        <rect width="200" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="100" y="30" text-anchor="middle" fill="#38bdf8" font-weight="700">Are Intervals Equal?</text>
      </g>
      <!-- Equal path -->
      <line x1="240" y1="45" x2="310" y2="45" stroke="#38bdf8" stroke-width="2" marker-end="url(#acadArrow)"/>
      <text x="275" y="35" text-anchor="middle" fill="#34d399" font-size="10">YES (h constant)</text>
      <g transform="translate(320, 20)">
        <rect width="240" height="60" rx="6" fill="#0369a1" stroke="#38bdf8"/>
        <text x="120" y="25" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">Near Start of Table?</text>
        <text x="120" y="45" text-anchor="middle" fill="#bae6fd" font-size="10">-> Newton Forward Difference</text>
      </g>
      <g transform="translate(590, 20)">
        <rect width="230" height="60" rx="6" fill="#047857" stroke="#34d399"/>
        <text x="115" y="25" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">Near End of Table?</text>
        <text x="115" y="45" text-anchor="middle" fill="#a7f3d0" font-size="10">-> Newton Backward Difference</text>
      </g>
      <!-- Unequal path -->
      <path d="M 140 70 L 140 130 L 310 130" fill="none" stroke="#facc15" stroke-width="2" marker-end="url(#acadArrow)"/>
      <text x="220" y="120" text-anchor="middle" fill="#facc15" font-size="10">NO (Unequal intervals)</text>
      <g transform="translate(320, 105)">
        <rect width="240" height="60" rx="6" fill="#1e1b4b" stroke="#a855f7"/>
        <text x="120" y="25" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">Lagrange Interpolation</text>
        <text x="120" y="45" text-anchor="middle" fill="#e9d5ff" font-size="10">L_i(x) basis polynomials</text>
      </g>
      <g transform="translate(590, 105)">
        <rect width="230" height="60" rx="6" fill="#4c1d95" stroke="#c084fc"/>
        <text x="115" y="25" text-anchor="middle" fill="#fff" font-weight="700" font-size="11">Divided Differences</text>
        <text x="115" y="45" text-anchor="middle" fill="#ddd6fe" font-size="10">f[x0, x1, ... xk] table</text>
      </g>
    </svg>
  </div>
  `;
}
"""

code = code + "\n" + svg_definitions

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated js/diagrams_acad.js with complete 5004 SVG flowchart generators!")

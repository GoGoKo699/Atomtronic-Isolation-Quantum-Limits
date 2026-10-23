# Scattering, spontaneous noise, and additional ports

The canonical relation constrains noise before any encoding or recovery
protocol is chosen. This page derives those constraints in the
[vacuum model](model.md), distinguishes receiver-noise optimization from
positive-output-noise optimization, and shows how an additional positive
port changes the result.

## 1. Receiver-noise floor

From $`AA^\dagger-BB^\dagger=I_2`$ we have $`AA^\dagger\ge I_2`$.
The square matrix $`A`$ has the same singular values in $`AA^\dagger`$ and
$`A^\dagger A`$, so $`A^\dagger A\ge I_2`$ as well. Its second column gives

```math
R+|A_{22}|^2\ge1.
```

The second row commutator gives $`N=G+|A_{22}|^2-1`$. Hence

```math
\boxed{N\ge G-R.}
```

The statement needs the complete two-positive-channel basis. A selected
two-by-two submatrix of a larger passive device need not be expansive and
does not satisfy this proof's premise.

For $`0<R\le\min(G,1)`$, equality is attainable. Choose

```math
A=\begin{pmatrix}
-\sqrt{G(1-R)/R}&\sqrt R\\
\sqrt G&\sqrt{1-R}
\end{pmatrix}.
```

Then $`A^\dagger A=\mathrm{diag}(G/R,1)`$, so one idler completes
the canonical relation with $`BB^\dagger`$ of rank at most one. At
$`G=R`$ no idler coupling is needed. The occupations are

```math
N=G-R,\qquad n_1=\frac{(1-R)(G-R)}R.
```

At fixed forward power this receiver-optimal family needs a diverging source
occupation as $`R\to0`$. It differs from the bounded-noise family below.

## 2. Minimum summed occupation in the positive outputs

Order the directions so that $`f=\sqrt G\ge b=\sqrt R`$, and put
$`d=f-b`$. Let the singular values of $`A`$ be $`s_1\ge s_2\ge1`$.
Writing $`x=|A_{11}|`$ and $`y=|A_{22}|`$, the determinant triangle
inequality implies

```math
\begin{aligned}
(s_1-s_2)^2
&=\mathrm{Tr}(AA^\dagger)-2|\det A|\\
&\ge x^2+y^2+f^2+b^2-2(xy+fb)\\
&=(x-y)^2+(f-b)^2.
\end{aligned}
```

Thus $`s_1\ge s_2+d\ge1+d`$ and

```math
\boxed{n_1+N=s_1^2+s_2^2-2\ge d(d+2).}
```

For $`0\le b\le1`$, define $`r=\sqrt{(1-b)(1+f)}`$ and choose

```math
A=\begin{pmatrix}r&b\\-f&r\end{pmatrix},\qquad
B=\sqrt d\begin{pmatrix}\sqrt{1-b}\\-\sqrt{1+f}\end{pmatrix}.
```

Its singular values are $`1+d`$ and $`1`$, and its occupations are

```math
n_1=d(1-b),\qquad N=d(1+f).
```

One complete three-mode canonical scattering matrix is

```math
S=\begin{pmatrix}
r&b&\sqrt{d(1-b)}\\
-f&r&-\sqrt{d(1+f)}\\
\sqrt{d(1+f)}&-\sqrt{d(1-b)}&1+d
\end{pmatrix},\qquad
SJS^\dagger=J,\quad J=\mathrm{diag}(1,1,-1).
```

For $`G=1,R=0`$, the two positive output occupations are $`1`$ and $`2`$.
Both positive-port reflection powers are $`2`$; this is not a matched
low-reflection isolator. In this vacuum three-mode dilation the physical idler
output also has occupation $`3`$, so the sum over all three physical outputs
is $`6`$. A flux or pump-consumption estimate must also integrate over
frequency.

The inequality itself holds beyond $`b\le1`$, but sharpness there is not
asserted by this construction. The unity-forward branch has a uniformly
stable Hamiltonian realization in [Stable atomic model](stable_atomic_model.md).

## 3. Exact allocation and the cost of a useful reduced quantum link

At specified $`G,R,n_1,N`$, the reflection magnitudes are

```math
x=\sqrt{1+n_1-R},\qquad y=\sqrt{1+N-G}.
```

Optimizing phases, positivity of $`AA^\dagger-I_2`$ is equivalent to

```math
\left(\sqrt G\,x-\sqrt R\,y\right)^2\le n_1N,
```

together with nonnegative occupations and real $`x,y`$. The condition is
sufficient when enough independent idler modes are allowed: choose the
relative phase minimizing the off-diagonal magnitude and factor the resulting
positive matrix as $`BB^\dagger`$. For a single idler, rank one additionally
requires an attainable off-diagonal magnitude exactly $`\sqrt{n_1N}`$.

At $`R=0`$ and $`G>0`$ the condition reduces to

```math
n_1(N-G)\ge G.
```

Every finite-resource device at exact isolation therefore has $`N>G`$.
The reduced channel is strictly inside its entanglement-breaking region.
The [full-channel theorem](collection_boundary.md) shows that even access to
the reflected positive output cannot repair exact isolation in this model.

For the reduced channel to be non-entanglement-breaking, one needs $`N<G`$.
The allocation inequality then gives

```math
\sqrt G\sqrt{1+n_1-R}
\le\sqrt R\sqrt{1+N-G}+\sqrt{n_1N}
<\sqrt R+\sqrt{Gn_1}.
```

Squaring yields

```math
G-(G+1)R<2\sqrt{GRn_1}.
```

Consequently, for $`0<R<G/(G+1)`$,

```math
\boxed{n_1>\frac{[G-(G+1)R]^2}{4GR}.}
```

Equality is the sharp entanglement-breaking boundary $`N=G`$ with a rank-one
noise matrix. Infinitesimal parameter changes on the feasible side yield
$`N<G`$. At fixed $`G`$ the necessary source cost is
$`G/(4R)+O(1)`$. For $`G/(G+1)<R\le\min(G,1)`$, zero source noise is
feasible with $`N=G/R-1<G`$. At $`R=G/(G+1)`$, a non-entanglement-breaking
channel still requires $`n_1>0`$, although the infimum is zero. For other
parameters outside the positive-bound domain, use the full allocation
criterion above; the squared lower bound must not be extended there.

This cost concerns transmission through the reduced channel. Reflection-assisted
distillation can avoid that particular divergence; the finite-energy protocol
is in [Communication rates](communication_rates.md).

## 4. Additional positive auxiliary inputs

Let independent vacuum modes $`\boldsymbol e_+`$ enter through $`C`$:

```math
\boldsymbol b=A\boldsymbol a+C\boldsymbol e_++B\boldsymbol e_-^\dagger,
\qquad AA^\dagger+CC^\dagger-BB^\dagger=I_2.
```

Define $`\ell_j=(CC^\dagger)_{jj}`$ and $`t=R+\ell_1`$.
The smallest eigenvalue of $`AA^\dagger`$ is at least
$`1-\mathrm{Tr}(CC^\dagger)`$. Equality of singular-value spectra
therefore gives $`R+|A_{22}|^2\ge1-\ell_1-\ell_2`$. Combining this with
$`N=G+|A_{22}|^2+\ell_2-1`$ proves

```math
\boxed{N\ge G-R-\ell_1=G-t.}
```

$`\ell_1`$ is coupling power from positive auxiliary inputs into the source
output. It is not generally a measured forward attenuation fraction.

The bound is attained for $`0<t\le\min(G,1)`$, $`R\le t`$. Let

```math
u=\begin{pmatrix}-\sqrt{1-t}\\\sqrt t\end{pmatrix},\quad
v=\begin{pmatrix}\sqrt t\\\sqrt{1-t}\end{pmatrix},
```

and set

```math
A=[\sqrt{G/t}\,u,\sqrt{R/t}\,v],\quad
C=\sqrt{(t-R)/t}\,v,\quad B=\sqrt{G/t-1}\,u.
```

Their commutator matrix is $`uu^\dagger+vv^\dagger=I_2`$ and $`N=G-t`$.
The reduced-channel capacity bounds use $`t`$ in place of $`R`$ in their
stated domain. The vacuum scalar collection threshold, however, must not be
reused without the changed noise correlations; the general matrix criterion
in [Collection boundary](collection_boundary.md) is the appropriate test.

A passive circulator illustrates the escape. With
$`A=\left(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right)`$,
$`C=(1,0)^T`$ and $`B=0`$, one has $`G=1,R=0,\ell_1=1,N=0`$.
The forward link is noiseless because the missing positive port supplies the
necessary canonical channel. Thus reverse nonreciprocity alone does not
force spontaneous emission in an unrestricted multiport network.

## Attribution and verification

Phase-insensitive amplifier-noise limits and nonreciprocal amplifier synthesis
have substantial prior literature. This account uses the canonical relation
to connect the chosen scattering coefficients to a specified communication
interface. [Related work](../references/RELATED_WORK.md) identifies the
closest synthesis papers and the limit of the priority comparison.
The [verification suite](../verification/README.md) checks the saturation
matrices, full canonical relation, Hamiltonian response and channel
consequences independently of the inequalities' general proofs.

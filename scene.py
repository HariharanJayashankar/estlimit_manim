from manim import *
import numpy as np

def parab(x, coeff=0.2, offsetx=10, offsety=2):

    '''
    Parabola
    '''

    return coeff * (x - offsetx) ** 2 + offsety

def dist_parab(x, distx, offsetx=10, offsety=2):
    '''
    defines a distorted parabola. At the x coordinate distx
    the parabola takes the value of 0
    '''

    if x == distx:
        y = 0
    else:
        y = parab(x, offsetx=offsetx, offsety=offsety)

    return y

class Estimator(Scene):
    def construct(self):


        # main curve
        ax = Axes(x_range=(-0.5, 20, 5), y_range=(-2, 20.0, 5)).add_coordinates()
        curve = ax.plot(parab)

        # beta
        xtracker = ValueTracker(5.0)

        beta_pt = np.array([xtracker.get_value(), parab(xtracker.get_value()), 0])
        beta_dot = Dot(point=ax.c2p(*beta_pt))
        beta_txt = Tex(r"$\beta$").move_to(ax.c2p(beta_pt[0], -3))
        beta_line = DashedLine(start=ax.c2p(10, 0),
                         end=ax.c2p(10, parab(10)))

        f_always(
            beta_dot.move_to,
            lambda: ax.c2p(xtracker.get_value(), parab(xtracker.get_value()))
        )
        f_always(
            beta_txt.move_to,
            lambda: ax.c2p(xtracker.get_value(), -3)
        )

        beta_star = Tex(r"$\beta^*$").move_to(ax.c2p(10, -3))

        eqn = Tex(r'''
\begin{align*}
\beta_n &= \text{argmin} f_n(\beta) \\ 
\beta^* &= \text{argmin} f(\beta)
\end{align*}
''')
        limit = Tex(r"$f_n(\beta) \rightarrow f(\beta) \implies \beta_n \rightarrow \beta^*$").move_to(3*UP)

        self.play(Write(eqn))
        self.wait()
        self.play(Unwrite(eqn), runtime=0.5)
        self.play(Write(limit))
        self.play(Create(ax))
        self.play(Create(curve))
        self.play(Write(beta_txt), run_time=0.2)
        self.play(FadeIn(beta_dot), run_time=0.2)
        self.play(xtracker.animate.set_value(15), run_time=1)
        self.play(xtracker.animate.set_value(10), run_time=1)
        self.play(Create(beta_line), run_time=0.2)
        self.play(ReplacementTransform(beta_txt, beta_star))
        self.play(FadeOut(beta_star))

        # Estimator curves
        iter = 1
        colors = ['34a0a4', '168aad', '1a759f', '1e6091']
        colors = ['#' + c.upper() for c in colors]
        for xdist, yoffset in zip([7, 6, 5, 4], [6, 5, 4, 3]):
            
            c = colors[iter-1].upper()
            newparab = lambda x: parab(x, offsetx=10, offsety=yoffset)
            xtracker0 = ValueTracker(xdist-1)
            beta_pt = np.array([xtracker0.get_value(), newparab(xtracker0.get_value()), 0])
            beta_dot0 = Dot(point=ax.c2p(*beta_pt), color=c)
            f_always(
                beta_dot0.move_to,
                lambda: ax.c2p(xtracker0.get_value(), newparab(xtracker0.get_value()))
            )
            betamin = Tex(f"$\\beta_{iter}$", color=c).move_to(ax.c2p(10, -3))
            betaminline = DashedLine(
                start = ax.c2p(10, 0),
                end = ax.c2p(10, newparab(10)),
                color=c
            )
            
            curve1 = ax.plot(newparab, color=c)
            self.play(Create(curve1), run_time=1)
            self.play(FadeIn(beta_dot0), run_time=1)
            self.play(xtracker0.animate.set_value(15), run_time=1)
            self.play(xtracker0.animate.set_value(10), run_time=1)
            self.play(FadeIn(betamin), run_time=1)
            self.play(FadeIn(betaminline), runtime=0.2)
            self.play(FadeOut(betamin), run_time=0.5)
            self.play(FadeOut(beta_dot0), runtime=0.02)
            iter += 1
                    
        self.wait()

class Estimator_bad(Scene):
    def construct(self):


        # main curve
        ax = Axes(x_range=(-0.5, 20, 5), y_range=(-2, 20.0, 5)).add_coordinates()
        curve = ax.plot(parab)

        # beta
        xtracker = ValueTracker(5.0)

        beta_pt = np.array([xtracker.get_value(), parab(xtracker.get_value()), 0])
        beta_dot = Dot(point=ax.c2p(*beta_pt))
        beta_txt = Tex(r"$\beta$").move_to(ax.c2p(beta_pt[0], -3))
        beta_line = DashedLine(start=ax.c2p(10, 0),
                         end=ax.c2p(10, parab(10)))

        f_always(
            beta_dot.move_to,
            lambda: ax.c2p(xtracker.get_value(), parab(xtracker.get_value()))
        )
        f_always(
            beta_txt.move_to,
            lambda: ax.c2p(xtracker.get_value(), -3)
        )

        beta_star = Tex(r"$\beta^*$").move_to(ax.c2p(10, -3))



        limit = Tex(r"$f_n(\beta) \rightarrow f(\beta) \not \implies \beta_n \rightarrow \beta^*$").move_to(3*UP)

        self.play(Write(limit))
        self.play(Create(ax))
        self.play(Create(curve))
        self.play(Write(beta_txt), run_time=0.2)
        self.play(FadeIn(beta_dot), run_time=0.2)
        self.play(xtracker.animate.set_value(15), run_time=1)
        self.play(xtracker.animate.set_value(10), run_time=1)
        self.play(Create(beta_line), run_time=0.2)
        self.play(ReplacementTransform(beta_txt, beta_star))
        self.wait()

        # Estimator curves
        iter = 1
        colors = ['34a0a4', '168aad', '1a759f', '1e6091']
        colors = ['#' + c.upper() for c in colors]
        for xdist, yoffset in zip([7, 6, 5, 4], [6, 5, 4, 3]):
            
            c = colors[iter-1].upper()
            newparab = lambda x: dist_parab(x, xdist, 10, yoffset)
            xtracker0 = ValueTracker(xdist-1)
            beta_pt = np.array([xtracker0.get_value(), newparab(xtracker0.get_value()), 0])
            beta_dot0 = Dot(point=ax.c2p(*beta_pt), color=c)
            f_always(
                beta_dot0.move_to,
                lambda: ax.c2p(xtracker0.get_value(), newparab(xtracker0.get_value()))
            )
            
            curve1 = ax.plot(newparab, color=c)
            betamin = Tex(f"$\\beta_{iter}$", color=c).move_to(ax.c2p(xdist, -3))
            self.play(Create(curve1), run_time=1)
            self.play(FadeIn(beta_dot0), run_time=1)
            self.play(xtracker0.animate.set_value(15), run_time=1)
            self.play(xtracker0.animate.set_value(xdist), run_time=1)
            self.play(FadeIn(betamin))
            self.play(FadeOut(beta_dot0), runtime=0.02)
            iter += 1
                    
        limitarr = Arrow(start=ax.c2p(4, -3), end=ax.c2p(0, -3), color=c)
        self.play(Create(limitarr))
        self.wait()



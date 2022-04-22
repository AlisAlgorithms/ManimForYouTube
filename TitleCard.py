%%manim -v WARNING --disable_caching -qh TitleCard

config.media_width = "100%"


class TitleCard(Scene):
    def construct(self):
        circle = Circle().scale(2.1).set_fill(WHITE, opacity=1).set_stroke(BLACK)
        arabic_Ali = MarkupText(b'\xd8\xb9'.decode('utf8'), font_size=200, font="KufiStandardGK").set_color(BLACK).shift(0.3 * RIGHT, 0.0 * UP)
        arabic_alg = MarkupText(b'\xd8\xa7'.decode('utf8'), font_size=200, font="KufiStandardGK").set_color(BLACK).shift(0.7 * LEFT)
        japanese_Ali = Text(b'\xe4\xba\x9c'.decode('utf8'), font_size=120, weight="ULTRAHEAVY").set_color(BLACK).shift(0.7 * UP)
        japanese_alg = Text(b'\xe3\x82\xa2'.decode('utf8'), font_size=120, weight="ULTRAHEAVY").set_color(BLACK).shift(1.0 * DOWN)
        eng_Ali = Text("A", font_size=160, font="Futura").set_color(BLACK).shift(0.4 * LEFT, 0.1 * UP)
        eng_alg = Text("A", font_size=160, font="Futura").set_color(BLACK).shift(0.4 * RIGHT, 0.1 * UP)
        
        self.play(FadeIn(circle))
        self.play(Write(arabic_Ali),
                  Write(arabic_alg))
        self.wait(1.0)
        self.play(Transform(arabic_alg, japanese_alg), Transform(arabic_Ali, japanese_Ali))
        self.wait(1.0)
        self.play(Transform(arabic_alg, eng_alg), Transform(arabic_Ali, eng_Ali))
        self.wait(1.0)
        self.play(FadeOut(eng_alg), FadeOut(eng_Ali), FadeOut(circle))

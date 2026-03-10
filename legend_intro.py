from manim import *
import random

class NineKLegendsIntro(Scene):
    def construct(self):
        # 1. THE LIGHTNING "KNOCKS"
        knocks_text = "KNOCKS"
        knocks_group = VGroup()
        
        for char in knocks_text:
            letter = Text(char, font="Orbitron", weight=BOLD, color=WHITE).scale(2)
            # Lightning Effect: Quick flash before letter drops
            flash = Flash(UP * 3, color=BLUE_A, flash_radius=0.5, line_length=0.8)
            self.play(flash, run_time=0.1)
            letter.move_to(UP * 4)
            self.play(letter.animate.move_to(ORIGIN), run_time=0.2, rate_func=rush_into)
            knocks_group.add(letter)
        
        knocks_group.arrange(RIGHT, buff=0.5)
        self.wait(0.5)

        # 2. THE SCREECHING "CREATIVE" & REVERSE "STUDIOS"
        creative = Text("CREATIVE", font="Orbitron", color=YELLOW).scale(1.5)
        creative.to_edge(LEFT)
        
        studios_text = "STUDIOS"
        studios_group = VGroup(*[Text(char, font="Orbitron") for char in studios_text])
        
        # Creative passes through, Studios reverses in
        self.play(creative.animate.shift(RIGHT * 15), run_time=0.8, rate_func=linear)
        self.play(
            LaggedStart(*[Write(studios_group[i]) for i in range(len(studios_text)-1, -1, -1)], 
            lag_ratio=0.1),
            run_time=1
        )
        self.remove(knocks_group, creative)

        # 3. THE BULLET-SHOT "STUDIOS" (Bottom Up)
        self.clear()
        bullet_studios = VGroup(*[Text(char, weight=BOLD).scale(1.2) for char in "STUDIOS"])
        bullet_studios.arrange(RIGHT, buff=0.3)
        
        for letter in bullet_studios:
            letter.shift(DOWN * 5)
            # Bullet shot logic
            self.play(letter.animate.shift(UP * 5), run_time=0.15, rate_func=ease_out_expo)
            self.add(Explosion(letter.get_bottom(), color=GRAY)) # Custom explosion trigger

        # 4. THE TITANGINE BLOCK (Flicker & Color Spin)
        cube = Cube(side_length=3, fill_opacity=0.8).set_color(GREEN)
        
        # Flicker formation
        for _ in range(10):
            flicker_square = Square(side_length=0.5).move_to(np.random.randn(3))
            self.add(flicker_square)
            self.wait(0.05)
            self.remove(flicker_square)

        self.play(Create(cube))

        # The Sovereign Pulse Color Cycle
        colors = [GREEN, YELLOW, RED, BLUE]
        for col in colors:
            self.play(
                Rotate(cube, angle=PI/2, axis=RIGHT),
                cube.animate.set_color(col),
                # Background smoke simulation (Light color shift)
                self.camera.background_canvas.animate.set_fill(col, opacity=0.1),
                run_time=0.6
            )

        # FINAL TRADEMARK BURN
        trademark = Text("KNOCKSSTUDiOS", color=WHITE).scale(0.5).move_to(cube.get_center())
        self.play(AddTextLetterByLetter(trademark))
        self.wait(2)

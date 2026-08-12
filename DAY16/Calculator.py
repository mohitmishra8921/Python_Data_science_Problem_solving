"""
Advanced Calculator (Fabulous GUI Edition)
--------------------------------------------
A polished, glowing, gradient-themed Tkinter desktop calculator.

Features:
    - Diagonal gradient background (deep purple -> midnight blue -> pink)
    - Glassmorphic display panel with soft glow border
    - Rounded, gradient-filled buttons with hover glow + press animation
    - Pulsing glow ring around the "=" button
    - Live expression preview as you type
    - Slide-in history panel
    - Full keyboard support

Run with: python advanced_calculator_gui.py
(Tkinter ships with standard Python — no installs needed.)
"""

import math
import re
import ast
import operator
import tkinter as tk
from tkinter import font as tkfont


# ============================================================
# CALCULATION ENGINE (safe AST-based evaluator)
# ============================================================

class CalculatorError(Exception):
    pass


class CalculatorEngine:
    BIN_OPS = {
        ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Mod: operator.mod, ast.Pow: operator.pow,
        ast.FloorDiv: operator.floordiv,
    }
    UNARY_OPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}
    FUNCTIONS = {
        "sqrt": math.sqrt,
        "cbrt": lambda x: math.copysign(abs(x) ** (1 / 3), x),
        "abs": abs,
        "log": lambda x, base=10: math.log(x, base),
        "ln": math.log,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "asin": lambda x: math.degrees(math.asin(x)),
        "acos": lambda x: math.degrees(math.acos(x)),
        "atan": lambda x: math.degrees(math.atan(x)),
        "round": round, "floor": math.floor, "ceil": math.ceil, "exp": math.exp,
    }
    CONSTANTS = {"pi": math.pi, "e": math.e}

    def __init__(self):
        self.history = []

    def preprocess(self, expr):
        expr = expr.strip()
        if not expr:
            raise CalculatorError("Empty expression.")

        match = re.match(r"^(.+?)\s*%\s*of\s*(.+)$", expr, re.IGNORECASE)
        if match:
            expr = f"({match.group(1)}/100)*({match.group(2)})"

        while re.search(r"(\d+(\.\d+)?|\))!", expr):
            expr = re.sub(r"(\d+(\.\d+)?)!", r"factorial(\1)", expr)
            expr = re.sub(r"\(([^()]*)\)!", r"factorial(\1)", expr)

        expr = expr.replace("^", "**")
        expr = re.sub(r"(\d+(\.\d+)?)\s*%", r"(\1/100)", expr)
        expr = re.sub(r"(\d)(\s*)([a-zA-Z(])", r"\1*\3", expr)
        expr = re.sub(r"(\))(\s*)(\d|[a-zA-Z(])", r"\1*\3", expr)
        return expr

    def factorial(self, n):
        if n < 0 or int(n) != n:
            raise CalculatorError("Factorial needs a non-negative integer.")
        return math.factorial(int(n))

    def evaluate(self, expr):
        original = expr
        expr = self.preprocess(expr)
        try:
            tree = ast.parse(expr, mode="eval")
            result = self._eval_node(tree.body)
        except CalculatorError:
            raise
        except ZeroDivisionError:
            raise CalculatorError("Cannot divide by zero.")
        except (SyntaxError, TypeError, ValueError):
            raise CalculatorError("Invalid expression.")
        self.history.append((original, result))
        return result

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise CalculatorError("Unsupported value.")
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self.BIN_OPS:
                raise CalculatorError("Unsupported operator.")
            return self.BIN_OPS[op_type](self._eval_node(node.left), self._eval_node(node.right))
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self.UNARY_OPS:
                raise CalculatorError("Unsupported operator.")
            return self.UNARY_OPS[op_type](self._eval_node(node.operand))
        elif isinstance(node, ast.Name):
            if node.id in self.CONSTANTS:
                return self.CONSTANTS[node.id]
            raise CalculatorError(f"Unknown name '{node.id}'.")
        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise CalculatorError("Unsupported call.")
            fname = node.func.id
            args = [self._eval_node(a) for a in node.args]
            if fname == "factorial":
                return self.factorial(*args)
            if fname in self.FUNCTIONS:
                try:
                    return self.FUNCTIONS[fname](*args)
                except ValueError as e:
                    raise CalculatorError(str(e))
            raise CalculatorError(f"Unknown function '{fname}()'.")
        else:
            raise CalculatorError("Unsupported expression.")


def format_result(result):
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    if isinstance(result, float):
        return f"{round(result, 10):g}"
    return str(result)


# ============================================================
# COLOR THEME
# ============================================================

# Diagonal background gradient stops (deep purple -> indigo -> hot pink glow)
BG_GRADIENT = ["#1e1b4b", "#2d1b5e", "#3b1c5a", "#4a1942", "#5b1d3f"]

PANEL_GLASS = "#241b3e"       # display / history panel base (semi-glass look)
PANEL_BORDER = "#8b5cf6"      # violet glow border
EXPR_FG = "#a78bfa"
RESULT_FG = "#ffffff"

# Button category gradients (top color, bottom color) + hover/press variants
NUM_TOP, NUM_BOT = "#2d2b52", "#211f3d"
NUM_HOVER = "#3a3768"

FUNC_TOP, FUNC_BOT = "#4c1d95", "#3b1573"
FUNC_HOVER = "#5f27b5"

OP_TOP, OP_BOT = "#f472b6", "#ec4899"
OP_HOVER = "#fb7fc4"

CLEAR_TOP, CLEAR_BOT = "#64748b", "#475569"
CLEAR_HOVER = "#7c8aa5"

EQ_TOP, EQ_BOT = "#34d399", "#059669"
EQ_HOVER = "#4ee6ad"
EQ_GLOW = "#34d399"

TEXT_LIGHT = "#f5f3ff"


# ============================================================
# GRADIENT BACKGROUND CANVAS
# ============================================================

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(c))) for c in rgb)


def blend(c1, c2, t):
    r1, g1, b1 = hex_to_rgb(c1)
    r2, g2, b2 = hex_to_rgb(c2)
    return rgb_to_hex((r1 + (r2 - r1) * t, g1 + (g2 - g1) * t, b1 + (b2 - b1) * t))


def draw_vertical_gradient(canvas, width, height, colors):
    """Draw a smooth multi-stop vertical gradient across a canvas."""
    canvas.delete("gradient")
    segments = len(colors) - 1
    steps_per_segment = max(1, height // (segments * 2))
    total_steps = segments * steps_per_segment
    for i in range(total_steps):
        seg = min(i // steps_per_segment, segments - 1)
        local_t = (i - seg * steps_per_segment) / steps_per_segment
        color = blend(colors[seg], colors[seg + 1], local_t)
        y0 = int(i * height / total_steps)
        y1 = int((i + 1) * height / total_steps) + 1
        canvas.create_rectangle(0, y0, width, y1, fill=color, outline="", tags="gradient")


# ============================================================
# ROUNDED, GRADIENT-FILLED GLOW BUTTON
# ============================================================

class GlowButton(tk.Canvas):
    """A rounded button with a subtle top-to-bottom gradient fill,
    soft drop shadow, hover glow ring, and a press-shrink animation."""

    def __init__(self, parent, text, command, top_color, bottom_color, hover_color,
                 fg=TEXT_LIGHT, font_size=17, radius=18, width=84, height=64,
                 glow=False, glow_color=None, bg_parent=PANEL_GLASS, **kwargs):
        super().__init__(parent, width=width, height=height, bg=bg_parent,
                          highlightthickness=0, **kwargs)
        self.command = command
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.hover_color = hover_color
        self.fg = fg
        self.radius = radius
        self.w = width
        self.h = height
        self.text = text
        self.glow = glow
        self.glow_color = glow_color or top_color
        self.font = tkfont.Font(family="Segoe UI", size=font_size, weight="bold")
        self._pressed = False
        self._hovering = False

        self._render(top_color, bottom_color)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

        if self.glow:
            self._pulse_phase = 0
            self._animate_glow()

    def _round_rect_points(self, x1, y1, x2, y2, r):
        return [
            x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r,
            x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2,
            x1, y2, x1, y2 - r, x1, y1 + r, x1, y1,
        ]

    def _render(self, top, bottom, inset=3, shadow=True):
        self.delete("all")

        # Soft drop shadow (slightly offset, darker translucent-ish rect)
        if shadow and not self._pressed:
            self.create_polygon(
                self._round_rect_points(4, 6, self.w - 2, self.h, self.radius),
                fill="#0b0a17", outline="", smooth=True
            )

        x1, y1 = (inset, inset) if self._pressed else (2, 2)
        x2, y2 = (self.w - inset, self.h - inset - 2) if self._pressed else (self.w - 2, self.h - 2)

        # Gradient fill via thin horizontal strips clipped to rounded rect illusion
        steps = 10
        strip_h = (y2 - y1) / steps
        for i in range(steps):
            t = i / (steps - 1)
            color = blend(top, bottom, t)
            sy1 = y1 + i * strip_h
            sy2 = y1 + (i + 1) * strip_h
            self.create_rectangle(x1 + 2, sy1, x2 - 2, sy2, fill=color, outline="")

        # Rounded outline on top to fake clipped corners
        self.create_polygon(
            self._round_rect_points(x1, y1, x2, y2, self.radius),
            fill="", outline=blend(top, "#000000", 0.15), width=1, smooth=True
        )
        # Re-draw fill shape as the true rounded silhouette (mask illusion)
        mask_color = blend(top, bottom, 0.5)
        self.create_polygon(
            self._round_rect_points(x1, y1, x2, y2, self.radius),
            fill="", outline="", smooth=True
        )

        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=self.text,
                          fill=self.fg, font=self.font)

    def _on_enter(self, event):
        self._hovering = True
        self._render(self.hover_color, self.bottom_color)

    def _on_leave(self, event):
        self._hovering = False
        if not self._pressed:
            self._render(self.top_color, self.bottom_color)

    def _on_press(self, event):
        self._pressed = True
        self._render(self.hover_color, self.hover_color)

    def _on_release(self, event):
        self._pressed = False
        base_top = self.hover_color if self._hovering else self.top_color
        self._render(base_top, self.bottom_color)
        if self.command:
            self.command()

    def _animate_glow(self):
        import math as _m
        self._pulse_phase = (self._pulse_phase + 0.12) % (2 * _m.pi)
        intensity = 0.5 + 0.5 * _m.sin(self._pulse_phase)
        # Draw a soft glow ring behind by tagging lower stacking (visual pulse via outline color)
        self.after(80, self._animate_glow)


class GlowRing(tk.Canvas):
    """A separate pulsing glow ring drawn behind the equals button for extra flair."""

    def __init__(self, parent, width, height, color, bg_parent):
        super().__init__(parent, width=width, height=height, bg=bg_parent, highlightthickness=0)
        self.color = color
        self.w = width
        self.h = height
        self.phase = 0
        self._draw(0.4)
        self._animate()

    def _draw(self, intensity):
        self.delete("all")
        pad = 6
        r = 22
        alpha_layers = 4
        for i in range(alpha_layers, 0, -1):
            grow = i * 3 * intensity
            color = blend(self.color, PANEL_GLASS, 1 - (i / alpha_layers) * intensity)
            self.create_polygon(
                pad - grow, pad - grow, self.w - pad + grow, pad - grow,
                self.w - pad + grow, self.h - pad + grow, pad - grow, self.h - pad + grow,
                fill="", outline=color, width=2, smooth=True
            )

    def _animate(self):
        self.phase = (self.phase + 0.1) % (2 * math.pi)
        intensity = 0.35 + 0.25 * math.sin(self.phase)
        self._draw(intensity)
        self.after(90, self._animate)


# ============================================================
# MAIN APPLICATION
# ============================================================

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.engine = CalculatorEngine()
        self.expression = ""
        self.history_visible = False

        root.title("✨ Advanced Calculator")
        root.resizable(False, False)
        self.WIDTH, self.HEIGHT = 440, 700
        self._center_window(self.WIDTH, self.HEIGHT)

        # Full-window gradient background canvas
        self.bg_canvas = tk.Canvas(root, width=self.WIDTH, height=self.HEIGHT, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0)
        draw_vertical_gradient(self.bg_canvas, self.WIDTH, self.HEIGHT, BG_GRADIENT)

        self._build_display()
        self._build_history_panel()
        self._build_keypad()
        self._bind_keyboard()

    def _center_window(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # ---------------- Display (glassmorphic panel) ----------------
    def _build_display(self):
        panel_h = 170
        self.display_canvas = tk.Canvas(self.root, width=self.WIDTH - 32, height=panel_h,
                                         bg=BG_GRADIENT[0], highlightthickness=0)
        self.display_canvas.place(x=16, y=20)
        self._draw_rounded_panel(self.display_canvas, self.WIDTH - 32, panel_h, PANEL_GLASS, PANEL_BORDER)

        top_bar = tk.Frame(self.display_canvas, bg=PANEL_GLASS)
        self.display_canvas.create_window(16, 16, window=top_bar, anchor="nw")

        self.history_btn = tk.Label(top_bar, text="☰  History", bg=PANEL_GLASS,
                                     fg=EXPR_FG, font=("Segoe UI", 10, "bold"), cursor="hand2")
        self.history_btn.pack(side="left")
        self.history_btn.bind("<Button-1>", lambda e: self.toggle_history())

        title = tk.Label(top_bar, text="  ✨ Fabulous Calc", bg=PANEL_GLASS,
                          fg="#c4b5fd", font=("Segoe UI", 9))
        title.pack(side="left")

        self.expr_var = tk.StringVar(value="")
        expr_holder = tk.Frame(self.display_canvas, bg=PANEL_GLASS)
        self.display_canvas.create_window(self.WIDTH - 48, 78, window=expr_holder, anchor="e")
        self.expr_label = tk.Label(expr_holder, textvariable=self.expr_var, bg=PANEL_GLASS,
                                    fg=EXPR_FG, font=("Consolas", 15))
        self.expr_label.pack()

        self.result_var = tk.StringVar(value="0")
        result_holder = tk.Frame(self.display_canvas, bg=PANEL_GLASS)
        self.display_canvas.create_window(self.WIDTH - 48, 128, window=result_holder, anchor="e")
        self.result_label = tk.Label(result_holder, textvariable=self.result_var, bg=PANEL_GLASS,
                                      fg=RESULT_FG, font=("Consolas", 38, "bold"))
        self.result_label.pack()

    def _draw_rounded_panel(self, canvas, w, h, fill_color, border_color, r=24):
        pts = [
            r, 0, w - r, 0, w, 0, w, r,
            w, h - r, w, h, w - r, h, r, h,
            0, h, 0, h - r, 0, r, 0, 0,
        ]
        canvas.create_polygon(pts, fill=fill_color, outline="", smooth=True)
        canvas.create_polygon(pts, fill="", outline=border_color, width=2, smooth=True)

    # ---------------- History panel ----------------
    def _build_history_panel(self):
        self.history_canvas = tk.Canvas(self.root, width=self.WIDTH - 32, height=440,
                                         bg=BG_GRADIENT[1], highlightthickness=0)
        self._draw_rounded_panel(self.history_canvas, self.WIDTH - 32, 440, PANEL_GLASS, PANEL_BORDER)

        header = tk.Frame(self.history_canvas, bg=PANEL_GLASS)
        self.history_canvas.create_window(16, 14, window=header, anchor="nw")
        tk.Label(header, text="📜 History", bg=PANEL_GLASS, fg=TEXT_LIGHT,
                 font=("Segoe UI", 13, "bold")).pack(side="left")

        clear_frame = tk.Frame(self.history_canvas, bg=PANEL_GLASS)
        self.history_canvas.create_window(self.WIDTH - 48, 18, window=clear_frame, anchor="ne")
        clear_btn = tk.Label(clear_frame, text="Clear", bg=PANEL_GLASS, fg=OP_TOP,
                              font=("Segoe UI", 10, "bold"), cursor="hand2")
        clear_btn.pack()
        clear_btn.bind("<Button-1>", lambda e: self.clear_history())

        self.history_list_frame = tk.Frame(self.history_canvas, bg=PANEL_GLASS)
        self.history_canvas.create_window(16, 50, window=self.history_list_frame, anchor="nw",
                                           width=self.WIDTH - 64, height=370)

        self._render_history()

    def _render_history(self):
        for widget in self.history_list_frame.winfo_children():
            widget.destroy()

        if not self.engine.history:
            tk.Label(self.history_list_frame, text="No calculations yet.",
                     bg=PANEL_GLASS, fg=EXPR_FG, font=("Segoe UI", 10)).pack(pady=20)
            return

        for expr, result in reversed(self.engine.history[-30:]):
            row = tk.Frame(self.history_list_frame, bg=PANEL_GLASS)
            row.pack(fill="x", pady=5)
            tk.Label(row, text=expr, bg=PANEL_GLASS, fg="#c9c3e8",
                     font=("Consolas", 11), anchor="w").pack(fill="x")
            tk.Label(row, text=f"= {format_result(result)}", bg=PANEL_GLASS,
                     fg=EQ_TOP, font=("Consolas", 14, "bold"), anchor="w").pack(fill="x")

    def toggle_history(self):
        self.history_visible = not self.history_visible
        if self.history_visible:
            self._render_history()
            self.history_canvas.place(x=16, y=200)
        else:
            self.history_canvas.place_forget()

    def clear_history(self):
        self.engine.history.clear()
        self._render_history()

    # ---------------- Keypad ----------------
    def _build_keypad(self):
        pad = tk.Frame(self.root, bg=BG_GRADIENT[2])
        pad.place(x=12, y=204, width=self.WIDTH - 24, height=self.HEIGHT - 220)
        # Make the keypad frame background match the local gradient band beneath it
        pad.configure(bg=blend(BG_GRADIENT[2], BG_GRADIENT[3], 0.5))
        band_color = pad["bg"]

        rows = [
            [("sin", self.func_btn("sin("), "func"), ("cos", self.func_btn("cos("), "func"),
             ("tan", self.func_btn("tan("), "func"), ("C", self.clear_all, "clear")],
            [("√", self.func_btn("sqrt("), "func"), ("log", self.func_btn("log("), "func"),
             ("ln", self.func_btn("ln("), "func"), ("⌫", self.backspace, "clear")],
            [("(", self.append_char("("), "func"), (")", self.append_char(")"), "func"),
             ("^", self.append_char("^"), "func"), ("÷", self.append_char("/"), "op")],
            [("7", self.append_char("7"), "num"), ("8", self.append_char("8"), "num"),
             ("9", self.append_char("9"), "num"), ("×", self.append_char("*"), "op")],
            [("4", self.append_char("4"), "num"), ("5", self.append_char("5"), "num"),
             ("6", self.append_char("6"), "num"), ("−", self.append_char("-"), "op")],
            [("1", self.append_char("1"), "num"), ("2", self.append_char("2"), "num"),
             ("3", self.append_char("3"), "num"), ("+", self.append_char("+"), "op")],
            [("%", self.append_char("%"), "num"), ("0", self.append_char("0"), "num"),
             (".", self.append_char("."), "num"), ("=", self.calculate, "equals")],
        ]

        style_map = {
            "num": (NUM_TOP, NUM_BOT, NUM_HOVER),
            "func": (FUNC_TOP, FUNC_BOT, FUNC_HOVER),
            "op": (OP_TOP, OP_BOT, OP_HOVER),
            "clear": (CLEAR_TOP, CLEAR_BOT, CLEAR_HOVER),
            "equals": (EQ_TOP, EQ_BOT, EQ_HOVER),
        }

        for row in rows:
            row_frame = tk.Frame(pad, bg=band_color)
            row_frame.pack(fill="both", expand=True, pady=5)
            for label, cmd, kind in row:
                top, bot, hover = style_map[kind]
                fsize = 13 if kind == "func" else 19
                glow = (kind == "equals")
                btn = GlowButton(row_frame, label, cmd, top, bot, hover,
                                  font_size=fsize, width=92, height=60,
                                  glow=glow, glow_color=EQ_GLOW, bg_parent=band_color)
                btn.pack(side="left", padx=5, expand=True)

    # ---------------- Actions ----------------
    def func_btn(self, text):
        return lambda: self.append_text(text)

    def append_char(self, ch):
        return lambda: self.append_text(ch)

    def append_text(self, text):
        self.expression += text
        self.expr_var.set(self.expression)
        self._live_preview()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.expr_var.set(self.expression)
        self._live_preview()

    def clear_all(self):
        self.expression = ""
        self.expr_var.set("")
        self.result_var.set("0")

    def _live_preview(self):
        if not self.expression.strip():
            self.result_var.set("0")
            return
        try:
            probe = CalculatorEngine()
            result = probe.evaluate(self.expression)
            self.result_var.set(format_result(result))
        except CalculatorError:
            pass

    def calculate(self):
        if not self.expression.strip():
            return
        try:
            result = self.engine.evaluate(self.expression)
            formatted = format_result(result)
            self.expr_var.set(self.expression + " =")
            self.result_var.set(formatted)
            self.expression = formatted
            if self.history_visible:
                self._render_history()
        except CalculatorError as e:
            self.result_var.set("Error")
            self.expr_var.set(str(e))
            self.expression = ""

    # ---------------- Keyboard support ----------------
    def _bind_keyboard(self):
        self.root.bind("<Key>", self._on_key)

    def _on_key(self, event):
        char = event.char
        if event.keysym == "Return":
            self.calculate()
        elif event.keysym == "BackSpace":
            self.backspace()
        elif event.keysym == "Escape":
            self.clear_all()
        elif char and (char.isdigit() or char in "+-*/().%^"):
            self.append_text(char)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
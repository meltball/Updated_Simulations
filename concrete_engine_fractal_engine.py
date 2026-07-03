"""
Concrete Engine Continuous Fractal Engine
Version: 0.1 prototype

This replaces the old menu-based fractal demo with a continuous parameter engine.
It supports:
- Mandelbrot / Julia / Burning Ship / Multibrot style rendering
- Smooth morphing between presets
- Animation over time
- Concrete Engine-specific parameters such as gpu_load, cluster_size, network_bandwidth
- Preset scenes: AI Training, Compute Explosion, Mineral Scanner, Border Radar, Agriculture, Digital Twin

Install:
    pip install numpy matplotlib

Run:
    python concrete_engine_fractal_engine.py
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Callable
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ------------------------------------------------------------
# Parameter Models
# ------------------------------------------------------------

@dataclass
class GeometryParameters:
    xmin: float = -2.0
    xmax: float = 1.0
    ymin: float = -1.5
    ymax: float = 1.5
    zoom: float = 1.0
    offset_x: float = -0.5
    offset_y: float = 0.0
    rotation: float = 0.0


@dataclass
class FormulaParameters:
    fractal_type: float = 0.0
    # 0 = Mandelbrot
    # 1 = Julia
    # 2 = Burning Ship
    # 3 = Multibrot

    formula_blend: float = 0.0
    exponent: float = 2.0
    escape_radius: float = 4.0
    max_iter: int = 180

    julia_real: float = -0.8
    julia_imag: float = 0.156


@dataclass
class RenderParameters:
    palette_shift: float = 0.0
    palette_speed: float = 0.04
    gamma: float = 1.0
    contrast: float = 1.0
    brightness: float = 1.0
    glow: float = 0.35
    smooth_coloring: bool = True


@dataclass
class AnimationParameters:
    time_scale: float = 1.0
    zoom_speed: float = 0.002
    rotation_speed: float = 0.002
    morph_speed: float = 0.01
    pulse_strength: float = 0.05


@dataclass
class NoiseParameters:
    warp_strength: float = 0.0
    noise_frequency: float = 1.0
    turbulence: float = 0.0


@dataclass
class SymmetryParameters:
    mirror: float = 0.0
    kaleidoscope_segments: int = 0
    radial_strength: float = 0.0


@dataclass
class ConcreteEngineParameters:
    gpu_load: float = 0.50
    gpu_count: int = 256
    cluster_size: int = 1
    network_bandwidth: float = 0.50
    storage_bandwidth: float = 0.50
    memory_usage: float = 0.50
    power_usage: float = 0.50
    cooling_efficiency: float = 0.85
    parallelism: float = 0.70
    distributed_nodes: int = 8
    compute_intensity: float = 0.65


@dataclass
class DomainParameters:
    density_threshold: float = 0.50
    mineral_probability: float = 0.50
    heatmap_intensity: float = 0.50
    radar_range: float = 0.50
    thermal_intensity: float = 0.50
    crop_health: float = 0.50
    water_stress: float = 0.50


@dataclass
class FractalState:
    geometry: GeometryParameters
    formula: FormulaParameters
    render: RenderParameters
    animation: AnimationParameters
    noise: NoiseParameters
    symmetry: SymmetryParameters
    concrete: ConcreteEngineParameters
    domain: DomainParameters


# ------------------------------------------------------------
# Presets
# ------------------------------------------------------------

def base_state() -> FractalState:
    return FractalState(
        geometry=GeometryParameters(),
        formula=FormulaParameters(),
        render=RenderParameters(),
        animation=AnimationParameters(),
        noise=NoiseParameters(),
        symmetry=SymmetryParameters(),
        concrete=ConcreteEngineParameters(),
        domain=DomainParameters(),
    )


def preset_ai_training() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 1.0
    s.formula.julia_real = -0.745
    s.formula.julia_imag = 0.113
    s.formula.max_iter = 240
    s.render.palette_speed = 0.08
    s.render.glow = 0.70
    s.animation.zoom_speed = 0.006
    s.animation.rotation_speed = 0.004
    s.concrete.gpu_load = 0.88
    s.concrete.compute_intensity = 0.92
    s.concrete.parallelism = 0.95
    return s


def preset_compute_explosion() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 3.0
    s.formula.exponent = 4.0
    s.formula.max_iter = 320
    s.render.contrast = 1.35
    s.render.glow = 1.0
    s.animation.zoom_speed = 0.012
    s.animation.rotation_speed = 0.012
    s.animation.pulse_strength = 0.18
    s.noise.warp_strength = 0.06
    s.concrete.cluster_size = 24
    s.concrete.distributed_nodes = 128
    s.concrete.gpu_load = 0.96
    return s


def preset_mineral_scanner() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 2.0
    s.formula.max_iter = 220
    s.render.palette_shift = 0.22
    s.render.contrast = 1.50
    s.noise.warp_strength = 0.08
    s.domain.density_threshold = 0.78
    s.domain.mineral_probability = 0.72
    s.domain.heatmap_intensity = 0.90
    return s


def preset_border_radar() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 0.0
    s.formula.max_iter = 160
    s.geometry.rotation = 0.2
    s.render.palette_shift = 0.55
    s.render.glow = 0.85
    s.animation.rotation_speed = 0.018
    s.symmetry.kaleidoscope_segments = 8
    s.domain.radar_range = 0.90
    s.domain.thermal_intensity = 0.75
    return s


def preset_agriculture() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 1.0
    s.formula.julia_real = -0.4
    s.formula.julia_imag = 0.6
    s.formula.max_iter = 180
    s.render.palette_shift = 0.35
    s.noise.warp_strength = 0.05
    s.domain.crop_health = 0.82
    s.domain.water_stress = 0.32
    return s


def preset_digital_twin() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 3.0
    s.formula.exponent = 2.5
    s.formula.max_iter = 260
    s.render.palette_shift = 0.72
    s.render.contrast = 1.15
    s.animation.zoom_speed = 0.004
    s.noise.warp_strength = 0.04
    s.concrete.network_bandwidth = 0.88
    s.concrete.storage_bandwidth = 0.92
    return s


PRESETS: Dict[str, Callable[[], FractalState]] = {
    "AI Training": preset_ai_training,
    "Compute Explosion": preset_compute_explosion,
    "Mineral Scanner": preset_mineral_scanner,
    "Border Radar": preset_border_radar,
    "Agriculture": preset_agriculture,
    "Digital Twin": preset_digital_twin,
}


# ------------------------------------------------------------
# Interpolation
# ------------------------------------------------------------

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def interpolate_dataclass(a, b, t):
    values = {}
    for key, av in asdict(a).items():
        bv = getattr(b, key)
        if isinstance(av, bool):
            values[key] = bv if t > 0.5 else av
        elif isinstance(av, int):
            values[key] = int(round(lerp(float(av), float(bv), t)))
        else:
            values[key] = lerp(float(av), float(bv), t)
    return type(a)(**values)


def interpolate_state(a: FractalState, b: FractalState, t: float) -> FractalState:
    t = max(0.0, min(1.0, t))
    # Smoothstep for cinematic transitions
    t = t * t * (3.0 - 2.0 * t)

    return FractalState(
        geometry=interpolate_dataclass(a.geometry, b.geometry, t),
        formula=interpolate_dataclass(a.formula, b.formula, t),
        render=interpolate_dataclass(a.render, b.render, t),
        animation=interpolate_dataclass(a.animation, b.animation, t),
        noise=interpolate_dataclass(a.noise, b.noise, t),
        symmetry=interpolate_dataclass(a.symmetry, b.symmetry, t),
        concrete=interpolate_dataclass(a.concrete, b.concrete, t),
        domain=interpolate_dataclass(a.domain, b.domain, t),
    )


# ------------------------------------------------------------
# Fractal Renderer
# ------------------------------------------------------------

class FractalEngine:
    def __init__(self, width: int = 700, height: int = 700):
        self.width = width
        self.height = height
        self.time = 0.0

    def complex_grid(self, state: FractalState) -> np.ndarray:
        g = state.geometry
        aspect = self.width / self.height

        zoom = g.zoom * (1.0 + state.animation.pulse_strength * math.sin(self.time * 0.7))
        span_x = (g.xmax - g.xmin) / zoom
        span_y = (g.ymax - g.ymin) / zoom / aspect

        x = np.linspace(g.offset_x - span_x / 2, g.offset_x + span_x / 2, self.width)
        y = np.linspace(g.offset_y - span_y / 2, g.offset_y + span_y / 2, self.height)
        xx, yy = np.meshgrid(x, y)

        # Rotation
        theta = g.rotation + self.time * state.animation.rotation_speed
        c, s = np.cos(theta), np.sin(theta)
        xr = c * xx - s * yy
        yr = s * xx + c * yy

        # Optional domain warp
        if state.noise.warp_strength > 0:
            warp = state.noise.warp_strength
            xr = xr + warp * np.sin(yr * 8 + self.time)
            yr = yr + warp * np.cos(xr * 8 - self.time)

        return xr + 1j * yr

    def render(self, state: FractalState) -> np.ndarray:
        self.time += 0.04 * state.animation.time_scale

        C = self.complex_grid(state)
        Z = np.zeros_like(C, dtype=np.complex128)

        ftype = int(round(state.formula.fractal_type)) % 4
        exponent = max(2.0, state.formula.exponent)
        escape = state.formula.escape_radius
        max_iter = max(10, int(state.formula.max_iter))

        output = np.zeros(C.shape, dtype=np.float32)
        mask = np.ones(C.shape, dtype=bool)

        if ftype == 1:
            # Julia
            c_const = complex(state.formula.julia_real, state.formula.julia_imag)
            Z = C.copy()
            C_iter = np.full_like(C, c_const)
        else:
            # Mandelbrot / Burning Ship / Multibrot
            Z = np.zeros_like(C)
            C_iter = C.copy()

        for i in range(max_iter):
            if ftype == 2:
                # Burning Ship
                Z_abs = np.abs(Z.real) + 1j * np.abs(Z.imag)
                Z[mask] = Z_abs[mask] ** exponent + C_iter[mask]
            else:
                Z[mask] = Z[mask] ** exponent + C_iter[mask]

            escaped = np.abs(Z) > escape
            newly_escaped = escaped & mask
            output[newly_escaped] = i
            mask &= ~escaped

            if not mask.any():
                break

        output[mask] = max_iter

        # Normalize
        image = output / max_iter

        # Concrete Engine signal mapping
        ce = state.concrete
        domain = state.domain

        image = image ** max(0.15, state.render.gamma)
        image *= state.render.contrast
        image += state.render.brightness - 1.0

        # GPU load creates brightness/glow pressure
        image += ce.gpu_load * state.render.glow * 0.12

        # Domain overlays
        if domain.heatmap_intensity > 0.6:
            image += domain.mineral_probability * 0.08 * np.sin(np.abs(C.real) * 20)

        if state.symmetry.kaleidoscope_segments > 0:
            angle = np.angle(C)
            k = state.symmetry.kaleidoscope_segments
            radar = (np.sin(k * angle + self.time * 2.0) + 1.0) * 0.035
            image += radar * domain.radar_range

        # Palette shift over time
        image = (image + state.render.palette_shift + self.time * state.render.palette_speed) % 1.0

        return np.clip(image, 0, 1)


# ------------------------------------------------------------
# Demo Player
# ------------------------------------------------------------

class ContinuousPresetPlayer:
    def __init__(self, preset_names):
        self.preset_names = preset_names
        self.index = 0
        self.transition = 0.0
        self.transition_speed = 0.006

    def current_state(self) -> FractalState:
        a_name = self.preset_names[self.index % len(self.preset_names)]
        b_name = self.preset_names[(self.index + 1) % len(self.preset_names)]

        a = PRESETS[a_name]()
        b = PRESETS[b_name]()

        state = interpolate_state(a, b, self.transition)

        self.transition += self.transition_speed
        if self.transition >= 1.0:
            self.transition = 0.0
            self.index += 1

        return state

    def current_label(self) -> str:
        a = self.preset_names[self.index % len(self.preset_names)]
        b = self.preset_names[(self.index + 1) % len(self.preset_names)]
        return f"{a} → {b}"


def run_demo():
    engine = FractalEngine(width=600, height=600)
    player = ContinuousPresetPlayer(list(PRESETS.keys()))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis("off")

    image = engine.render(player.current_state())
    im = ax.imshow(image, cmap="inferno", animated=True)

    title = ax.set_title("Concrete Engine Continuous Fractal Engine", fontsize=13)

    def update(_frame):
        state = player.current_state()
        image = engine.render(state)

        im.set_array(image)
        title.set_text(
            f"Concrete Engine Fractal Engine | {player.current_label()} | "
            f"GPU Load {state.concrete.gpu_load:.0%} | Nodes {state.concrete.distributed_nodes}"
        )
        return [im, title]

    ani = FuncAnimation(fig, update, interval=33, blit=False)
    plt.show()


if __name__ == "__main__":
    run_demo()

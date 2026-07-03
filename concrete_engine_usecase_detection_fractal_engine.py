"""
Concrete Engine Bombastic Fractal Engine
Version: 0.2 -- "AI FEATURE DETECTION IGNITION"

This is the loud, noisy, investor-demo version.

Features:
- Continuous morphing fractal field
- Shockwaves
- Radar sweeps
- Particle sparks
- Compute-grid overlay
- Noise/warp distortion
- High contrast inferno/plasma style visuals
- Concrete Engine themed presets:
    AI Factory Ignition
    GPU Storm
    Mineral Heat Scanner
    Border Radar Wall
    Sovereign Compute Grid
    Digital Twin Explosion

Install:
    pip install numpy matplotlib

Run:
    python concrete_engine_feature_detection_fractal_engine.py
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Callable
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ============================================================
# PARAMETER MODELS
# ============================================================

@dataclass
class GeometryParameters:
    zoom: float = 1.0
    offset_x: float = -0.45
    offset_y: float = 0.0
    rotation: float = 0.0
    camera_shake: float = 0.03


@dataclass
class FormulaParameters:
    fractal_type: float = 0.0
    # 0 = Mandelbrot
    # 1 = Julia
    # 2 = Burning Ship
    # 3 = Multibrot

    exponent: float = 2.0
    escape_radius: float = 5.0
    max_iter: int = 240

    julia_real: float = -0.745
    julia_imag: float = 0.113


@dataclass
class RenderParameters:
    palette: str = "inferno"
    palette_shift: float = 0.0
    palette_speed: float = 0.10
    gamma: float = 0.65
    contrast: float = 1.75
    brightness: float = 1.10
    glow: float = 1.25
    bloom: float = 0.60
    scanlines: float = 0.08
    vignette: float = 0.40


@dataclass
class AnimationParameters:
    time_scale: float = 1.0
    zoom_speed: float = 0.016
    rotation_speed: float = 0.018
    pulse_strength: float = 0.20
    shockwave_strength: float = 0.45
    shockwave_speed: float = 2.5
    glitch_strength: float = 0.04


@dataclass
class NoiseParameters:
    warp_strength: float = 0.12
    turbulence: float = 0.22
    electric_noise: float = 0.18
    grain: float = 0.06


@dataclass
class SymmetryParameters:
    kaleidoscope_segments: int = 6
    radial_strength: float = 0.22
    mirror_strength: float = 0.15


@dataclass
class ConcreteEngineParameters:
    gpu_load: float = 0.97
    gpu_count: int = 4096
    cluster_size: int = 32
    network_bandwidth: float = 0.92
    storage_bandwidth: float = 0.88
    memory_usage: float = 0.91
    power_usage: float = 0.96
    cooling_efficiency: float = 0.91
    parallelism: float = 0.98
    distributed_nodes: int = 256
    compute_intensity: float = 0.99


@dataclass
class DomainParameters:
    mineral_probability: float = 0.70
    heatmap_intensity: float = 0.90
    radar_range: float = 0.85
    threat_level: float = 0.60
    terrain_depth: float = 0.80
    ai_training_progress: float = 0.55


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


# ============================================================
# PRESETS
# ============================================================

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


def preset_ai_factory_ignition() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 3
    s.formula.exponent = 3.5
    s.formula.max_iter = 320
    s.render.palette = "inferno"
    s.render.contrast = 2.0
    s.render.glow = 1.4
    s.animation.shockwave_strength = 0.60
    s.animation.zoom_speed = 0.020
    s.noise.warp_strength = 0.16
    s.symmetry.kaleidoscope_segments = 9
    s.concrete.gpu_load = 0.99
    s.concrete.gpu_count = 8192
    s.concrete.distributed_nodes = 512
    return s


def preset_gpu_storm() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 1
    s.formula.julia_real = -0.835
    s.formula.julia_imag = -0.2321
    s.formula.max_iter = 280
    s.render.palette = "plasma"
    s.render.palette_speed = 0.16
    s.animation.rotation_speed = 0.030
    s.animation.pulse_strength = 0.28
    s.noise.electric_noise = 0.28
    s.noise.grain = 0.08
    s.concrete.network_bandwidth = 0.98
    s.concrete.parallelism = 1.0
    return s


def preset_mineral_heat_scanner() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 2
    s.formula.exponent = 2.0
    s.render.palette = "turbo"
    s.render.contrast = 2.15
    s.render.glow = 1.15
    s.noise.warp_strength = 0.20
    s.domain.mineral_probability = 0.95
    s.domain.heatmap_intensity = 1.0
    s.domain.terrain_depth = 0.95
    return s


def preset_border_radar_wall() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 0
    s.render.palette = "magma"
    s.animation.rotation_speed = 0.040
    s.animation.shockwave_speed = 4.0
    s.symmetry.kaleidoscope_segments = 16
    s.domain.radar_range = 1.0
    s.domain.threat_level = 0.85
    s.render.scanlines = 0.18
    return s


def preset_sovereign_compute_grid() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 3
    s.formula.exponent = 5.0
    s.formula.max_iter = 360
    s.render.palette = "viridis"
    s.render.contrast = 1.85
    s.animation.zoom_speed = 0.012
    s.symmetry.kaleidoscope_segments = 12
    s.concrete.cluster_size = 64
    s.concrete.distributed_nodes = 1024
    s.concrete.storage_bandwidth = 0.99
    return s


def preset_digital_twin_explosion() -> FractalState:
    s = base_state()
    s.formula.fractal_type = 1
    s.formula.julia_real = -0.4
    s.formula.julia_imag = 0.6
    s.render.palette = "cubehelix"
    s.animation.shockwave_strength = 0.70
    s.animation.glitch_strength = 0.06
    s.noise.turbulence = 0.35
    s.domain.terrain_depth = 1.0
    s.domain.ai_training_progress = 0.88
    return s


PRESETS: Dict[str, Callable[[], FractalState]] = {
    "AI FEATURE DETECTION IGNITION": preset_ai_factory_ignition,
    "GPU STORM": preset_gpu_storm,
    "MINERAL HEAT SCANNER": preset_mineral_heat_scanner,
    "BORDER RADAR WALL": preset_border_radar_wall,
    "SOVEREIGN COMPUTE GRID": preset_sovereign_compute_grid,
    "DIGITAL TWIN EXPLOSION": preset_digital_twin_explosion,
}


# ============================================================
# INTERPOLATION
# ============================================================

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def interpolate_dataclass(a, b, t):
    values = {}
    ad = asdict(a)
    for key, av in ad.items():
        bv = getattr(b, key)
        if isinstance(av, str):
            values[key] = bv if t > 0.5 else av
        elif isinstance(av, bool):
            values[key] = bv if t > 0.5 else av
        elif isinstance(av, int):
            values[key] = int(round(lerp(float(av), float(bv), t)))
        else:
            values[key] = lerp(float(av), float(bv), t)
    return type(a)(**values)


def interpolate_state(a: FractalState, b: FractalState, t: float) -> FractalState:
    t = max(0.0, min(1.0, t))
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


# ============================================================
# ENGINE
# ============================================================

class BombasticFractalEngine:
    def __init__(self, width: int = 760, height: int = 760):
        self.width = width
        self.height = height
        self.time = 0.0
        self.rng = np.random.default_rng(42)

        x = np.linspace(-1, 1, width)
        y = np.linspace(-1, 1, height)
        self.screen_x, self.screen_y = np.meshgrid(x, y)
        self.radius = np.sqrt(self.screen_x**2 + self.screen_y**2)
        self.angle = np.arctan2(self.screen_y, self.screen_x)

    def complex_grid(self, state: FractalState) -> np.ndarray:
        g = state.geometry
        a = state.animation
        n = state.noise

        shake_x = g.camera_shake * math.sin(self.time * 8.1)
        shake_y = g.camera_shake * math.cos(self.time * 7.3)

        zoom = g.zoom * (1.0 + a.pulse_strength * math.sin(self.time * 1.6))
        zoom *= 1.0 + self.time * a.zoom_speed

        span = 3.0 / zoom
        xx = self.screen_x * span + g.offset_x + shake_x
        yy = self.screen_y * span + g.offset_y + shake_y

        theta = g.rotation + self.time * a.rotation_speed
        c, s = np.cos(theta), np.sin(theta)
        xr = c * xx - s * yy
        yr = s * xx + c * yy

        # Heavy cinematic domain warp
        xr += n.warp_strength * np.sin(yr * 7.0 + self.time * 2.0)
        yr += n.warp_strength * np.cos(xr * 6.0 - self.time * 1.7)

        xr += n.turbulence * 0.05 * np.sin((xr + yr) * 18.0 + self.time * 3.0)
        yr += n.turbulence * 0.05 * np.cos((xr - yr) * 18.0 - self.time * 2.5)

        return xr + 1j * yr

    def fractal_field(self, state: FractalState) -> np.ndarray:
        C = self.complex_grid(state)
        Z = np.zeros_like(C, dtype=np.complex128)

        ftype = int(round(state.formula.fractal_type)) % 4
        exponent = max(2.0, state.formula.exponent)
        escape = max(2.0, state.formula.escape_radius)
        max_iter = max(20, int(state.formula.max_iter))

        output = np.zeros(C.shape, dtype=np.float32)
        mask = np.ones(C.shape, dtype=bool)

        if ftype == 1:
            Z = C.copy()
            C_iter = np.full_like(C, complex(state.formula.julia_real, state.formula.julia_imag))
        else:
            Z = np.zeros_like(C)
            C_iter = C.copy()

        for i in range(max_iter):
            if ftype == 2:
                Z_abs = np.abs(Z.real) + 1j * np.abs(Z.imag)
                Z[mask] = Z_abs[mask] ** exponent + C_iter[mask]
            else:
                Z[mask] = Z[mask] ** exponent + C_iter[mask]

            escaped = np.abs(Z) > escape
            newly = escaped & mask
            output[newly] = i
            mask &= ~escaped

            if not mask.any():
                break

        output[mask] = max_iter
        return output / max_iter

    def overlays(self, state: FractalState) -> np.ndarray:
        ce = state.concrete
        d = state.domain
        a = state.animation
        n = state.noise
        s = state.symmetry

        overlay = np.zeros((self.height, self.width), dtype=np.float32)

        # Shockwave rings
        wave = np.sin((self.radius * 18.0) - self.time * a.shockwave_speed)
        overlay += a.shockwave_strength * 0.08 * (wave > 0.92)

        # Radar sweep
        sweep_angle = (self.time * 1.8) % (2 * np.pi)
        sweep = np.cos(self.angle - sweep_angle)
        overlay += d.radar_range * 0.08 * np.maximum(sweep, 0) ** 28

        # Kaleidoscope spokes
        if s.kaleidoscope_segments > 0:
            spokes = np.sin(self.angle * s.kaleidoscope_segments + self.time * 3.0)
            overlay += s.radial_strength * 0.06 * (spokes > 0.96)

        # Grid overlay removed for cleaner cinematic visuals.

        # Electric noise
        electric = self.rng.random((self.height, self.width))
        overlay += n.electric_noise * 0.10 * (electric > 0.985)

        # Mining heatmap pulses
        heat = np.sin(self.screen_x * 16 + self.screen_y * 11 + self.time * 2.3)
        overlay += d.heatmap_intensity * d.mineral_probability * 0.04 * np.maximum(heat, 0)

        return overlay

    def render(self, state: FractalState) -> np.ndarray:
        self.time += 0.045 * state.animation.time_scale

        field = self.fractal_field(state)

        r = state.render
        ce = state.concrete
        n = state.noise

        # Color intensity shaping
        img = field
        img = img ** max(0.2, r.gamma)
        img = img * r.contrast + (r.brightness - 1.0)

        # Compute-driven glow
        img += ce.gpu_load * ce.compute_intensity * r.glow * 0.13
        img += ce.parallelism * 0.05 * np.sin(self.radius * 30 - self.time * 4)

        # Overlays
        img += self.overlays(state)

        # Scanlines
        scan = np.sin(np.arange(self.height)[:, None] * 2.2 + self.time * 3.0)
        img += r.scanlines * scan

        # Vignette, but inverted enough to keep center explosive
        img -= r.vignette * (self.radius ** 2) * 0.35

        # Grain
        img += n.grain * self.rng.normal(0, 1, img.shape)

        # Palette animation
        img = (img + r.palette_shift + self.time * r.palette_speed) % 1.0

        return np.clip(img, 0, 1)


# ============================================================
# PARTICLES
# ============================================================

class ParticleSystem:
    def __init__(self, count=900):
        self.count = count
        self.rng = np.random.default_rng(7)
        self.x = self.rng.uniform(-1, 1, count)
        self.y = self.rng.uniform(-1, 1, count)
        self.vx = self.rng.normal(0, 0.003, count)
        self.vy = self.rng.normal(0, 0.003, count)
        self.life = self.rng.uniform(0, 1, count)

    def update(self, state: FractalState, t: float):
        force = 0.002 + state.concrete.gpu_load * 0.008
        angle = np.arctan2(self.y, self.x) + np.pi / 2

        self.vx += force * np.cos(angle) * 0.04
        self.vy += force * np.sin(angle) * 0.04

        # Outward explosion pulse
        pulse = 0.002 * np.sin(t * 3.0)
        self.vx += self.x * pulse
        self.vy += self.y * pulse

        self.x += self.vx
        self.y += self.vy
        self.life -= 0.006

        reset = (np.abs(self.x) > 1.15) | (np.abs(self.y) > 1.15) | (self.life <= 0)
        n = reset.sum()
        if n:
            self.x[reset] = self.rng.normal(0, 0.05, n)
            self.y[reset] = self.rng.normal(0, 0.05, n)
            self.vx[reset] = self.rng.normal(0, 0.004, n)
            self.vy[reset] = self.rng.normal(0, 0.004, n)
            self.life[reset] = self.rng.uniform(0.5, 1.0, n)



# ============================================================
# USE-CASE AWARE FEATURE DETECTION POPUPS
# ============================================================

class FeatureDetectionSystem:
    """
    Use-case aware detection overlays.

    The feature labels, density, positions, and confidence behavior now change
    based on the current preset/scene. This makes the overlays feel like they
    belong to the mission rather than being random labels pasted on top.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.rng = np.random.default_rng(123)
        self.current_scene = None
        self.features = []

    def scene_from_label(self, label: str) -> str:
        label = label.upper()

        if "MINERAL" in label:
            return "MINING"
        if "BORDER" in label or "RADAR" in label:
            return "BORDER"
        if "DIGITAL TWIN" in label:
            return "DIGITAL_TWIN"
        if "SOVEREIGN" in label or "COMPUTE GRID" in label:
            return "COMPUTE_GRID"
        if "GPU STORM" in label:
            return "GPU_STORM"
        if "AI FACTORY" in label or "IGNITION" in label:
            return "AI_FACTORY"

        return "AI_FACTORY"

    def build_features(self, scene: str):
        if scene == "MINING":
            return [
                {"label": "ORE VEIN", "metric": "density", "x": 0.18, "y": 0.42, "w": 0.24, "h": 0.10, "conf": 0.91, "phase": 0.2},
                {"label": "SULFIDE BAND", "metric": "spectral", "x": 0.52, "y": 0.34, "w": 0.22, "h": 0.12, "conf": 0.88, "phase": 1.0},
                {"label": "FAULT LINE", "metric": "edge", "x": 0.36, "y": 0.64, "w": 0.34, "h": 0.08, "conf": 0.84, "phase": 2.0},
                {"label": "HIGH-DENSITY POCKET", "metric": "mass", "x": 0.66, "y": 0.70, "w": 0.19, "h": 0.14, "conf": 0.93, "phase": 3.3},
            ]

        if scene == "BORDER":
            return [
                {"label": "MOVING OBJECT", "metric": "track", "x": 0.22, "y": 0.29, "w": 0.13, "h": 0.10, "conf": 0.89, "phase": 0.4},
                {"label": "THERMAL SIGNATURE", "metric": "thermal", "x": 0.61, "y": 0.38, "w": 0.16, "h": 0.13, "conf": 0.92, "phase": 1.7},
                {"label": "DRONE TRACK", "metric": "altitude", "x": 0.48, "y": 0.18, "w": 0.20, "h": 0.09, "conf": 0.81, "phase": 2.5},
                {"label": "PERIMETER BREACH", "metric": "risk", "x": 0.70, "y": 0.66, "w": 0.18, "h": 0.12, "conf": 0.86, "phase": 4.0},
            ]

        if scene == "DIGITAL_TWIN":
            return [
                {"label": "STRUCTURAL NODE", "metric": "stress", "x": 0.29, "y": 0.31, "w": 0.18, "h": 0.13, "conf": 0.90, "phase": 0.5},
                {"label": "HEAT ISLAND", "metric": "thermal", "x": 0.57, "y": 0.24, "w": 0.22, "h": 0.15, "conf": 0.87, "phase": 1.2},
                {"label": "FLOW BOTTLENECK", "metric": "traffic", "x": 0.44, "y": 0.58, "w": 0.26, "h": 0.10, "conf": 0.93, "phase": 2.9},
                {"label": "SIMULATION DELTA", "metric": "change", "x": 0.18, "y": 0.68, "w": 0.21, "h": 0.14, "conf": 0.85, "phase": 4.1},
            ]

        if scene == "COMPUTE_GRID":
            return [
                {"label": "ACTIVE GPU CLUSTER", "metric": "load", "x": 0.19, "y": 0.24, "w": 0.22, "h": 0.13, "conf": 0.98, "phase": 0.1},
                {"label": "DATAFLOW HOTSPOT", "metric": "bandwidth", "x": 0.54, "y": 0.32, "w": 0.24, "h": 0.12, "conf": 0.95, "phase": 1.4},
                {"label": "STORAGE BURST", "metric": "iops", "x": 0.34, "y": 0.63, "w": 0.23, "h": 0.11, "conf": 0.91, "phase": 2.7},
                {"label": "POWER EFFICIENCY ZONE", "metric": "pue", "x": 0.63, "y": 0.68, "w": 0.24, "h": 0.13, "conf": 0.88, "phase": 3.9},
            ]

        if scene == "GPU_STORM":
            return [
                {"label": "TENSOR SATURATION", "metric": "gpu", "x": 0.27, "y": 0.26, "w": 0.22, "h": 0.12, "conf": 0.97, "phase": 0.3},
                {"label": "MEMORY PRESSURE", "metric": "vram", "x": 0.58, "y": 0.29, "w": 0.20, "h": 0.11, "conf": 0.94, "phase": 1.6},
                {"label": "INTERCONNECT SPIKE", "metric": "fabric", "x": 0.42, "y": 0.56, "w": 0.29, "h": 0.10, "conf": 0.92, "phase": 2.6},
                {"label": "BATCH QUEUE SURGE", "metric": "queue", "x": 0.16, "y": 0.70, "w": 0.25, "h": 0.13, "conf": 0.90, "phase": 4.2},
            ]

        # AI_FACTORY default
        return [
            {"label": "MODEL CONVERGENCE", "metric": "training", "x": 0.20, "y": 0.30, "w": 0.22, "h": 0.12, "conf": 0.94, "phase": 0.0},
            {"label": "SYNTHETIC DATA STREAM", "metric": "data", "x": 0.56, "y": 0.25, "w": 0.24, "h": 0.14, "conf": 0.91, "phase": 1.2},
            {"label": "ORCHESTRATION EVENT", "metric": "nodes", "x": 0.39, "y": 0.57, "w": 0.28, "h": 0.11, "conf": 0.96, "phase": 2.4},
            {"label": "LATENCY DROP", "metric": "latency", "x": 0.64, "y": 0.69, "w": 0.19, "h": 0.12, "conf": 0.86, "phase": 3.8},
        ]

    def update(self, t: float, state: FractalState, scene_label: str):
        scene = self.scene_from_label(scene_label)

        if scene != self.current_scene:
            self.current_scene = scene
            self.features = self.build_features(scene)

        for i, f in enumerate(self.features):
            # Movement pattern depends on use case.
            if scene == "BORDER":
                # Border/security detections track laterally like moving targets.
                f["dx"] = 0.035 * math.sin(t * 0.55 + f["phase"])
                f["dy"] = 0.012 * math.cos(t * 0.75 + f["phase"])
            elif scene == "MINING":
                # Geological features should be mostly stable.
                f["dx"] = 0.006 * math.sin(t * 0.30 + f["phase"])
                f["dy"] = 0.005 * math.cos(t * 0.25 + f["phase"])
            elif scene in ["COMPUTE_GRID", "GPU_STORM", "AI_FACTORY"]:
                # Compute features pulse with load.
                f["dx"] = 0.010 * math.sin(t * 0.90 + f["phase"])
                f["dy"] = 0.010 * math.cos(t * 1.10 + f["phase"])
            else:
                # Digital twin features drift slowly.
                f["dx"] = 0.012 * math.sin(t * 0.40 + f["phase"])
                f["dy"] = 0.010 * math.cos(t * 0.35 + f["phase"])

            conf_driver = (
                state.concrete.gpu_load * 0.02
                + state.domain.heatmap_intensity * 0.012
                + state.domain.radar_range * 0.012
            )

            f["live_conf"] = max(
                0.65,
                min(0.99, f["conf"] + conf_driver + 0.035 * math.sin(t * 1.2 + f["phase"]))
            )

            f["metric_value"] = self.metric_value(f["metric"], state, t, f["phase"])

    def metric_value(self, metric: str, state: FractalState, t: float, phase: float) -> str:
        metric = metric.lower()

        if metric == "density":
            return f"DENS {72 + 9 * math.sin(t + phase):.1f}%"
        if metric == "spectral":
            return f"BAND {1.8 + 0.3 * math.sin(t + phase):.2f}µm"
        if metric == "edge":
            return f"EDGE {state.domain.terrain_depth * 100:.0f}%"
        if metric == "mass":
            return f"MASS {state.domain.mineral_probability * 100:.0f}%"

        if metric == "track":
            return f"VEL {18 + 5 * math.sin(t + phase):.1f}m/s"
        if metric == "thermal":
            return f"THERM {70 + 18 * math.sin(t + phase):.0f}°C"
        if metric == "altitude":
            return f"ALT {120 + 45 * math.sin(t + phase):.0f}m"
        if metric == "risk":
            return f"RISK {state.domain.threat_level * 100:.0f}%"

        if metric == "stress":
            return f"STRESS {55 + 14 * math.sin(t + phase):.0f}%"
        if metric == "traffic":
            return f"FLOW {state.concrete.network_bandwidth * 100:.0f}%"
        if metric == "change":
            return f"Δ {state.domain.ai_training_progress * 100:.0f}%"

        if metric == "load":
            return f"LOAD {state.concrete.gpu_load * 100:.0f}%"
        if metric == "bandwidth":
            return f"BW {state.concrete.network_bandwidth * 100:.0f}%"
        if metric == "iops":
            return f"IO {state.concrete.storage_bandwidth * 100:.0f}%"
        if metric == "pue":
            return f"PUE {1.02 + (1 - state.concrete.cooling_efficiency) * 0.08:.2f}"

        if metric == "gpu":
            return f"GPU {state.concrete.gpu_load * 100:.0f}%"
        if metric == "vram":
            return f"VRAM {state.concrete.memory_usage * 100:.0f}%"
        if metric == "fabric":
            return f"FABRIC {state.concrete.network_bandwidth * 100:.0f}%"
        if metric == "queue":
            return f"QUEUE {18 + 9 * math.sin(t + phase):.0f}K"

        if metric == "training":
            return f"LOSS ↓ {8 + 3 * math.sin(t + phase):.1f}%"
        if metric == "data":
            return f"DATA {state.concrete.storage_bandwidth * 100:.0f}%"
        if metric == "nodes":
            return f"NODES {state.concrete.distributed_nodes}"
        if metric == "latency":
            return f"LAT {8 + 2 * math.sin(t + phase):.1f}ms"

        return "ACTIVE"

    def draw(self, ax, t: float):
        artists = []

        for i, f in enumerate(self.features):
            x = (f["x"] + f.get("dx", 0.0)) * self.width
            y = (f["y"] + f.get("dy", 0.0)) * self.height
            w = f["w"] * self.width
            h = f["h"] * self.height

            alpha = 0.50 + 0.35 * max(0.0, math.sin(t * 2.0 + f["phase"]))

            rect = plt.Rectangle(
                (x, y),
                w,
                h,
                fill=False,
                edgecolor="white",
                linewidth=1.2,
                alpha=alpha,
            )
            ax.add_patch(rect)
            artists.append(rect)

            corner_len = min(w, h) * 0.22
            segments = [
                ((x, y), (x + corner_len, y)),
                ((x, y), (x, y + corner_len)),
                ((x + w, y), (x + w - corner_len, y)),
                ((x + w, y), (x + w, y + corner_len)),
                ((x, y + h), (x + corner_len, y + h)),
                ((x, y + h), (x, y + h - corner_len)),
                ((x + w, y + h), (x + w - corner_len, y + h)),
                ((x + w, y + h), (x + w, y + h - corner_len)),
            ]

            for (x1, y1), (x2, y2) in segments:
                line, = ax.plot([x1, x2], [y1, y2], color="white", linewidth=2.0, alpha=alpha)
                artists.append(line)

            label = (
                f"ID-{i+101}  {f['label']}  "
                f"{f.get('live_conf', f['conf']):.0%}  "
                f"{f.get('metric_value', '')}"
            )

            txt = ax.text(
                x,
                max(8, y - 10),
                label,
                fontsize=7.3,
                color="white",
                family="monospace",
                bbox=dict(
                    boxstyle="round,pad=0.25",
                    facecolor="black",
                    edgecolor="white",
                    alpha=0.52,
                    linewidth=0.6,
                ),
            )
            artists.append(txt)

            cx = x + w / 2
            cy = y + h / 2

            marker = ax.scatter([cx], [cy], s=14, c="white", alpha=alpha)
            artists.append(marker)

            pulse_size = 42 + 28 * max(0, math.sin(t * 3.0 + f["phase"]))
            pulse = ax.scatter([cx], [cy], s=pulse_size, facecolors="none", edgecolors="white", alpha=0.22)
            artists.append(pulse)

        return artists

# ============================================================
# PLAYER
# ============================================================

class ContinuousPresetPlayer:
    def __init__(self, preset_names):
        self.preset_names = preset_names
        self.index = 0
        self.transition = 0.0
        self.transition_speed = 0.0045

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

    def label(self):
        a = self.preset_names[self.index % len(self.preset_names)]
        b = self.preset_names[(self.index + 1) % len(self.preset_names)]
        return f"{a}  →  {b}"


# ============================================================
# DEMO
# ============================================================

def run_demo():
    engine = BombasticFractalEngine(width=720, height=720)
    player = ContinuousPresetPlayer(list(PRESETS.keys()))
    particles = ParticleSystem(count=1100)
    detections = FeatureDetectionSystem(engine.width, engine.height)
    detection_artists = []

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_facecolor("black")
    ax.axis("off")

    state = player.current_state()
    image = engine.render(state)

    im = ax.imshow(image, cmap=state.render.palette, animated=True, interpolation="bilinear")
    scatter = ax.scatter(
        particles.x * engine.width / 2 + engine.width / 2,
        particles.y * engine.height / 2 + engine.height / 2,
        s=1.0,
        alpha=0.55,
    )

    title = ax.text(
        0.02,
        0.96,
        "CONCRETE ENGINE // AI FEATURE DETECTION IGNITION",
        transform=ax.transAxes,
        fontsize=15,
        weight="bold",
        color="white",
    )

    subtitle = ax.text(
        0.02,
        0.91,
        "",
        transform=ax.transAxes,
        fontsize=10,
        color="white",
    )

    telemetry = ax.text(
        0.02,
        0.04,
        "",
        transform=ax.transAxes,
        fontsize=9,
        color="white",
        family="monospace",
    )

    def update(_frame):
        nonlocal detection_artists

        # Remove previous detection overlays so they do not accumulate.
        for artist in detection_artists:
            try:
                artist.remove()
            except Exception:
                pass
        detection_artists = []

        state = player.current_state()
        image = engine.render(state)

        im.set_array(image)
        im.set_cmap(state.render.palette)

        particles.update(state, engine.time)
        scatter.set_offsets(
            np.column_stack([
                particles.x * engine.width / 2 + engine.width / 2,
                particles.y * engine.height / 2 + engine.height / 2,
            ])
        )

        detections.update(engine.time, state, player.label())
        detection_artists = detections.draw(ax, engine.time)

        subtitle.set_text(player.label())
        telemetry.set_text(
            f"GPU LOAD: {state.concrete.gpu_load:05.1%}   "
            f"GPUs: {state.concrete.gpu_count:05d}   "
            f"NODES: {state.concrete.distributed_nodes:04d}\n"
            f"NETWORK: {state.concrete.network_bandwidth:05.1%}   "
            f"STORAGE: {state.concrete.storage_bandwidth:05.1%}   "
            f"PARALLELISM: {state.concrete.parallelism:05.1%}"
        )

        return [im, scatter, title, subtitle, telemetry] + detection_artists

    # IMPORTANT: keep a reference to the animation object.
    # Without this, Python may garbage-collect it and you only see one still figure.
    ani = FuncAnimation(fig, update, interval=30, blit=False, cache_frame_data=False)

    # Optional: uncomment this line to save a GIF instead of only previewing.
    # ani.save('concrete_engine_bombastic.gif', writer='pillow', fps=30)

    plt.show()
    return ani


if __name__ == "__main__":
    run_demo()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from scipy.interpolate import make_interp_spline
import random
from matplotlib.patches import Ellipse

def draw_flower(ax, x, y, flower_color):
    petal_width = 0.5
    petal_height = 1.0

    for angle in range(0, 360, 72):
        petal = Ellipse(
            (x, y), width=petal_width, height=petal_height, angle=angle, color=flower_color, alpha=0.8
        )
        ax.add_patch(petal)

    ax.plot(x, y, 'o', color="yellow", markersize=8)

coordinates = [
    (-2.557682962387015, -2.7363097314265783),
    (-2.051802896297016, -2.416463201953261),
    (-1.6434055787734474, -2.1161492849668644),
    (-1.1760132179998055, -1.706662016044646),
    (-0.8246671202254835, -1.2920590628996627),
    (-0.4290990378073671, -0.7495640041855598),
    (-0.12566818932840898, -0.3957679339611673),
    (0.29478083390028187, 0.23241483548424602),
    (0.6795606958888133, 0.7831647482850831),
    (1.1760132179998055, 1.5585397046855016),
    (1.6851005928661678, 2.5677246831763747),
    (2.2530858198075614, 3.778630391814905),
    (2.5313441539508212, 4.5265666782932215),
    (2.827971620176888, 5.701430066271364),
    (2.882690251725143, 6.7450296477153815),
    (2.7713091651278066, 7.846878269968608),
    (2.2927398192244146, 8.414951749796534),
    (1.6739236077364175, 8.376467852575281),
    (1.3254932452133346, 8.054063480990582),
    (1.0478180581203227, 7.710963841413789),
    (0.7985226941393722, 7.185327287524706),
    (0.5375643891534648, 6.451807929310545),
    (0.35688599475167654, 5.980932449715149),
    (0.2872971134221013, 5.551796302755493),
    (0.1540480124404704, 5.188001395186606),
    (0.05083098454660317, 5.6324845948145565),
    (-0.03460005831470502, 6.262992675270317),
    (0.05083098454660317, 5.6324845948145565),
    (-0.12139177762659151, 6.847924659923264),
    (-0.35328992127514824, 7.608998953610045),
    (-0.8373019729808533, 8.002906638762934),
    (-1.324618524637963, 8.340658063015928),
    (-1.75148216541938, 8.273572840367398),
    (-2.1960346000583146, 7.715381932333449),
    (-2.3853630090387794, 6.915126148122311),
    (-2.4681698901739724, 5.974654109987211),
    (-2.3491107007483722, 4.997558423439135),
    (-2.1341238215570026, 4.215207534007673),
    (-1.83778792885606, 3.3381002209045456),
    (-1.6279521819418796, 2.6291128938495523),
    (-1.3174263776849062, 2.005580746424834),
    (-0.9506268830790164, 1.3140332519474478),
    (-0.5988920206045291, 0.7514242529938379),
    (-0.20565652638740403, 0.19404720381351004),
    (0.2866167751968121, -0.3842576444599465),
    (0.7958985324132569, -0.7065457504941286),
    (1.4584507726698417, -0.9573305429601209),
    (2.1190591894256, -1.2507847924659923),
    (2.9098065895616676, -1.3224043715846994),
    (3.656332005053941, -1.2279967445645854),
    (4.280979687044416, -1.1666085338914078),
    (4.793079988337059, -0.9167538658295546),
    (5.231509378948392, -0.736542262527613),
    (5.932743706871416, -0.4165794675037786),
    (6.7439012537661585, 0.02964771538193233),
    (7.491884536884051, 0.43855365655156375),
    (8.242977937603266, 0.7457272410184862),
    (8.891243075128779, 1.0510405766771305),
    (9.506949169015453, 1.3474014649459365),
    (9.990572456020994, 1.6545750494128588),
    (10.549032947808339, 1.9453551912568305),
]

x, y = zip(*coordinates)

t = np.linspace(0, len(x) - 1, len(x))  
new_t = np.linspace(0, len(x) - 1, len(x) * 5) 
spl_x = make_interp_spline(t, x, k=3) 
spl_y = make_interp_spline(t, y, k=3) 
smooth_x = spl_x(new_t)
smooth_y = spl_y(new_t)

# colors i think she'd like
cute_colors = ["#FFB6C1", "#87CEEB", "#FFD700", "#ADFF2F", "#FF69B4", "#9370DB", "#FFA07A", "#98FB98"]

fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor("#d8f3dc")
ax.set_xlim(min(smooth_x) - 1, max(smooth_x) + 1)
ax.set_ylim(min(smooth_y) - 2, max(smooth_y) + 2)
ax.axis('off')

text_color = "#C2185B"
valentine_text = ax.text(
    max(smooth_x) - 2,
    min(smooth_y) - 3,
    "Will you be my Valentine?",
    fontsize=20,  # Increased font size
    ha="right",
    color=text_color,
    fontweight="bold",
    alpha=0,  # Initially invisible
)

trail, = ax.plot([], [], linestyle=(0, (5, 5)), color=text_color, linewidth=1.5)

flower_positions = [
    (
        random.uniform(min(smooth_x), max(smooth_x)),
        random.uniform(min(smooth_y), max(smooth_y)),
        random.choice(cute_colors),
    )
    for _ in range(30)
]

plane_img = plt.imread("transparentPlane.png")
imagebox = OffsetImage(plane_img, zoom=0.08)
airplane = AnnotationBbox(imagebox, (smooth_x[0], smooth_y[0]), frameon=False)
ax.add_artist(airplane)

def init():
    trail.set_data([], [])
    ax.add_artist(airplane)
    valentine_text.set_alpha(0)  # hide
    return trail, airplane, valentine_text

def update(frame):
    if frame < len(smooth_x):  # Plane 
        trail.set_data(smooth_x[:frame + 1], smooth_y[:frame + 1])
        airplane.xybox = (smooth_x[frame], smooth_y[frame])
    elif frame < len(smooth_x) + len(flower_positions):  # Flowerz
        flower_index = frame - len(smooth_x)
        fx, fy, fcolor = flower_positions[flower_index]
        draw_flower(ax, fx, fy, fcolor)
    elif frame == len(smooth_x) + len(flower_positions):  # Text
        valentine_text.set_alpha(1)
    return trail, airplane, valentine_text

num_frames = len(smooth_x) + len(flower_positions) + 1

ani = FuncAnimation(
    fig, update, frames=num_frames, init_func=init, interval=20, repeat=False
)

ani.save("pie_for_sab.mp4", writer=FFMpegWriter(fps=30))

plt.show()


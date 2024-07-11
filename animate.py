import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def draw_pattern_animation(points, xlim=None, ylim=None, num_frames=100, interval=50):
    plt.rcParams['toolbar'] = 'None'

    fig, ax = plt.subplots()

    fig.patch.set_facecolor('white')
    fig.canvas.toolbar_visible = False

    ax.axis('off')

    if xlim is None:
        all_x = [point[0] for point in points]
        xlim = (min(all_x), max(all_x))
    if ylim is None:
        all_y = [point[1] for point in points]
        ylim = (min(all_y), max(all_y))

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    ax.plot(*zip(*points), 'bo')  

    line, = ax.plot([], [], 'r-')  

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        current_x = []
        current_y = []
        total_frames_per_segment = num_frames // (len(points) - 1)

        for j in range(1, len(points)):
            start_index = (j - 1) * total_frames_per_segment
            end_index = j * total_frames_per_segment

            if start_index <= i < end_index:
                x = np.linspace(points[j-1][0], points[j][0], total_frames_per_segment)
                y = np.linspace(points[j-1][1], points[j][1], total_frames_per_segment)
                current_x.extend(x[:i - start_index + 1])
                current_y.extend(y[:i - start_index + 1])
                break
            elif i >= end_index:
                x = np.linspace(points[j-1][0], points[j][0], total_frames_per_segment)
                y = np.linspace(points[j-1][1], points[j][1], total_frames_per_segment)
                current_x.extend(x)
                current_y.extend(y)

        line.set_data(current_x, current_y)
        return line,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=interval, blit=True, repeat=False)

    plt.show()
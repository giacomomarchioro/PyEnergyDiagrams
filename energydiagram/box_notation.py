# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:01:16 2018

@author: giacomo
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


def plot_orbital_boxes(
    ax, x, y, boxes_number, electrons_number, box_side=1, spacing_f=5
):
    """Utility for adding an electron box to the energy state.

    Args:
        ax (matplotlib ax): The matplotlib ax object used for adding the box.
        x (float): x coordinate of the box.
        y (float): y coordinate of the box.
        boxes_number (int): Number of boxes to add.
        electrons_number (int): Number of electrons to add inside the boxes.
        box_side (int, optional): The dimension of the side. Defaults to 1.
        spacing_f (int, optional): The spacing between the boxes. Defaults to 5.

    Returns:
        None: The function does not return but affects ax object.
    """
    Xi = x - boxes_number * box_side / 2.0
    Yi = y - box_side / 2.0

    def add_spin(Xi, Yi, box_side, direction):
        """Add spin to electron box.

        Args:
            Xi (float): X coordinate.
            Yi (float): Y coordinate.
            box_side (float): The side of the electron box.
            direction (str): The direction of the spin "up" or "down".

        Returns:
            patches.PathPatch : The spin path object.
        """
        unit = box_side * 0.8
        spacing = unit / float(spacing_f)
        hspacing = spacing / 2.0
        v_pad = box_side * 0.1 + Yi
        h_pad = box_side / 2.0 + Xi

        codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
        ]
        if direction == "down":
            verts_down = [
                (h_pad + hspacing, v_pad + unit),  # left, bottom
                (h_pad + hspacing, v_pad),  # left, top
                (h_pad + hspacing + unit / 5.0, v_pad + unit * 0.40),  # right, top
                (h_pad + hspacing + unit / 20.0, v_pad + unit * 0.40),  # right, bottom
                (h_pad + hspacing + unit / 20.0, v_pad + unit),
                (h_pad + hspacing, v_pad + unit),  # ignored
            ]
            spin_down = patches.PathPatch(
                Path(verts_down, codes), facecolor="k", lw=0.1, zorder=10
            )

            return spin_down

        if direction == "up":
            verts_up = [
                (h_pad - hspacing, v_pad),  # left, bottom
                (h_pad - hspacing, v_pad + unit),  # left, top
                (h_pad - hspacing - unit / 5.0, v_pad + unit * 0.60),  # right, top
                (h_pad - hspacing - unit / 20, v_pad + unit * 0.60),  # right, bottom
                (h_pad - hspacing - unit / 20, v_pad),
                (h_pad - hspacing, v_pad),  # ignored
            ]

            spin_up = patches.PathPatch(
                Path(verts_up, codes), facecolor="k", lw=0.1, zorder=10
            )
            return spin_up

    # plot the rectangles
    for i in range(boxes_number):
        square = patches.Rectangle(
            (Xi + box_side * i, Yi),  # X,Y
            box_side,
            box_side,
            fill=True,
            fc="w",
            linewidth=1,
            edgecolor="k",
            zorder=10,
        )
        ax.add_patch(square)
    # plot the spins using Aufbau
    if electrons_number > boxes_number * 2:
        Warning("electrons_number grater than number of availabe sites")
    if electrons_number > 0:
        if electrons_number <= boxes_number:
            for e in range(electrons_number):
                ax.add_patch(add_spin(Xi + box_side * e, Yi, box_side, direction="up"))
        else:
            for e in range(boxes_number):
                ax.add_patch(add_spin(Xi + box_side * e, Yi, box_side, direction="up"))
            for j in range(electrons_number - boxes_number):
                ax.add_patch(
                    add_spin(Xi + box_side * j, Yi, box_side, direction="down")
                )


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect="equal")
    ax.set_xlim(10, 14)
    ax.set_ylim(8, 12)
    plot_orbital_boxes(ax, 12, 10, 3, 4)
    plt.grid()

import time
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt


class Raycasting:
    def __init__(self, path: str):
        mesh = o3d.io.read_triangle_mesh(o3d.data.ArmadilloMesh().path if path == '' else path)
        self.mesh = o3d.t.geometry.TriangleMesh.from_legacy(mesh)

        self.scene = o3d.t.geometry.RaycastingScene()
        self.scene.add_triangles(self.mesh)

    def get_image(self, origin: list[float], point: list[float]):

        rays = self.scene.create_rays_pinhole(
            180,
            point,
            origin,
            [0, -1, 0],
            180,
            1
        )

        ans = self.scene.cast_rays(rays)

        plt.imshow(ans['t_hit'].numpy())
        plt.show()

    def get_distance(self, origin: list[float], point: list[float]):
        rays = self.scene.create_rays_pinhole(
            90,
            point,
            origin,
            [0, -1, 0],
            180,
            1
        )

        ans = self.scene.cast_rays(rays)

        distances: list[float] = []

        for i, distance in enumerate(ans['t_hit'].numpy()[0]):
            if distance == np.inf:
                distances.append(999)
            else:
                distances.append(distance)

        return distances

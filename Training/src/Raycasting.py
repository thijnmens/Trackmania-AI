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
            90,
            point,
            origin,
            [0, -1, 0],
            500,
            10
        )

        ans = self.scene.cast_rays(rays)

        plt.close('all')
        plt.imshow(ans['t_hit'].numpy())
        plt.show()

    def get_distance(self, origin: list[float], point: list[float]):
        rays = self.scene.create_rays_pinhole(
            90,
            point,
            origin,
            [0, -1, 0],
            500,
            10
        )

        ans = self.scene.cast_rays(rays)

        distances: list[float] = []

        for _, row in enumerate(ans['t_hit'].numpy()):
            for i, distance in enumerate(row):
                if distance == np.inf:
                    distances.append(999)
                else:
                    distances.append(distance)

        return distances

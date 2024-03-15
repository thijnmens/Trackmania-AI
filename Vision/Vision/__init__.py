import matplotlib.pyplot as plt
import open3d as o3d


class Vision:

	def __init__(self, path: str):
		"""
		Creates new raycasting scene using Open3D

		:param path: Relative path of mesh to load
		"""

		# Load level mesh
		mesh = o3d.io.read_triangle_mesh(path)
		self.mesh = o3d.t.geometry.TriangleMesh.from_legacy(mesh)

		# Create scene and add mesh
		self.scene = o3d.t.geometry.RaycastingScene()
		self.scene.add_triangles(self.mesh)

	def show_scene(self,
					fov_deg: int = 90,
					center: list[float] = [0.0, 0.0, 0.0],
					eye: list[float] = [100, 100, 100],
					up: list[float] = [0, -1, 0],
					width_px: int = 640,
					height_px: int = 480):
		"""
		Shows render of scene from position
		"""

		# Create camera
		rays = self.scene.create_rays_pinhole(
			fov_deg,
			center,
			eye,
			up,
			width_px,
			height_px
		)

		# Cast rays
		ans = self.scene.cast_rays(rays)

		# Create and show image
		plt.imshow(ans['t_hit'].numpy())
		plt.show()

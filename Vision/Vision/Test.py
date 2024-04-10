from Vision import Vision
import keyboard
import open3d as o3d

vision = Vision('')

eye = [10, 10, 10]
center = [0, 0, 0]
vision.show_scene(center=center, eye=eye, fov_deg=20)
while True:
	pressed = False
	if keyboard.is_pressed('w'):
		eye[0] += 50
		pressed = True
	elif keyboard.is_pressed('a'):
		eye[2] += 50
		pressed = True
	elif keyboard.is_pressed('s'):
		eye[0] -= 50
		pressed = True
	elif keyboard.is_pressed('d'):
		eye[2] -= 50
		pressed = True
	elif keyboard.is_pressed('q'):
		eye[1] += 1
		pressed = True
	elif keyboard.is_pressed('e'):
		eye[1] -= 1
		pressed = True
	elif keyboard.is_pressed('i'):
		center[0] += 10
		pressed = True
	elif keyboard.is_pressed('j'):
		center[2] += 10
		pressed = True
	elif keyboard.is_pressed('k'):
		center[0] -= 10
		pressed = True
	elif keyboard.is_pressed('l'):
		center[2] -= 10
		pressed = True
	elif keyboard.is_pressed('u'):
		center[1] += 1
		pressed = True
	elif keyboard.is_pressed('o'):
		center[1] -= 1
		pressed = True

	if pressed:
		print(f"\nEye: {eye}, Center: {center}")
		vision.show_scene(center=center, eye=eye, fov_deg=20)

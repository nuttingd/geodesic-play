import math

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


def generate_geodesic_dome_wireframe(radius, faces, floor_height_ratio):
    vertices = []

    # Generate the coordinates of each vertex for the upper section
    for i in range(faces):
        phi = math.pi * (i + 0.5) / faces

        for j in range(2 * faces):
            theta = 2 * math.pi * j / (2 * faces)

            x = radius * math.sin(phi) * math.cos(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(phi)

            vertices.append((x, y, z))

    # Calculate the floor height based on the specified ratio
    floor_height = floor_height_ratio * radius

    # Generate the coordinates of each vertex for the floor
    for i in range(2 * faces):
        theta = 2 * math.pi * i / (2 * faces)

        x = floor_height * math.cos(theta)
        y = floor_height * math.sin(theta)
        z = -radius

        vertices.append((x, y, z))

    return vertices


# Example usage
radius = 1.0  # Define the radius of the geodesic dome
faces = 50  # Specify the number of triangular faces (excluding the floor)
floor_height_ratio = 0.25  # Specify the height ratio for the floor

vertices = generate_geodesic_dome_wireframe(radius, faces, floor_height_ratio)

print(vertices)

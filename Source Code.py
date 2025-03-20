#===============================================================================================
#  python code to simulate and plot the results (for illustration only)
#===============================================================================================
import numpy as np
import matplotlib.pyplot as plt

def calculate_balls_packed(room_size, ball_diameter, packing_factor):
    """
    Calculate the number of balls that can fit in a given room size based on packing efficiency.
    """
    room_volume = room_size[0] * room_size[1] * room_size[2]
    ball_radius = ball_diameter / 2
    ball_volume = (4/3) * np.pi * (ball_radius ** 3)
    num_balls = (room_volume * packing_factor) / ball_volume
    return int(num_balls)

def plot_packing(room_size, ball_diameter, num_balls):
    """
    Generate a simple 3D scatter plot representing the packed balls inside the room.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ball_radius = ball_diameter / 2
    x_vals = np.linspace(ball_radius, room_size[0] - ball_radius, int(np.cbrt(num_balls)))
    y_vals = np.linspace(ball_radius, room_size[1] - ball_radius, int(np.cbrt(num_balls)))
    z_vals = np.linspace(ball_radius, room_size[2] - ball_radius, int(np.cbrt(num_balls)))
    
    for x in x_vals:
        for y in y_vals:
            for z in z_vals:
                ax.scatter(x, y, z, color='blue', s=10)
    
    ax.set_xlim([0, room_size[0]])
    ax.set_ylim([0, room_size[1]])
    ax.set_zlim([0, room_size[2]])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Ball Packing Visualization')
    plt.show()

def main():
    room_size = (8, 7, 3)  # Room dimensions in meters
    ball_diameter = 0.1  # Ball diameter in meters
    packing_types = {"SC": 0.52, "BCC": 0.68, "HCP": 0.74}
    
    print("Select a packing type:")
    for i, key in enumerate(packing_types.keys(), 1):
        print(f"{i}. {key}")
    choice = int(input("Enter your choice (1-3): "))
    
    packing_type = list(packing_types.keys())[choice - 1]
    packing_factor = packing_types[packing_type]
    
    num_balls = calculate_balls_packed(room_size, ball_diameter, packing_factor)
    
    with open("balls_packing_results.txt", "w") as file:
        file.write(f"Packing Type: {packing_type}\n")
        file.write(f"Room Size: {room_size} m^3\n")
        file.write(f"Ball Diameter: {ball_diameter} m\n")
        file.write(f"Packing Factor: {packing_factor}\n")
        file.write(f"Number of Packed Balls: {num_balls}\n")
    
    print(f"Packing Type: {packing_type}, Balls Packed: {num_balls}")
    plot_packing(room_size, ball_diameter, num_balls)

if __name__ == "__main__":
    main()

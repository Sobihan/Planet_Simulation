import math
from Color import Color

class Object:
    AU = 149.6e6 * 1000 #Astronomical Unit in meter
    G = 6.67428e-11 #Gravity
    SCALE = 250 / AU #1 AU => 100 Pixels
    TIMESTEP = 3600 * 24 # 1 Day

    def __init__(self, x, y, radius, color, mass, y_vel, name) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass # in Kg
        #Velocity
        self.x_vel = 0
        self.y_vel = y_vel
        self.star = False
        self.distance_to_star = 0 #Distance to the sun
        self.orbit = [] #List of last position

    def draw(self, win, FONT, pygame) -> None:
        WIDTH, HEIGHT = 800, 800 
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x , y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.color,False, updated_points, 2)
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if self.color == Color.white:
            name_text = FONT.render(self.name, 1, Color.blue)
        else:
            name_text = FONT.render(self.name, 1, Color.white)
        win.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.star:
            self.distance_to_star = distance
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, objects):
        total_fx = total_fy = 0
        for obj in objects:
            if self == obj:
                continue
            fx, fy = self.attraction(obj)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.TIMESTEP # F = m / a // a = f / m 
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

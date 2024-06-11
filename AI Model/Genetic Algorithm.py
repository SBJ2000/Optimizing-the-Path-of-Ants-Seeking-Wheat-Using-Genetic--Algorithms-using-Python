# Auteur : BEN JEDDI Selim 3 IDL 1
import random
import math
import pygame
import sys
# Initialisation de Pygame
pygame.init()

# Définition des variables
width, height = 625, 416
life_span = 250
count = 0
ox, oy, ow, oh = 215, 220, 200, 10
max_force = 0.2
generation_count = 0
sugar = pygame.Vector2(width/2, 50)

# Définition de la classe DNA
class DNA:
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            self.genes = [pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(life_span)]
            self.genes = [gene.normalize() * max_force for gene in self.genes]

    def crossover(self, partner):
        mid = random.randint(0, len(self.genes) - 1)
        new_genes = [self.genes[i] if i > mid else partner.genes[i] for i in range(len(self.genes))]
        return DNA(new_genes)

    def mutation(self):
        for i in range(len(self.genes)):
            if random.random() < 0.01:
                self.genes[i] = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
                self.genes[i] = self.genes[i].normalize() * max_force

# Définition de la classe Ant
class Ant:
    def __init__(self, dna=None):
        self.pos = pygame.Vector2(width/2, height)
        self.vel = pygame.Vector2()
        self.acc = pygame.Vector2()
        self.fitness = 0
        self.completed = False
        self.crashed = False
        self.reached_wheat = False  # Nouvelle variable pour suivre si la fourmi a atteint le blé


        if dna:
            self.dna = dna
        else:
            self.dna = DNA()

    def apply_force(self, force):
        self.acc += force

    def update(self):
        global count
        d = pygame.Vector2.distance_to(self.pos, sugar)
        if d < 30:
            self.completed = True
            self.reached_wheat = True  # Mettez à jour la variable si la fourmi atteint le blé


        if ox < self.pos.x < ox + ow and oy < self.pos.y < oy + oh:
            self.crashed = True

        if count < len(self.dna.genes):  # Ajout de la vérification de la plage valide
            self.apply_force(self.dna.genes[count])

        if not self.completed and not self.crashed:
            self.vel += self.acc
            self.pos += self.vel
            self.acc *= 0
    def show(self):
        # Dessiner l'image de la fourmi à la place du cercle blanc
        screen.blit(ant_image, (int(self.pos.x), int(self.pos.y)))

    def calc_fitness(self, ant_number):
        d = pygame.Vector2.distance_to(self.pos, sugar)
        print(f"Fitness de la fourmi numéro {ant_number} : {1 / (d + 1)}, Distance: {d}, Position: {self.pos}")
        self.fitness = 1 / (d + 1)  # Ajoutez 1 pour éviter la division par zéro
        if self.completed:
            self.fitness *= 50
        if self.crashed:
            self.fitness /= 100

# Ajoutez la variable fitness_generale_de_la_generation à la classe Population
class Population:
    def __init__(self):
        self.ants = [Ant() for _ in range(20)]
        self.pop_size = 20
        self.pool = []
        self.fitness_generale_de_la_generation = 0  # Nouvelle variable

    def run(self):
        for ant in self.ants:
            ant.update()
            ant.show()

    def evaluate(self):
        max_fit = 0
        sum_fitness = 0  # Nouvelle variable pour stocker la somme des fitness individuelles
        for ant_number, ant in enumerate(self.ants):
            ant.calc_fitness(ant_number)
            sum_fitness += ant.fitness  # Ajoutez la fitness individuelle à la somme
            if ant.fitness > max_fit:
                max_fit = ant.fitness

        for ant in self.ants:
            ant.fitness /= max_fit

        self.pool = []
        for ant in self.ants:
            n = int(ant.fitness * 100)
            for _ in range(n):
                self.pool.append(ant)

        # Calculez la moyenne de fitness de la génération
        self.fitness_generale_de_la_generation = sum_fitness / len(self.ants)
        # Réinitialiser la valeur maximale de fitness après chaque génération
        max_fit = 0

    def selection(self):
        new_ants = []
        for ant in self.ants:
            parent_a = random.choice(self.pool).dna
            parent_b = random.choice(self.pool).dna
            child = parent_a.crossover(parent_b)
            child.mutation()
            new_ants.append(Ant(child))

        self.ants = new_ants

    def afficher_fitness_generale(self, screen, font):
        # Afficher la moyenne de fitness à l'écran
        print(f"Fitness générale de la génération: {self.fitness_generale_de_la_generation}")


# Initialisation de Pygame
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ant Game")

# Chargement de l'image d'arrière-plan
background_image = pygame.image.load("ant.jpg").convert()
# Chargement de l'image de blé
wheat_image = pygame.image.load("ble.png").convert_alpha()
# Redimensionnez l'image au besoin (par exemple, 10x10 pixels)
wheat_image = pygame.transform.scale(wheat_image, (80, 80))
# Chargement de l'image de la fourmi
ant_image = pygame.image.load("fourmi.png").convert_alpha()
# Redimensionnez l'image au besoin (par exemple, 20x20 pixels)
ant_image = pygame.transform.scale(ant_image, (30, 30))
# Chargement de l'image de la barrière
barriere_image = pygame.image.load("barriere.png").convert_alpha()
# Redimensionnez l'image au besoin
barriere_image = pygame.transform.scale(barriere_image, (200, 10))  # Ajustez la taille selon vos besoins

# Initialisation de la population
population = Population()

# Boucle principale
running = True
font = pygame.font.Font(None, 36)  # Choisissez une police et une taille appropriées

# Ajoutez une liste pour stocker les fitness générales de chaque génération
all_fitness_scores = []
# Boucle principale
while running and generation_count < 100:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner l'arrière-plan
    screen.blit(background_image, (0, 0))
    population.run()

    # Affichage du nombre de générations
    text = font.render(f"Generation count {generation_count}", True, (255, 255, 255))
    screen.blit(text, (10, 10))  # Choisissez la position appropriée

    

    # Affichage des rectangles
    pygame.draw.rect(screen, (255, 255, 255), (ox, oy, ow, oh))
    # Dessiner l'image de la barrière à la place du rectangle blanc
    screen.blit(barriere_image, (ox, oy))
    wheat_x = int(sugar.x) - 30  # Ajustez le décalage selon vos besoins
    wheat_y = int(sugar.y)  # Ajustez la position selon vos besoins
    screen.blit(wheat_image, (wheat_x, wheat_y))
    pygame.display.flip()

    # Vérifier si toutes les fourmis ont atteint le blé
    if all(ant.reached_wheat for ant in population.ants):
        # Afficher le message de félicitations
        text = font.render("Félicitations, toutes les fourmis ont atteint le blé!", True, (255, 255, 255))
        screen.blit(text, (width // 4, height // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # Pause pendant 3 secondes
        running = False  # Arrêter la boucle

    clock = pygame.time.Clock()
    fps = 400  # Réglez le nombre de mises à jour par seconde que vous souhaitez
    clock.tick(fps)

     # Gestion du compteur
    if count == life_span:
        population.evaluate()
        population.selection()
        count = 0
        generation_count += 1
        # Affichage de la fitness générale de la génération
        population.afficher_fitness_generale(screen, font)

        # Ajoutez la fitness générale actuelle à la liste
        all_fitness_scores.append(population.fitness_generale_de_la_generation)

    count += 1

# Afficher le meilleur résultat de la fitness générale de toutes les générations
best_fitness = max(all_fitness_scores)
print(f"Meilleur résultat de la fitness générale : {best_fitness}")
# Fermeture de Pygame
pygame.quit()

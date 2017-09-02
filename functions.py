import pygame, sys
from bullet import Bullet, AlienBullet
from alien import Alien
from random import sample, random

def fire_bullet(settings, screen, ship, bullets):
    """Fire bullet if limit is not reached yet"""
    bullet = Bullet(settings, screen, ship)
    if len(bullets) < settings.max_bullets:
        bullets.add(bullet)


def check_events(settings, screen, ship, bullets):
    """Respond to keypress events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.moving_right = True
            elif event.key == pygame.K_a:
                ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                # Create bullet and add it to bullet list
                fire_bullet(settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.moving_right = False
            elif event.key == pygame.K_a:
                ship.moving_left = False
            
def update_screen(settings, screen, ship, bullets, alien_bullets, aliens):
    """Update objects position on the screen and flips the screen"""
    # Fill screen with background color
    # screen.fill(settings.black)
    # screen.blit(background, background.get_rect())

    draw_random_background(settings, screen, settings.background)
    # Draw each bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw alien bullets
    for bullet in alien_bullets.sprites():
        bullet.draw_bullet()
    # Draw fleet of aliens
    aliens.draw(screen)

    ship.blit_me()
    pygame.display.flip()

def update_bullets(bullets, alien_bullets):
    """Check if bullets is outside of the screen and updates bullets"""
    for bullet in bullets.copy():
        if bullet.rect.top < 0:
            bullets.remove(bullet)

    alien_bullets.update()
    bullets.update()

def make_row(settings, screen, aliens):
    """Count how many aliens can be spawned on screen and spawn each alien"""
    # Margin of 2 aliens
    space_left = settings.screen_width - settings.alien_size * settings.margin
    number_of_aliens = int(space_left / (settings.alien_size * settings.spacing_x))

    for alien_position in range(number_of_aliens):
        alien = Alien(settings, screen)
        alien.x = settings.alien_size + settings.spacing_x * settings.alien_size * alien_position
        alien.rect.x = alien.x
        aliens.add(alien)


def update_fleet(settings, screen, aliens):
    """Updates aliens position on the screen"""
    for alien in aliens:
        if alien.rect.left < 0 or alien.rect.right > settings.screen_width:
            settings.alien_velocity = -settings.alien_velocity
            move_aliens_down(settings, screen, aliens)
            break
    aliens.update()

def check_collisions(bullets, aliens, ship, alien_bullets):
    """Check if any bullet collides with any alien"""
    for alien in aliens.copy():
        for bullet in bullets.copy():
            if alien.rect.colliderect(bullet):
                aliens.remove(alien)
                bullets.remove(bullet)
    for bullet in alien_bullets:
        if ship.rect.colliderect(bullet):
            sys.exit()

def spawn_new_row(settings, screen, aliens):
    """Spawn new row of aliens"""
    move_aliens_down(settings, screen, aliens)
    make_row(settings, screen, aliens)

def move_aliens_down(settings, screen, aliens):
    """Moves aliens when they reach the edge of screen"""
    for alien in aliens:
        alien.rect.y += settings.alien_size + settings.spacing_y * settings.alien_size

def check_lose(settings, aliens):
    for alien in aliens:
        if alien.rect.bottom > settings.screen_height:
            return True
    return False

def check_win(settings, screen, aliens, clock):
    if len(aliens) == 0:
        # If player won, increse difficulity (faster aliens, less time between shots)
        clock.tick(60*2)
        settings.alien_velocity = abs(settings.alien_velocity)
        settings.alien_velocity += 0.7

        settings.shooting_time *= 0.8
        settings.max_bullets += 1
        spawn_new_wave(settings, screen, aliens)
        settings.background = make_random_background(settings)

def spawn_new_wave(settings, screen, aliens):
    """Increse alien's velocity and spawn new wave"""
    for row in range(settings.number_of_rows):
        spawn_new_row(settings, screen, aliens)

def shoot(settings, screen, aliens, alien_bullets):
    """Random alien shoots a bullet in player's direction"""
    # if there are any aliens to shoot a bullet
    if len(aliens):
        # Randomly pick alien and shoot
        shooting_alien = sample(list(aliens), 1)[0]
        bullet = AlienBullet(settings, screen, shooting_alien)
        alien_bullets.add(bullet)

def make_random_background(settings):
    stars = []
    for col in range(settings.screen_width):
        for row in range(settings.screen_height):
            if random() > 0.9996:
                stars.append([col, row])
    return stars


def draw_random_background(settings, screen, stars):
    screen.fill(settings.black)
    for star in stars:
        pygame.draw.circle(screen, settings.white, (star[0], star[1]), 2)








#Jacob Hill
#Comp 151
#Final Project

import arcade
import Comp151Window
import types
import random


def sound(self, selected_sound):
    print(selected_sound)
    self.HeroGunshot_sound = None
    self.EnemyGunshot_sound = None
    self.background_music = arcade.load_sound("BackgroundMusic.mp3")


def setup_window(graphicsWindow):
    enemy_list = []
    landmine_list = []
    width, height = graphicsWindow.get_size()
    for enemy_count in range(10):
        enemies = arcade.Sprite("Enemy2.png")
        xPos = random.randint(0, width)
        if xPos < 100:
            xPos = 500
        elif xPos > 900:
            xPos = 500
        yPos = random.randint(0, height)
        if yPos < 500:
            yPos = 800
        elif yPos > 900:
            yPos = 500
        enemies.set_position(xPos, yPos)
        enemy_list.append(enemies)

    for landmine_count in range(10):
        landmines = arcade.Sprite("LandMine2.png")
        landmine_list.append(landmines)
        graphicsWindow.landmine_list = []

    player = arcade.Sprite("Hero2.png")
    player.set_position(200, 400)
    graphicsWindow.player = player
    graphicsWindow.playerDx = 0
    graphicsWindow.playerDy = 0
    graphicsWindow.enemyList = enemy_list
    graphicsWindow.up_pressed = False
    graphicsWindow.down_pressed = False
    graphicsWindow.left_pressed = False
    graphicsWindow.right_pressed = False
    graphicsWindow.score = 0

    graphicsWindow.Hero_Gun_sound = arcade.sound.load_sound("HeroGunshot.mp3")
    graphicsWindow.Enemy_Gun_sound = arcade.sound.load_sound("EnemyGunshot.mp3")
    graphicsWindow.Hitmarker = arcade.sound.load_sound("Hitmarker.mp3")
    graphicsWindow.background_music = arcade.load_sound("Background Music.mp3")
    graphicsWindow.DeathSound = arcade.load_sound("DeathNoise.mp3")
    graphicsWindow.Explosion = arcade.load_sound("Explosion.mp3")
    arcade.play_sound(graphicsWindow.background_music)


def update(window, delta_time):
    if window.up_pressed and not window.down_pressed:
        window.playerDy = 3
    elif window.down_pressed and not window.up_pressed:
        window.playerDy = -3
    else:
        window.playerDy = 0
    if window.left_pressed and not window.right_pressed:
        window.playerDx = -3
    elif window.right_pressed and not window.left_pressed:
        window.playerDx = 3
    else:
        window.playerDx = 0
    window.player.center_x = window.player.center_x + window.playerDx
    window.player.center_y = window.player.center_y + window.playerDy
    enemies_to_remove = None
    landmines_to_remove = None
    for enemies in window.enemyList:
        if enemies.collides_with_sprite(window.player):

            enemies_to_remove = enemies
            window.score += 10
            window.Hero_Gun_sound = arcade.sound.load_sound("HeroGunshot.mp3")
            window.Hitmarker = arcade.sound.load_sound("Hitmarker.mp3")
            arcade.play_sound(window.Hero_Gun_sound)
            arcade.play_sound(window.Hitmarker)
            print(f"Your score is{window.score}")
            if enemies._get_right() > enemies._get_left() < 0:
                break
            if enemies_to_remove:
                window.enemyList.remove(enemies_to_remove)

    for landmines in window.landmine_list:
        if landmines.collides_with_sprite(window.player):
            window.player.kill()
            window.Explosion = arcade.load_sound("Explosion.mp3")
            arcade.play_sound(window.Explosion)
            window.landmines.kill()
        if window.player.kill():
            arcade.play_sound(window.DeathNoise)


def draw(window_being_updated):
    arcade.start_render()
    window_being_updated.player.draw()
    enemies = random.randint(0, 2)

    print(enemies)
    for enemies in window_being_updated.enemyList:
        enemies.draw()
    arcade.draw_rectangle_filled(590, 920, 300, 80, (0, 0, 0, 150))
    arcade.draw_text(f"Score: {window_being_updated.score}", 498, 898, arcade.color.DARK_RED, 36)
    arcade.draw_text(f"Score: {window_being_updated.score}", 500, 900, arcade.color.ORANGE_RED, 36)
    arcade.set_background_color(arcade.color.GREEN)
    if enemies == 0:
        arcade.draw_text(f"You win", 500, 500, arcade.color.BLACK, 50)
        arcade.draw_text(f"You saved the day!", 500, 400, arcade.color.BLACK, 50)


def draw_landmines(window_being_updated):
    arcade.start_render()
    landmines = random.randint(0, 7)
    print(landmines)
    for landmines in window_being_updated.landmine_list:
        landmines.draw()

def key_pressed(game_window, key, modifiers):
    if key == arcade.key.LEFT:
        game_window.left_pressed = True
    if key == arcade.key.RIGHT:
        game_window.right_pressed = True
    if key == arcade.key.UP:
        game_window.up_pressed = True
    if key == arcade.key.DOWN:
        game_window.down_pressed = True


def key_released(game_window, key, modifiers):
    if key == arcade.key.LEFT:
        game_window.left_pressed = False
    if key == arcade.key.RIGHT:
        game_window.right_pressed = False
    if key == arcade.key.UP:
        game_window.up_pressed = False
    if key == arcade.key.DOWN:
        game_window.down_pressed = False


def main():
    graphicsWindow = Comp151Window.Comp151Window(1000, 1000, "Game Demo")
    setup_window(graphicsWindow)
    graphicsWindow.on_draw = types.MethodType(draw, graphicsWindow)
    graphicsWindow.on_update = types.MethodType(update, graphicsWindow)
    graphicsWindow.on_key_press = types.MethodType(key_pressed, graphicsWindow)
    graphicsWindow.on_key_release = types.MethodType(key_released, graphicsWindow)
    arcade.run()


main()

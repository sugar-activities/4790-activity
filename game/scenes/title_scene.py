import pygame
from . import SceneBase, GameScene
from game.objects import Text, Button, STATE

class TitleScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.createTitle()
        self.createStartButton()

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_button.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                self.start_button.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                self.start_button.isHovered(event)

    def Update(self):
        pass

    def Render(self):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen.fill((255, 255, 255))
        self.title.drawOn(self.screen)
        self.start_button.drawOn(self.screen)
        #self.screen.blit(self.start_button.draw(),
        #        ( (self.context.width - self.start_button.width) // 2,
        #         ((self.context.height - self.start_button.height) + self.title.get_height()) // 2))
        #pygame.draw.rect(self.screen, (0, 100, 100), pygame.Rect(100, 100, 200, 200))

    def createTitle(self):
        self.title = Text(self.context, self.context.title)
        self.title.setPen(self.context.font_large)
        self.title.setLocation( (self.context.width - self.title.width) // 2,
                                (self.context.height - self.title.height) // 2)

    def createStartButton(self):
        self.start_button = Button(self.context, "Play Game")
        self.start_button.setPen(self.context.font_small)
        self.start_button.setPen(self.context.font, STATE.HOVER)
        self.start_button.setOnLeftClick(self.handleStartButtonClick)
        self.start_button.setOnHover(self.handleStartButtonHover)
        self.start_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.start_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.start_button.setLocation((self.context.width - self.start_button.width) // 2,
                                      ((self.context.height - self.start_button.height) // 2) + self.title.height )
    """
    helper methods below this point
    """
    def handleStartButtonHover(self):
        pass

    def handleStartButtonClick(self):
        self.SwitchToScene(GameScene)

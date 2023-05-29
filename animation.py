import pygame

class Explose():
    def __init__(self,x_ex,y_ex,screen):
        
        self.image=pygame.image.load("explose/explose1.png")
        self.rect=self.image.get_rect()
        self.rect.x=x_ex
        self.rect.y=y_ex
        self.image_courante=0
        self.animation=True
        self.images=animations.get("explose")
        self.screen=screen
    
    def dessin(self,screen):
        
        
        
        for i in range(1,46):
            pygame.time.delay(1)
            self.screen.blit(self.image,self.rect)
            #print(self.rect)
       

def load_ani_image():
    images=[]
    path="explose/explose"
    
    for i in range(1,46):
        image_path=path+ str(i) + ".png"
        img=pygame.image.load(image_path)
        img_scale=pygame.transform.scale(img,(80,80))
        images.append(img_scale)
    return(images)

animations={"explose" :load_ani_image()}

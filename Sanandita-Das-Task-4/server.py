import pygame
import socket
import time
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = str(10) + "," + str(40)

screen=pygame.display.set_mode((300,300))


ico=pygame.image.load('icon1.jpg')
icon=pygame.transform.scale(ico,(32,32))
pygame.display.set_icon(icon)
pygame.display.set_caption('Player 1')
host1 = '127.0.0.10'

port1 = 8080

def main():

    first  =pygame.draw.rect(screen,(255,255,255),(0,0,100,100))
    second =pygame.draw.rect(screen,(255,255,255),(100,0,100,100))
    third  =pygame.draw.rect(screen,(255,255,255),(200,0,100,100))
    fourth =pygame.draw.rect(screen,(255,255,255),(0,100,100,100))
    fifth  =pygame.draw.rect(screen,(255,255,255),(100,100,100,100))
    sixth  =pygame.draw.rect(screen,(255,255,255),(200,100,100,100))
    seventh=pygame.draw.rect(screen,(255,255,255),(0,200,100,100))
    eighth =pygame.draw.rect(screen,(255,255,255),(100,200,100,100))
    nineth =pygame.draw.rect(screen,(255,255,255),(200,200,100,100))
    pygame.draw.line(screen,(255,0,100),(100,300),(100,0))
    pygame.draw.line(screen,(255,0,100),(200,300),(200,0))
    pygame.draw.line(screen,(255,0,100),(0,100),(300,100))
    pygame.draw.line(screen,(255,0,100),(0,200),(300,200))

    abc(first,second,third,fourth,fifth,sixth,seventh,eighth,nineth)

def abc(first,second,third,fourth,fifth,sixth,seventh,eighth,nineth):

        b=1
        s1=0
        s2=0
        s3=0
        s4=0
        s5=0
        s6=0
        s7=0
        s8=0
        s9=0

        d=0


        cross = pygame.image.load('cross.jpg')
        circle = pygame.image.load('circle.jpg')
        win1 = pygame.image.load('win1.jpg')
        win2 = pygame.image.load('win2.jpg')
        draw = pygame.image.load('draw.jpg')
        pygame.display.flip()
        while 1:
            d+=1
   
            so1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            so1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            so1.bind((host1,port1))
            so1.listen(10)
            cc, addrr = so1.accept()
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            while 1:              
                c=0
                event=pygame.event.wait()
                if event.type==pygame.QUIT:
                    pygame.quit()
                
                if event.type==pygame.MOUSEBUTTONUP:
                        
                        pos=pygame.mouse.get_pos()
                        if first.collidepoint(pos):
                            screen.blit(cross,[1,1])
                            s1=1
                            
                            first=pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='1'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if second.collidepoint(pos):
                            screen.blit(cross,[101,1])
                            two=1
                            s2=1
                            
                            second =pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='2'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            
                            break
                        
                        if third.collidepoint(pos):
                            screen.blit(cross,[201,1])
                            three=1
                            s3=1
                            
                            third  =pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='3'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if fourth.collidepoint(pos):
                            screen.blit(cross,[1,101])
                            four=1
                            s4=1
                            
                            fourth =pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='4'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if fifth.collidepoint(pos):
                            screen.blit(cross,[101,101])
                            five=1
                            s5=1
                            
                            fifth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='5'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if sixth.collidepoint(pos):
                            screen.blit(cross,[201,101])
                            six=1
                            s6=1
                            
                            sixth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='6'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if seventh.collidepoint(pos):
                            screen.blit(cross,[1,201])
                            seven=1
                            s7=1
                            
                            seventh  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='7'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if eighth.collidepoint(pos):
                            screen.blit(cross,[101,201])
                            eight=1
                            s8=1
                            
                            eighth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='8'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                        if nineth.collidepoint(pos):
                            screen.blit(cross,[201,201])
                            nine=1
                            s9=1
                            
                            nineth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            msg='9'
                            co= msg.encode(encoding='UTF-8')
                            cc.send(co)
                            break
                    
            so1.close()
            
                     
            if((s1==1&s2==1&s3==1)|(s1==1&s4==1&s7==1)|(s1==1&s5==1&s9==1)|(s2==1&s5==1&s8==1)|(s3==1&s5==1&s7==1)|(s3==1&s6==1&s9==1)|(s4==1&s5==1&s6==1)|(s7==1&s8==1&s9==1)):
                    
                    screen.blit(win1,[0,0])
                    pygame.display.flip()
                    time.sleep(5)
                    main()
            if((s1==2&s2==2&s3==2)|(s1==2&s4==2&s7==2)|(s1==2&s5==2&s9==2)|(s2==2&s5==2&s8==2)|(s3==2&s5==2&s7==2)|(s3==2&s6==2&s9==2)|(s4==2&s5==2&s6==2)|(s7==2&s8==2&s9==2)):

                    screen.blit(win2,[0,0])
                    pygame.display.flip()

                    time.sleep(5)
                    main()       
            pygame.display.flip()
            if d==5:
                screen.blit(draw,[0,0])
                pygame.display.flip()
                time.sleep(5)
                main()
            
            so1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            so1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            so1.connect((host1,port1))
            
            
            mess = so1.recv(1024)
            do=int(mess)
            if do==1:
                screen.blit(circle,[1,1])
                s1=2
                first=pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
            if do==2:
                screen.blit(circle,[101,1])
                s2=2
                second =pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
            if do==3:
                screen.blit(circle,[201,1])
                s3=2
                
                third  =pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
            if do==4:
                screen.blit(circle,[1,101])
                s4=2
                
                fourth =pygame.draw.rect(screen,(255,0,0),(0,-1,0,0))
            if do==5:
                screen.blit(circle,[101,101])
                s5=2
                
                fifth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
            if do==6:
                screen.blit(circle,[201,101])
                s6=2
                
                sixth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
            if do==7:
                screen.blit(circle,[1,201])
                s7=2
                
                seventh  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
            if do==8:
                screen.blit(circle,[101,201])
                s8=2
                
                eighth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
            if do==9:
                screen.blit(circle,[201,201])
                s9=2
                
                nineth  =pygame.draw.rect(screen,(255,255,255),(0,-1,0,0))
            so1.close()
            if((s1==1&s2==1&s3==1)|(s1==1&s4==1&s7==1)|(s1==1&s5==1&s9==1)|(s2==1&s5==1&s8==1)|(s3==1&s5==1&s7==1)|(s3==1&s6==1&s9==1)|(s4==1&s5==1&s6==1)|(s7==1&s8==1&s9==1)):
                if(d==0):
                    
                    screen.blit(win1,[0,0])
                    pygame.display.flip()
                    time.sleep(5)
                    main()
            if((s1==2&s2==2&s3==2)|(s1==2&s4==2&s7==2)|(s1==2&s5==2&s9==2)|(s2==2&s5==2&s8==2)|(s3==2&s5==2&s7==2)|(s3==2&s6==2&s9==2)|(s4==2&s5==2&s6==2)|(s7==2&s8==2&s9==2)):

                    screen.blit(win2,[0,0])
                    pygame.display.flip()
                    time.sleep(5)
                    main()
            
            

            pygame.display.flip()
pygame.display.flip()
if __name__=="__main__":
    main() 

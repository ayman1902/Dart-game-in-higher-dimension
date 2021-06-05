#100% programmable by Belhaj Ayman MPSI2
#the idea is inspirated by 3brown1blue and his video about this subject
#! those esperance E[s] in this animation converge slowly to exp(pi/4)
#all animation is dynamique
#n men how much game you wanna play
#enjoy the Game
#Import library
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math as mt
#configuration
plt.style.use('dark_background')
time_animation1=0.000001
color=['#3498db','#9b59b6','#2ecc71','#e74c3c','#f1c40f','#22a6b3','#34495e']
second=1
second2=0.001
#some prequeris
def create_rectangle():
    x=[-1,1,1,-1,-1]
    y=[1,1,-1,-1,1]
    return x,y
def create_cercle_radius(k):
    c0=[k*np.cos(i) for i in np.arange(0,2*np.pi,0.01)]
    l0=[k*np.sin(i) for i in np.arange(0,2*np.pi,0.01)]
    return c0,l0
def mean_value(l):
    s=0
    g=0
    for i in range(len(l)):
        s+=l[i]*(i+1)
        g+=l[i]
    return s/g
def mean_value_score(l):
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s/len(l)
#algorithme to get score
def score():
    s=1
    r=[1]
    h=[]
    for i in range(100):
        x=rd.uniform(-1,1)
        y=rd.uniform(-1,1)
        h.append(mt.sqrt(x**2 + y**2))
        if (h[len(h)-1])**2<=(r[len(r)-1])**2:
            r.append(mt.sqrt(r[len(r)-1]**2-h[len(h)-1]**2))
            s+=1
        else:
            break
    return s
#calcule of esperence of score E[s]
def lim_frequen(n):
    l=[]
    s=0
    for i in range(1,n+1):
        s=score()
        l.append(s)
    return mean_value_score(l)
#animation of simulation of dart game in higher dimension
def figi(n):
    plt.figure('Dart',[6,5.5])
    m=[]
    for l in range(1,n+1): 
        s=1
        r=[1]
        h=[]
        data=[]
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        Rect=plt.plot(create_rectangle()[0],create_rectangle()[1],color='blue')
        Rext_fill=plt.fill_between(create_rectangle()[0],create_rectangle()[1],color=color[0])
        Cerc,=plt.plot(create_cercle_radius(1)[0],create_cercle_radius(1)[1],color='red')
        Cerc_fill=plt.fill_between(create_cercle_radius(1)[0],create_cercle_radius(1)[1],color='red')
        plt.plot(0,0,'ro',color='black')
        plt.title('Game '+str(l)+' your score is :'+str(s))
        plt.pause(second)
        ax = plt.gca()
        for i in range(10):
            x=rd.uniform(-1,1)
            y=rd.uniform(-1,1)
            data.append((x,y))
            h.append(mt.sqrt(x**2 + y**2))#
            plt.plot(x,y,'ro',color='black')
            plt.text(x,y,i+1,color='white',fontsize=15)
            if h[len(h)-1]<=r[len(r)-1]:
                s+=1
                
                plt.title('Game '+str(l)+' your score is :'+str(s))
                
                plt.pause(second)
                line,=plt.plot([0,x],[0,y],color='white')
                plt.pause(second)
                '''
                if y==0:
                    eq,=plt.plot([x,x],[-1,1])
                else:
                    #eq,=plt.plot([-1,1],[get_equation(x,y,-1),get_equation(x,y,1)],color='white')
                    eq,=plt.plot(get_cordinate_eq(x,y,r[len(r)-1])[0],get_cordinate_eq(x,y,r[len(r)-1])[1],'ro',color='pink')'''
                r.append(mt.sqrt(r[len(r)-1]**2-h[len(h)-1]**2))#
                plt.pause(second)
                ax.lines.remove(line)
                #ax.lines.remove(eq)
                plt.pause(second)
                #ax.lines.remove(Cerc)
                Cerc_fill.remove()
                Cerc,=plt.plot(create_cercle_radius(r[len(r)-1])[0],create_cercle_radius(r[len(r)-1])[1],color='red')
                Cerc_fill=plt.fill_between(create_cercle_radius(r[len(r)-1])[0],create_cercle_radius(r[len(r)-1])[1],color='red')
                plt.pause(second)
                
            else:
                break
            
            plt.title('Game over your score is :'+str(s))
                
        m.append(s)
        print(m)        
        plt.pause(1)
        
        if l<n:
            plt.pause(1)
            plt.clf()
    plt.title(' your best score is'+ str(max(m)))
    plt.pause(1)
    plt.show()
#animation 1 of score and esperance E[s]
def lim_frequen_animation(n):
        plt.figure('Dart',[12,5.5])
        s=0
        x=[]
        y=[]
        z=[]
        sl=[0,0,0,0,0,0]
        
        for i in range(1,n+1):
            a=plt.subplot(1,2,1)
            l=score()
            s+=l
            z.append(s/i)
            sl[l-1]+=1
            sm=[(sl[k]/i)*100 for k in range(len(sl))]
            x.append(i)
            y.append(mean_value(sm))
            plt.title('E[s]='+str(s/i))
            plt.bar(i,l,align='edge',width=1,ec='black',color=color[l-1])
            plt.ylabel("Score")
            plt.xlabel('Game')
            b=plt.subplot(1,2,2)
            plt.title('Ecart='+str(mt.exp(mt.pi/4) - (mean_value(sm))))
            plt.plot(x,y,color=color[4])
            
            #plt.ylim(0,6)
            #plt.plot(x,z,color=color[4])
            plt.ylabel("E[s]")
            plt.xlabel('Game')
            plt.plot(x,[mt.exp(mt.pi/4) for k in range(1,i+1)],color='#e74c3c')
            plt.pause(time_animation1)
        plt.show()
#animation 2 of score and esperance E[s]
def scare(n):

    plt.figure('Dart',[12,5.5])
    sl=[0,0,0,0,0,0,0]
    x=[]
    y=[]
    ax  = plt.subplot()
    for i in range(1,n+1):
        x.append(i)
        l=score()
        sl[l-1]+=1
        sm=[(sl[k]/i)*100 for k in range(len(sl))]
        plt.subplot(1,2,1)
        plt.bar([1,2,3,4,5,6,7],sm,align='center',width=1,ec='black',color=color[1:7])
        plt.ylim(0,100)
        plt.xlabel('score')
        plt.ylabel("frequence d'apparence")
        plt.title('#Game:' + str(i)+' E[s]='+ str(mean_value(sm)) +' Last Score='+str(l))
        plt.subplot(1,2,2)
        y.append(mean_value(sm))
        plt.plot(x,y)
        plt.plot(x,[mt.exp(mt.pi/4) for k in range(1,i+1)],color='#e74c3c')
        plt.ylabel('E[s]')
        plt.xlabel('Games')
        plt.title('#Game:' + str(i)+' Ecart='+ str(mt.exp(mt.pi/4)-mean_value(sm)))
        plt.pause(time_animation1)
        if i<n:
            plt.clf()
    plt.show()
#animation of score and the ecart between exp(pi/4) and E[s] the esperance
def Ecart(n):
    plt.figure('Dart',[12,5.5])
    sl=[0,0,0,0,0,0,0,0]
    x=[]
    y=[]
    ax  = plt.subplot()
    for i in range(1,n+1):
        x.append(i)
        l=score()
        sl[l-1]+=1
        sm=[(sl[k]/i)*100 for k in range(len(sl))]
        plt.subplot(1,2,1)
        plt.bar([1,2,3,4,5,6,7,8],sm,align='center',width=1,ec='black',color=color[1:7])
        plt.ylim(0,100)
        plt.xlabel('score')
        plt.ylabel("frequence d'apparence")
        plt.title('#Game:' + str(i)+' E[s]='+ str(mean_value(sm)) +' Last Score='+str(l))
        plt.subplot(1,2,2)
        y.append(mt.exp(mt.pi/4)-mean_value(sm))
        plt.plot(x,y)
        plt.axhline(color = '#e74c3c')
        plt.ylabel('Ecart')
        plt.xlabel('Games')
        plt.title('#Game:' + str(i)+' Ecart='+str(mt.exp(mt.pi/4)-mean_value(sm)))
        plt.pause(time_animation1)
        if i<n:
            plt.clf()
    plt.show()
#here some example to use one by one 
#scare(1000)
#Ecart(100)
#lim_frequen_animation(30)
figi(3)
#print(lim_frequen(100000))
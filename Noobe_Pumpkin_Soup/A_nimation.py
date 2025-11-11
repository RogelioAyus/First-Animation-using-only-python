from scene import *
import sound
from random import *
from math import *
from time import strftime, gmtime
from console import input_alert
A = Action


def rr(cir,cx,cy):
	alpha = 2 * math.pi * random()
	r = cir * math.sqrt(1)
	x = r * math.cos(alpha) + cx
	y = r * math.sin(alpha) + cy
	return x,y

class Lyrb (LabelNode):
	def __init__(self,text,color,x,index,fonte,fsi, *args,**kwargs):
		LabelNode.__init__(self, text,position=(x,164),anchor_point=(index,0.5),alpha=0,font=(fonte,fsi),color=color,z_position=99, *args, **kwargs)
		self.queue = 0

class Syrb (SpriteNode):
	def __init__(self,img,color, *args,**kwargs):
		SpriteNode.__init__(self, img,position=(200,164),anchor_point=(0,0.5),alpha=0,color=color, *args, **kwargs)
		self.queue = 0
		self.decay_effect = 0
		self.subactions = None

class efq (SpriteNode):
	def __init__(self,color,w=64,y=64, *args,**kwargs):
		SpriteNode.__init__(self, color=color, size=(w,y),blend_mode=BLEND_ADD,alpha=0.5, *args, **kwargs)
		
class cubq (SpriteNode):
	def __init__(self,color, *args,**kwargs):
		SpriteNode.__init__(self, color=color, size=(64,64),blend_mode=BLEND_ADD,alpha=0.05, *args, **kwargs)
	 
		

class MyScene (Scene):
	def stop(self):
		self.player1.stop()
	def setup(self):
		self.player1 = sound.Player('Noobe_Pumpkin_Soup_Final.mp3')
		#self.beat = 0
		self.n = 0
		self.lyriclist = []
		self.lx = []
		self.affected = []
		self.wh = self.size.w/2
		self.hh = self.size.h/2
		self.background_color = '#000000'
		self.Foreground = SpriteNode(color='#000000',size=(1080,730),z_position=50,position=(self.size.w/2,self.size.h/2),parent=self,alpha=0)
		self.border = SpriteNode('border.PNG',position=(self.wh,self.hh),size=(1024,768),parent=self,z_position=100)
		self.backg = SpriteNode('img/9.PNG',position=(self.wh,self.hh),size=(1024,768),parent=self,z_position=0)
		self.backg2 = SpriteNode('img/9.PNG',position=(self.size.w*1.5,self.hh),size=(1024,768),parent=self,z_position=0)		
		
		self.ground = SpriteNode('img/4.png',position=(self.wh,self.hh),size=(1024,768),parent=self,z_position=3,blend_mode=BLEND_NORMAL)
		
		self.ground2 = SpriteNode('img/4.png',position=(self.size.w*1.5-32,self.hh),size=(1024,768),parent=self,z_position=3,blend_mode=BLEND_NORMAL)
		
		self.p1 = SpriteNode('ami_walk/Ami_Walk_Frame_1.png',parent=self,position=(200,313),z_position=4,size=(254,254),color='#ffffff')
		self.n1 = SpriteNode('Noobe/Noobe_Walk_Frame_1.png',parent=self,position=(-50,313),z_position=4,size=(254,254))
		self.transition = SpriteNode('IMG_0339.PNG',parent=self.p1,scale=0.5,alpha=0)
		
		self.ghoul = SpriteNode('ghoul.PNG',parent=self,position=(1200,350),z_position=4,size=(254,254))
		self.ghoul2 = SpriteNode('ghoul.PNG',parent=self,position=(1200,350),z_position=4,size=(254,254))
		self.ghoul3 = SpriteNode('ghoul.PNG',parent=self,position=(1200,350),z_position=4,size=(254,254))
		self.ghoul4 = SpriteNode('ghoul.PNG',parent=self,position=(1200,350),z_position=4,size=(254,254))
		self.pot = SpriteNode('Other img/pot.png',size=(254,254),position=(1200,600),parent=self,z_position=5)
		
		self.effectg2 = SpriteNode('img/5.png',position=(self.wh,self.hh),size=(1024,768),parent=self,z_position=4,blend_mode=BLEND_NORMAL)
		
		self.bar = SpriteNode(color="#ffffff",parent=self,
		position=(200,128),z_position=51,size=(600,7),anchor_point=(0,0.5))
		#self.finishbar = SpriteNode(color="#000000",parent=self,position=(200,128),z_position=51,size=(0,7),anchor_point=(0,0.5))
		#self.timetell = LabelNode("00:00-03:02",parent=self,position=(190,128),z_position=51,font=('Arial Rounded MT Bold',16),color='#ffffff',anchor_point=(1,0.5))
		
		self.tibar = SpriteNode('title.PNG',parent=self,
		position=(0,630),z_position=51,anchor_point=(0,0.5),scale=0.3)
		
		self.titleso = SpriteNode('blackw.PNG',position=(self.wh,self.hh),size=(1024,768),parent=self,z_position=9)
		self.titleso2 = SpriteNode('btitle.PNG',position=(self.wh,self.hh),size=(1024,768),parent=self,z_position=9,alpha=0)
		
		
		self.barlth = 0
		self.cut = False
		self.effectsize = 0
		self.videoend = False;
		self.paused = True
	def did_change_size(self):
		pass
	
	def grounds(self):
		self.ground.position = (self.ground.position.x - 3,self.ground.position.y)
		self.ground2.position = (self.ground2.position.x - 3,self.ground2.position.y)
		if self.ground.position.x < -(self.size.w-513):
			self.ground.position=(self.size.w/2,self.size.h/2)
			self.ground2.position=(self.size.w*1.5,self.size.h/2)
		
		self.backg.position = (self.backg.position.x - 1,self.backg.position.y)
		self.backg2.position = (self.backg2.position.x - 1,self.backg2.position.y)
		if self.backg.position.x <= -(self.size.w-513):
			self.backg.position=(self.size.w/2,self.size.h/2)
			self.backg2.position=(self.size.w*1.5,self.size.h/2)
	def update(self):
		e = uniform(0,30)
		d = uniform(1,3)
		if self.n == 69:
			eq = efq(parent=self,position=(uniform(0,1024),0),z_position=choice([2,5]),color='#ffffff')
			if e > 20:
				cq = cubq(parent=self,position=(uniform(0,1024),0),z_position=20,color='#ffffff')
				actiow = [A.group(A.scale_y_to(self.size.h,d-1),A.scale_x_to(0,d/5)),A.remove()]
				cq.run_action(A.sequence(actiow))
		else:
			if self.n <= 87:
				co = choice(['#f740ff','#ff4072','#9340ff'])
				eq = efq(parent=self,position=(uniform(0,1024),0),color=co,z_position=choice([2,5]))
		if self.n <= 87:
			action = [A.group(A.move_by(-150*d,uniform(100,500),d),A.fade_to(0,d),A.scale_to(0,d)),A.remove()]
			eq.run_action(A.sequence(action))
			
		self.grounds()
		#self.barup()
		self.pt = self.player1.current_time
		self.chnage_p()
		if self.n <= 49:
			self.lyric()
		elif self.n <= 80:
			self.lyric2()
		else:
			self.lyric3()
		
		if self.player1.playing == False and self.videoend == False:
			self.bar.run_action(A.move_by(0,-50,9,TIMING_EASE_OUT))
		#	self.finishbar.run_action(A.move_by(0,-50,9,TIMING_EASE_OUT))
			#self.timetell.run_action(A.move_by(0,-50,9,TIMING_EASE_OUT))
			

		#print(self.pt)
		#print(str(self.lyriclist))
	def chnage_p (self):
		if 17 <= self.n <= 20:
			self.p1.texture = Texture('Ami_transform/Ami_Ghost_Walk_withlgs_Frame_'+str(int((self.t/0.15)%8)+1)+'.png')
		elif 81 <= self.n <= 81:
			self.p1.texture = Texture('Ami_Ghost_Walk_withoutlgsScream.png')
		elif 21 <= self.n <= 116:
			self.p1.texture = Texture('Ami_ghost/Ami_Ghost_Walk_withoutlgs_Frame_'+str(int((self.t/0.15)%8)+1)+'.png')
			a = uniform(0,30)
			if a > 28:
				e = efq(parent=self,color="white",w=5,y=5,position=(-20+self.p1.position.x,uniform(-64,64)+self.p1.position.y),z_position=5)
				e.run_action(A.sequence(A.group(A.move_by(-250,uniform(-10,10),2),A.scale_to(0,2)),A.remove()))
		elif 117 <= self.n:
			self.p1.texture = Texture('AmiNoove/Ami_Noobe_Walk_Frame_'+str(int((self.t/0.15)%8)+1)+'.png')
		else:
			self.p1.texture = Texture('ami_walk/Ami_Walk_Frame_'+str(int((self.t/0.15)%8)+1)+'.png')
		self.p1.size = (256,256)
		
		self.n1.texture = Texture('Noobe/Noobe_Walk_Frame_'+str(int((self.t/0.05)%12)+1)+'.png')
		self.n1.size = (256,256)
		self.ghoul.texture = Texture('Ghoul/Ghoul_Frame_'+str(int((self.t/0.4)%4)+1)+'.png')
		self.ghoul2.texture = Texture('Ghoul/Ghoul_Frame_'+str(int((self.t/0.1)%4)+1)+'.png')
		self.ghoul3.texture = Texture('Ghoul/Ghoul_Frame_'+str(int((self.t/0.07)%4)+1)+'.png')
		self.ghoul4.texture = Texture('Ghoul/Ghoul_Frame_'+str(int((self.t/0.5)%4)+1)+'.png')
		#def barup(self):
		'''
		self.barlth = min((self.player1.current_time/self.player1.duration)*600,600)
		self.effectsize += (0.01*self.barlth)
		if self.effectsize >= self.barlth:
			self.effectsize = 0;
		self.timetell.text= (str(strftime("%M:%S",gmtime(min(self.player1.current_time,194))))+"-"+str(strftime("%M:%S",gmtime(self.player1.duration))))
		self.finishbar.size = (self.barlth,7)
		'''
	def touch_began(self,touch): #<--- touch
		self.onto = 0
		if touch.location.x < self.size.w/2:
			self.player1.pause()
			self.paused = True
		else:
			self.lyriclist.clear()
	def touch_moved(self,touch):
		if touch.location.x < self.size.w/2:
			self.onto = 0
			self.onto = touch.location.x/2
			print(self.onto)
	def touch_ended(self,touch):
		if touch.location.x < self.size.w/2:
			self.player1.current_time = int(self.onto)
			self.paused =False
			self.n = 0
			self.player1.play()
			
	def updatelyr(self, x):
		for i in x:
			if not i.parent:
				x.remove(i);
			elif i.queue >= 4:
				i.remove_from_parent()
			elif i.queue >= 3:
				i.run_action(A.group(A.move_by(0,32,0.5,TIMING_EASE_OUT),A.fade_to(0,0.5)))
			elif i.queue >= 1:
				i.run_action(A.group(A.move_by(0,32,0.5,TIMING_EASE_OUT),A.fade_to(0.2,0.5)))
			elif i.queue == 0:
				i.run_action(A.fade_to(1,0.5))
			i.queue += 1
			
	def lyric(self):
			if 8 <= self.pt <= 8.2:
				self.titleso2.run_action(A.fade_to(1,2))
			if 15 <= self.pt <= 15.2:
				self.titleso2.run_action(A.fade_to(0,1))
				self.titleso.run_action(A.fade_to(0,1))
			self.nelyric("Strolling through the grounds,",16.6,0,'#f980ff')
			self.nelyric("I can tell",17.8,1,'#f980ff')
			self.nelyric("Worry not",18.3,2,'#f980ff')
			self.nelyric("its gonna be fine.",19,3,'#f980ff')
			self.nelyric("My name is Ami",20.6,4,'#f980ff')
			self.nelyric("and i will guide you",21.6,5,'#f980ff')
			self.nelyric("through this spooky rhyme.",22.6,6,'#f980ff')
			self.nelyric("I was walking one day",24.8,7,'#f980ff')
			self.nelyric("through the fields of green,",25.8,8,'#f980ff')
			self.nelyric("then stumbled across a castle",26.6,9,'#f980ff')
			self.nelyric("that\'s never been seen.",27.8,10,'#f980ff')
			self.nelyric("I entered the grounds",28.8,11,'#f980ff')
			self.nelyric('and went through the door,',29.8,12,'#f980ff')
			self.nelyric('then something new happened',30.8,13,'#f980ff')
			self.nelyric('to me like never before.',31.8,14,'#f980ff')
			self.nelyric('My hair turned white',33.2,15,'#f980ff')
			if 33.2 <= self.pt <= 33.25:
				self.transition.run_action(A.fade_to(1,1))
			self.nelyric('and my skin got pale,',34.2,16,'#f980ff')
			if 34.2 <= self.pt <= 34.25:
				self.transition.run_action(A.fade_to(0,1))
			self.nelyric('it\'s like something that',35.2,17,'#f980ff')
			self.nelyric('came out of a fairytale.',35.7,18,'#f980ff')
			self.nelyric('My arc twitched twice', 37.2,19,'#f980ff')
			if 37.5 <= self.pt <= 37.55:
				self.transition.run_action(A.fade_to(1,0.3))
			self.nelyric('and my legs went POOF,',38,20,'#f980ff')
			if 39 <= self.pt <= 39.05:
				i = 0
				while i <= 10:
					smallt = SpriteNode('IMG_0339.PNG',parent=self,size=(64,64),position=(200,280),z_position=5)
					x,y = rr(400,0,0)
					smallt.run_action(A.sequence(A.group(A.move_by(x,y,uniform(2,5)),A.scale_to(0,uniform(0.3,2)),A.fade_to(0,uniform(0.3,2))),A.remove()))
					i += 1
					
				#print("poof")
				self.transition.alpha = 0
			self.nelyric('then all of a sudden ',39.5,21,'#f980ff')
			self.nelyric('I can fly to the roof!',40.2,22,'#f980ff')
			if 39 <= self.pt <= 39.5:
				self.p1.run_action(A.group(A.move_by(1200,900,3,TIMING_EASE_IN),A.fade_to(0,2)))
			self.endl(40.7,23,self.lyriclist)
			if 41 < self.pt < 41.5:
				self.lyriclist.clear()
			self.pn('Pumpkin',42,24,'#ffc280',800,1)
			self.nelyric('Pumpkin',42,25,'#f980ff')
			self.pn('Soup',43.8,26,'#ffc280',800,1)
			self.nelyric('Soup',43.8,27,'#f980ff')
			self.pn('Pumpkin',46,28,'#ffc280',800,1)
			self.nelyric('Pumpkin',46,29,'#f980ff')
			self.pn('Soup',47.8,30,'#ffc280',800,1)
			self.nelyric('Soup',46,31,'#f980ff')
			self.endl(48.7,32,self.lx)
			self.endl(48.7,33,self.lyriclist)
			if self.pt > 48.8 and self.pt < 48.9:
				self.p1.run_action(A.group(A.fade_to(1,1),A.move_to(200,313,0)))
				self.lyriclist.clear()
				self.lx.clear()
			self.pn('Noobe',50,34,'#ffc280',800,1)
			self.pn('Pumpkin',51,35,'#ffc280',800,1)
			self.pn('Soup',52,36,'#ffc280',800,1)
			self.nelyric('That\'s where I found my noobe.',53,37,'#f980ff')
			self.pn('Noobe',54,38,'#ffc280',800,1)
			self.pn('Pumpkin',55,39,'#ffc280',800,1)
			self.pn('Soup',55.7,40,'#ffc280',800,1)
			self.nelyric('You Noobe.',58,41,'#f980ff')
			self.pn('Noobe',58.5,42,'#ffc280',800,1)
			self.pn('Pumpkin',59.3,43,'#ffc280',800,1)
			self.pn('Soup',60.2,44,'#ffc280',800,1)
			self.nelyric('That\'s right,',61,45,'#f980ff')
			self.nelyric('I found my noobe',61.7,46,'#f980ff')
			self.pn('Noobe',62.6,47,'#ffc280',800,1)
			self.pn('Pumpkin',63.4,48,'#ffc280',800,1)
			self.pn('Soup',64,49,'#ffc280',800,1)
	def lyric2(self):
			self.endl(66,50,self.lx)
			self.endl(66,51,self.lyriclist)
			if self.pt > 66 and self.pt < 66.1:
				self.lyriclist.clear()
				self.lx.clear()
			self.nelyric('I was flying around the room ',66.6,52,'#f980ff')
			self.nelyric('with little white trail,',67.8,53,'#f980ff')
			self.nelyric('coming from',69,54,'#f980ff')
			self.nelyric('behind me like a tail.',69.5,55,'#f980ff')
			
			self.nelyric('I was flying through walls',71,56,'#f980ff')
			self.nelyric('and the halls,',72,57,'#f980ff')
			self.nelyric('then all of a sudden',73,58,'#f980ff')
			self.nelyric('I came across a white ball.',73.7,59,'#f980ff')
			if 73.7 <= self.pt <= 73.9:
				self.n1.run_action(A.sequence(A.move_to(1100,313,5),A.move_to(-30,313,0),A.wait(1),A.move_to(250,313,3)))
			
			self.nelyric('It rolled by itself',74.8,60,'#f980ff')
			self.nelyric('into a black room',76,61,'#f980ff')
			self.nelyric('and knocked itself',77,62,'#f980ff')
			self.nelyric('into a broom.',78,63,'#f980ff')
			
			self.nelyric('The little ball shook and jumped in twos,',79,64,'#f980ff')
			self.nelyric('it revealed itself to be a ',81,65,'#f980ff')
			self.nelyric('little',82,66,'#f980ff')
			self.nelyric('white',82.5,67,'#f980ff')
			self.nelyric('NOOBE',83.2,68,'#ffffff')
			self.nelyric('The Noobe smiled at me',100,69,'#f980ff')
			self.nelyric('and purred so loud,',101,70,'#f980ff')
			self.nelyric('it suddenly attracted',101.9,71,'#f980ff')
			self.nelyric('a goulish crowd.',102.8,72,'#f980ff')
			if 102.8 < self.pt < 103:
				self.ghoul.run_action(A.move_to(800,250,1,TIMING_EASE_BACK_OUT))
				self.pot.run_action(A.move_to(600,550,1.5,TIMING_EASE_BACK_OUT))
				self.ghoul2.run_action(A.move_to(900,400,0.5,TIMING_EASE_BACK_OUT))
				self.ghoul3.run_action(A.move_to(700,300,2,TIMING_EASE_BACK_OUT))
				self.ghoul4.run_action(A.move_to(600,350,1.5,TIMING_EASE_BACK_OUT))
			
			self.nelyric('They grabbed their pots',104,73,'#f980ff')
			self.nelyric('with purple goo,',105,74,'#f980ff')
			self.nelyric('and said',106,75,'#f980ff')
			self.nelyric('we here to cook that little white NOOBE.',106.4,76,'#96ff80',fonte='Noteworthy')
			
			self.nelyric('My eyes turned pink,',108.3,77,'#f980ff')
			self.nelyric('and my arc twitched twice,',109.2,78,'#f980ff')
			self.nelyric('my anger grew then',110,79,'#f980ff')
			if 110 <= self.pt <= 110.2:
				self.transition.run_action(A.fade_to(1,0.6))
			self.nelyric('I screamed BOO!',111,80,'#ffffff')
	def lyric3(self):
			if self.pt > 111.5 and self.pt < 111.7:
				self.pot.z_position = 20
				at = A.sequence(A.group(A.fade_to(1,1),A.move_to(560,290,1)),A.move_by(-500,0,4),A.remove())
				self.pot.run_action(at)
				
				self.ghoul.run_action(A.fade_to(0,1))
				self.ghoul2.run_action(A.fade_to(0,1))
				self.ghoul3.run_action(A.fade_to(0,1.5))
				self.ghoul4.run_action(A.fade_to(0,1))
				self.transition.run_action(A.fade_to(0,1))
				i = 0
				self.transition.run_action(A.fade_to(0,0.2))
				while i <= 5:
					smallt = SpriteNode('IMG_0339.PNG',parent=self,size=(64,64),position=(200,340),z_position=5)
					x,y = rr(2000,0,0)
					smallt.run_action(A.sequence(A.group(A.move_by(x,y,uniform(2,5)),A.scale_to(0,uniform(0.3,2)),A.fade_to(0,uniform(0.3,2))),A.remove()))
					i += 1
			self.nelyric('The crowd got dizzy',112.5,81,'#f980ff')
			self.nelyric('and dropped their pots, ',113.2,82,'#f980ff')
			self.nelyric('I snatched the NOOBE up ',114.5,83,'#f980ff')
			self.nelyric('before we got caught. ',115.2,84,'#f980ff')
			if self.pt > 115.3 and self.pt < 115.6:
				self.Foreground.run_action(A.fade_to(1,1))
				self.lx.clear()
			self.pn('Pumpkin',116.6,85,'#ffc280',800,1)
			self.nelyric('Pumpkin',116.6,86,'#f980ff')
			self.pn('Soup',119,87,'#ffc280',800,1)
			self.nelyric('Soup',119,88,'#f980ff')
			self.pn('Pumpkin',121,89,'#ffc280',800,1)
			self.nelyric('Pumpkin',121,90,'#f980ff')
			self.pn('Soup',123,91,'#ffc280',800,1)
			self.nelyric('Soup',123,92,'#f980ff')
			self.endl(124,93,self.lx)
			self.endl(124,94,self.lyriclist)
			if self.pt > 124 and self.pt < 124.2:
				self.cuti()
				self.Foreground.run_action(A.sequence(A.fade_to(0,1),A.remove()))
				self.lyriclist.clear()
				self.lx.clear()
			self.pn('Noobe',125.3,95,'#ffc280',800,1)
			self.pn('Pumpkin',126,96,'#ffc280',800,1)
			self.pn('Soup',126.5,97,'#ffc280',800,1)
			self.nelyric('That\'s where I found my noobe.',128.2,98,'#f980ff')
			self.pn('Noobe',129.2,99,'#ffc280',800,1)
			self.pn('Pumpkin',130,100,'#ffc280',800,1)
			self.pn('Soup',130.7,101,'#ffc280',800,1)
			self.nelyric('You Noobe.',133,102,'#f980ff')
			self.pn('Noobe',133.5,103,'#ffc280',800,1)
			self.pn('Pumpkin',134.5,104,'#ffc280',800,1)
			self.pn('Soup',135,105,'#ffc280',800,1)
			self.nelyric('That\'s right,',136,106,'#f980ff')
			self.nelyric('I found my noobe',136.8,107,'#f980ff')
			self.pn('Noobe',137.6,108,'#ffc280',800,1)
			self.pn('Pumpkin',138.6,109,'#ffc280',800,1)
			self.pn('Soup',139.2,110,'#ffc280',800,1)
			self.endl(141,111,self.lyriclist)
			self.endl(141,112,self.lx)
			if self.pt > 141 and self.pt < 141.3:
				self.lyriclist.clear()
				self.lx.clear()
			self.nelyric('We flew out the castle',141.9,113,'#f980ff')
			self.nelyric('quick and free,',142.5,114,'#f980ff')
			self.nelyric('then landed and',143.5,115,'#f980ff')
			if self.pt > 143 and self.pt < 143.2:
				self.n1.run_action(A.sequence(A.move_to(200,313,0.6),A.remove()))
				self.transition.run_action(A.fade_to(1,0.5))
			self.nelyric('turned back to little pink me.',144.3,116,'#f980ff')
			if self.pt > 144.3 and self.pt < 144.5:
				self.transition.run_action(A.fade_to(0,1))
				i = 0
				while i <= 10:
					smallt = SpriteNode('IMG_0339.PNG',parent=self,size=(64,64),position=(200,280),z_position=5)
					x,y = rr(400,0,0)
					smallt.run_action(A.sequence(A.group(A.move_by(x,y,uniform(2,5)),A.scale_to(0,uniform(0.3,2)),A.fade_to(0,uniform(0.3,2))),A.remove()))
					i += 1
				
			
			self.nelyric('The Noobe looked at me',145.7,117,'#f980ff')
			self.nelyric('with a smile on his face,',146.8,118,'#f980ff')
			self.nelyric('I sighed and thought',148,119,'#f980ff')
			self.nelyric('\"I\'m glad we\'re out of that place.\"',148.8,120,'#f980ff')
			
			self.nelyric('The Noobe yawned and fell asleep in my arms,',152,121,'#f980ff') 
			self.nelyric('and that\'s rescued Noobe safe from harm.',156.2,122,'#f980ff')
			self.endl(158,123,self.lyriclist)
			if self.pt > 158 and self.pt < 158.5:
				self.lyriclist.clear()
				
			self.pn('Noobe',158.5,124,'#ffc280',800,1)
			self.pn('Pumpkin',159.4,125,'#ffc280',800,1)
			self.pn('Soup',160.2,126,'#ffc280',800,1)
			self.nelyric('That\'s where I found my noobe.',161.2,127,'#f980ff')
			self.pn('Noobe',162.5,128,'#ffc280',800,1)
			self.pn('Pumpkin',163.7,129,'#ffc280',800,1)
			self.pn('Soup',164.4,130,'#ffc280',800,1)
			self.nelyric('You Noobe.',166.5,131,'#f980ff')
			self.pn('Noobe',166.9,132,'#ffc280',800,1)
			self.pn('Pumpkin',167.5,133,'#ffc280',800,1)
			self.pn('Soup',168.4,134,'#ffc280',800,1)
			self.nelyric('Thats right,',169.6,135,'#f980ff')
			self.nelyric('I found my noobe',170,136,'#f980ff')
			self.pn('Noobe',170.6,137,'#ffc280',800,1)
			self.pn('Pumpkin',171.6,138,'#ffc280',800,1)
			self.pn('Soup',172.8,139,'#ffc280',800,1)
			self.endl(174,140,self.lyriclist)
			self.endl(174,141,self.lx)
			if self.pt > 174 and self.pt < 174.3:
				self.lyriclist.clear()
				self.lx.clear()
			
			
	def nelyric(self, text, exe, n, color,fonte='Chalkduster',x=200,index=0):
		if self.player1.current_time > exe and self.n == n:
			lyri = Lyrb(text,color,x,index,parent=self,fonte=fonte,fsi=20)
			self.lyriclist.append(lyri)
			self.updatelyr(self.lyriclist)
			self.n += 1
			#print(self.n)
	def pn(self, text, exe, n, color,x=200,index=0):
		if self.player1.current_time > exe and self.n == n:
			lyri = Lyrb(text,color,x,index,parent=self,fonte='Papyrus',fsi=28)
			self.lx.append(lyri)
			self.updatelyr(self.lx)
			self.n += 1;
	def witchp(self, img, exe, n, color):
		if self.player1.current_time > exe and self.n == n:
			lyri = Syrb(img,parent=self,color=color,size=(28,28))
			self.lyriclist.append(lyri)
			self.updatelyr(self.lyriclist)
			self.n += 1;
	def prnp(self, img, exe, n, color):
		if self.player1.current_time > exe and self.n == n:
			lyri = Syrb(img,parent=self,color=color,size=(28,28))
			self.lx.append(lyri)
			self.updatelyr(self.lx)
			self.n += 1;
	def endl(self, exe, n,list):
		if self.player1.current_time > exe and self.n == n:
			self.n += 1
			for i in list:
				i.run_action(A.fade_to(0,1))
				i.run_action(A.sequence(A.move_by(0,100,1,TIMING_EASE_IN)))
	def cuti(self):
		if self.cut == False:
			self.newbg = SpriteNode('Other img/background1.png',size=(1080,730),z_position=-1,position=(self.size.w/2,self.size.h/2),parent=self)
			self.effectg2.remove_from_parent()
			self.titleso.remove_from_parent()
			self.ground.texture = Texture('Other img/floor.png')
			self.ground2.texture = Texture('Other img/floor.png')
			self.backg.texture = Texture('Other img/ bg1.png')
			self.backg2.texture = Texture('Other img/ bg1.png')
			self.cut = True
if __name__ == '__main__':
	run(MyScene(), show_fps=True,anti_alias=False)

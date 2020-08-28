from graphics import *
import random
from time import *
import os
QuestionsCorrect=0
NumOfQAnswered=1
 
#--------------------------------------------------------------------------------------------------------------------------        
class HomePage():

    def __init__():
        self.UserName=''
        self.Score=''
        self.Grade=''
    
    def HomePageMain(self,):
        Bar=Rectangle(Point(0,150),Point(610,200))
        Bar.setFill('orange')
        Bar.draw(Homewindow)
        
        Bar=Rectangle(Point(0,30),Point(610,80))
        Bar.setFill('orange')
        Bar.draw(Homewindow)
        
        LogoText=Text(Point(300,120),'MATHS FUN')
        LogoText.setFace('courier')
        LogoText.setStyle('bold')
        LogoText.setSize(34)
        LogoText.draw(Homewindow)
        
        EntryText1=Text(Point(80,350),'Username:')
        EntryText1.setSize(15)
        EntryText1.draw(Homewindow)
        
        EntryText2=Text(Point(80,430),'Password:')
        EntryText2.setSize(15)
        EntryText2.draw(Homewindow)
        
        Button=Rectangle(Point(50,500),Point(130,550))
        Button.setFill('orange')
        Button.draw(Homewindow)
        LoginText=Text(Point(90,525),'LOG IN')
        LoginText.draw(Homewindow)

        Button1=Rectangle(Point(180,500),Point(260,550))
        Button1.setFill('orange')
        Button1.draw(Homewindow)
        SignUpText=Text(Point(220,525),'SIGN UP')
        SignUpText.draw(Homewindow)
        AnswerBox1=Entry(Point(230,350),15)
        AnswerBox1.setFill('white')
        AnswerBox1.setSize(18)
        AnswerBox1.draw(Homewindow)

        AnswerBox2=Entry(Point(230,430),15)
        AnswerBox2.setFill('white')
        AnswerBox2.setSize(18)
        AnswerBox2.draw(Homewindow)
        Details=[]
        validLogin=False
        
        while validLogin==False:
            print(validLogin)
            k=Homewindow.getMouse()
            X=int(k.getX())
            Y=int(k.getY())
            LoopCount=0
            self.UserName=''
            print('X:',X)
            print('Y:',Y)
            if (X>=50 and X<=130) and (Y>=500 and Y<=550):
                validLogin,Details=self.GetEnterBoxInfo(self,AnswerBox2,AnswerBox1,validLogin)
                print(validLogin)
                
            elif (X>=180 and X<260) and (Y>=500 and Y<=550):
                self.UserSignUp(self)
        self.UserName=Details[0]
        self.Score=Details[1]
        print(self.Score)
        try:
            int(self.Score)
        except:
            print('')
        self.Grade=Details[2]
        Homewindow.close()
            
    def GetEnterBoxInfo(self,AnswerBox2,AnswerBox1,validLogin):
     
        NameStore=[[],[],[]]
        PasswordStore=[[],[],[]]
        ScoreStore=[[],[],[]]
        GradeStore=[[],[],[]]

        UserName=AnswerBox1.getText()
        Password=AnswerBox2.getText()
        UserInfo=open('Userinfo.txt','r')
        x=UserInfo.read()
        
        
        NameComplete=False
        PasswordComplete=False
        ScoreComplete=False
        GradeComplete=False
        Completed=0
        Accounts=0
        for char in x:
            if char==';' :
                Completed+=1
            if char==':':
                Accounts+=1
                Completed=0
               
            if char !=';' and char!=':' and char!='\n' and Completed==0:
                NameStore[Accounts]+=char
                #print('NameStore:',NameStore[Accounts])
                NameStore.append([])
            if char !=';' and char!=':' and  Completed==1:
                PasswordStore[Accounts]+=char
                #print('PasswordStore:',PasswordStore[Accounts])
                PasswordStore.append([])
            if char !=';' and char!=':'  and Completed==2:
                ScoreStore[Accounts]+=char
                #print('ScoreStore:',ScoreStore[Accounts])
                ScoreStore.append([])
            if char !=';' and char!=':' and  Completed==3:
                GradeStore[Accounts]+=char
                #print('GradeStore:',GradeStore[Accounts])
                GradeStore.append([])
    
        y=NameStore[5]
        AllPasswords=[]
        allNames=[]
        AllScore=[]
        AllGrades=[]
        
        for cycle in NameStore:
            f=''
            for count in range(len(cycle)):
                f=f+cycle[count]
            allNames.append(f)
        print(allNames)
          
        for cycle in PasswordStore:
            f=''
            for count in range(len(cycle)):
                f=f+cycle[count]
            AllPasswords.append(f)
        print(AllPasswords)

        for cycle in ScoreStore:
            f=''
            for count in range(len(cycle)):
                f=f+cycle[count]
            AllScore.append(f)
        print(AllScore)
        for cycle in GradeStore:
            f=''
            for count in range(len(cycle)):
                f=f+cycle[count]
            AllGrades.append(f)
        print(AllGrades)
        
        loops=0
        Matches=0
        UserName=AnswerBox1.getText()
        Password=AnswerBox2.getText()
        for count in allNames:
            loops+=1
            if UserName==count and UserName!='':
                Matches+=1
                
                for count2 in AllPasswords:
                    print(count2)
                    if Password==count2:
                        print('hello')
                        validLogin=True
                        
                        Score=AllScore[loops-1]
                        Grade=AllGrades[loops-1]
                        Details=[]
                        Details.append(UserName)
                        Details.append(Score)
                        Details.append(Grade)
                        print(Details)
                        
                        return validLogin,Details
                    
        if Matches<2:
            t=Text(Point(400,550),'Invalid UserName or Password')
            t.setFill('red')
            t.setStyle('bold')
            t.draw(Homewindow)
            UserName=''
            return validLogin,UserName
                        
                    
    def UserSignUp(self):
        
        Signwin=GraphWin('Sign up',450,400)
        Signwin.setBackground('turquoise')
        
        AnswerBox1=Entry(Point(180,100),15)
        AnswerBox1.setFill('white')
        AnswerBox1.draw(Signwin)
        t=Text(Point(60,100),'UserName:')
        t.draw(Signwin)

        AnswerBox2=Entry(Point(180,200),15)
        AnswerBox2.setFill('white')
        AnswerBox2.draw(Signwin)
        t=Text(Point(60,200),'Password:')
        t.draw(Signwin)
    
        Button=Rectangle(Point(50,310),Point(130,350))
        Button.setFill('orange')
        Button.draw(Signwin)
        t=Text(Point(90,330),'Finish')
        t.draw(Signwin)


        NameStore=[[],[],[]]
        PasswordStore=[[],[],[]]
        ScoreStore=[[],[],[]]
        GradeStore=[[],[],[]]
        

        self.GetInfo(self,AnswerBox1,AnswerBox2)


        valid=False
        while valid==False:
             k=Signwin.getMouse()
             X=int(k.getX())
             Y=int(k.getY())
             if (X>=50 and X<=130) and (Y>=310 and Y<=350):
                 
                 UserName=AnswerBox1.getText()
                 Password=AnswerBox2.getText()
                 for count in PasswordStore:
                     if UserName!=NameStore:
                         valid=True
                         

                 UserInfo=open('UserInfo.txt','a')
                 UserInfo.write(UserName+';'+Password+';0;5:\n')
                 UserInfo.close()

    def GetInfo(self,AnswerBox1,AnswerBox2):
        NameStore=[[],[],[]]
        PasswordStore=[[],[],[]]
        ScoreStore=[[],[],[]]
        GradeStore=[[],[],[]]
        
        UserName=AnswerBox1.getText()
        Password=AnswerBox2.getText()
        UserInfo=open('Userinfo.txt','r')
        x=UserInfo.read()
        UserInfo.close()
        
        NameComplete=False
        PasswordComplete=False
        ScoreComplete=False
        GradeComplete=False
        Completed=0
        Accounts=0

        for char in x:
            if char==';' :
                Completed+=1
            if char==':':
                Accounts+=1
                Completed=0
               
            if char !=';' and char!=':' and char!='\n' and Completed==0:
                NameStore[Accounts]+=char
                print('NameStore:',NameStore[Accounts])
                NameStore.append([])
            if char !=';' and char!=':' and  Completed==1:
                PasswordStore[Accounts]+=char
                print('PasswordStore:',PasswordStore[Accounts])
                PasswordStore.append([])
            if char !=';' and char!=':'  and Completed==2:
                ScoreStore[Accounts]+=char
                print('ScoreStore:',ScoreStore[Accounts])
                ScoreStore.append([])
            if char !=';' and char!=':' and  Completed==3:
                GradeStore[Accounts]+=char
                print('GradeStore:',GradeStore[Accounts])
                GradeStore.append([])
  
        
             
                
                     
#--------------------------------------------------------------------------------------------------------------------------------
        
AlgebraTopics=['Quadratic equation','NthTerm']
ShapeTopics=['Pythagerous','Circumeference','Area of circles','Area of other shapes']
NumberTopics=['Fractional addition','Fractional multiplication','Conversion']

#-------------------------------------------------------------------------------------------------------------------------------        
class Student(HomePage):
    
    def __init__(self,Username,Score,Grade):
        
        self.Username=Username
        self.Grade=''                            ''
        self.Percentage=50
        print(self.Percentage)
        self.Score=Score
        self.TotalCorrect=0

    def UpdateScore(self,TotalCorrect):
        try:
            self.Score=int(self.Score)
        except:
            print('Fail')
        print(NumOfQAnswered)
        self.Score+=self.TotalCorrect
        print('elephant')
        print(self.TotalCorrect)     

    def UpdateGrade(self):
        if self.Percentage<=40:
            self.Grade='4'
            if self.Percentage<=50:
                self.Grade='5'
                if self.Percentage<=60:
                    self.Grade='6'
                    if self.Percentage<=70:
                        self.Grade='7'
                        if self.Percentage<=80:
                            self.Grade='8'
                            if self.Percentage<=90:
                                self.Grade='9'
        else:
            self.Grade='3'

    def UpdatPercent(self):
         self.Percentage=QuestionsCorrect/NumOfQAnswered
         UpdateGrade(self)
         UpdateInfo(self)
           
            
        

#--------------------------------------------------------------------------------------------------------------------------------        
class Question(Student):

    def __init__(self,score,Percentage):
        #initiates Question classs assigning attributes 
        self.Topic='Nth Term'
        self.UserAnswers=[[],[],[],[],[]]
        self.Questions=[[None,None,None,None,None,],
                        [None,None,None,None,None,],
                        [None,None,None,None,None,],
                        [None,None,None,None,None,],
                        [None,None,None,None,None,]]
        self.NumOfQAnswered=0
        self.QuestionsCorrect=0
        self.Category=''
        
        self.CorrectAnswer=[[],[],[],[],[]]
        
  
    def DisplayGenerateQuestion(self):
        #this method display questions generated in other methods
        #All topic are displayed sing this function
    
        
        try:
            AnswerBoxes=[[],[],[],[],[]]
            
            if self.Category=='Algebra': 
                if self.Topic==2:
                    QuestionWin=GraphWin("NthTerm",600,400)
                    QuestionWin.setBackground('turquoise')
                    self.NthTerm()

                elif self.Topic==1:
                    QuestionWin=GraphWin('Quadratic equations',600,400)
                    QuestionWin.setBackground('turquoise')
                    self.QuadEquation()
                    
                    
            if self.Category=='Numbers':
                
                if self.Topic==1:
                    QuestionWin=GraphWin("Fractional addition",600,400)
                    QuestionWin.setBackground('turquoise')
                    self.FractionalAddition()

                elif self.Topic==2:
                    QuestionWin=GraphWin("Multiplication",600,400)
                    QuestionWin.setBackground('turquoise')
                    self.Mutiplication()
                    
            if self.Category=='Geometry':
                
                if self.Topic==2:
                    QuestionWin=GraphWin("Circumference",600,400)
                    QuestionWin.setBackground('turquoise')
                    self.Circumference()
                    
                elif self.Topic==3:
                    QuestionWin=GraphWin("CircleArea",600,400)
                    QuestionWin.setBackground('turquoise')
                    self.CircleArea()
            
                elif self.Topic==4:
                    QuestionWin=GraphWin('Area of shape',600,400)
                    QuestionWin.setBackground('turquoise')
                    self.AreasOfshapes()
                    
                elif self.Topic==1:
                    QuestionWin=GraphWin('pythagerous',600,400)
                    QuestionWin.setBackground('turquoise')
                    self.Pythagerous()
                    
            for QuestionNum in range(5):
                AnswerBoxes[QuestionNum]=Entry(Point(45,(QuestionNum+1)*50),6)
                AnswerBoxes[QuestionNum].setFill('white')
                AnswerBoxes[QuestionNum].draw(QuestionWin)
                
                EnterButton=Rectangle(Point(15,340),Point(70,370))
                EnterButton.setFill('orange')
                EnterButton.draw(QuestionWin)
                
                Entertext=Text(Point(38,357),'ENTER')
                Entertext.setSize(8)
                Entertext.draw(QuestionWin)
                
                DisplayNthQ=Text(Point(320,(QuestionNum+1)*50),self.Questions[QuestionNum])
                DisplayNthQ.setSize(10)
                DisplayNthQ.draw(QuestionWin)
               

            k=QuestionWin.getMouse()
            X=int(k.getX())
            Y=int(k.getY())
            valid=False
            LoopCount=0
            
                           
            UsersInput=[[],[],[],[],[]]
            while valid==False:
                k=QuestionWin.getMouse()
                X=int(k.getX())
                Y=int(k.getY())
                count=+1
                for count in range(5):
                    self.UserAnswers[count]=AnswerBoxes[count].getText()
                print(self.UserAnswers)

                
                if  (X>=15 and X<=70) and (Y>=340 and Y<=370):
                    print(self.UserAnswers[count])
                    valid=True
                          
            QuestionWin.close()
            self.CheckAnswersAndMark()
        except:
            print('hello')
    def CheckAnswersAndMark(self):
        
        #this loads the window that will show the user what they got wrong 
        CheckWin=GraphWin('Answer check and correction',600,400)
        CheckWin.setBackground('turquoise')
        
        BottomBar=Rectangle(Point(0,350),Point(610,410))
        BottomBar.setFill('orange')
        BottomBar.draw(CheckWin)
        for count in range(5):
           
            QuestionNum=Text(Point(20,((count+1)*60)-20),'Q'+str(count+1)+')')
            QuestionNum.draw(CheckWin)
            CheckedQtxt=Text(Point(300,((count+1)*60)-20),self.Questions[count])
            CheckedQtxt.draw(CheckWin)
            print(self.CorrectAnswer[count])
            CorrectAnswerTxt=Text(Point(300,((count+1)*60)),self.CorrectAnswer[count])
            CorrectAnswerTxt.draw(CheckWin)
            
            UserAnswerTxt=Text(Point(300,((count+1)*60)+20),str(self.UserAnswers[count]))
            UserAnswerTxt.setFill('yellow')
            UserAnswerTxt.draw(CheckWin)
            print(self.UserAnswers,'\n',self.CorrectAnswer)
            
            #checks if the users answer and the correct answer match
            if self.UserAnswers[count]==self.CorrectAnswer[count]:

                Tick=Text(Point(490,((count+1)*60)-20),'y')
                print('1')
                Tick.setFill('red')
                print('2')
                Tick.draw(CheckWin)
                print('3')
                self.NumOfQAnswered=+1
                print('4')
                self.TotalCorrect=+1
    
                
            elif self.UserAnswers!=self.CorrectAnswer:
                print('X')
                 
                    
    def NthTerm(self):
        
        print('hello')
    
        Temporary=['','','','','']
        for QuestionNum in range(5):
            #Generates the NthTerm sequence
            A=random.randint(-10,+10)
            B=random.randint(-10,+10)
            
            for count in range(5):
                NthSequence=str((A*(count+1))+B)
                Temporary[count]=NthSequence
                self.Questions[QuestionNum][count]=NthSequence
                
                
        
            #comes up with a correct answer for the sequence    
            if B<0:
                NthTerm=(str(A)+'n'+str(B))
            else:
                NthTerm=(str(A)+'n+'+str(B))
            self.CorrectAnswer[QuestionNum]=NthTerm
        print(self.CorrectAnswer)
    
        return self

         
    def FractionalAddition(self):
        for count in range(5):
            #randomly the numeraters and denominaters
            Numerater1=random.randint(1,10)
            Numerater2=random.randint(1,10)

            Denominater1=random.randint(1,10)
            Denominater2=random.randint(1,10)
            print(Numerater1,Numerater2,'\n____________________')
            print(Denominater1,Denominater2,'\n')
            #finds the common the denominater and multiplies the numerater

            Temp=Denominater1
            Denominater1Calc=Denominater1*Denominater2
            Numerater1Calc=Numerater1*Denominater2
            Denominater2Calc=Temp*Denominater2
            Numerater2Calc=Numerater2*Temp
            print(Numerater1Calc,Numerater2Calc,'\n_______________________')
            print(Denominater1Calc,Denominater2Calc)
            #adds the numeraters together

            AddedNumerater=Numerater2Calc+Numerater1Calc
            print(AddedNumerater,'\n_______________________')
            print(Denominater1Calc)

            self.Questions[count]=(str(Numerater1)+'/'+str(Denominater1)+' + '+str(Numerater2)+'/'+str(Denominater2))
            print(self.Questions)
            self.CorrectAnswer[count]=str(AddedNumerater)+' / '+str(Denominater2Calc)

    def Mutiplication(self):
        for count in range(5):
            NumberA=random.randint(-20,40)
            NumberB=random.randint(-10,10)
            self.CorrectAnswer[count]=str(NumberA*NumberB)
            self.Questions[count]=str(NumberA)+' x '+str(NumberB)

    def Pythagerous(self):
        for count in range(5):
            Hypotanouse=random.randint(8,20)
            OtherSideB=random.randint(1,15)
            OtherSideA=random.randint(1,15)
            
            while(OtherSideA>=Hypotanouse) or (OtherSideB>=Hypotanouse):
                
                OtherSideA=random.randint(1,15)
                OtherSideB=random.randint(1,15)
            Choice=random.randint(1,2)
            
            if Choice==1:
                print('hello')
                self.Questions[count]='Calculate The Value of SideA: B=',str(OtherSideB),'Hypotanouse='+str(Hypotanouse)
                self.CorrectAnswer[count]=round((((Hypotanouse**2)-(OtherSideA**2))**0.5),3)
                
            elif Choice==2:
                self.CorrectAnswer[count]=((OtherSideB**2)+(OtherSideA**2))**0.5
                self.Questions[count]='Calculate','The', 'Value', 'of', 'hypotanouse:','B=',str(OtherSideB),'A='+str(OtherSideA)

                
    def Circumference(self):
        for count in range(5):
            size=0
            PI=3.16
            QuestionType=''
            ChoiceList=['Radius','Diameter']
            RadOrDiam=random.choice(ChoiceList)
            Size=random.randint(2,20)
            Size=random.randint(3,50)
            print(QuestionType)
            self.Questions[count]='Circle with ',RadOrDiam,'of',str(Size)+'CM'
            if RadOrDiam=='Radius':
                self.CorrectAnswer[count]=round(((Size*2)*PI),3)
                print((Size*2)*PI)
            elif RadOrDiam=='Diameter':
                print(Size*PI)
                self.CorrectAnswer[count]=round(Size*PI,3)

    def CircleArea(self):
        for count in range(5):
            size=0
            PI=3.16
            QuestionType=''
            ChoiceList=['Radius','Diameter']
            RadOrDiam=random.choice(ChoiceList)
            Size=random.randint(3,50)
            print(QuestionType)
            self.Questions[count]='A Circle with',RadOrDiam,'of',str(Size)+'CM.' 
            if RadOrDiam=='Radius':
                self.CorrectAnswer[count]=round(((Size**2)*PI),3)
                print((Size**2)*PI)
            elif RadOrDiam=='Diameter':
                print(((Size/2)**2)*PI)
                self.CorrectAnswer[count]=round(((Size/2)**2)*PI,3)

    def AreasOfshapes(self):
        for count in range(5):
            
            Shapes=['Rectangle','Triangle','Cube']
            ShapeChoice=random.choice(Shapes)
            ShapeSizeY=random.randint(5,70)
            ShapeSizeX=random.randint(5,70)
            ShapeSizeZ=random.randint(5,70)
            
            if ShapeChoice =='Rectangle':
                self.CorrectAnswer[count]=ShapeSizeX*ShapeSizeY
                self.Questions[count]='Square: X-axis='+str(ShapeSizeX)+' ,Y-axis='+str(ShapeSizeY)
                
            elif ShapeChoice=='Triangle':
                self.CorrectAnswer[count]=(ShapeSizeX*ShapeSizeY)/2
                self.Questions[count]='Triangle: X-axis='+str(ShapeSizeX)+' ,Y-axis='+str(ShapeSizeY)
                
            elif ShapeChoice=='Cube':
                self.CorrectAnswer[count]=ShapeSizeX*ShapeSizeY*ShapeSizeY
                self.Questions[count]='Cubeoid: X-axis='+str(ShapeSizeX)+' ,Y-axis='+str(ShapeSizeY)+' ,Z-axis='+str(ShapeSizeZ)

    def Conversion(self):
        ConversionTopic=['mass''volume','converion']
        Topic=random.choice(ConversionTopc)

        if Topic=='mass':
            for count in range(5):
                Units=['pounds','ounces','kilogram',]
                ConvertFrom=random.choice(Units)
                ConvertTo=random.choice(Units)
                while ConvertFrom==ConvertTo:
                    ConvertTo=random.choice(Units)
                    
                if ConverFrom=='pounds':
                    if ConvertTo=='ounces':
                        Value=random.randint(2,20)
                        self.CorrectAnswer[count]=Value*16
                    elif ConvertTo=='kilogram':
                        Value=random.randint(2,20)
                        self.CorrectAnswer[count]=Value*0.45
                    elif ConvertTo=='gram':
                        Value=random.randint(2,20)
                        self.CorrectAnswer[count]=Value*453.5
                        
                elif ConvertFrom=='ounces':
                    if ConvertTo == 'pounds':
                        Value=random.randint(3,15)
                        self.CorrectAnswer[count]=Value/16
                    elif ConvertTo=='kilogram':
                        Value=random.randint(3,15)
                        self.CorrectAnswer[count]=Value*(0.0283)
                   

                elif ConvertFrom=='kilograms':
                    if ConvertTo == 'pound':
                        Value=random.randint(3,15)
                        self.CorrectAnswer[count]=Value*2.2
                    elif ConvertTo=='ounces':
                        Value=random.randint(3,15)
                        self.CorrectAnswer[count]=Value*(0.0283)
        elif Topic=='volume':
            print('Not Complete')

                
                             
#-------------------------------------------------------------------------------------------------------                

class Connect4():
    def __init__ (self):
        self.Board = [['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','','']]

    def DrawBoard(win,self):
        for cycle1 in range(8):
            for cycle2 in range(8):
                c=Circle(Point(25+cycle1*50,25+cycle2*50),20)
                if self.Board[cycle1][cycle2]=='':
                    c.setFill('white')
                else:
                    c.setFill(self.Board[cycle1][cycle2])
                c.draw(win)

                
    def GetPosition(win,self):
        valid = False
        while not valid:
            p=win.getMouse()
            cycle1 = p.getX()//50
            for z in range(7,-1,-1):
                if self.Board[cycle1][z]=='':
                    valid=True
                    break
        return cycle1,z
                
    def ClearBoard(self):
        for cycle1 in range(8):
            for cycle2 in range(8):
                self.Board[cycle1][cycle2] = ''

    def CheckWin(self,c):
        won=False
        # horizontal
        for cycle1 in range(5):
            for cycle2 in range(8):
                if self.Board[cycle1][cycle2]==c:
                    if self.Board[cycle1+1][cycle2]==c:
                        if self.Board[cycle1+2][cycle2]==c:
                            if self.Board[cycle1+3][cycle2]==c:
                                won=True
        # vertical
        for cycle1 in range(8):
            for cycle2 in range(5):
                if self.Board[cycle1][cycle2]==c:
                    if self.Board[cycle1][cycle2+1]==c:
                        if self.Board[cycle1][cycle2+2]==c:
                            if self.Board[cycle1][cycle2+3]==c:
                                won=True
        # diagonal
        for cycle1 in range(0,5):
            for cycle2 in range(0,5):
                if self.Board[cycle1][cycle2]==c:
                    if self.Board[cycle1+1][cycle2+1]==c:
                        if self.Board[cycle1+2][cycle2+2]==c:
                            if self.Board[cycle1+3][cycle2+3]==c:
                                won=True
        for cycle1 in range(0,5):
            for cycle2 in range(3,8):
                if self.Board[cycle1][cycle2]==c:
                    if self.Board[cycle1+1][cycle2-1]==c:
                        if self.Board[cycle1+2][cycle2-2]==c:
                            if self.Board[cycle1+3][cycle2-3]==c:
                                won=True
        return won

    def Connect4Main(self):
        print('hello')
        win = GraphWin("Connect 4", 400, 450)
        win.setBackground('yellow')
        play=True
        self.Board = [['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','',''],
                     ['','','','','','','','']]
        while play==True:
           
            self.ClearBoard(self)
            moves = 0
            drawn = False
            won = False
            colour='red'
            r=Rectangle(Point(10,410),Point(390,440))
            r.setFill('white')
            r.draw(win)
            r=Rectangle(Point(15,415),Point(35,435))
            r.setFill(colour)
            r.draw(win)
            t=Text(Point(85,425),'to move')      
            t.setSize(18)
            t.draw(win)
            self.DrawBoard(win,self)
            
            while not drawn and not won:
                
                cycle1,cycle2=self.GetPosition(win,self)
                moves+=1
                self.Board[cycle1][cycle2]=colour
                self.DrawBoard(win,self)
                won=self.CheckWin(self,colour)
                if moves==64:
                    drawn=True
                if colour=='red':
                    colour='green'
                else:
                    colour='red'
                r=Rectangle(Point(15,415),Point(35,435))
                r.setFill(colour)
                r.draw(win)
            r=Rectangle(Point(10,410),Point(390,440))
            r.setFill('white')
            r.draw(win)
            if colour=='red':
                colour='green'
            else:
                colour='red'
            if won:
                r=Rectangle(Point(15,415),Point(35,435))
                r.setFill(colour)
                r.draw(win)
                t=Text(Point(65,425),'wins')      
                t.setSize(18)
                t.draw(win)
            else:
                t=Text(Point(90,425),'Game drawn')      
                t.setSize(18)
                t.draw(win)
            play=False
       
    
                 
#---------------------------------------------------------------------------------------------------------------------------                  
class MatchTheTiles():
  def __init__(self):
    self.Tiles=[[1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1]]
    
  def Main(self):
    self.Tiles=[[1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1]]

    self.Grid= [[1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1]]
  
    win=GraphWin('Maths aided learning',400,450)
    win.setBackground('white')

    Y_AxisEnd=0
    TileEnd=50
    X_AxisEnd=-50
    
    for count in range(8):
        TileEnd=50
        X_AxisEnd+=50
        for count1 in range(8):
            self.Tiles[count][count1]=Rectangle(Point(X_AxisEnd,Y_AxisEnd-5),Point((X_AxisEnd+50),TileEnd))
            
            self.Tiles[count][count1].draw(win)
            TileEnd+=50
        TileTurnsBar=Rectangle(Point(0,450),Point(400,400))
        TileTurnsBar.setFill('yellow')

    #loads all the images
    ImageList=[]
    list2=[]
    Clicks=0
    for Xposition in range(8):
        for Yposition in range(8):

            for file in os.listdir("/images/"):
                if file.endswith(".gif"):
                    ImageList.append(('/images/'+file))

            File=random.choice(ImageList)
            ImageListLen=len(ImageList)
            
            for count in ImageList:
                if count==File:
                    ImageList.remove(File)
                    list2.append(File)
            

            if self.Grid[Xposition][Yposition]==1:
                self.Tiles[Xposition][Yposition]=Image(Point(50*Xposition+25,(50*Yposition+25)),File)
                #self.Tiles[Xposition][Yposition].draw(win)
                self.Grid[Xposition][Yposition]=File
          
          
       
            valid=False    
            while valid==False:
                Number1=random.randint(0,7)
                Number2=random.randint(0,7)
               
                if self.Grid[Number1][Number2]==1:
                    self.Tiles[Number1][Number2]=Image(Point(50*Number1+25,(50*Number2+25)),File)
                    self.Grid[Number1][Number2]=File
                    #self.Tiles[Number1][Number2].draw(win)
                    
                     
                   
                    valid=True
                if self.Grid[Number1][Number2]!=1:
                    valid=True
                     
                                
           
    Matches=0        
    for count in range(1000000):
        click=win.getMouse()
        X_click=int(click.getX())
        Y_click=int(click.getY())
        Xposition=int(str(X_click//50))
        Yposition=int(str(Y_click//50))
        print('X:',Xposition)
        print('Y:',Yposition,'\n----------------------------------------')
        
        try:
            self.Tiles[Xposition][Yposition].draw(win)
            
            click=win.getMouse()
            X_click=int(click.getX())
            Y_click=int(click.getY())

            Xposition2=int(str(X_click//50))
            Yposition2=int(str(Y_click//50))

            self.Tiles[Xposition2][Yposition2].draw(win)

            if self.Grid[Xposition2][Yposition2]==self.Grid[Xposition][Yposition]:
                self.Grid[Xposition2][Yposition2]='empty'
                self.Grid[Xposition][Yposition]='empty'
                self.Tiles[Xposition][Yposition].undraw()
                self.Tiles[Xposition][Yposition]=Rectangle(Point((Xposition*50),(Yposition*50)),Point((Xposition*50)+50,(Yposition*50)+50))
                self.Tiles[Xposition][Yposition].setFill('red')
                self.Tiles[Xposition][Yposition].draw(win)
                self.Tiles[Xposition2][Yposition2]=Rectangle(Point((Xposition2*50),(Yposition2*50)),Point((Xposition2*50)+50,(Yposition2*50)+50))
                self.Tiles[Xposition2][Yposition2].setFill('red')
                self.Tiles[Xposition2][Yposition2].draw(win)

                

                CountTurns=Text(Point(400,450),str(count+1))
                CountTurns.setFill('Pink')

                self.Tiles[Xposition2][Yposition2]=0
                self.Tiles[Xposition][Yposition]=0
                
                CountTurns.draw(win)
                print('Match Found')
            
            for count in range(8):
                for count1 in range(8):
                    if self.Grid[count][count1]=='empty':
                        Matches=+2
            if Matches==32:
                FinishedWin=GraphWin('Winnerrrr!!!',250,100)
                FinishedWin.setBackground('turquoise')
                
                FinishedText=Text(Point(125,50),'Winner!!!')
                FinishedText.draw(FinishedWin)
                
                FinishedWin.getMouse()
                FinishedWin.close()
                win.close()
                return
            else:
                sleep(2)
                self.Tiles[Xposition][Yposition].undraw()
                self.Tiles[Xposition2][Yposition2].undraw()
                print('No Match Found')
                CountTurns=Text(Point(450,500),str(count+1))
                CountTurns.setFill('Pink')
                CountTurns.draw(win)
            
        except:
            print('object already drawn')
            self.Tiles[Xposition][Yposition].undraw()
        
#-------------------------------------------------------------------------------------------------------------------------------
def MainPage(Mainwindow):
    #creates the main page for the program
    DrawHeader(Mainwindow)
    sideBar(Mainwindow)
    drawBars(Mainwindow)
    DrawCatergories(Mainwindow,AColour,NColour,GColour)
    Drawtopic(Mainwindow)
    slideshowbtn(Mainwindow)
   
   
    
AlgebraTopics=['Quadratic equation','NthTerm']
ShapeTopics=['Pythagerous','Circumeference','Area of circles','Area of other shapes']
NumberTopics=['Fractional addition','Fractional multiplication','Conversion','Multiplication']
    
def Drawtopic(Mainwindow):
    if Question.Category=='Algebra':
        loop=1
        x=''
        for count in AlgebraTopics:
            print(count)
            TopicsDisplayed=Text(Point(350,(115+(45*loop))),count)
            TopicsDisplayed.setSize(12)
            TopicsDisplayed.draw(Mainwindow)
            loop+=1
            
    elif Question.Category=='Numbers':
        loop=1
        x=''
        for count in NumberTopics:
            print(count)
            TopicsDisplayed=Text(Point(350,(115+(45*loop))),count)
            TopicsDisplayed.setSize(12)
            TopicsDisplayed.draw(Mainwindow)
            loop+=1
            
    elif Question.Category=='Geometry':
        loop=1
        x=''
        for count in ShapeTopics:
            print(count)
            TopicsDisplayed=Text(Point(350,(115+(45*loop))),count)
            TopicsDisplayed.setSize(12)
            TopicsDisplayed.draw(Mainwindow)
            
            loop+=1
    
           
def DrawHeader(Mainwindow):

    #draws the header#
    DeaderRect1=Rectangle(Point(0,0),Point(600,60))
    DeaderRect1.setFill('turquoise')
    DeaderRect1.setOutline('black')
    DeaderRect1.draw(Mainwindow)

    DeaderRect2=Rectangle(Point(150,0),Point(420,60))
    DeaderRect2.setFill('white')
    DeaderRect2.setOutline('black')
    DeaderRect2.draw(Mainwindow)

    HeaderText=Text(Point(70,45),'maths fun')
    HeaderText.setSize(20)
    HeaderText.setFace('arial')
    HeaderText.setStyle('bold')
    HeaderText.setFill('orange')
    HeaderText.draw(Mainwindow)
   
def sideBar(Mainwindow):
    #draw side bar
    SideBarRect1=Rectangle(Point(0,70),Point(150,700))
    SideBarRect1.setFill('turquoise')
    SideBarRect1.setOutline('black')
    SideBarRect1.draw(Mainwindow)
    
    SideBarRect2=Rectangle(Point(150,70),Point(700,700))
    SideBarRect2.setFill('turquoise')
    SideBarRect2.setOutline('black')
    SideBarRect2.draw(Mainwindow)
    
    SideBarRect3=Rectangle(Point(150,660),Point(0,540))
    SideBarRect3.setFill('white')
    SideBarRect3.setOutline('black')
    SideBarRect3.draw(Mainwindow)

    for count in range(4):
        Game=Rectangle(Point(150,(55*(count+1))+70),Point(0,(55*(count+1))+125))
        Game.setFill('orange')
        Game.setOutline('black')
        Game.draw(Mainwindow)
        
    t=Text(Point(75,152),'Connect4: 10 points')
    t.draw(Mainwindow)
    t.setSize(10)
    t=Text(Point(75,200),'MineSweeper: 20 points')
    t.setSize(10)
    t.draw(Mainwindow)
    t=Text(Point(75,257),'Match 2 tiles: 10 points')
    t.setSize(10)
    t.draw(Mainwindow)
    t=Text(Point(75,312),'Hangman: 10 points')
    t.setSize(10)
    t.draw(Mainwindow)

def drawBars(Mainwindow):
    #makes the rows
    LineTops=(530/5)-8
    LineBottom=530/6
    for count in range(5):
        LineTops+=LineBottom
        TopicBar=Rectangle(Point(150,LineTops),Point(700,LineTops-45))
        TopicBar.setFill('white')
        TopicBar.setOutline('black')
        TopicBar.draw(Mainwindow)

def drawBlueBars(Mainwindow):
    LineTops=(530/5)-8
    LineBottom=530/6
    for count in range(4):
        LineTops+=LineBottom
        TopicBar=Rectangle(Point(150,LineTops+45),Point(700,LineTops))
        TopicBar.setFill('turquoise')
        TopicBar.setOutline('black')
        TopicBar.draw(Mainwindow)
def slideshowbtn(Mainwindow):
    SlideBtn=Rectangle(Point(200,560),Point(300,610))
    SlideBtn.setFill('orange')
    SlideBtn.draw(Mainwindow)
    SlideBtnTxt=Text(Point(250,585),'lesson slides')
    SlideBtnTxt.draw(Mainwindow)

GColour='white'
NColour='white'
AColour='white'

def DrawCatergories(Mainwindow,AColour,NColour,GColour):
     CategoryR1=Rectangle(Point(150,70),Point(267,140))
     CategoryR1.setFill(AColour)
     CategoryR1.draw(Mainwindow)
     CategoryT1=Text(Point(210,105),'ALGEBRA')
     CategoryT1.draw(Mainwindow)

     CategoryR2=Rectangle(Point(267,70),Point(383,140))
     CategoryR2.setFill(NColour)
     CategoryR2.draw(Mainwindow)
     CategoryT2=Text(Point(320,105),'NUMBERS')
     CategoryT2.draw(Mainwindow)
     
     CategoryR3=Rectangle(Point(383,70),Point(500,140))
     CategoryR3.setFill(GColour)
     CategoryR3.draw(Mainwindow)
     CategoryT2=Text(Point(440,105),'GEOMETRY')
     CategoryT2.draw(Mainwindow)

#-------------------------------------------------------------------------------------------------------------------------
class SlideShow ():
    
    def PageLines(SlideWin,self):
        Page=1
       
        for count in  range(8):
            x='white'
            r=Rectangle(Point(2,(55*count)),Point(700,((1+count)*55)))
            print(count%2)
            if count%2==1:
                x='orange'
            r.setFill(x)
            r.draw(SlideWin)

        for count in  range(8):
            x='orange'
            r=Rectangle(Point(0,(55*count)),Point(50,((1+count)*55)))
            print(count%2)
            if count%2==1:
                x='white'
            r.setFill(x)
            r.draw(SlideWin)
        f=Rectangle(Point(100,475),Point(200,525))
        f.setFill('grey')
        f.draw(SlideWin)
        BtnTxt1=Text(Point(150,500),'previous')
        BtnTxt1.draw(SlideWin)
        f=Rectangle(Point(250,475),Point(350,525))
        f.setFill('grey')
        f.draw(SlideWin)
        BtnTxt1=Text(Point(300,500),'Next')
        BtnTxt1.draw(SlideWin)
        
        for count in range(1000):
            self.GetClicks(Page)
            self.SlideTopics(SlideWin,Page)

    def SlideTopics(SlideWin,Page):
        Topics=['Nth Term','Quadratic equations','Fractional addition','Fractional multiplication',
                'Pythagerous','Circumeference','Area of circles','Area of other shapes','Conversion',]
        loop=0
        if Page==1:
            for count in Topics:
                t=Text(Point(350,(loop*55)+35),count)
                t.draw(SlideWin)
                loop+=1
                if loop==8:
                    break

        elif Page==2:
            for count in Topics:
                
                if loop>=8:
                    t=Text(Point(350,((loop-8)*55)+35),count)
                    t.draw(SlideWin)
                    break
                loop+=1

    def GetClicks(SlideWin,Page):
          row=0
          f=SlideWin.getMouse()
          X_click=int(f.getX())
          Y_click=int(f.getY())
          print(X_click)
          print(Y_click)

          if Y_click<=440:
              row=Y_click//55

          elif (X_click>=100 and X_click<=200) and (Y_click<=525 and Y_click>=475):
                  Page=Page-1
          elif (X_click>=250 and X_click<=350) and (Y_click<=525 and Y_click>=475):
                  Page+=1
                
    def DisplayLnk(row,LinkList):
        
        WebLnkWin=GraphWin('',400,200)
        WebLnkWin.setBackground('yellow')
        Link=Text(Point(200,100),LinkList[row])
        Link.draw(WebLnkWin)
        
        
        
        
        
              
    def GetWebSites():
          File=open('WebPages.txt','r')
          WebPages=File.read()
          File.close()
          LinkList=['','','','','',]
          loop=0
          for count1 in range(len(temp)):
              while WebPages[loop]!='\n':
                      LinkList[count1]=LinkList[count1]+WebPages[loop]
                      loop+=1
              loop+=1
          print(temp)
        
            
              
Page=0    


#-------------------------------------------------------------------------------------------------------------------------

class MineSweeper():
     def __init__(self):
        self.Tiles=[]
        self.Grid=[]
        self.Score=0
     
     def MineSweeperMain(self):
        self.Score=0
        self.Tiles=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
       

        self.Grid=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        Minewin=GraphWin('Minesweeper',500,550)
        Minewin.setBackground('white')
        MineSweepBar=Rectangle(Point(0,555),Point(510,501))
        MineSweepBar.setFill('Yellow')
        MineSweepBar.draw(Minewin)

       
        Y_AxisEnd=0
        TileEnd=25
        X_AxisEnd=-25
        
        for count in range(20):
            TileEnd=25
            X_AxisEnd+=25
            for count1 in range(20):
                self.Tiles[count][count1]=Rectangle(Point(X_AxisEnd,Y_AxisEnd-5),Point((X_AxisEnd+25),TileEnd))
                
                self.Tiles[count][count1].draw(Minewin)
                TileEnd+=25
            TileTurnsBar=Rectangle(Point(0,450),Point(400,400))
        self.GenerateBoard(Minewin)
        self.Score+=1
        
        self.UpdateBoard(Minewin)

     def GenerateBoard(self,Minewin):
         
        for count in range(100):
            Xposition=random.randint(0,19)
            Yposition=random.randint(0,19)
            print('X:',Xposition,'\n===============================================\n','Y:',Yposition)
            if self.Grid[Xposition][Yposition]==1:
                    self.Tiles[Xposition][Yposition]=Image(Point(25*Xposition+12,(25*Yposition+12)),'Minesweep/mine.gif')
                    #self.Tiles[Xposition][Yposition].draw(Minewin)
                    self.Grid[Xposition][Yposition]='mine'
              
                    valid=False    
                    while valid==False:
                        Number1=random.randint(0,19)
                        Number2=random.randint(0,19)
                       
                        if self.Grid[Number1][Number2]==1:
                            self.Tiles[Number1][Number2]=Image(Point(25*Number1+12,(25*Number2+12)),'Minesweep/mine.gif')
                            self.Grid[Number1][Number2]='mine'
                            #self.Tiles[Number1][Number2].draw(Minewin)
                            valid=True
        print(self.Grid)

     def UpdateBoard(self,Minewin):
        x=0
        
        for count in range(1000):
            MinesNear=0
            click=Minewin.getMouse()
            X_click=int(click.getX())
            Y_click=int(click.getY())
            Xposition=int(str(X_click//25))
            Yposition=int(str(Y_click//25))

            print('X:',Xposition)
            print('Y:',Yposition,'\n----------------------------------------')

            if self.Grid[Xposition][Yposition]=='mine':
                for cycle in range(20):
                    for cycle2 in range(20):
                        if self.Grid[cycle][cycle2]=='mine':
                            
                            self.Tiles[cycle][cycle2].draw(Minewin)
                GameOver=GraphWin('GameOver',300,100)
                GameOver.setBackground('red')
                GameOverText=Text(Point(150,50),'GAMEOVER :(')
                GameOverText.setSize(30)
                GameOverText.draw(GameOver)
                GameOver.getMouse()
                Minewin.close()
                GameOver.close()
                return
            try:
                print(self.Grid[Xposition])
                if self.Grid[Xposition][Yposition+1]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition+1][Yposition]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition+1][Yposition+1]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition-1][Yposition-1]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition-1][Yposition]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition+1][Yposition-1]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition-1][Yposition+1]=='mine':
                    MinesNear+=1
                if self.Grid[Xposition][Yposition-1]=='mine':
                    MinesNear+=1
            except:
                print('Error 5')
                
        
            print(MinesNear)
            self.Grid[Xposition][Yposition]='diffused'
            MinesNearText=Text(Point((Xposition*25)+12,(Yposition*25)+12),MinesNear)
            MinesNearText.draw(Minewin)
#---------------------------------------------------------------------------------------------------------------------------            
class HangMan():
    def __init__(self):
        self.PossibleWord=['HELLO','TRIANGLE','CIRCLE','SQUARE','SUMS','FRACTIONS']
        self.Letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.Word=random.choice(self.PossibleWord)
        self.Guess='_'*len(self.Word)
        self.ImageNumber=1
   #gets the letter the user clicked on
    def getLetter(self,HangManWin):
       p=HangManWin.getMouse()
       x =int(p.getX()-25)
       y =int(p.getY())
       place=int(x//20)
       print(place)
       
       if y>=381 and y<=428:
          char=chr(65+place)
          Letters=self.Letters[:place]+' '+self.Letters[place+1:]
          self.Letters=Letters
          print(self.Letters)
       elif y>428:
          place=place+13
          print(place)
          char=chr(65+place)
          print(char)
          Letters=self.Letters[:place]+' '+self.Letters[place+1:]
          self.Letters=Letters
          
       return self ,char,Letters
       
        #updates the image
    def scaffold(ImageNumber,self,HangManWin):
        File='/HangMan/hman'+str(self.ImageNumber)+'.gif'
        print(File)
        pic=Image(Point(150,170),File)
        #pic.draw(HangManWin)
        self.ImageNumber+=1
        
        #draws the letters
    def drawLetters(self,HangManWin,Letters):
        
            print(self.Letters)
            r=Rectangle(Point(25,381),Point(45,400))
            r.setFill('pink')
            r.draw(HangManWin)
            r=Rectangle(Point(20,381),Point(281,510))
            r.setFill('green')
            r.draw(HangManWin)
            t=Text(Point(150,400),str(self.Letters[0:13]))
            t.setFace('courier')
            t.setStyle('bold')
            t.setSize(24)
            t.setFill('white')
            t.draw(HangManWin)
            t=Text(Point(150,450),self.Letters[13:26])
            t.setFace('courier')
            t.setStyle('bold')
            t.setSize(24)
            t.setFill('white')
            t.draw(HangManWin)
          
            return
       #if the user chooses the right letter it updates the guess on screen
    def updateGuess(self,char):
        for x in range(len(self.Word)):
            text=False
            if char==self.Word[x]:
                text=True
                print(text)
                print(self.Word[x])
                
                Guess=str(self.Guess[:x]+char+self.Guess[x+1:])
                print(Guess)
                self.Guess=Guess
        return  self.Guess
          #draw the guess every turn      
    def drawGuess(self,HangManWin):
       
        GuessText=Text(Point(120,360),self.Guess)
        GuessText.setFace('courier')
        GuessText.setStyle('bold')
        GuessText.draw(HangManWin)
     
        print(self.Guess)
        
        return

    def getWord(self):
       self.PossibleWord=['HELLO','TRIANGLE','CIRCLE','SQUARE','SUMS','FRACTIONS']
       self.Word=random.choice
       print(self.Word)
       return self.Word
        
        
    def Main(self):
        
        HangManWin = GraphWin("Hangman", 300, 500)
        HangManWin.setBackground('purple')
        
        ImageNumber=1
        
        used=''
        self.PossibleWord=['HELLO','TRIANGLE','CIRCLE','SQUARE','SUMS','FRACTIONS']

        self.Word=random.choice(self.PossibleWord)
        print(self.Word)
        self.Guess='-'*(len(self.Word))
        Letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ImageBack=Rectangle(Point(20,20),Point(280,320))
        ImageBack.setFill('white')
        ImageBack.draw(HangManWin)    
        self.drawLetters(HangManWin,Letters)

        while ImageNumber<9 and self.Guess!=self.Word:
            self.drawLetters(HangManWin,Letters)
            t=Rectangle(Point(20,330),Point(300,370))
            t.setFill('purple')
            t.setOutline('purple')
            t.draw(HangManWin)
            self.drawGuess(HangManWin)
            Letters,char,self.Letters=self.getLetter(HangManWin)
            if char in self.Word:
                 self.Guess=self.updateGuess(self)
                 
            else:
               self.scaffold(self,HangMan)
               
             
        self.Guess=updateGuess(guess,char)   
        if next==9:
           t=Text(Point(150,150),'You lose :P')
        else:
           t=Text(Point(150,150),'You HangManWin :)')

        t.setSize(36)
        t.setFace('arial')
        t.draw(HangManWin)
        p=HangManWin.getMouse()
       
                
#--------------------------------------------------------------------------------------------------------------------------
TotalCorrect=0    
def TopicChoice(Mainwindow):
    try:
        Student.Score=int(Student.Score)
    except:
        print('')
    Student.UpdateScore(y,TotalCorrect)
    NameInfo=Text(Point(280,30),'welcome: '+Student.UserName)
    NameInfo.setSize(15)
    NameInfo.draw(Mainwindow)
    print(Student.Score)
    
    ScoreInfo=Text(Point(560,20),'Score: '+str(Student.Score))
    ScoreInfo.setSize(13)
    ScoreInfo.draw(Mainwindow)
    GradeInfo=Text(Point(560,40),'Grade: '+Student.Grade)
    GradeInfo.setSize(13)
    GradeInfo.draw(Mainwindow)
          
    # finds where the user clicks
    f=Mainwindow.getMouse()
    X_click=int(f.getX())
    Y_click=int(f.getY())
    print('X:',str(X_click)+'\nY:'+str(Y_click),int(Student.Score)+1)

    #displays which category has been chosen
    if (Y_click<=139 and Y_click>70) and (X_click>=150 and X_click<=700):
        drawBars(Mainwindow)
        drawBlueBars(Mainwindow)
        
        if (X_click<267 and X_click>=150):
            GColour='white'
            NColour='white'
            AColour='orange'
            DrawCatergories(Mainwindow,AColour,NColour,GColour)
            Question.Category='Algebra'
            Drawtopic(Mainwindow)

        elif (X_click>268 and X_click<=383):
            GColour='white'
            NColour='orange'
            AColour='white'
            DrawCatergories(Mainwindow,AColour,NColour,GColour)
            Question.Category='Numbers'
            Drawtopic(Mainwindow)
            
            
        elif (X_click>383 and X_click<500):
            GColour='orange'
            NColour='white'
            AColour='white'
            DrawCatergories(Mainwindow,AColour,NColour,GColour)
            Question.Category='Geometry'
            Drawtopic(Mainwindow)
            
        #generates qusetion based on what the user clicks
    if (Y_click>=140 and Y_click<=550) and (X_click>=150 and X_click<=700):
        TopicRow=(Y_click-140)//55
        print(TopicRow+1)
        Question.Topic=TopicRow+1
        Question.DisplayGenerateQuestion()
        
       #updates the users information aswell as runs the minesweeper class
    elif (Y_click>180 and Y_click<=235) and (X_click>0 and X_click<=150):
        try:
            Student.Score=int(Student.Score)-20
            DrawHeader(Mainwindow)
            ScoreInfo=Text(Point(560,20),'Score: '+str(Student.Score))
            ScoreInfo.setSize(13)
            ScoreInfo.draw(Mainwindow)
            GradeInfo=Text(Point(560,40),'Grade: '+Student.Grade)
            GradeInfo.setSize(13)
            GradeInfo.draw(Mainwindow)
            print(Student.Score) 
            MineSweeper.MineSweeperMain(player2)
           
        except:
            print('error 1')
        #updates the users information aswell as runs the connect4 class
    elif (X_click<=150 and X_click>0) and (Y_click>=125 and Y_click<=180) and (int(Student.Score)>=10):
       player=Connect4
       try:
           Student.Score=int(Student.Score)-10
           DrawHeader(Mainwindow)
           ScoreInfo=Text(Point(560,20),'Score: '+str(Student.Score))
           ScoreInfo.setSize(13)
           ScoreInfo.draw(Mainwindow)
           GradeInfo=Text(Point(560,40),'Grade: '+Student.Grade)
           GradeInfo.setSize(13)
           GradeInfo.draw(Mainwindow)
           print(Student.Score)
           Connect4.Connect4Main(player)
           
       except:
           
           print('error 2')
       #updates the users information aswell as runs the match the tiles class
    elif (X_click<=150 and X_click>0) and (Y_click>=235 and Y_click<=290) and (int(Student.Score)>=10):
        try:
            print('Tiles')
            Student.Score=int(Student.Score)-10
            DrawHeader(Mainwindow)
            ScoreInfo=Text(Point(560,20),'Score: '+str(Student.Score))
            ScoreInfo.setSize(13)
            ScoreInfo.draw(Mainwindow)
            GradeInfo=Text(Point(560,40),'Grade: '+Student.Grade)
            GradeInfo.setSize(13)
            GradeInfo.draw(Mainwindow)
            print(Student.Score)
            MatchTheTiles.Main(Game)
            
        except:
            print('error 3')
      #updates the users information aswell as runs the hangman class
    elif (X_click<=150 and X_click>0) and (Y_click>290 and Y_click<=345) and (int(Student.Score)>=10):
        try:
            Student.Score=int(Student.Score)-10
            DrawHeader(Mainwindow)
            ScoreInfo=Text(Point(560,20),'Score: '+str(Student.Score))
            ScoreInfo.setSize(13)
            ScoreInfo.draw(Mainwindow)
            GradeInfo=Text(Point(560,40),'Grade: '+Student.Grade)
            GradeInfo.setSize(13)
            GradeInfo.draw(Mainwindow)
            print(Student.Score)
            HangMan.Main(player3)
        except:
            print('Error 4')
    elif (X_click>=200 and X_click<=300) and (Y_click>=560 and Y_click<=610):
        SlideWin=GraphWin('Fun maths login page',700,550)
        SlideWin.setBackground('white')
        SlideShow.PageLines(SlideWin,S)
        
            
#--------------------------------------------------------------------------------------------------------------------------            
Homewindow=GraphWin('Fun maths login page',600,650)
Homewindow.setBackground('turquoise')

P=HomePage
HomePage.HomePageMain(P)

y=Student(P.UserName,P.Score,P.Grade)

Question=Question(y.Score,y.Percentage)
Game=MatchTheTiles
player=Connect4()
player2=MineSweeper()
player3=HangMan()
S=SlideShow()

Mainwindow=GraphWin('Fun maths login page',600,650)
Mainwindow.setBackground('turquoise')
MainPage(Mainwindow)

Category=None     
while True:
    
    TopicChoice(Mainwindow)

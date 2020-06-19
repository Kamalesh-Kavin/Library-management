print("NOTE: RUN 'STARTUP.PY' BEFORE RUNNING THIS PROGRAM")
import mysql.connector as mc
import string
c=mc.connect(host="localhost",user="root",passwd="yoursqlpassword",database="Library")
m=c.cursor()
def libr():
    print("WELCOME TO LIBRARY")
    print("------------------")
    ch=int(input('(1)Staff\n(2)Student\n(3)Help\n(4)Exit\nEnter:'))
    print("")
    if(ch==1):
        def stafpswd():
            print("STAFF LOGIN")
            print("-----------")
            st_id=int(input("Enter staff-ID:"))
            a="select Status from staffs where Staff_ID='%s'"%(st_id)
            m.execute(a)
            ro=m.fetchone()
            for i in ro:
                lol=i
            if(lol=='Fired'):
                print('--SORRY, YOU HAVE BEEN BANNED!--')
            else:
                s="select * from Staffs where Staff_ID=%s"%(st_id)
                pswd=input("Enter password:")
                m.execute(s)
                results=m.fetchall()
                for q in results:
                    nmd=q[1]
                    password=q[4]
                print('')
                if(pswd==password):
                    print('STAFF MENU')
                    print('----------')
                    print("Welcome",nmd,",")
                    def staff():
                        ch2=int(input('(1)Add books\n(2)Remove books\n(3)View books\n(4)View current records\n(5)View students\n(6)Add Warning to Student\n(7)View Banned Students\n(8)Give Shout-out to student\n(9)Help\n(10)Back\n(11)Exit\nEnter:'))
                        if(ch2==1):
                            print('')
                            print('ADD BOOKS')
                            print('---------')
                            ch21=int(input('(1)Add Book_ID for books manually\n(2)Add Book_ID for books automatically\n(3)Back\nEnter Choice:'))
                            print("")
                            if(ch21==3):
                                staff()
                            elif(ch21==1):
                                n=int(input("Enter number of books to be added:"))
                                for i in range(n):
                                    bn=int(input("Enter book ID:"))
                                    bN=input("Enter book name:")
                                    s="insert into Books(Book_ID, Book_Name) values(%s, %s)"
                                    r=[(bn,bN)]
                                    m.executemany(s,r)
                                    print("")
                                    print("-BOOK ADDED-")
                                    print('')
                                c.commit()
                                staff()
                            elif(ch21==2):
                                n=int(input("Enter number of books to be added:"))
                                for i in range(n):
                                    maxi='select max(Book_ID) from books'
                                    m.execute(maxi)
                                    re=m.fetchall()
                                    print('')
                                    if(re==[(None,)]):
                                        print('Sorry, you have to add Books manually only, as this happens to be your first entry')
                                        print('')
                                        idm=input("Enter Book ID:")
                                        na=input("Enter book name:")
                                        sq="insert into books(Book_ID,Book_Name) values(%s,%s)"
                                        rol=[(idm,na)]
                                        m.executemany(sq,rol)
                                        print('')
                                        print("-BOOK ADDED-")
                                        c.commit()
                                    else:
                                        for p in re:
                                            maxv=p[0]
                                            ma=maxv+1
                                        na=input("Enter book name:")
                                        sq="insert into books(Book_ID,Book_Name) values(%s,%s)"
                                        rol=[(ma,na)]
                                        m.executemany(sq,rol)
                                        print("")
                                        print("BOOK ID=",ma,'\nBOOK NAME=',na)
                                        print('')
                                        print("-BOOK ADDED-")
                                        print("")
                                        c.commit()
                                staff()
                        elif(ch2==2):
                            print('')
                            print('REMOVE BOOKS')
                            print('------------')
                            n=int(input("Enter number of books to be removed:"))
                            for i in range(n):
                                bi=int(input("Enter Book_ID:"))
                                s='select * from books where Book_ID=%s'%(bi)
                                m.execute(s)
                                result=m.fetchall()
                                if(result==[]):
                                    print('')
                                    print("-THE GIVEN BOOK DOESN'T EXIST-")
                                    print('')
                                else:
                                    s="delete from Books where Book_ID=%d"%(bi)
                                    m.execute(s)
                                    print("")
                                    print("-BOOK REMOVED-")
                                    print('')
                            c.commit()
                            staff()
                        elif(ch2==3):
                            def boo():
                                print('')
                                print('BOOKS')
                                print('-----')
                                l=int(input("(1)View specific books\n(2)View all books\n(3)Help\n(4)Back\nEnter:"))
                                print('')
                                if(l==3):
                                    print('')
                                    print('HELP')
                                    print('----')
                                    print('Choice 1 is used to view specific Books by giving their ID and Choice 2 is used to view all the Books the library is containing.\nThis fucntion is logiccaly useful only when you have some added books in the library')
                                    print('')
                                    boo()
                                elif(l==4):
                                    staff()
                                elif(l==2):
                                    s="select * from Books"
                                    m.execute(s)
                                    res=m.fetchall()
                                    if(res==[]):
                                        print("-EMPTY-")
                                        print("")
                                        staff()
                                    else:
                                        for r in res:
                                            Book_ID=r[0]
                                            Book_Name=r[1]
                                            Status=r[2]
                                            print("| Book-ID=%d | Name=%s | Status=%s |"%(Book_ID,Book_Name,Status))
                                            print('')
                                        staff()
                                elif(l==1):
                                    n=int(input("Enter number of books to be viewed:"))
                                    for i in range(n):
                                        bi=int(input("Enter Book ID:"))
                                        s="select * from Books where Book_ID=%s"%(bi)
                                        m.execute(s)
                                        res=m.fetchone()
                                        print('')
                                        if(res==None):
                                            print("-BOOK DOES NOT EXIST-")
                                            print("")
                                        else:
                                            Book_ID=res[0]
                                            Book_Name=res[1]
                                            Status=res[2]
                                            print("| Book-ID=%d | Name=%s | Status=%s |"%(Book_ID,Book_Name,Status))
                                            print('')
                                    staff()
                                else:
                                    print("-ENTER CORRECT OPTION-")
                                    staff()
                            boo()        
                        elif(ch2==11):
                            print('')
                            print("-GOOD-BYE!-")
                            print('')
                        elif(ch2==10):
                            print('')
                            libr()
                        elif(ch2==9):
                            print('')
                            print('HELP')
                            print('----')
                            a=int(input('Enter choice about what you need to be briefed:'))
                            print('')
                            if(a==1):
                                print('This function is used to ADD books to the library')
                            elif(a==2):
                                print('This function is used to REMOVE books from the library')
                            elif(a==3):
                                print('This function is used to VIEW the available books in the library')
                            elif(a==4):
                                print('This function is used to look about the taken books with information regarding date taken and student id')
                            elif(a==5):
                                print('This function is used to view students who are currently members of the library')
                            elif(a==6):
                                print('This function is used to WARN students for their mischievous activity in the library')
                            elif(a==7):
                                print('This function is used to VIEW students who are BANNED due to their ill code-of-conduct')
                            elif(a==8):
                                print('This function is used to PRAISE students for their good conduct in library')
                            elif(a==9 or a==10 or a==11):
                                print('Its quite obvious, dont mess around with the help function')
                            else:
                                print('SORRY, HELP IS PROVIDED FOR GIVEN CHOICES ONLY')
                            print('')
                            staff()
                        elif(ch2==7):
                            print('')
                            print('BANNED STUDENTS')
                            print('---------------')
                            s='select * from Stud_Profile'
                            m.execute(s)
                            f=m.fetchall()
                            if(f==[]):
                                print("-EMPTY-")
                                print("")
                                staff()
                            else:
                                for i in f:
                                    idm=i[0]
                                    idn=i[1]
                                    pro=i[2]
                                    print("| ID_Number=%s | Name=%s | Profile=%s |"%(idm,idn,pro)) 
                                    print("")
                                staff()
                        elif(ch2==6):
                            print('')
                            print("WARNING DIVISION FOR STUDENTS")
                            print('-----------------------------')
                            print('NOTE: MAX WARNINGS BEFORE GETTING BANNED=4')
                            n=int(input('Enter no.of students to be warned:'))
                            for i in range(n):
                                idm=int(input('Enter student ID:'))
                                a='select * from students where ID_Number=%s'%(idm)
                                m.execute(a)
                                al=m.fetchall()
                                if(al==[]):
                                    print('')
                                    print("-GIIVEN STUDENT DOESN'T EXIST-")
                                    print('')
                                else:
                                    maxi='select Warning from students where ID_Number=%s'%(idm)
                                    na='select Name from students where ID_Number=%s'%(idm)
                                    m.execute(na)
                                    ro=m.fetchone()
                                    m.execute(maxi)
                                    re=m.fetchall()
                                    for p in re:
                                        maxv=p[0]
                                        ma=maxv+1
                                    for name in ro:
                                        nam=name
                                    sq="UPDATE students SET Warning = %s WHERE ID_Number = %s"
                                    rol=[(ma,idm)]
                                    m.executemany(sq, rol)
                                    c.commit()
                                    print('')
                                    print('--THE STUDENT',nam.upper(),'HAS BEEN WARNED--')
                                    print('CURRENT NO. OF WARNINGS=',ma)
                                    print('')
                                    if(ma==4):
                                        u="UPDATE students SET Profile ='Banned' WHERE Warning = %s"%(ma)
                                        m.execute(u)
                                        i='insert into Stud_Profile(ID_Number, Name, Profile) values(%s,%s,%s)'
                                        val=[(idm,nam,'Banned')]
                                        m.executemany(i,val)
                                        print('--The Student has exceeded the permissible no. of warnings, and hence',nam,'(',idm,')','is banned--')
                                        c.commit()
                                    elif(ma>4):
                                        print('--SELECTED STUDENT IS ALREADY BANNED!--')
                            staff()
                        elif(ch2==5):
                            def sto():
                                print('')
                                print('STUDENTS')
                                print('--------')
                                l=int(input("(1)View specific Students\n(2)View temporary Students\n(3)View permanent Students\n(4)View all Students\n(5)Help\n(6)Back\nEnter:"))
                                print("")
                                if(l==5):
                                    print('HELP')
                                    print('----')
                                    print('(1) gives info about specific records about students you want, you just need to type the STUDENT ID\n(2) gives you info about the temporary students in the library\n(3) gives info about the permanent students\n(4) lets you views all the students record')
                                    print('')
                                    sto()
                                if(l==6):
                                    staff()
                                elif(l==4):                        
                                    s='select * from students'
                                    m.execute(s)
                                    f=m.fetchall()
                                    print('')
                                    if(f==[]):
                                        print("-EMPTY-")
                                        print("")
                                        staff()
                                    else:
                                        for i in f:
                                            idn=i[0]
                                            idm=i[1]
                                            cl=i[2]
                                            mb=i[3]
                                            wr=i[5]
                                            pro=i[6]
                                            print("| ID_Number=%s | Name=%s | Class=%s | Mobile_Num=%s | Warning=%s | Profile=%s |"%(idn,idm,cl,mb,wr,pro)) 
                                            print("")
                                        staff()
                                elif(l==1):
                                    n=int(input('Enter no. of students to be viewed:'))
                                    for i in range(n):
                                        si=input("Enter student ID:")
                                        s='select * from students where ID_Number=%s'%(si)
                                        m.execute(s)
                                        f=m.fetchone()
                                        print('')
                                        if(f==None):
                                            print("-EMPTY-")
                                            print("")
                                        else:
                                            idn=f[0]
                                            idm=f[1]
                                            cl=f[2]
                                            mb=f[3]
                                            ps=f[4]
                                            wr=f[5]
                                            pro=f[6]
                                            mem=f[8]
                                            print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s | Membership=%s"%(idn,idm,cl,mb,ps,wr,pro,mem))
                                            print('')
                                    staff()
                                elif(l==2):
                                    s='select * from students where Membership="Temporary"'
                                    m.execute(s)
                                    f=m.fetchall()
                                    print('')
                                    if(f==[]):
                                        print("-EMPTY-")
                                        print("")
                                        staff()
                                    else:
                                        for i in f:
                                            idn=i[0]
                                            idm=i[1]
                                            cl=i[2]
                                            mb=i[3]
                                            ps=i[4]
                                            wr=i[5]
                                            pro=i[6]
                                            mem=i[8]
                                            print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s | Membership=%s"%(idn,idm,cl,mb,ps,wr,pro,mem))
                                            print('')
                                        staff()
                                elif(l==3):
                                    s='select * from students where Membership="Permanent"'
                                    m.execute(s)
                                    f=m.fetchall()
                                    print('')
                                    if(f==[]):
                                        print("-EMPTY-")
                                        print("")
                                        staff()
                                    else:
                                        for i in f:
                                            idn=i[0]
                                            idm=i[1]
                                            cl=i[2]
                                            mb=i[3]
                                            ps=i[4]
                                            wr=i[5]
                                            pro=i[6]
                                            mem=i[8]
                                            print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s | Membership=%s"%(idn,idm,cl,mb,ps,wr,pro,mem))
                                            print('')
                                        staff()
                                else:
                                    print("-ENTER CORRECT OPTION-")
                                    staff()
                            sto()                    
                        elif(ch2==8):
                            print('')
                            print('SHOUT-OUT DIVISION(STUDENTS)')
                            print('----------------------------')
                            print('NOTE: NO. OF SHOUT-OUTS TO BECOME PERMANENT MEMBER=10')
                            n=int(input('Enter no. of students to be given shout-outs:'))
                            for i in range(n):
                                idm=int(input('Enter student ID:'))
                                a='select * from students where ID_Number=%s'%(idm)
                                m.execute(a)
                                al=m.fetchall()
                                if(al==[]):
                                    print('')
                                    print("-GIIVEN STUDENT DOESN'T EXIST-")
                                    print('')
                                else:
                                    maxi='select Shout_out from students where ID_Number=%s'%(idm)
                                    na='select Name from students where ID_Number=%s'%(idm)
                                    m.execute(na)
                                    ro=m.fetchone()
                                    m.execute(maxi)
                                    re=m.fetchall()
                                    for p in re:
                                        maxv=p[0]
                                        ma=maxv+1
                                    for name in ro:
                                        nam=name
                                    sq="UPDATE students SET Shout_out = %s WHERE ID_Number = %s"
                                    rol=[(ma,idm)]
                                    m.executemany(sq, rol)
                                    c.commit()
                                    print('')
                                    print('--THE STUDENT',nam.upper(),'HAS BEEN GIVEN SHOUT-OUT--')
                                    print('CURRENT NO. OF SHOUTOUTS=',ma)
                                    print('')
                                    if(ma==10):
                                        u="UPDATE students SET Membership ='Permanent' WHERE Shout_out = %s"%(ma)
                                        m.execute(u)
                                        c.commit()
                            staff()
                        elif(ch2==4):
                            def cur():
                                print('')
                                print('CURRENT RECORDS')
                                print('---------------')
                                l=int(input('(1)View specific student records\n(2)View all records\n(3)Help\n(4)Back\nEnter choice:'))
                                if(l==4):
                                    print('')
                                    staff()
                                elif(l==3):
                                    print('')
                                    print('HELP')
                                    print('----')
                                    print('(1) gives info about the specified students and the books they have taken\n(2) shows you all the records about books taken')
                                    cur()
                                elif(l==2):
                                    s='select * from stud_book'
                                    m.execute(s)
                                    f=m.fetchall()
                                    print('')
                                    if(f==[]):
                                        print("-EMPTY-")
                                        print("")
                                        staff()
                                    else:
                                        for i in f:
                                            StudID=i[0]
                                            StudName=i[1]
                                            BookID=i[2]
                                            BookName=i[3]
                                            Taken=i[4]
                                            print("| Student-ID=%s | Name=%s | Book-ID=%s | Book-Name=%s | Taken-Date=%s |"%(StudID,StudName,BookID,BookName,Taken))
                                            print('')
                                        staff()
                                elif(l==1):
                                    n=int(input("Enter no. of student's records to be viewed:"))
                                    for i in range(n):
                                        si=int(input("Enter student ID:"))
                                        s='select * from stud_book where Student_ID_Number=%s'%(si)                                                                  
                                        m.execute(s)
                                        f=m.fetchall()
                                        nl=len(f)
                                        print('')
                                        if(f==[]):
                                            print("-EMPTY-")
                                            print("")
                                        else:
                                            for j in f:
                                                for i in range(nl):
                                                    al=j
                                                StudID=al[0]
                                                StudName=al[1]
                                                BookID=al[2]
                                                BookName=al[3]
                                                Taken=al[4]
                                                print("| Student-ID=%s | Name=%s | Book-ID=%s | Book-Name=%s | Taken-Date=%s |"%(StudID,StudName,BookID,BookName,Taken))
                                                print('')
                                    staff()
                                else:
                                    print('')
                                    print("-ENTER THE CORRECT OPTION-")
                                    print("")
                                    cur()
                            cur()    
                        else:
                            print('')
                            print("-ENTER THE CORRECT OPTION-")
                            print("")
                            staff()
                    staff()
                else:
                    print('')
                    print("-WRONG PASSWORD-")
                    print('')
                    stafpswd()
        stafpswd()
    elif(ch==2):
        def noob():
            print("STUDENTS LOGIN")
            print("--------------")
            noo=int(input('(1)New Member\n(2)Existing Member\n(3)Help\n(4)Back\nEnter:'))
            print("")
            if(noo==1):
                maxi='select max(ID_Number) from students'
                m.execute(maxi)
                re=m.fetchall()
                if(re==[(None,)]):
                    idm=input("Create your ID:")
                    na=input("Enter your name:")
                    cl=input("Enter your class:")
                    mn=int(input("Enter your mobile number:"))
                    ps=input("Create your password:")
                    sq="insert into students(ID_Number, Name, Class, Mobile_Num, Password) values(%s, %s, %s, %s, %s)"
                    rol=[(idm,na,cl,mn,ps)]
                    m.executemany(sq,rol)
                    print("")
                    print("-DONE-")
                    print("")
                    c.commit()
                    noob()
                else:
                    for p in re:
                        maxv=p[0]
                        ma=maxv+1
                        na=input("Enter your name:")
                        cl=input("Enter your class:")
                        mn=int(input("Enter your mobile number:"))
                        ps=input("Create your password:")
                        sq="insert into students(ID_Number, Name, Class, Mobile_Num, Password) values(%s, %s, %s, %s, %s)"
                        rol=[(ma,na,cl,mn,ps)]
                        m.executemany(sq, rol)
                        print('')
                        print("YOUR ID=",ma,'\nYOUR PASSWORD=',ps)
                        print("")
                        print("-DONE-")
                        print("")
                        c.commit()
                        noob()
            elif(noo==3):
                print("")
                print('HELP')
                print('----')
                print('If you are a new student in the library, use choice (1) and create your own login-ID\nExisting students can login using their login-ID by going into choice (2)')
                print('')
                noob()
            elif(noo==2):
                def studid():
                    si=int(input("Enter your ID number:"))
                    a="select Profile from students where ID_Number='%d'"%(si)
                    m.execute(a)
                    ro=m.fetchone()
                    for i in ro:
                        lol=i
                    if(lol=='Banned'):
                        print('')
                        print('--SORRY, YOU HAVE BEEN BANNED!--')
                        print('')
                    else:
                        s="select * from students where ID_Number='%d'"%(si)
                        passwd=input("Enter your password:")
                        m.execute(s)
                        res=m.fetchall()
                        for r in res:
                            Name=r[1]
                            pswd=r[4]
                            mem=r[8]
                            if(pswd==passwd):
                                if(res!=[(None,)]):
                                    print("")
                                    print("Welcome",Name,",")
                                    print("Profile Status -",mem)
                                    print("")
                                    def ch3o():
                                        print("STUDENTS MENU")
                                        print("-------------")
                                        ch3=int(input('(1)Borrow books\n(2)Return books\n(3)View Books\n(4)Help\n(5)Back\nEnter:'))
                                        if(ch3==1):
                                            def book1():
                                                print('')
                                                print('BORROW BOOKS')
                                                print('------------')
                                                e='select Membership from students where ID_Number=%s'%(si)
                                                m.execute(e)
                                                r=m.fetchone()
                                                mem=r[0]
                                                if(mem=="Temporary"):
                                                    print("Maximum limit for borrowing books = 3")
                                                    n=int(input("Enter number of books:"))
                                                    for i in range(n):
                                                        v='select Books_taken from students where ID_Number=%s'%(si)
                                                        m.execute(v)
                                                        res=m.fetchall()
                                                        for j in res:
                                                            nobu=j[0]
                                                            nob=nobu+1
                                                        if(n<=3 and nob<=4):
                                                            dob=nob
                                                            sq='UPDATE students set Books_taken=%s where ID_Number=%s'
                                                            rol=[(dob,si)]
                                                            m.executemany(sq, rol)
                                                            bi=int(input("Enter Book_ID:"))
                                                            s='select * from books where Book_ID=%s'%(bi)
                                                            m.execute(s)
                                                            result=m.fetchall()
                                                            for r in result:
                                                                B=r[1]
                                                                print("Book Name:",B)
                                                            if(result!=[]):
                                                                s='insert into Stud_Book(Student_ID_Number, Student_Name, Book_ID, Book_Name, Taken_Date) values(%s,%s,%s,%s,%s)'
                                                                import datetime
                                                                t=str(datetime.datetime.now())
                                                                rl=[(si,Name,bi,B,t)]
                                                                m.executemany(s,rl)
                                                                u="update books set Status='Taken' where Book_ID='%s'"%(bi)
                                                                m.execute(u)
                                                                c.commit()
                                                                print("")
                                                                print("-ENJOY YOUR BOOK!-")
                                                                print("")
                                                            else:
                                                                print('')
                                                                print("-BOOK DOESN'T EXIST-\n(OR)\n-BOOK ID MIGHT BE WRONG. PLEASE CHECK-")
                                                                print("")
                                                        else:
                                                            print('')
                                                            print('!!!YOU ARE EXCEEDING THE MAX POSSIBLE BORROWED LIMIT!!!')
                                                            print('')
                                                            ch3o()    
                                                else:
                                                    print("Maximum limit for borrowing books = 6")
                                                    n=int(input("Enter number of books:"))
                                                    for i in range(n):
                                                        v='select Books_taken from students where ID_Number=%s'%(si)
                                                        m.execute(v)
                                                        res=m.fetchall()
                                                        for j in res:
                                                            nobu=j[0]
                                                            nob=nobu+1
                                                        if(n<=6 and nob<=7):
                                                            dob=nob
                                                            sq='UPDATE students set Books_taken=%s where ID_Number=%s'
                                                            rol=[(dob,si)]
                                                            m.executemany(sq, rol)
                                                            bi=int(input("Enter Book_ID:"))
                                                            s='select * from books where Book_ID=%s'%(bi)
                                                            m.execute(s)
                                                            result=m.fetchall()
                                                            for r in result:
                                                                B=r[1]
                                                                print("Book Name:",B)
                                                            if(result!=[]):
                                                                s='insert into Stud_Book(Student_ID_Number, Student_Name, Book_ID, Book_Name, Taken_Date) values(%s,%s,%s,%s,%s)'
                                                                import datetime
                                                                t=str(datetime.datetime.now())
                                                                rl=[(si,Name,bi,B,t)]
                                                                m.executemany(s,rl)
                                                                u="update books set Status='Taken' where Book_ID='%s'"%(bi)
                                                                m.execute(u)
                                                                c.commit()
                                                                print("")
                                                                print("-ENJOY YOUR BOOK!-")
                                                                print("")
                                                            else:
                                                                print('')
                                                                print("-BOOK DOESN'T EXIST- Try Entering other Book_ID")
                                                                print("")
                                                        else:
                                                            print('')
                                                            print('!!!YOU ARE EXCEEDING THE MAX POSSIBLE BORROWED LIMIT!!!')
                                                            print('')
                                                            ch3o()
                                                print('')
                                                ch3o()
                                            book1()
                                        elif(ch3==5):
                                            print('')
                                            noob()
                                        elif(ch3==4):
                                            print('')
                                            print('HELP')
                                            print('----')
                                            print('(1) is used to borrow books from the library by giving the respective Book-ID\n(2) is used to return the taken books\n(3) is used to View details about the books in the library')
                                            print('TIP: IT WOULD BE HELPFUL TO VIEW BOOKS FIRST BEFORE TAKING THE BOOKS, AS IT WOULD GIVE DETAILS ABOUT THE AVAILABILITY OF BOOKS')
                                            print('')
                                            ch3o()
                                        elif(ch3==2):
                                            def book2():
                                                print('')
                                                print('RETURN TAKEN BOOKS')
                                                print('------------------')
                                                n=int(input("Enter number of books:"))
                                                for i in range(n):
                                                    bi=int(input("Enter Book_ID:"))
                                                    s='select * from stud_book where Student_ID_Number=%s'%(si)
                                                    m.execute(s)
                                                    result=m.fetchall()
                                                    if(result==[]):
                                                        print('')
                                                        print("The given student hasn't taken any books")
                                                        print('')
                                                    else:
                                                        B=[]
                                                        lol='select * from stud_book where Student_ID_Number=%s'%(si)
                                                        m.execute(lol)
                                                        result=m.fetchall()
                                                        for i in result:
                                                            B.append(i[2])
                                                        a=bi in B
                                                        if(a==True):
                                                            v='select Books_taken from students where ID_Number=%s'%(si)
                                                            m.execute(v)
                                                            res=m.fetchall()
                                                            for j in res:
                                                                nobu=j[0]
                                                                nob=nobu-1
                                                            sq='UPDATE students set Books_taken=%s where ID_Number=%s'
                                                            rol=[(nob,si)]
                                                            m.executemany(sq, rol)
                                                            w="delete from stud_book where Book_ID=%s"%(bi)
                                                            u="update books set Status='Available' where Book_ID='%s'"%(bi)
                                                            m.execute(w)
                                                            m.execute(u)
                                                            print("")
                                                            print("-THANK YOU FOR RETURNING-")
                                                            print("")
                                                            c.commit()
                                                        else:
                                                            print("")
                                                            print("-YOU HAVEN'T TAKEN THAT BOOK-\n(OR)\n-BOOK ID MIGHT BE WRONG. PLEASE CHECK IT-")
                                                            print("")
                                                ch3o()
                                            book2()
                                        elif(ch3==3):
                                            def boolu():
                                                print('')
                                                print("BOOKS")
                                                print('-----')
                                                l=int(input("(1)View specific books\n(2)View all books\n(3)Help\n(4)Back\nEnter:"))
                                                if(l==4):
                                                    print('')
                                                    ch3o()
                                                elif(l==3):
                                                    print('')
                                                    print('HELP')
                                                    print('----')
                                                    print('(1) is used to view specified books at a time\n(2) is used to view all books')

                                                    boolu()
                                                elif(l==2):
                                                    s="select * from Books"
                                                    m.execute(s)
                                                    res=m.fetchall()
                                                    print('')
                                                    if(res==[]):
                                                        print("-EMPTY-")
                                                        print("")
                                                        ch3o()
                                                    else:
                                                        for r in res:
                                                            Book_ID=r[0]
                                                            Book_Name=r[1]
                                                            Status=r[2]
                                                            print("| Book-ID=%s | Name=%s | Status=%s |"%(Book_ID,Book_Name,Status))
                                                            print("")
                                                        ch3o()
                                                elif(l==1):
                                                    n=int(input("Enter number of books to be viewed:"))
                                                    for i in range(n):
                                                        bi=input("Enter Book ID:")
                                                        print('')
                                                        s="select * from Books where Book_ID=%s"%(bi)
                                                        m.execute(s)
                                                        res=m.fetchone()
                                                        if(res==None):
                                                            print("-EMPTY-")
                                                            print("")
                                                        else:
                                                            Book_ID=res[0]
                                                            Book_Name=res[1]
                                                            Status=res[2]
                                                            print("| Book-ID=%d | Name=%s | Status=%s |"%(Book_ID,Book_Name,Status))
                                                            print('')
                                                    ch3o()
                                                else:
                                                    print("-ENTER CORRECT OPTION-")
                                                    ch3o()
                                            boolu()
                                        elif(ch3==4):
                                            print('')
                                            noob()
                                    ch3o()
                                else:
                                    print("")
                                    print("-ID DOESN'T EXIST-")
                                    print("")
                                    studid()
                            else:
                                print('')
                                print("-WRONG PASSWORD-")
                                print('')
                                studid()  
            elif(noo==4):
                print('')
                libr()
            else:
                print('')
                print("-ENTER CORRECT OPTION-")
                noob()
            studid()
        noob()
    elif(ch==3):
        print('')
        print('HELP')
        print('----')
        print('This is the main block of the library, Here you can access Staff, student by entering the choices.\nYou can even access supervisor division by using the secret choice.\nEverything here requires Authentication password, so dont forget the passwords given to you.')
        print('')
        libr()
    elif(ch==4):
        print('')
        print("\t---THANK YOU FOR USING---")
    elif(ch==10):
        def svd():
            print("SUPERVISOR DIVISION")
            print("-------------------")
            spid=input("Enter your ID:")
            sppd=input("Enter your password:")
            sp="select * from SuperVisor where SP_ID='%s'"%(spid)
            m.execute(sp)
            r=m.fetchall()
            for ro in r:
                Pass=ro[2]
                Name=ro[1]
            if(sppd==Pass):
                print("")
                print("Welcome",Name)
                print("------------")
                def spdude():
                    spch=int(input('(1)Add Staffs\n(2)Remove Staffs\n(3)View Staffs\n(4)View students\n(5)View books\n(6)View Banned students\n(7)Add Warning to Staffs\n(8)View Fired(banned) staffs\n(9)Help\n(10)Back\n(11)Exit\nEnter:'))
                    print('')
                    if(spch==9):
                        print('HELP')
                        print('----')
                        a=int(input('Enter choice on which you need help:'))
                        print('')
                        if(a==1):
                            print('It is used to add staffs to the library')
                        elif(a==2):
                            print('It is used to remove staffs from the library')
                        elif(a==3):
                            print('It is used to view staff list of the library')
                        elif(a==5):
                            print('It is used to view books available in the library')
                        elif(a==4):
                            print('It is used to view students enrolled in the library')
                        elif(a==6):
                            print('It is used to view BANNED students from the library')
                        elif(a==7):
                            print('It is used to warn staffs')
                        elif(a==8):
                            print('It is used to view FIRED staffs from the library')
                        elif(a==9 or a==10 or a==11):
                            print('Its quite obvious, dont mess around with the help function')
                        else:
                            print('SORRY, HELP IS PROVIDED FOR GIVEN OPTIONS ONLY')
                        print('')
                        spdude()
                    elif(spch==2):
                        print('REMOVING STAFFS DIVISON')
                        print('-----------------------')
                        spsid=input("Enter Staff ID:")
                        spids="select * from Staffs where Staff_ID='%s'"%(spsid)
                        m.execute(spids)
                        f=m.fetchall()
                        if(f!=[]):
                            for i in f:
                                Stid=i[0]
                                Nam=i[1]
                                a=i[2]
                                mbn=i[3]
                                print("Staff Name =",Nam)
                                print("Staff ID =",Stid)
                                print("Age =",a)
                                print("Mobile Number =",mbn)
                                cont=int(input('Want to Continue?Press:\n(1)YES\n(2)NO\nEnter:'))
                                print("")
                                if(cont==1):
                                    o="delete from staffs where Staff_ID='%s'"%(spsid)
                                    m.execute(o)
                                    print("-STAFF REMOVED-")
                                    print("")
                                    c.commit()
                                    spdude()
                                elif(cont==2):
                                    spdude()
                                else:
                                    print('')
                                    print("-ENTER CORRECT STAFF ID-")
                                    print('')
                                    spdude()
                        else:
                           print('')
                           print("-ENTER CORRECT STAFF ID-")
                           print('')
                           spdude()
                    elif(spch==1):
                        def adds():
                            print("ADDING STAFFS DIVISION")
                            print("----------------------")
                            spch2=int(input('(1)To assign an ID value manually\n(2)To assign ID value automatically\n(3)Help\n(4)Back\nEnter your choice:'))
                            print("")
                            if(spch2==2):
                                n=int(input("Enter number of staffs to be added:"))
                                for i in range(n):
                                    maxi='select max(Staff_ID) from staffs'
                                    m.execute(maxi)
                                    re=m.fetchall()
                                    if(re==[(None,)]):
                                        print('')
                                        print('Sorry, you have to add staff manually only, as this happens to be your first entry')
                                        print('')
                                        idm=input("Enter Staff ID:")
                                        na=input("Enter Staffname:")
                                        cl=input("Enter age:")
                                        mn=int(input("Enter mobile number:"))
                                        ps=input("Provide a password:")
                                        sq="insert into Staffs(Staff_ID,Staff_Name,Age,Mobile_Number,Password) values(%s,%s,%s,%s,%s)"
                                        rol=[(idm,na,cl,mn,ps)]
                                        m.executemany(sq,rol)
                                        print('')
                                        print("-STAFF ADDED-")
                                        c.commit()
                                    else:
                                        for p in re:
                                            maxv=p[0]
                                            ma=maxv+1
                                        print('')
                                        na=input("Enter Staffname:")
                                        cl=input("Enter age:")
                                        mn=int(input("Enter mobile number:"))
                                        ps=input("Provide a password:")
                                        sq="insert into Staffs(Staff_ID,Staff_Name,Age,Mobile_Number,Password) values(%s,%s,%s,%s,%s)"
                                        rol=[(ma,na,cl,mn,ps)]
                                        m.executemany(sq, rol)
                                        print('')
                                        print("YOUR ID=",ma,'\nPassword=',ps)
                                        print("")
                                        print("-DONE-")
                                        c.commit()
                                spdude()
                            elif(spch2==1):
                                print("")
                                n=int(input("Enter number of staffs to be added:"))
                                for i in range(n):
                                    print('')
                                    stname=input("Enter StaffName:")
                                    stID=input("Enter Staff ID:")
                                    age=input("Enter age:")
                                    mbn=input("Enter mobile number:")
                                    psd=input("Provide a password:")
                                    g="insert into Staffs(Staff_ID,Staff_Name,Age,Mobile_Number,Password) values(%s,%s,%s,%s,%s)"
                                    k=[(stID,stname,age,mbn,psd)]
                                    m.executemany(g,k)
                                    print('')
                                    print("-STAFF ADDED-")
                                    print("")
                                    c.commit()
                                spdude()
                            elif(spch2==3):
                                print('')
                                print('HELP')
                                print('----')
                                print('Manual function is used to enter your STAFF-ID manually.\nAutomatic function would assign a STAFF ID on its own, you just have to give the staff-name')
                                print('')
                                adds()
                            elif(spch2==4):
                                print('')
                                spdude()
                            else:
                                print('ENTER VALID CHOICE ONLY!!!')
                                adds()
                        adds()    
                    elif(spch==3):
                        def stok():
                            print('STAFFS')
                            print('------')
                            l=int(input("(1)View specific records\n(2)View all\n(3)Help\n(4)Back\nEnter:"))
                            print("")
                            if(l==4):
                                print('')
                                spdude()
                            elif(l==3):
                                print('')
                                print('HELP')
                                print('----')
                                print('(1) is used to view specific records\n(2) is used to view all records')
                                print('')
                                stok()
                            elif(l==2):
                                g='select * from Staffs'
                                m.execute(g)
                                r=m.fetchall()
                                if(r==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for i in r:
                                        Stid=i[0]
                                        Nam=i[1]
                                        a=i[2]
                                        mbn=i[3]
                                        ps=i[4]
                                        wr=i[5]
                                        st=i[6]
                                        print("| Staff ID=%s | Staff Name=%s | Age=%s | MobileNumber=%s | Password=%s | Warning=%s | Status=%s |"%(Stid,Nam,a,mbn,ps,wr,st))
                                        print("")
                                    spdude()
                            elif(l==1):
                                n=int(input("Enter number of records:"))
                                for i in range(n):
                                    s=int(input("Enter Staff ID:"))
                                    g='select * from Staffs where Staff_ID=%s'%(s)
                                    m.execute(g)
                                    r=m.fetchone()
                                    print('')
                                    if(r==None):
                                        print("-STAFF ID DOESNT EXIST-")
                                        print("")
                                        spdude()
                                    else:
                                        Stid=r[0]
                                        Nam=r[1]
                                        a=r[2]
                                        mbn=r[3]
                                        ps=r[4]
                                        wr=r[5]
                                        st=r[6]
                                        print("| Staff ID=%s | Staff Name=%s | Age=%s | MobileNumber=%s | Password=%s | Warning=%s | Status=%s |"%(Stid,Nam,a,mbn,ps,wr,st))
                                        print("")
                                spdude()
                            else:
                                print("-ENTER CORRECT OPTION-")
                                spdude()
                        stok()                
                    elif(spch==11):
                        print('')
                        print("---THANKYOU SUPERVISOR---")
                    elif(spch==10):
                        print('')
                        libr()
                    elif(spch==8):
                        def stouk():
                            print('')
                            print('FIRED/BANNED STAFFS')
                            print('-------------------')
                            l=int(input('(1)View Specifc records\n(2)View all records\n(3)Help\n(4)Back\nEnter choice:'))
                            if(l==4):
                                print('')
                                spdude()
                            elif(l==3):
                                print('')
                                print('HELP')
                                print('----')
                                print('(1) is used to view specific records\n(2) is used to view all records')
                                stouk()
                            elif(l==2):
                                s='select * from Staff_Fired'
                                m.execute(s)
                                f=m.fetchall()
                                print('')
                                if(f==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for i in f:
                                        idm=i[0]
                                        idn=i[1]
                                        ag=i[2]
                                        mob=i[3]
                                        res=i[4]
                                        print("| Staff_ID=%s | Staff_Name=%s | Age=%s | Mobile_Number=%s | Reason=%s |"%(idm,idn,ag,mob,res)) 
                                        print("")
                                    staff()
                            elif(l==1):
                                n=int(input('Enter no. of records to be viewed:'))
                                for i in range(n):
                                    a=int(input('Enter staff id:'))
                                    s='select * from Staff_Fired where Staff_ID=%s'%(a)
                                    m.execute(s)
                                    f=m.fetchone()
                                    print('')
                                    if(f==None):
                                        print("-EMPTY-")
                                        print("")
                                    else:
                                        idm=f[0]
                                        idn=f[1]
                                        ag=f[2]
                                        mob=f[3]
                                        res=f[4]
                                        print("| Staff_ID=%s | Staff_Name=%s | Age=%s | Mobile_Number=%s | Reason=%s |"%(idm,idn,ag,mob,res)) 
                                        print("")
                                spdude()
                            else:
                                print("")
                                print("-ENTER CORRECT OPTION-")
                                print("")
                                spdude()
                        stouk()
                    elif(spch==7):
                        print('')
                        print("WARNING DIVISION(STAFFS)")
                        print('------------------------')
                        print('NOTE: MAX PERMISSIBLE WARNING BEFORE GETTING BANNED=3')
                        n=int(input('Enter no.of staffs to be warned:'))
                        for i in range(n):
                            idm=int(input('Enter staff ID:'))
                            maxi='select Warning from staffs where Staff_ID=%s'%(idm)
                            na='select Staff_Name from staffs where Staff_ID=%s'%(idm)
                            age='select Age from staffs where Staff_ID=%s'%(idm)
                            mob='select Mobile_Number from staffs where Staff_ID=%s'%(idm)
                            m.execute(age)
                            ra=m.fetchone()
                            m.execute(mob)
                            rm=m.fetchone()
                            m.execute(na)
                            ro=m.fetchone()
                            m.execute(maxi)
                            re=m.fetchall()
                            for z in ra:
                                ag=z
                            for u in rm:
                                mo=u
                            for name in ro:
                                nam=name
                            for p in re:
                                maxv=p[0]
                                ma=maxv+1
                            sq="UPDATE staffs SET Warning = %s WHERE Staff_ID = %s"
                            rol=[(ma,idm)]
                            m.executemany(sq, rol)
                            c.commit()
                            print('')
                            print('--THE STAFF',nam.upper(),'HAS BEEN WARNED--')
                            print('CURRENT NO. OF WARNINGS=',ma)
                            print('')
                            if(ma==3):
                                print('The Staff with ID:',idm,'and Name:',nam,'has exceeded the permissible no. of warnings.')
                                ty=int(input('Do you want to FIRE(BAN) them?\n(1)Yes\n(2)No\nEnter your choice:'))
                                if(ty==1):
                                    reas=str(input('Enter reason for firing(if any in specific):'))
                                    u="UPDATE staffs SET Status ='Fired' WHERE Warning = %s"%(ma)
                                    m.execute(u)
                                    i='insert into Staff_Fired(Staff_ID, Staff_Name, Age, Mobile_Number, Reason) values(%s,%s,%s,%s,%s)'
                                    val=[(idm,nam,ag,mo,reas)]
                                    m.executemany(i,val)
                                    c.commit()
                                    print('--THE STAFF',nam.upper(),'(',idm,')','HAS BEEN FIRED(BANNED)--')
                                    spdude()
                                elif(ty==2):
                                    spdude()
                                else:
                                    print("-ENTER CORRECT OPTION-")
                                    spdude()
                            elif(ma>3):
                                jk='select status from staffs where Staff_ID=%s'%(idm)
                                m.execute(jk)
                                jok=m.fetchone()
                                for f in jok:
                                    fir=f
                                if(fir=='Fired'):
                                    print('--SELECTED STAFF IS ALREADY FIRED!--')
                                else:
                                    print('The Staff with ID:',idm,'and Name:',nam,'has exceeded the permissible no. of warnings.')
                                    ty=int(input('Do you want to FIRE(BAN) them?\n(1)Yes\n(2)No\nEnter your choice:'))
                                    if(ty==1):
                                        reas=str(input('Enter reason for firing(if any in specific):'))
                                        u="UPDATE staffs SET Status ='Fired' WHERE Warning = %s"%(ma)
                                        m.execute(u)
                                        i='insert into Staff_Fired(Staff_ID, Staff_Name, Age, Mobile_Number, Reason) values(%s,%s,%s,%s,%s)'
                                        val=[(idm,nam,ag,mo)]
                                        m.executemany(i,val)
                                        c.commit()
                                        print('--THE STAFF',nam.upper(),'(',idm,')','HAS BEEN FIRED(BANNED)--')
                                        spdude()
                                    elif(ty==2):
                                        spdude()
                                    else:
                                        print("-ENTER CORRECT OPTION-")
                                        spdude()
                        spdude()            
                    elif(spch==6):
                        def steak():
                            print('')
                            print('BANNED STUDENTS')
                            print('---------------')
                            l=int(input('(1)View Specific records\n(2)View all records\n(3)Help\n(4)Back\nEnter Choice:'))
                            print("")
                            if(l==4):
                                spdude()
                            elif(l==3):
                                print('HELP')
                                print('----')
                                print('(1) is used to view specific records\n(2) is used to view all records')
                                steak()
                            elif(l==2):
                                s='select * from Stud_Profile'
                                m.execute(s)
                                f=m.fetchall()
                                if(f==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for i in f:
                                        idm=i[0]
                                        idn=i[1]
                                        pro=i[2]
                                        print("| ID_Number=%s | Name=%s | Profile=%s |"%(idm,idn,pro)) 
                                        print("")
                                    spdude()
                            elif(l==1):
                                n=int(input('Enter no of banned records to be viewed:'))
                                for i in range(n):
                                    a=int(input('Enter Student ID:'))
                                    s='select * from Stud_Profile where ID_Number=%s'%(a)
                                    m.execute(s)
                                    f=m.fetchone()
                                    print('')
                                    if(f==None):
                                        print("-EMPTY-")
                                        print("")
                                    else:
                                        idm=f[0]
                                        idn=f[1]
                                        pro=f[2]
                                        print("| ID_Number=%s | Name=%s | Profile=%s |"%(idm,idn,pro)) 
                                        print("")
                                spdude()
                            else:
                                print("-ENTER CORRECT OPTION-")
                                spdude()
                        steak()
                    elif(spch==5):
                        def stak():
                            print('BOOKS')
                            print('-----')
                            l=int(input("(1)View specific books\n(2)View all books\n(3)Help\n(4)Back\nEnter:"))
                            print("")
                            if(l==4):
                                print('')
                                spdude()
                            elif(l==3):
                                print('')
                                print('HELP')
                                print('----')
                                print('(1) is used to view specific records\n(2) is used to view all records')
                                print('')
                                stak()
                            elif(l==2):
                                s="select * from Books"
                                m.execute(s)
                                res=m.fetchall()
                                if(res==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for r in res:
                                        Book_ID=r[0]
                                        Book_Name=r[1]
                                        Status=r[2]
                                        print("| Book-ID=%d | Name=%s | Status=%s |"%(Book_ID,Book_Name,Status))
                                        print('')
                                    spdude()
                            elif(l==1):
                                n=int(input("Enter number of books to be viewed:"))
                                for i in range(n):
                                    bi=int(input("Enter Book ID:"))
                                    s="select * from Books where Book_ID=%s"%(bi)
                                    m.execute(s)
                                    res=m.fetchone()
                                    print('')
                                    if(res==None):
                                        print("-BOOK DOES NOT EXIST-")
                                        print("")
                                    else:
                                        Book_ID=res[0]
                                        Book_Name=res[1]
                                        Status=res[2]
                                        print("| Book-ID=%d | Name=%s | Status=%s |"%(Book_ID,Book_Name,Status))
                                        print('')
                                spdude()
                            else:
                                print("-ENTER CORRECT OPTION-")
                                spdude()
                        stak()
                    elif(spch==4):
                        def tok():
                            print('STUDENTS')
                            print('--------')
                            l=int(input("(1)View specific records\n(2)View temporary records\n(3)View permanent records\n(4)View all\n(5)Help\n(6)Back\nEnter Choice:"))
                            print("")
                            if(l==6):
                                print('')
                                spdude()
                            elif(l==5):
                                print('')
                                print('HELP')
                                print('----')
                                print('(1) is used to view specific records\n(2) is used to temporary students records\n(3) is used to view permanent student records\n(4) is used to view all records')
                                print('')
                                tok()
                            elif(l==4):
                                s='select * from students'
                                m.execute(s)
                                f=m.fetchall()
                                if(f==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for i in f:
                                        idn=i[0]
                                        idm=i[1]
                                        cl=i[2]
                                        mb=i[3]
                                        ps=i[4]
                                        wr=i[5]
                                        pro=i[6]
                                        print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s |"%(idn,idm,cl,mb,ps,wr,pro))
                                        print('')
                                    spdude()
                            elif(l==1):
                                n=int(input('Enter no. of students to be viewed:'))
                                for i in range(n):
                                    si=input("Enter student ID:")
                                    s='select * from students where ID_Number=%s'%(si)
                                    m.execute(s)
                                    f=m.fetchone()
                                    print('')
                                    if(f==None):
                                        print("-EMPTY-")
                                        print("")
                                    else:
                                        idn=f[0]
                                        idm=f[1]
                                        cl=f[2]
                                        mb=f[3]
                                        ps=f[4]
                                        wr=f[5]
                                        pro=f[6]
                                        mem=f[8]
                                        print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s | Membership=%s"%(idn,idm,cl,mb,ps,wr,pro,mem))
                                        print('')
                                spdude()
                            elif(l==2):
                                s='select * from students where Membership="Temporary"'
                                m.execute(s)
                                f=m.fetchall()
                                if(f==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for i in f:
                                        idn=i[0]
                                        idm=i[1]
                                        cl=i[2]
                                        mb=i[3]
                                        ps=i[4]
                                        wr=i[5]
                                        pro=i[6]
                                        mem=i[8]
                                        print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s | Membership=%s"%(idn,idm,cl,mb,ps,wr,pro,mem))
                                        print('')
                                    spdude()
                            elif(l==3):
                                s='select * from students where Membership="Permanent"'
                                m.execute(s)
                                f=m.fetchall()
                                if(f==[]):
                                    print("-EMPTY-")
                                    print("")
                                    spdude()
                                else:
                                    for i in f:
                                        idn=i[0]
                                        idm=i[1]
                                        cl=i[2]
                                        mb=i[3]
                                        ps=i[4]
                                        wr=i[5]
                                        pro=i[6]
                                        mem=i[8]
                                        print("| ID_Number=%s | Name=%s | Class=%s | Mobile Number=%s | Password=%s | Warning=%s | Profile=%s | Membership=%s |"%(idn,idm,cl,mb,ps,wr,pro,mem))
                                        print('')
                                        spdude()
                            else:
                                print("-ENTER CORRECT OPTION-")
                                spdude()
                        tok()
                    else:
                        print("-ENTER CORRECT OPTION-")
                        print("")
                        spdude()
            else:
                print("")
                print("-WRONG PASSWORD OR USERNAME-")
                print("")
                svd()
            spdude()
        svd()
    else:
        print('')
        print("-OPTION DOESN'T EXIST-")
        print('')
        libr()
libr()

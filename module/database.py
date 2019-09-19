import pymysql
import datetime

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","","html_proj")

    def check_login1(self,data):
        con=Database.connect(self)
        cursor=con.cursor()
        try:
            cursor.execute("SELECT * FROM signup where username=%s and password=%s",(data['username'],data['password'],))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()

    def sign(self,data):
        con=Database.connect(self)
        cursor=con.cursor()
        cursor.execute("INSERT INTO signup(full_name,dob,email,username,password,mobile,gender,type)VALUES(%s,%s,%s,%s,%s,%s,%s,'User')",(data['full_name'],data['dob'],data['email'],data['username'],data['password'],data['mobile'],data['gender'],))
        con.commit()
        con.close()
			
    def iit(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'iit' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()


    def nit(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'nit' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()
                    

    def top10engg(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'top10engg' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()			

			
    def iim(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'iim' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()

    def top10mba(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'top10mba' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()

    def top10law(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'top10law' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()

    def top10medpvt(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'top10medpvt' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()
                    
    def  top10medgovt(self):
            con = Database.connect(self)
            cursor = con.cursor()
    
            try: 
                    cursor.execute("SELECT * FROM colleges where type = 'top10medgovt' order by rank asc")

                    return cursor.fetchall()
            except:
                    return()
            finally:
                    con.close()
                                        

    def contactus(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("INSERT INTO contactus VALUES(%s, %s,%s)", (data['name'],data['email'],data['message']))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
            
    def adm_signup(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM signup where type='User' order by full_name asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_top10mba(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='top10mba' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_iim(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='iim' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_top10engg(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='top10engg' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_iit(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='iit' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_nit(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='nit' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_top10medgovt(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='top10medgovt' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_top10medpvt(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='top10medpvt' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  

    def adm_top10law(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM colleges where type='top10law' order by rank asc;")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()  


    def adm_contactus(self):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("SELECT * FROM contactus order by name asc")
            return cursor.fetchall()
        except:
            return
            
        finally:
            con.close()
      
    def read_contactus(self, name):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if name == None:
                cursor.execute("SELECT * FROM contactus")
                return cursor.fetchall()
            else: 
                cursor.execute("SELECT * FROM contactus where name = %s ", (name,))
                return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def delete_contactus(self, name):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM contactus where name= %s", (name,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()

    def read_colleges(self, sno):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if sno == None:
                cursor.execute("SELECT * FROM colleges ")
            else: 
                cursor.execute("SELECT * FROM colleges where sno= %s ", (sno,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()            
       
    def delete_colleges(self, sno):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM colleges where sno= %s", (sno,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()

    def update_colleges(self, sno,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("UPDATE colleges set image = %s, name = %s, state = %s, rank = %s, link =%s, type = %s where sno = %s", (data['image'],data['name'],data['state'],data['rank'],data['link'],data['type'],sno,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()         

    def insert_colleges(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        cursor.execute("INSERT INTO colleges(image,name,state,rank,link,type) VALUES(%s,%s,%s,%s,%s,%s)",(data['image'],data['name'],data['state'],data['rank'],data['link'],data['type'],))
        con.commit()
        con.close()         

    def read_signup(self, username):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if username == None:
                cursor.execute("SELECT * FROM signup")
                return cursor.fetchall()
            else: 
                cursor.execute("SELECT * FROM signup where username = %s ", (username,))
                return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def delete_signup(self, username):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM signup where username= %s", (username,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()

    def update_signup(self, username,data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("UPDATE signup set full_name='%s', dob='%s', email='%s', username='%s', password='%s',mobile='%d',gender='%s',type='%s' where username = %s", (data['full_name'],data['dob'],data['email'],data['username'],data['password'],data['mobile'],data['gender'],data['type'],username,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()         

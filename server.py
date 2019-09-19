'''Created By- Ruchika and Rubina'''

from flask import Flask,flash,render_template,redirect,url_for,request,session
from module.database import Database
import os
import urllib
import sqlite3

app=Flask(__name__)
app.secret_key="mys3cr3tk3y"
db = Database()



@app.route('/')
def home_page():
    if 'username' not in session:
        return render_template('home_page.html')
    else:
        return render_template("home_page_logout.html")

@app.route('/home_page_logout')
def home_page_logout():
    return render_template('home_page_logout.html')

@app.route('/about1')
def about():
    return render_template('about.html')

#contactus
@app.route('/contact1')
def contact():
    return render_template('contactus.html')

@app.route('/contactus', methods = ['POST', 'GET'])
def contactus():
    if request.method == 'POST':
        if db.contactus(request.form):
            flash("New Record  Added")
        else:
            flash("New Record not Added")
        return redirect(url_for('contact'))
    else:
        return redirect(url_for('home_page'))


#login pages
@app.route('/user')
def user():
    return render_template('user_login.html')	

@app.route('/user_login', methods = ['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        n = db.check_login1(request.form)
        if len(n)==0:
            return redirect(url_for('invalid'))
        for row in n:
            s=row[3]
            t=row[7]
            session['username']=s
            if t=='Admin':
                return render_template('welcome.html')
            elif t=='User':
                return redirect(url_for('home_page_logout'))
            else:
                return render_template('signup.html')
        else:
            return redirect(url_for('home_page'))
    else:
        return redirect(url_for('user_login'))

@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('home_page'))


#signup pages
@app.route('/sign')
def sign():
    return render_template('signup.html')

@app.route('/insert_user', methods=['POST'])
def signup():
    if request.method=='POST':
        db.sign(request.form)
        return render_template('home_page.html')
    else:
        return render_template('signup.html')


#main stream pages
@app.route('/engg')
def engg():
    if 'username' not in session:
        return render_template('user_login.html')
    return render_template('engg.html')

@app.route('/mba')
def mba():
    if 'username' not in session:
        return render_template('user_login.html')
    return render_template('management.html')

@app.route('/medical')
def medical():
    if 'username' not in session:
        return render_template('user_login.html')
    return render_template('medical.html')

@app.route('/law')
def law():
    if 'username' not in session:
        return render_template('user_login.html')
    return render_template('law.html')


#sub streams
@app.route('/nit')
def nit():
    data=db.nit()
    return render_template('nit.html',data=data)

@app.route('/iit')
def iit():
    data=db.iit()
    return render_template('iit.html',data=data)

@app.route('/top10engg')
def top10engg():
    data=db.top10engg()
    return render_template('top10engg.html',data=data)

@app.route('/iim')
def iim():
    data=db.iim()
    return render_template('iim.html',data=data)

@app.route('/top10mba')
def top10mba():
    data=db.top10mba()
    return render_template('top10mba.html',data=data)

@app.route('/top10medpvt')
def top10medpvt():
    data=db.top10medpvt()
    return render_template('top10medpvt.html',data=data)

@app.route('/top10medgovt')
def top10medgovt():
    data=db.top10medgovt()
    return render_template('top10medgovt.html',data=data)

@app.route('/top10law')
def top10law():
    data=db.top10law()
    return render_template('top10law.html',data=data)

@app.route('/highsec')
def highsec():
    if 'username' not in session:
        return render_template('user_login.html')
    return render_template('highsec.html')


#higher secondary pages
@app.route('/12medical')
def medical12():
    return render_template('12medical.html')

@app.route('/12nonmedical')
def nonmedical12():
    return render_template('12nonmedical.html')

@app.route('/12commerce')
def commerce12():
    return render_template('12commerce.html')

@app.route('/12arts')
def arts12():
    return render_template('12arts.html')

#top10engg pages
@app.route('/bitspilani')
def bitspilani():
    return render_template('bitspilani.html')

@app.route('/delhitechnological')
def delhitechnologicals():
    return render_template('delhitechnological.html')

@app.route('/bitsmesra')
def bitsmesra():
    return render_template('bitsmesra.html')

@app.route('/https://www.iiit.ac.in/')
def iiith():
    with urllib.request.urlopen('https://www.iiit.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.nsit.ac.in/')
def nsit():
    with urllib.request.urlopen('http://www.nsit.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.annauniv.edu/')
def au():
    with urllib.request.urlopen('https://www.annauniv.edu/') as response:
        html=response.read()
    return html

@app.route('/http://www.jaduniv.edu.in/')
def ju():
    with urllib.request.urlopen('http://www.jaduniv.edu.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.pec.ac.in/')
def pec():
    with urllib.request.urlopen('http://www.pec.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.iiita.ac.in/')
def iiita():
    with urllib.request.urlopen('https://www.iiita.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.coep.org.in/')
def cep():
    with urllib.request.urlopen('http://www.coep.org.in/') as response:
        html=response.read()
    return html


#iit pages
@app.route('/iitmadras')
def iitmadras():
    return render_template('iitmadras.html')

@app.route('/iitbombay')
def iitbombay():
    return render_template('iitbombay.html')

@app.route('/iitkharagpur')
def iitkharagpur():
    return render_template('iitkharagpur.html')


@app.route('/http://www.iitd.ac.in/')
def iitdelhi():
    with urllib.request.urlopen('http://www.iitd.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iitk.ac.in/')
def iitkanpur():
    with urllib.request.urlopen('http://www.iitk.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.iith.ac.in/')
def iithyderabad():
    with urllib.request.urlopen('https://www.iith.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iitg.ac.in/')
def iitguwahati():
    with urllib.request.urlopen(' http://www.iitg.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.iitr.ac.in/')
def iitroorkee():
    with urllib.request.urlopen(' https://www.iitr.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.iitbhu.ac.in/')
def iitvaranasi():
    with urllib.request.urlopen('https://www.iitbhu.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iiti.ac.in/')
def iitindore():
    with urllib.request.urlopen('http://www.iiti.ac.in/') as response:
        html=response.read()
    return html


#nit pages
@app.route('/nitnagpur')
def nitnagpur():
    return render_template('nitnagpur.html')

@app.route('/nitsurat')
def nitsurat():
    return render_template('nitsurat.html')

@app.route('/nittiruchirappalli')
def nittiruchirappalli():
    return render_template('nittiruchirappalli.html')

@app.route('/http://www.nitrkl.ac.in/')
def nitrourkela():
    with urllib.request.urlopen('http://www.nitrkl.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.nitk.ac.in/')
def nitsurathkal():
    with urllib.request.urlopen('http://www.nitk.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.nitw.ac.in/')
def nitwarangal():
    with urllib.request.urlopen('https://www.nitw.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.mnnit.ac.in/')
def mnnit():
    with urllib.request.urlopen('http://www.mnnit.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.nitc.ac.in/')
def nitcalicut():
    with urllib.request.urlopen('http://www.nitc.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.nits.ac.in/')
def nitsilchar():
    with urllib.request.urlopen('http://www.nits.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.nitdgp.ac.in/')
def nitdurgapur():
    with urllib.request.urlopen('http://www.nitdgp.ac.in/') as response:
        html=response.read()
    return html

	

#iim pages
@app.route('/iimahmedabad')
def iimahmedabad():
    return render_template('iimahmedabad.html')

@app.route('/iimbangalore')
def iimbangalore():
    return render_template('iimbangalore.html')

@app.route('/iimcalcutta')
def iimcalcutta():
    return render_template('iimcalcutta.html')

@app.route('/https://www.iimidr.ac.in/')
def iimindore():
    with urllib.request.urlopen('https://www.iimidr.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iiml.ac.in/')
def iimlucknow():
    with urllib.request.urlopen('http://www.iiml.ac.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.iimranchi.ac.in/')
def iimranchi():
    with urllib.request.urlopen('https://www.iimranchi.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iimkashipur.ac.in/')
def iimkashipur():
    with urllib.request.urlopen('http://www.iimkashipur.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iimrohtak.ac.in/')
def iimrohtak():
    with urllib.request.urlopen('http://www.iimrohtak.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iimk.ac.in/')
def iimkozhikode():
    with urllib.request.urlopen('http://www.iimk.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.iimraipur.ac.in/')
def iimraipur():
    with urllib.request.urlopen('http://www.iimraipur.ac.in/') as response:
        html=response.read()
    return html


#top10mba pages
@app.route('/xlrij')
def xlrij():
    return render_template('xlrij.html')

@app.route('/fmsd')
def fmsd():
    return render_template('fms.html')

@app.route('/spjimrm')
def spjimrm():
    return render_template('spjimrm.html')

@app.route('/https://www.mdi.ac.in/')
def mdig():
    with urllib.request.urlopen('https://www.mdi.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://tedu.iift.ac.in/iift/index.php')
def iiftnd():
    with urllib.request.urlopen('http://tedu.iift.ac.in/iift/index.php') as response:
        html=response.read()
    return html

@app.route('/http://www.imi.edu/')
def imind():
    with urllib.request.urlopen('http://www.imi.edu/') as response:
        html=response.read()
    return html

@app.route('/http://www.nmims.edu/')
def nmimsm():
    with urllib.request.urlopen('http://www.nmims.edu/') as response:
        html=response.read()
    return html

@app.route('/https://www.nitie.edu/')
def nitiem():
    with urllib.request.urlopen('https://www.nitie.edu/') as response:
        html=response.read()
    return html

@app.route('/http://jbims.edu/')
def jbimsm():
    with urllib.request.urlopen('http://jbims.edu/') as response:
        html=response.read()
    return html

@app.route('/http://www.isb.edu/pgp/campuses/hyderabad')
def isbh():
    with urllib.request.urlopen('http://www.isb.edu/pgp/campuses/hyderabad') as response:
        html=response.read()
    return html


#top10law colleges pages
@app.route('/nlsiub')
def nlsiub():
    return render_template('nlsiub.html')

@app.route('/wbnujsk')
def wbnujsk():
    return render_template('wbnujsk.html')

@app.route('/slsp')
def slsp():
    return render_template('slsp.html')

@app.route('/https://ilslaw.edu/')
def ils():
    with urllib.request.urlopen('https://ilslaw.edu/') as response:
        html=response.read()
    return html

@app.route('/http://www.bhu.ac.in/law/')
def flbhuv():
    with urllib.request.urlopen('http://www.bhu.ac.in/law/') as response:
        html=response.read()
    return html

@app.route('/http://www.amity.edu/als/')
def alsn():
    with urllib.request.urlopen('http://www.amity.edu/als/') as response:
        html=response.read()
    return html

@app.route('/https://www.amu.ac.in/dshowfacultydata2.jsp?did=16&eid=1603')
def amuv():
    with urllib.request.urlopen('https://www.amu.ac.in/dshowfacultydata2.jsp?did=16&eid=1603') as response:
        html=response.read()
    return html

@app.route('/http://bvpnlcpune.org/')
def bvnlp():
    with urllib.request.urlopen('http://bvpnlcpune.org/') as response:
        html=response.read()
    return html

@app.route('/https://www.jmi.ac.in/law')
def fljmid():
    with urllib.request.urlopen('https://www.jmi.ac.in/law') as response:
        html=response.read()
    return html

@app.route('/https://christuniversity.in/academics/school-of-law')
def slcub():
    with urllib.request.urlopen('https://christuniversity.in/academics/school-of-law') as response:
        html=response.read()
    return html


#top medical govt colleges
@app.route('/aiimsnd')
def aiimsnd():
    return render_template('aiimsnd.html')

@app.route('/kgmul')
def kgmul():
    return render_template('kgmul.html')

@app.route('/ucmsd')
def ucmsd():
    return render_template('ucmsd.html')

@app.route('/http://www.jipmer.puducherry.gov.in/')
def jipmerp():
    with urllib.request.urlopen('http://www.jipmer.puducherry.gov.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.bhu.ac.in/ims/')
def imsbhdv():
    with urllib.request.urlopen('http://www.bhu.ac.in/ims/') as response:
        html=response.read()
    return html

@app.route('/http://www.mamc.ac.in/')
def mamcnd():
    with urllib.request.urlopen('http://www.mamc.ac.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.afmc.nic.in/')
def afmcp():
    with urllib.request.urlopen('http://www.afmc.nic.in/') as response:
        html=response.read()
    return html

@app.route('/http://lhmc-hosp.gov.in/')
def lhmcwnd():
    with urllib.request.urlopen('http://lhmc-hosp.gov.in/') as response:
        html=response.read()
    return html

@app.route('/https://gmch.gov.in/')
def gmchc():
    with urllib.request.urlopen('https://gmch.gov.in/') as response:
        html=response.read()
    return html

@app.route('/http://www.kem.edu/')
def sgsmcakemmcm():
    with urllib.request.urlopen('http://www.kem.edu/') as response:
        html=response.read()
    return html

#top10 medical private colleges
@app.route('/cmcv')
def cmcv():
    return render_template('cmcv.html')

@app.route('/kmkm')
def kmkm():
    return render_template('kmcm.html')

@app.route('/sjmcb')
def sjmcb():
    return render_template('sjmcb.html')

@app.route('/http://cmcludhiana.in/medical_college/contactus.php')
def cmcl():
    with urllib.request.urlopen('http://cmcludhiana.in/medical_college/contactus.php') as response:
        html=response.read()
    return html

@app.route('/https://www.sriramachandra.edu.in/')
def srmcric():
    with urllib.request.urlopen('https://www.sriramachandra.edu.in/') as response:
        html=response.read()
    return html

@app.route('/https://www.jnmc.edu/')
def jnmcb():
    with urllib.request.urlopen('https://www.jnmc.edu/') as response:
        html=response.read()
    return html

@app.route('/https://manipal.edu/kmc-mangalore.html')
def kmcm():
    with urllib.request.urlopen('https://manipal.edu/kmc-mangalore.html') as response:
        html=response.read()
    return html

@app.route('/http://www.srmuniv.ac.in/medical-college/hospital-and-research-centre')
def srmmchrcc():
    with urllib.request.urlopen('http://www.srmuniv.ac.in/medical-college/hospital-and-research-centre') as response:
        html=response.read()
    return html

@app.route('/https://www.jssuni.edu.in/JSSWeb/WebShowFromDB.aspx?MID=0&CID=4&PID=10002')
def jssmchm():
    with urllib.request.urlopen('https://www.jssuni.edu.in/JSSWeb/WebShowFromDB.aspx?MID=0&CID=4&PID=10002') as response:
        html=response.read()
    return html

@app.route('/http://www.msrmc.ac.in/')
def msrmcb():
    with urllib.request.urlopen('http://www.msrmc.ac.in/') as response:
        html=response.read()
    return html




#extra pages		
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

@app.route('/invalid')
def invalid():
    return render_template('invalid.html')








#admin pages
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/adm_contactus')
def adm_contactus():
    data=db.adm_contactus()
    return render_template('adm_contactus.html',data=data)

@app.route('/adm_signup')
def adm_signup():
    data=db.adm_signup()
    return render_template('adm_signup.html',data=data)

#management pages
@app.route('/adm_top10mba')
def adm_top10mba():
    data=db.adm_top10mba()
    return render_template('adm_top10mba.html',data=data)

@app.route('/adm_iim')
def adm_iim():
    data=db.adm_iim()
    return render_template('adm_iim.html',data=data)

#engineering pages
@app.route('/adm_top10engg')
def adm_top10engg():
    data=db.top10engg()
    return render_template('adm_top10engg.html',data=data)

@app.route('/adm_iit')
def adm_iit():
    data=db.adm_iit()
    return render_template('adm_iit.html',data=data)

@app.route('/adm_nit')
def adm_nit():
    data=db.adm_nit()
    return render_template('adm_nit.html',data=data)

#medical pages
@app.route('/adm_top10medgovt')
def adm_top10medgovt():
    data=db.adm_top10medgovt()
    return render_template('adm_top10medgovt.html',data=data)

@app.route('/adm_top10medpvt')
def adm_top10medpvt():
    data=db.adm_top10medpvt()
    return render_template('adm_top10medpvt.html',data=data)

#law pages
@app.route('/adm_top10law')
def adm_top10law():
    data=db.adm_top10law()
    return render_template('adm_top10law.html',data=data)

#delete contactus details
@app.route('/delete/<string:name>')
def delete(name):
    data = db.read_contactus(name);
    
    if len(data) == 0:
        return render_template('adm_contactus.html')
    else:
        session['delete'] = name
        return render_template('delete_contactus.html', data = data)

@app.route('/delete_contactus', methods = ['POST'])
def delete_contactus():
    if request.method == 'POST':
        
        if db.delete_contactus(session['delete']):
            flash('data  has been deleted')
           
        else:
            flash('data has can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('adm_contactus'))
    else:
        return redirect(url_for('welcome'))

#delete colleges details
@app.route('/delete1/<string:sno>')
def delete1(sno):
    data = db.read_colleges(sno);
    
    if len(data) == 0:
        return redirect(url_for('welcome'))
    else:
        session['delete'] = sno
        return render_template('delete_colleges.html', data = data)

@app.route('/delete_colleges', methods = ['POST'])
def delete_colleges():
    if request.method == 'POST':
        
        if db.delete_colleges(session['delete']):
            flash('data  has been deleted')
           
        else:
            flash('data has can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('welcome'))


#update colleges details
@app.route('/update/<string:sno>')
def update(sno):
    data = db.read_colleges(sno);
    
    if len(data) == 0:
        return redirect(url_for('welcome'))
    else:
        session['update']=sno
        return render_template('update.html', data = data)

@app.route('/update_colleges', methods = ['POST'])
def update_colleges():
    if request.method == 'POST':
        db.update_colleges(session['update'],request.form)
        session.pop('update',None)
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('welcome'))

	
#insert new college
@app.route('/insert1')
def insert1():
    return render_template('insert_colleges.html')

@app.route('/insert_colleges', methods = ['POST'])
def insert_colleges():
    if request.method == 'POST':
        db.insert_colleges(request.form)
        return render_template('welcome.html')
    else:
        return render_template('welcome.html')


#delete signup details
@app.route('/delete2/<string:username>')
def delete2(username):
    data = db.read_signup(username);
    
    if len(data) == 0:
        return render_template('adm_signup.html')
    else:
        session['delete'] = username
        return render_template('delete_signup.html', data = data)

@app.route('/delete_signup', methods = ['POST'])
def delete_signup():
    if request.method == 'POST':
        
        if db.delete_signup(session['delete']):
            flash('data  has been deleted')
           
        else:
            flash('data has can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('adm_signup'))
    else:
        return redirect(url_for('welcome'))

#update signup details
@app.route('/update2/<string:username>/')
def update2(username):
    data = db.read_signup(username);
    
    if len(data) == 0:
        return redirect(url_for('adm_signup'))
    else:
        session['update']=username
        return render_template('update_signup.html', data = data)

@app.route('/update_signup', methods = ['POST'])
def update_signup():
    if request.method == 'POST':
        
        if db.update_signup(session['update'],request.form):
            flash('Data is updated')
           
        else:
            flash('Data cannot be updated')
        
        session.pop('update',None)
        return redirect(url_for('adm_signup'))
    else:
        return redirect(url_for('welcome'))

	

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")


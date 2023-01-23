from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pymysql
import webbrowser

db=pymysql.connect(host="localhost",user="root",password="",db="dbdigitalvehicle")
c=db.cursor()

######################################################################
#                                                                    #
#                                                                    #
#                           COMMON                                   #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    s="select * from tblrto where rtoemail in (select uname from tbllogin where status='1') order by rtoid desc limit 6"
    c.execute(s)
    rto=c.fetchall()
    s="select * from tblinsurancecompany where insEmail in (select uname from tbllogin where status='1') order by insId desc limit 6"
    c.execute(s)
    ins=c.fetchall()
    s="select * from tblpollutioncenter where polEmail in (select uname from tbllogin where status='1') order by polId desc limit 6"
    c.execute(s)
    pol=c.fetchall()
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where uname='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="rto"):
                        s="select * from tblrto where rtoEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/rtohome")
                    elif(i[2]=="insurance"):
                        s="select * from tblinsurancecompany where insEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/insurancehome")
                    elif(i[2]=="pollution"):
                        s="select * from tblpollutioncenter where polEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/pollutionhome")
                    elif(i[2]=="police"):
                        s="select * from tblpolice where pEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/policehome")
                    elif(i[2]=="customer"):
                        s="select * from tblvehicle where vNumber='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/customerhome")
                    
                elif(i[3]=="inactive"):
                    msg="Your registration is incomplete. Please register"
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"

    return render(request,"index.html",{"rto":rto,"ins":ins,"pol":pol})
######################################################################
#                           LOAD LOGIN PAGE
######################################################################
def login(request):
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where uname='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="rto"):
                        s="select * from tblrto where rtoEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/rtohome")
                    elif(i[2]=="insurance"):
                        s="select * from tblinsurancecompany where insEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/insurancehome")
                    elif(i[2]=="pollution"):
                        s="select * from tblpollutioncenter where polEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/pollutionhome")
                    elif(i[2]=="police"):
                        s="select * from tblpolice where pEmail='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/policehome")
                    elif(i[2]=="customer"):
                        s="select * from tblvehicle where vNumber='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/customerhome")
                    
                elif(i[3]=="inactive"):
                    msg="Your registration is incomplete. Please register"
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"commonlogin.html",{"msg":msg})
######################################################################
#                   LOAD RTO REGISTRATION PAGE
######################################################################
def rto(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        region=request.POST['txtRegion']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        pwd=request.POST['txtPassword']  
        licens=request.POST['txtLicense']  
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Already registered"
        else:
            s="insert into tblrto (rtoname,rtoregion,rtocontact,rtoemail,rtoLicense) values('"+name+"','"+region+"','"+contact+"','"+email+"','"+licens+"')"
            print(s)
            try:
                c.execute(s)
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','rto','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry some error occured"
                else:
                    msg="Registration successfull. Wait for approval"
    return render(request,"commonrto.html",{"msg":msg})
######################################################################
#                 LOAD INSURANCE COMPANY REGISTRATION PAGE
######################################################################
def insurance(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        address=request.POST['txtAddress']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        pwd=request.POST['txtPassword']     
        licens=request.POST['txtLicense'] 
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Already registered"
        else:   
            s="insert into tblinsurancecompany (insName,insAddress,insContact,insEmail,insLicense) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+licens+"')"
            print(s)
            try:
                c.execute(s)
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','insurance','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry some error occured"
                else:
                    msg="Registration successfull. Wait for approval"
    return render(request,"commoninsurance.html",{"msg":msg})
######################################################################
#                 LOAD POLLUTION CENTER REGISTRATION PAGE
######################################################################
def pollution(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        address=request.POST['txtAddress']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        pwd=request.POST['txtPassword']
        lic=request.POST['txtLicense']  
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Already exist"
        else: 
            s="insert into tblpollutioncenter (polName,polAddress,polContact,polEmail,polLicense) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+lic+"')"
            print(s)
            try:
                c.execute(s)
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','pollution','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry some error occured"
                else:
                    msg="Registration successfull. Wait for approval"
    return render(request,"commonpollution.html",{"msg":msg})
######################################################################
#                 LOAD POLICE REGISTRATION PAGE
######################################################################
def police(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        station=request.POST['txtStation']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        pwd=request.POST['txtPassword']
        aadhar=request.POST['txtAadhar'] 
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Already exist"
        else:
            s="insert into tblpolice (pName,pStation,pContact,pEmail,pAadhar,pPhoto) values('"+name+"','"+station+"','"+contact+"','"+email+"','"+aadhar+"','"+uploaded_file_url+"')"
            print(s)
            try:
                c.execute(s)
            except:
                msg="Sorry registration error"
            else:
                s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','police','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry some error occured"
                else:
                    msg="Registration successfull. Wait for approval"
    return render(request,"commonpolice.html",{"msg":msg})

######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def adminhome(request):
    return render(request,"adminhome.html")
def adminrto(request):
    s="select tblrto.*,tbllogin.status from tblrto,tbllogin where tbllogin.uname=tblrto.rtoEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminrto.html",{"data":data})
def admininsurance(request):
    s="select tblinsurancecompany.*,tbllogin.status from tblinsurancecompany,tbllogin where tbllogin.uname=tblinsurancecompany.insEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"admininsurance.html",{"data":data})
def adminpollution(request):
    s="select tblpollutioncenter.*,tbllogin.status from tblpollutioncenter,tbllogin where tbllogin.uname=tblpollutioncenter.polEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminpollution.html",{"data":data})
def adminpolice(request):
    s="select tblpolice.*,tbllogin.status from tblpolice,tbllogin where tbllogin.uname=tblpolice.pEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminpolice.html",{"data":data})
def updateuser(request):
    email=request.GET.get("id")
    status=request.GET.get("status")
    url=request.GET.get("url")
    s="update tbllogin set status='"+status+"' where uname='"+email+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect(url)
def adminfeedback(request):
    s="select tblfeedback.*,tblvehicle.rcowner from tblfeedback,tblvehicle where tblfeedback.vid=tblvehicle.vid"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminfeedback.html",{"data":data})
######################################################################
#                                                                    #
#                                                                    #
#                           RTO                                      #
#                                                                    #
#                                                                    #
######################################################################
def rtohome(request):
    return render(request,"rtohome.html")
def rtoaddvehicle(request):
    msg=""
    rto=request.session['id']
    s="SELECT DATE_ADD((select sysdate()), INTERVAL 365 DAY)"
    c.execute(s)
    data=c.fetchone()
    edate=data[0]
    s="select * from tblinsurancecompany where insEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    ins=c.fetchall()
    print(ins)
    if request.POST:
        number=request.POST['txtNumber']
        chasis=request.POST['txtChasis']
        manu=request.POST['txtManu']
        rc=request.POST['txtName']
        address=request.POST['txtAddress']
        contact=request.POST['txtContact']
        ins=request.POST['ins']
        s="insert into tblvehicle (rtoId,vNumber,vChasis,manufacturer,rcowner,address,contact,insExp,polExp,insId) values('"+str(rto)+"','"+str(number)+"','"+str(chasis)+"','"+str(manu)+"','"+str(rc)+"','"+str(address)+"','"+str(contact)+"','"+str(edate)+"','"+str(edate)+"','"+str(ins)+"')"
        s1=f"insert into tblowner(vId,ownerName,ownerAddress,ownerContact) values((select max(vid) from tblvehicle),'{rc}','{address}','{contact}')"
        try:
            c.execute(s)
            c.execute(s1)
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin (uname,pwd,utype,status) values('"+number+"','"+contact+"','customer','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Registration successfull."
    return render(request,"rtoaddvehicle.html",{"edate":edate,"msg":msg,"ins":ins})
def rtoviewvehicle(request):
    rto=request.session['id']
    s="select tblvehicle.*,tblrto.rtoName from tblvehicle, tblrto where tblvehicle.rtoId=tblrto.rtoId and tblvehicle.rtoId='"+str(rto)+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        no=request.POST['txtNumber']
        s="select tblvehicle.*,tblrto.rtoName from tblvehicle, tblrto where tblvehicle.rtoId=tblrto.rtoId and tblvehicle.vNumber='"+no+"'"
        c.execute(s)
        data=c.fetchall()
    return render(request,"rtoviewvehicle.html",{"data":data})
def rtoownership(request):
    data=""
    msg=""
    rto=request.session['id']
    if 'search' in request.POST:
        num=request.POST['txtNumber']
        s="select * from tblvehicle where vNumber='"+num+"'"
        c.execute(s)
        data=c.fetchall()
    if 'update' in request.POST:
        num=request.POST['txtNumber']
        name=request.POST['txtName']
        address=request.POST['txtAddress']
        contact=request.POST['txtContact']
        s="select vid from tblvehicle where vNumber='"+num+"'"
        c.execute(s)
        d=c.fetchone()
        vid=d[0]
        s=f"update tblvehicle set rcowner='{name}',address='{address}',contact='{contact}',rtoId='{rto}' where vid='{vid}'"
        c.execute(s)
        s=f"insert into tblowner(vId,ownerName,ownerAddress,ownerContact) values('{vid}','{name}','{address}','{contact}')"
        c.execute(s)
        s=f"update tbllogin set pwd='{contact}' where uname='{num}'"
        c.execute(s)
        db.commit()
        msg="Data updated"
    return render(request,"rtoownership.html",{"data":data,"msg":msg})
######################################################################
#                                                                    #
#                                                                    #
#                           CUSTOMER                                 #
#                                                                    #
#                                                                    #
######################################################################
def customerhome(request):
    vid=request.session['id']
    s="SELECT tblvehicle.*,tblrto.rtoName,tblinsurancecompany.insName from tblvehicle,tblrto,tblinsurancecompany where tblvehicle.vid='"+str(vid)+"' and tblvehicle.rtoId=tblrto.rtoId and tblinsurancecompany.insId=tblvehicle.insId"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerhome.html",{"data":data})
def customerinsurance(request):
    vid=request.session['id']
    s="SELECT tblvehicle.*,tblrto.rtoName,tblinsurancecompany.insName from tblvehicle,tblrto,tblinsurancecompany where tblvehicle.vid='"+str(vid)+"' and tblvehicle.rtoId=tblrto.rtoId and tblinsurancecompany.insId=tblvehicle.insId"
    c.execute(s)
    data=c.fetchall()
    insid=data[0][10]
    s="SELECT DATEDIFF((select sysdate()), (select insExp from tblvehicle where vid='"+str(vid)+"'))"
    c.execute(s)
    d=c.fetchone()
    diff=d[0]
    print(diff)
    if request.POST:
        s="insert into tblinsurancedetails(vid,iDate,amt,insId) values('"+str(vid)+"',(select sysdate()),'1000','"+str(insid)+"') "
        c.execute(s)
        db.commit()
        s="SELECT DATE_ADD((select sysdate()), INTERVAL 365 DAY)"
        c.execute(s)
        data=c.fetchone()
        edate=data[0]
        s="update tblvehicle set insExp='"+str(edate)+"' where vid='"+str(vid)+"' "
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/payment")
    return render(request,"customerinsurance.html",{"data":data,"diff":diff})
def customerfeedback(request):
    msg=""
    vid=request.session['id']
    if request.POST:
        feedback=request.POST['txtFeedback']
        s="insert into tblfeedback(fDate,vid,feedback) values((select sysdate()),'"+str(vid)+"','"+str(feedback)+"') "
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Feedback added successfully"
    return render(request,"customerfeedback.html",{"msg":msg})
def payment(request):
    if request.POST:
        return HttpResponseRedirect("/customerinsurance")
    return render(request,"payment.html")
def customercase(request):
        vid=request.session['id']
        s="select * from tblcase where vid ='"+str(vid)+"'"
        c.execute(s)
        data=c.fetchall()
        return render(request,"customercase.html",{"data":data})
def payment1(request):
    amt=request.GET.get("amt")
    cid=request.GET.get("id")
    if request.POST:
        s="update tblcase set status='paid' where caseId='"+cid+"'"
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/customercase")
    return render(request,"payment1.html",{"amt":amt})
######################################################################
#                                                                    #
#                                                                    #
#                           INSURANCE                                #
#                                                                    #
#                                                                    #
######################################################################
def insurancehome(request):
    return render(request,"insurancehome.html")
def insurancerenew(request):
    msg=""
    if request.POST:
        insId=request.session['id']
        vnumber=request.POST['txtNumber']
        myfile=request.FILES.get("txtFile")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)
        s="SELECT vid from tblvehicle where vNumber='"+str(vnumber)+"' "
        c.execute(s)
        data=c.fetchone()
        vid=data[0]
        request.session['vid']=vid
        s="insert into tblinsurancedetails(vid,iDate,amt,insId,img) values('"+str(vid)+"',(select sysdate()),'1000','"+str(insId)+"','"+uploaded_file_url+"') "
        c.execute(s)
        db.commit()
        s="SELECT DATE_ADD((select sysdate()), INTERVAL 365 DAY)"
        c.execute(s)
        data=c.fetchone()
        edate=data[0]
        s="update tblvehicle set insExp='"+str(edate)+"',insId='"+str(insId)+"' where vid='"+str(vid)+"' "
        c.execute(s)
        db.commit()
        msg="Insurance updated"
    return render(request,"insurancerenew.html",{"msg":msg})
def getinsurance(request):
    no=request.GET.get("no")
    s="select count(*) from tblvehicle where  vNumber='"+no+"'"
    c.execute(s)
    d=c.fetchone()
    edate=""
    if d[0]>0:
        s="select insExp from tblvehicle where  vNumber='"+no+"'"
        c.execute(s)
        d=c.fetchone()
        edate=d[0]
    else:
        edate="Not found"
    return HttpResponse(edate)
def insurancedetails(request):
    vid=request.session['vid']
    insId=request.session['id']
    s="select tblvehicle.vNumber,tblvehicle.vChasis,tblvehicle.insExp,tblinsurancedetails.amt,tblinsurancedetails.img from tblvehicle,tblinsurancedetails where tblvehicle.vid='"+str(vid)+"' and tblvehicle.vid=tblinsurancedetails.vId and tblinsurancedetails.iId=(select max(iId) from tblinsurancedetails)"
    c.execute(s)
    data=c.fetchall()
    s="select sysdate()"
    c.execute(s)
    d=c.fetchone()
    tdate=d[0]
    s=f"select insName from tblinsurancecompany where insId='{insId}'"
    c.execute(s)
    d=c.fetchone()
    insname=d[0]
    return render(request,"insurancedetails.html",{"data":data,"tdate":tdate,"insname":insname})
######################################################################
#                                                                    #
#                                                                    #
#                           POLLUTION                                #
#                                                                    #
#                                                                    #
######################################################################
def pollutionhome(request):
    return render(request,"pollutionhome.html")
def pollutionrenew(request):
    msg=""
    if request.POST:
        insId=request.session['id']
        vnumber=request.POST['txtNumber']
        amt=request.POST['txtAmt']
        myfile=request.FILES.get("txtFile")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)
        s="SELECT vid from tblvehicle where vNumber='"+str(vnumber)+"' "
        c.execute(s)
        data=c.fetchone()
        vid=data[0]
        request.session['vid']=vid
        s="insert into tblpollutiondetails(vId,polId,polDate,amt,img) values('"+str(vid)+"','"+str(insId)+"',(select sysdate()),'"+str(amt)+"','"+str(uploaded_file_url)+"') "
        c.execute(s)
        db.commit()
        s="SELECT DATE_ADD((select sysdate()), INTERVAL 365 DAY)"
        c.execute(s)
        data=c.fetchone()
        edate=data[0]
        s="update tblvehicle set polExp='"+str(edate)+"' where vid='"+str(vid)+"' "
        c.execute(s)
        db.commit()
        msg="Pollution updated"
    return render(request,"pollutionrenew.html",{"msg":msg})
def getpollution(request):
    no=request.GET.get("no")
    s="select count(*) from tblvehicle where  vNumber='"+no+"'"
    c.execute(s)
    d=c.fetchone()
    edate=""
    if d[0]>0:
        s="select polExp from tblvehicle where  vNumber='"+no+"'"
        c.execute(s)
        d=c.fetchone()
        edate=d[0]
    else:
        edate="Not found"
    return HttpResponse(edate)
def pollutiondetails(request):
    vid=request.session['vid']
    insId=request.session['id']
    s="select tblvehicle.vNumber,tblvehicle.vChasis,tblvehicle.polExp,tblpollutiondetails.amt,tblpollutiondetails.img from tblvehicle,tblpollutiondetails where tblvehicle.vid='"+str(vid)+"' and tblvehicle.vid=tblpollutiondetails.vId and tblpollutiondetails.poluId=(select max(poluId) from tblpollutiondetails)"
    c.execute(s)
    data=c.fetchall()
    s="select sysdate()"
    c.execute(s)
    d=c.fetchone()
    tdate=d[0]
    s=f"select polName from tblpollutioncenter where polId='{insId}'"
    c.execute(s)
    d=c.fetchone()
    insname=d[0]
    return render(request,"pollutiondetails.html",{"data":data,"tdate":tdate,"insname":insname})
######################################################################
#                                                                    #
#                                                                    #
#                           POLICE                                   #
#                                                                    #
#                                                                    #
######################################################################
def policehome(request):
    return render(request,"policehome.html")
def findvehicle(request):
    no=request.GET.get("no")
    s="select count(*) from tblvehicle where  vNumber='"+no+"'"
    c.execute(s)
    d=c.fetchone()
    return HttpResponse(d[0])
def policecase(request):
    msg=""
    if request.POST:
        pId=request.session['id']
        vnumber=request.POST['txtNumber']
        case=request.POST['txtCase']
        fine=request.POST['txtFine']
        s="SELECT vid from tblvehicle where vNumber='"+str(vnumber)+"' "
        c.execute(s)
        data=c.fetchone()
        vid=data[0]
        request.session['vid']=vid
        s="insert into tblcase(vid,casedetails,fine,pid,cdate,status) values('"+str(vid)+"','"+case+"','"+str(fine)+"','"+str(pId)+"',(select sysdate()),'case reported') "
        print(s)
        c.execute(s)
        db.commit()
        msg="Case updated"
    return render(request,"policecase.html",{"msg":msg})
def policecasestatus(request):
    data=""
    dates=[]
    if request.POST:
        vnumber=request.POST['txtNumber']
        s="select insExp,polExp from tblvehicle where vNumber='"+str(vnumber)+"' "
        c.execute(s)
        dates=c.fetchall()
        s="select * from tblcase where vid in(select vid from tblvehicle where vNumber='"+str(vnumber)+"') "
        c.execute(s)
        data=c.fetchall()
    return render(request,"policecasestatus.html",{"data":data,"dates":dates})
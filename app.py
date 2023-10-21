from flask import Flask,render_template,url_for,request,redirect
import requests
app=Flask(__name__)
URL="https://api.mfapi.in/mf/"
detail=[]


@app.route('/',methods =['POST','GET'])
def home():
    if request.method=='POST':
        fundcode=request.form.get("fundcode")
        api=requests.get(URL+str(fundcode))
        api_js=api.json()
        name=request.form.get('name')
        fund_house=api_js.get('meta').get('fund_house')
        invested_amount=request.form.get('investedamount')
        unitheld=request.form.get('unitheld')
        nav=api_js.get('data')[0].get('nav')
        currentvalue=float(nav)*float(invested_amount)
        growth=float(currentvalue)-float(unitheld)
        detail_dict={}
        detail_dict['fundcode']=fundcode
        detail_dict['name']=name
        detail_dict['fund_house']=fund_house
        detail_dict['invested_amount']=invested_amount
        detail_dict['unitheld']=unitheld
        detail_dict['nav']=nav
        detail_dict['currentvalue']=currentvalue
        detail_dict['growth']=growth
        detail.append(detail_dict)
    return render_template('home.html',detail=detail)

@app.route('/del/<a>',methods=['POST','GET'])
def delete(a):
    a=int(a)-1
    detail.pop(a)
    return render_template('home.html',detail=detail)

@app.route('/edit/<a>',methods=['POST','GET'])
def edit(a):
    a=int(a)-1  
    if request.method=='POST':    
        fundcode=request.form.get("fundcode")
        api=requests.get(URL+str(fundcode))
        api_js=api.json()
        name=request.form.get('name')
        fund_house=api_js.get('meta').get('fund_house')
        invested_amount=request.form.get('investedamount')
        unitheld=request.form.get('unitheld')
        nav=api_js.get('data')[0].get('nav')
        currentvalue=float(nav)*float(invested_amount)
        growth=float(currentvalue)-float(unitheld)
        edit_dict={}
        edit_dict['fundcode']=fundcode
        edit_dict['name']=name
        edit_dict['fund_house']=fund_house
        edit_dict['invested_amount']=invested_amount
        edit_dict['unitheld']=unitheld
        edit_dict['nav']=nav
        edit_dict['currentvalue']=currentvalue
        edit_dict['growth']=growth
        detail[a]=edit_dict
        return redirect(url_for('home'))
    return render_template('edit.html',val=detail[a])



if __name__=='__main__':
    app.run(debug=True)



    
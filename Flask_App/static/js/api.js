$("#btn_savedata").click(function(){
  debugger
  
  var uname=document.getElementById('nm').value;
  var email=document.getElementById('em').value;
  var phone=document.getElementById('ph').value;
  var gender=document.getElementById('gender').value;
  var addr=document.getElementById('addr').value;
  var pswd=document.getElementById('pswd').value;
  //alert(uname);
  
  var nmpattern=/^[a-zA-Z ]+$/;
  var phpattern=/^[6-9]{1}[0-9]{9}$/;
  var addrpattern=/^[a-zA-Z ]+$/;
  var empattern = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+$/;
  var pswdpattern = /^[a-zA-Z0-9]{5,8}$/;

  if(!nmpattern.test(uname))
  {
	  alert("Invalid Name");
	  return false;
  }
  
  if(!empattern.test(email))
  {
    alert("invalid email");
    return false;
  }
  if(!phpattern.test(phone))
  {
	  alert("Invalid phone");
	  return false;
  }
  if(!addrpattern.test(addr))
  {
	  alert("Invalid address");
	  return false;
  }
  
 

  $.ajax({
    type:'GET',
    url:"/regdata",
    contentType:"application/json;charset=UTF-8",
    data:{ 
      'stname':uname,
      'email':email,
      'phone':phone,
      'gender':gender,
      'addr1':addr,
      'pswd':pswd
    },
    dataType:'json',
    success:function(resp){
      alert(resp);
      window.location="register";
    },
    failure:function(resp){
      alert('Data Saved Failed');
    },
  });


});





$("#btn_login").click(function(){
  
  var email=document.getElementById('em').value;
  var pswd=document.getElementById('pswd').value;
  //alert(uname);
  
  var empattern = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+$/;
  var pswdpattern = /^[a-zA-Z0-9]{5,8}$/;
 
 

  $.ajax({
    type:'GET',
    url:"/logdata",
    contentType:"application/json;charset=UTF-8",
    data:{ 
      'email':email,
      'pswd':pswd
    },
    dataType:'json',
    success:function(resp){
      if(resp=='success')
      {        
        window.location="dashboard";
      }
      if(resp=='failure')
      {    
        alert('Credentials not found');    
        window.location="register";
      }
    },
    failure:function(resp){
      alert('Data Saved Failed');
    },
  });


});


$("#btn_reset_log").click(function(){
  
window.location='login';
  
});


$("#btn_reset_reg").click(function(){
  
  window.location='register';
    
  });


  
$("#btn_loaddata").click(function(){
  var form_data=new FormData($("#dataloadform")[0]);
  
  
  $.ajax({
    type:'POST',
    url:"/dataparser",
    data:form_data,
    contentType:false,
    cache:false,
    processData:false,
    success:function(resp){
      alert(resp);
    },
    failure:function(resp){
      alert('Data Saved Failed');
    },
  });
});

$("#btn_contact").click(function(){
  
  var uname=document.getElementById('nm').value;
  var phone=document.getElementById('ph').value;
  var email=document.getElementById('em').value;
  var country=document.getElementById('country').value;
  var message=document.getElementById('message').value;
  
  //alert(uname);

  var nmpattern=/^[a-zA-Z ]+$/;
  var phpattern=/^[6-9]{1}[0-9]{9}$/;
  var messagepattern=/^[a-zA-Z ]+$/;

  if(!nmpattern.test(uname))
  {
	  alert("Invalid Name");
	  return false;
  }
 
  if(!phpattern.test(phone))
  {
	  alert("Invalid phone");
	  return false;
  }
  if(!email.includes('@') || !email.includes('.com'))
  {
    alert("invalid email");
    return false;
  }
  if(!messagepattern.test(message))
  {
	  alert("Invalid message");
	  return false;
  }
});

$("#btn_cleardata").click(function(){
  debugger;    
  $.ajax({
    type:'GET',
    url:"/datadelete",
    // data:form_data,
     contentType:false,
     cache:false,
     processData:false,
    success:function(resp){
      alert(resp);
    },
    failure:function(resp){
      alert('Data deleting Failed');
    },
  });

});

$("#btn_predictdata").click(function () {
  debugger;
  var age = document.getElementById('age').value;
  var sex = document.getElementById('sex').value;
  var cp = document.getElementById('cp').value;
  var trtbps = document.getElementById('trtbps').value;
  var chol = document.getElementById('chol').value;
  var fbs = document.getElementById('fbs').value;
  var restecg = document.getElementById('restecg').value;
  var thalachh = document.getElementById('thalachh').value;
  var exng = document.getElementById('exng').value;
  var oldpeak = document.getElementById('oldpeak').value;
  var slp = document.getElementById('slp').value;
  var caa = document.getElementById('caa').value;
  var thall = document.getElementById('thall').value;

  var cppattern=/^[0-3]$/;

  var ageNo = parseInt(age);
  if (!(ageNo >= 1 && ageNo <= 100)) {
    alert("Invalid age");
    return false;
  }

  if (sex == '') { alert('Please select gender'); return }

  if(!cppattern.test(cp))
    {
  	  alert("Invalid cp");
  	  return false;
    }

  var trtbpsNo = parseInt(trtbps);
  if (!(trtbpsNo >= 94 && trtbpsNo <= 200)) {
    alert(" Blood Pressure must between 94 and 200");
    return false;
  }

  var cholNo = parseInt(chol);
  if (!(cholNo >= 126 && cholNo <= 564)) {
    alert("The Cholestrol must  between 126 and 564");
    return false;
  }

  if (fbs == '') { alert('Please select fbs '); return }


  if (restecg == '') { alert('Please select restecg'); return }


  var thalachhNo = parseInt(thalachh);
  if (!(thalachhNo >= 60 && thalachhNo <= 202)) {
    alert("The heart rate must between 60 and 202");
    return false;
  }

  if (exng == '') { alert('Please select exng'); return }


  var oldpeakNo = parseFloat(oldpeak);
  if (!(oldpeakNo >= 0 && oldpeakNo <= 6.2)) {
    alert("The Oldpeak must between 0 and 6.2");
    return false;
  }

  if (slp == '') { alert('Please select slp'); return }

  if (caa == '') { alert('Please select caa'); return }


  if (thall == '') { alert('Please select thall'); return }


  $.ajax({
    type: 'GET',
    url: "/predictdata",
    contentType: "application/json;charset=UTF-8",
    data: {
      'age': age,
      'sex': sex,
      'cp': cp,
      'trtbps': trtbps,
      'chol': chol,
      'fbs': fbs,
      'restecg': restecg,
      'thalachh': thalachh,
      'exng': exng,
      'oldpeak': oldpeak,
      'slp': slp,
      'caa': caa,
      'thall': thall,
    },
    dataType: 'json',
    success: function (resp) {
      //alert(resp);
      if (resp == 0)
        alert("Patient is normal")
      else
        alert("Patient is prone to heart attack")
    },
    failure: function (resp) {
      alert('Data prediction Failed');
    },
  });

});

window.deleteRow = function(row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13) {
  $.ajax({
    type: 'GET',
    url: "/deletedata",
    contentType: "application/json;charset=UTF-8",
    data: {
      'age': row0,
      'sex': row1,
      'cp': row2,
      'trtbps': row3,
      'chol': row4,
      'fbs': row5,
      'restecg': row6,
      'thalachh': row7,
      'exng': row8,
      'oldpeak': row9,
      'slp': row10,
      'caa': row11,
      'thall': row12,
      'output':row13,
    },
    dataType: 'json',
    success: function (resp) {
      alert(resp);
      window.location = "planning";
    },
    failure: function (resp) {
      alert('Data Deletion Failed');
    },
  });
}




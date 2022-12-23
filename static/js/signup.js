function signup_validation(){
    // fetching value from the form
    var fname=document.getElementById("exampleInputfname").value();
    var lname=document.getElementById("exampleInputlname").value();
    var uname=document.getElementById("exampleInputuname").value();
    var email=document.getElementById("exampleInputEmail1").value();
    var pwd1=document.getElementById("inputPassword5").value();
    var pwd2=document.getElementById("inputPassword6").value();

    // var for validations
    var letters=/^[A-Za-z]+$/;
    var email_value= /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;


    if (fname==""||lname==""||uname==""||email==""||pwd1==""||pwd2==""){
        window.alert("Please fill all the Details")
    }
    


}
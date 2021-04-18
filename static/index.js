var googleUser = {};

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  var id_token = googleUser.getAuthResponse().id_token;
  window.localStorage.token = id_token;
  /*console.log("ID: " + profile.getId()); 
  console.log('Full Name: ' + profile.getName());
  console.log('Given Name: ' + profile.getGivenName());
  console.log('Family Name: ' + profile.getFamilyName());
  console.log("Image URL: " + profile.getImageUrl());
  console.log("Email: " + profile.getEmail());*/

  //If the user is logged in
  var x = document.getElementById('myBtn');
  if(x != null){
    x.textContent = "Hello, " + profile.getName();
    var t = document.createElement("SPAN");
    t.className = "caret";
    x.appendChild(t);
    document.getElementsByClassName('abcRioButton')[0].style.display = "none";
    document.getElementsByClassName('signout')[0].style.display =  "block";
  }

  
  if(!window.location.href.includes('kibana') && typeof(window.localStorage.token) != 'undefined')
    window.location.href = 'kibana';
  else if(window.location.href.includes('kibana') && typeof(window.localStorage.token) == 'undefined')
    window.location.href = 'index';
}



function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();

  auth2.signOut().then(function () {
    /*document.getElementById('logged-name').innerHTML = "Please Sign in";
    document.getElementsByClassName('abcRioButton')[0].style.display =  "block";
    document.getElementsByClassName('signout')[0].style.display =  "none";*/
    window.location.href = '/';
    window.localStorage.clear();
  });
  
}

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
  var y = document.getElementsByClassName("dropdown");
  var z = document.getElementsByClassName('g-signin2');
  if(x != null){
    x.textContent = "Hello, " + profile.getName();
    y[0].style.display = "block";
    z[1].style.display = "none";
  }
  
  if(window.location.href.includes('kibana')){
    if(typeof(window.localStorage.token) != 'undefined')
      window.location.href = '/kibana?id_token='+window.localStorage.token;
    else if(typeof(window.localStorage.token) == 'undefined')
      window.location.href = 'index';
  } 
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  var y = document.getElementsByClassName("dropdown");
  var z = document.getElementsByClassName('g-signin2');
  
  auth2.signOut().then(function () {
    z[0].style.display = "block";
    y[0].style.display = "none";
    window.location.href = '/';
    window.localStorage.clear();
  });
  
}

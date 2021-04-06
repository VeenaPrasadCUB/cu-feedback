var googleUser = {};

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  var id_token = googleUser.getAuthResponse().id_token;
  /*console.log("ID: " + profile.getId()); 
  console.log('Full Name: ' + profile.getName());
  console.log('Given Name: ' + profile.getGivenName());
  console.log('Family Name: ' + profile.getFamilyName());
  console.log("Image URL: " + profile.getImageUrl());
  console.log("Email: " + profile.getEmail());*/

  //If the user is logged in
  if(document.getElementById('logged-name') != null){
    document.getElementById('logged-name').innerHTML = "Hello, " + profile.getName();
    document.getElementsByClassName('abcRioButton')[0].style.display = "none";
    document.getElementsByClassName('signout')[0].style.display =  "block";
  }
  
  if(!window.location.href.includes('kibana') && id_token != null)
    window.location.href = 'kibana';
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();

  auth2.signOut().then(function () {
    /*document.getElementById('logged-name').innerHTML = "Please Sign in";
    document.getElementsByClassName('abcRioButton')[0].style.display =  "block";
    document.getElementsByClassName('signout')[0].style.display =  "none";*/
    window.location.href = '/';
  });
  
}

var googleUser = {};
var username='';
  function onSignIn(googleUser) {
        // Useful data for your client-side scripts:
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());

    if(document.getElementById('logged-name') != null){
      document.getElementById('logged-name').innerHTML = "Hello, " + profile.getName();
      console.log(document.getElementsByClassName('signout')[0].style);
      document.getElementsByClassName('abcRioButton')[0].style.display = "none";
      document.getElementsByClassName('signout')[0].style.display =  "block";
    }
    
    var id_token = googleUser.getAuthResponse().id_token;
    if(!window.location.href.includes('kibana') && id_token != null)
      window.location.href = 'kibana';
    // The ID token you need to pass to your backend:
    
    //console.log("ID Token: " + id_token);
  }

  function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    console.log(auth2);
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
    document.getElementById('logged-name').innerHTML = "Please Sign in";
    document.getElementsByClassName('abcRioButton')[0].style.display =  "block";
    document.getElementsByClassName('signout')[0].style.display =  "none";
    window.location.href = '/';
  }

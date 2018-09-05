document.querySelector('.signup-form').addEventListener('submit', signUp);

function signUp (event) {
    event.preventDefault();
    fetch('https://andela-diaryapi.herokuapp.com/api/v1/auth/signup', {
        method: 'POST',
        body: JSON.stringify({
            name: document.querySelector('input[name=name]').value,
            username: document.querySelector('input[name=username]').value,
            email: document.querySelector('input[name=email]').value,
            password: document.querySelector('input[name=password]').value
        }),
        headers: {
            'content-type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            // displays the error message
            if (data.message.email){
                document.querySelector('#message p').innerText = data.message.email;
            } else if (data.message.password){
                document.querySelector('#message p').innerText = data.message.password;
            } else if (data.message.username){
                document.querySelector('#message p').innerText = data.message.username;
            } else {
                document.querySelector('#message p').innerText = data.message;
            }                       
            // checks if the user has signs up and redirect
            if (data.message == 'You have registered succesfully'){
                setTimeout(function(){
                    window.location.replace('signin.html');
                }, 1000);              
            }
        } );
}

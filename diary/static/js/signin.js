document.querySelector('.signin-form').addEventListener('submit', signIn)

function signIn (event) {
    event.preventDefault()
    fetch('https://andela-diaryapi.herokuapp.com/api/v1/auth/signin', {
        method: 'POST',
        body: JSON.stringify({
            username: document.querySelector('input[name=username]').value,
            password: document.querySelector('input[name=password]').value
        }),
        headers: {
            'content-type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            let token = data.token;
            localStorage.setItem('token', token);
            document.querySelector('#message p').innerText = data.message;            
            if (data.message === 'You have successfully logged in'){
                window.location.assign('diary-entries.html');
            }            
        })
        .catch(error => console.log(error));
}

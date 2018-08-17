document.querySelector('.signup-form').addEventListener('submit', signUp)

function signUp (event) {
  event.preventDefault()
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
    .then(function (response) {
      if (response.ok) {
        window.location.href = 'signin.html'
        return response.json()
      } else {
        document.querySelector('#signup-message').innerHTML = 'Registration failed! Please Enter all details'
      }
    })
    .then((data) => console.log(data))
}

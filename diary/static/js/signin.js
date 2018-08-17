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
    .then(function (response) {
      if (response.ok) {
        return response.json()
      } else {
        document.querySelector('#signin-message').innerHTML = 'Login Failed! '
      }
    })
    .then(data => {
      if (data.token) {
        var token = data.token
        localStorage.setItem('token', token)
        window.location.href = 'diary-entries.html'
      }
    })
}

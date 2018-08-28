
window.onload = function(){
    let token = localStorage.getItem('token');
    let url = 'https://andela-diaryapi.herokuapp.com/api/v1/profile'
    fetch(url, {
        headers: {
            'content-type': 'application/json',
            'x-access-token': token
        }
    }) 
        .then(response => response.json())
        .then(data => {
            document.querySelector('input[name=name]').value = data.name;
            document.querySelector('input[name=username]').value = data.username;
            document.querySelector('input[name=email]').value = data.email;
            document.querySelector('span#total_entries').innerText = data.total_entries;
            console.log(data.name, data.email, data.username, data.total_entries);
        })
        .catch(error => console.log(error));
};
document.querySelector('.add-entry').addEventListener('click', addEntry);
let token = localStorage.getItem('token');
function addEntry(event){
    event.preventDefault();
    fetch('https://andela-diaryapi.herokuapp.com/api/v1/entries', {
        method: 'POST',
        body: JSON.stringify({
            title: document.querySelector('input[name=title]').value,
            story: document.querySelector('#text-area').value
        }),
        headers: {
            'x-access-token': token,
            'content-type': 'application/json'
        }
    })
        .then(response => response.json())
        .then((data) => {
            let message = data.message;
            document.querySelector('#display-message').innerHTML = message;
            if (message === 'Entry posted successfully'){
                window.location.replace('diary-entries.html');
            }
        })
        .catch(error => console.log(error));
    document.querySelector('input[name=title]').value = '';
    document.querySelector('#text-area').value = '';
}




let token = localStorage.getItem('token');
let url = 'https://andela-diaryapi.herokuapp.com/api/v1/profile';
window.onload = function(){    
    fetch(url, {
        mode: 'cors',
        headers: {
            'content-type': 'application/json',
            'x-access-token': token
            // 'Access-Control-Allow-Origin': '*'
        }
    }) 
        .then(response => response.json())
        .then(data => {
            document.querySelector('input[name=name]').value = data.name;
            document.querySelector('input[name=username]').value = data.username;
            document.querySelector('input[name=email]').value = data.email;
            document.querySelector('span#total_entries').innerText = data.total_entries;
            
            if (data.reminder === true){
                document.querySelector('input[name=reminder]').checked = true;
                console.log('TRUE');
            }
        })
        .catch(error => console.log(error));
};

function addReminder(){    
    let reminder = document.querySelector('input[name=reminder]').checked;
    fetch(url, {        
        method: 'POST',        
        headers: {
            'content-type': 'application/json',
            'x-access-token': token           
            
        },
        body: JSON.stringify({
            'reminder': reminder
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}
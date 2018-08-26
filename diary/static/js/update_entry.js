let entry_id = localStorage.getItem('update_entryid');
let title = localStorage.getItem('update_title');
let story = localStorage.getItem('update_story');
let token = localStorage.getItem('token');

window.onload = function (){
    
    document.querySelector('input[name=title]').value = title;
    document.querySelector('#text-area').value = story;   
    
};

let update = document.querySelector('.update');
let url = 'https://andela-diaryapi.herokuapp.com/api/v1/entries/'+entry_id; 
update.addEventListener('click', function (event){
    event.preventDefault();
    fetch(url, {
        method: 'PUT',
        headers: {
            'x-access-token': token,
            'content-type': 'application/json'
        },
        body: JSON.stringify({
            'title': document.querySelector('input[name=title]').value,
            'story': document.querySelector('#text-area').value
        })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.querySelector('#display-message').innerText = data.message;
            window.location.replace('diary-entries.html');
            localStorage.removeItem('update_entryid');
            localStorage.removeItem('update_title');
            localStorage.removeItem('update_story');            
        });

});

function discardPost(){    
    let title = document.querySelector('input[name=title]').value;
    let story = document.querySelector('#text-area').value;
    if ((!(title)) && (!(story))) {
        window.location.replace('diary-entries.html');        
    } else {
        let result = confirm('Are you sure you want to discard?');
        if (result){
            window.location.replace('diary-entries.html');
        } else {event => event.preventDefault();}       
    }
}

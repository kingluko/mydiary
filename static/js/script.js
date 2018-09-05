// This function implements the logout funcitonality
const logout = () => {
    if (confirm('Are you sure?')){
        window.location.replace('signin.html');
        localStorage.clear();
    }
};

// This function is used to prompt a user on discard
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

const invalidToken = () => {
    let text = document.querySelector('#message p').innerText;
    if (text === 'Token is invalid'){
        alert('Please login!!');
        window.location.replace('signin.html');
    }
};
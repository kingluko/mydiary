let token = localStorage.getItem('token');
// Fetch the data
fetch('https://andela-diaryapi.herokuapp.com/api/v1/entries', {
    headers: {
        'x-access-token': token,
        'content-type': 'application/json'
    }
})
    .then((response) => response.json())
    .then(data => {
        let message = data.message;
        // displays message from api
        document.querySelector('#message p').innerHTML = message;
        let entries = data.entry;
        let entriesTable = document.querySelector('.entriestable');

        // Create tables to displat entries        
        if (data.message != 'Entries not found' || data.message === 'Token is invalid'){
            let rows = '';
            for (let i = 0; i < entries.length; i++) {
                const entry = entries[i];
                var row = `<tr>
                    <td>${entry.title}</td>
                    <td><a href="#" onclick="viewEntry(${entry.entry_id})">View</a></td>
                    <td><a href="update_entry.html" onclick="updateEntry(${entry.entry_id}, '${entry.title}', \`${entry.story}\`)">Modify</a></td>
                    <td><a href="#" onclick="deleteEntry(${entry.entry_id}, '${entry.title}')">Delete</a></td>
                    </tr>`;
                rows += row;
            }
            entriesTable.innerHTML = rows;
        }
        // console.log(data);        
    });

function viewEntry(entry_id) {
    let url = 'https://andela-diaryapi.herokuapp.com/api/v1/entries/'+entry_id;
    fetch(url, {
        headers : {
            'x-access-token': token,
            'content-type': 'application/json'
        }        
    })
        .then(response => response.json())
        .then(data => {
            let entry_id = data.entry[0].entry_id;
            let title = data.entry[0].title;
            let story = data.entry[0].story;
            let date_created = data.entry[0].date_created;

            localStorage.setItem('entry_id', entry_id);
            localStorage.setItem('title', title);
            localStorage.setItem('story', story);
            localStorage.setItem('date_created', date_created);

            window.location.replace('view_entry.html');
        })
        .catch(error => console.log(error));
}

function updateEntry(entry_id, title, story) {
    localStorage.setItem('update_entryid', entry_id);
    localStorage.setItem('update_title', title);
    localStorage.setItem('update_story', story);        
}

function deleteEntry(entry_id, title) {    
    let result = window.confirm('Are you sure you want to delete Title: '+ title + '?');
    if (result){
        let url = 'https://andela-diaryapi.herokuapp.com/api/v1/entries/'+entry_id;
        fetch(url, {
            method: 'DELETE',
            headers: {
                'x-access-token': token,
                'content-type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                window.location.reload();
            });
    }    
}
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
        let entries = data.entry;
        let entriesTable = document.querySelector('.entriestable');

        // Create tables to displat entries
        let rows = '';
        for (let i = 0; i < entries.length; i++) {
            const entry = entries[i];
            var row = `<tr>
                <td>${entry.title}</td>
                <td><a href="#" onclick="viewEntry(${entry.entry_id})">View</a></td>
                <td><a href="new-entry.html">Modify</a></td>
                <td><a href="">Delete</a></td>
              </tr>`;
            rows += row;
        }
        entriesTable.innerHTML = rows;
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
            let entry_id = data.entry[0].entry_id
            let title = data.entry[0].title
            let story = data.entry[0].story
            let date_created = data.entry[0].date_created

            localStorage.setItem('entry_id', entry_id)
            localStorage.setItem('title', title);
            localStorage.setItem('story', story);
            localStorage.setItem('date_created', date_created);

            window.location.replace('view_entry.html');
        })
        .catch(error => console.log(error));
}

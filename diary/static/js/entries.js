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
                <td><a href="entry.html">View</a></td>
                <td><a href="new-entry.html">Modify</a></td>
                <td><a href="">Delete</a></td>
              </tr>`;
            rows += row;
        }
        entriesTable.innerHTML = rows;
    });

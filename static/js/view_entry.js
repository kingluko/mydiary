function displayEntry() {
    let title = localStorage.getItem('title');
    let story = localStorage.getItem('story');
    let entry_id = localStorage.getItem('entry_id');
    let date_created = localStorage.getItem('date_created');

    document.querySelector('#page_title').innerText = 'Diary Entry ' +entry_id;
    document.querySelector('#date_created').innerText = date_created;
    document.querySelector('#story').innerText = story;
    document.querySelector('#entry_title').innerText = title;
}
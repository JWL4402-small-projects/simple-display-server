"use strict";

let active = true;

function displayMessages(data) {
    let messages = data['messages'];

    let html = "";

    messages.forEach(msg => {
        let author = msg.author ? msg.author : "Unknown";
        let time = msg.time ? msg.time : "unknown time"

        html += `<dt>${author} @ ${time}</dt>`;
        html +=`<dd>${msg.content}</dd>`;
    });
    
    $('#messages').html(html);
}

function sendRequest() {
    if (!active) { return; }
    $.ajax({
        method: 'GET',
        url: '/requests',
        mimeType: 'application.json',
        dataType: 'json',
        success: (data, status) => {
            displayMessages(data);
        },
        error: () => {
            $('#messages').html("No messages so far.");
        }
    })
}

sendRequest();
setInterval(sendRequest, 1000);

$('#clear').click(() => {
    $.ajax({
        method: 'POST',
        url: '/requests/clear',
        success: (data, status) => {
            if (status == 'success') {
                $('#messages').html("Messages cleared.");
                active = false;
                setTimeout(() => { active = true; }, 2500);
            }
        }
    })
})
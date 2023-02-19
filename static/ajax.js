"use strict";

function displayMessages(data) {
    console.log(data)

    let messages = data['messages'];
    console.log(messages.length)

    let html = "";

    if (messages.length == 0) {
        html = "No messages so far.";
    } else {
        messages.forEach(msg => {
            let author = msg.author ? msg.author : "Unknown";
            let time = ""

            html += `<dt>${author} @ ${time}</dt>`;
            html +=`<dd>${msg.content}</dd>`;
        });
    }

    $('#messages').html(html);
}

function sendRequest() {
    $.ajax({
        method: 'GET',
        url: '/requests',
        mimeType: 'application.json',
        dataType: 'json',
        success: (data, status) => {
            displayMessages(data);
            // console.log(data);
            // $('#data').html($('#data').text() + data);
        }
    })
}

sendRequest();
setInterval(sendRequest, 1000);
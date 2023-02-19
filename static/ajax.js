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
            html += msg + '<br>';
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

setInterval(sendRequest, 1000);